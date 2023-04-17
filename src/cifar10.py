import argparse
import json
import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.datasets import cifar10

if __name__ == "__main__":
    import keras
    from keras.preprocessing.image import ImageDataGenerator
    from keras.layers import Dense, Dropout, Activation, Flatten
    from keras.layers import Conv2D, MaxPooling2D

    parser = argparse.ArgumentParser()
    
    parser.add_argument('--epochs', type=int, default=2)
    parser.add_argument('--learning-rate', type=float, default=0.0001)
    parser.add_argument('--batch-size', type=int, default=32)
    parser.add_argument('--dropout', type=int)
    
    # https://github.com/aws/sagemaker-training-toolkit/blob/master/ENVIRONMENT_VARIABLES.md
    parser.add_argument('--train', type=str, default=os.environ.get('SM_CHANNEL_TRAINING'))
    parser.add_argument('--model-dir', type=str)
    parser.add_argument('--sm-model-dir', type=str, default=os.environ.get('SM_MODEL_DIR'))
    
    args, _ = parser.parse_known_args()
    
    #x_train = np.load(os.path.join(args.train, 'train_data.npy'))
    #y_train = np.load(os.path.join(args.train, 'train_labels.npy'))
    #x_test = np.load(os.path.join(args.train, 'eval_data.npy'))
    #y_test = np.load(os.path.join(args.train, 'eval_labels.npy'))
      
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()
    
    x_train = x_train.astype('float32')
    x_test = x_test.astype('float32')
    x_train /= 255
    x_test /= 255
    
    
    model = Sequential()
    # CONV => RELU => CONV => RELU => POOL => DROPOUT
    model.add(Conv2D(32, (3, 3), padding='same',input_shape=x_train.shape[1:]))
    model.add(Activation('relu'))
    model.add(Conv2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    # CONV => RELU => CONV => RELU => POOL => DROPOUT
    model.add(Conv2D(64, (3, 3), padding='same'))
    model.add(Activation('relu'))
    model.add(Conv2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    #ADDED THIRD CONV => RELU => POOL LAYER
    model.add(Conv2D(128, (3, 3), padding='same'))
    model.add(Activation('relu'))
    model.add(Conv2D(128, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    # FLATTERN => DENSE => RELU => DROPOUT
    model.add(Flatten())
    model.add(Dense(128))
    model.add(Activation('sigmoid'))
    model.add(Dropout(0.5))

    model.add(Dense(128))
    model.add(Activation('sigmoid'))
    model.add(Dropout(0.5))

    model.add(Dense(128))
    model.add(Activation('sigmoid'))
    model.add(Dropout(0.5))

    # a softmax classifier
    model.add(Dense(10))
    model.add(Activation('softmax'))
    
    model.compile(optimizer = RMSprop(learning_rate = args.learning_rate, decay=1e-6),
                        loss = 'sparse_categorical_crossentropy',
                        metrics = ['accuracy'])

    model.fit(x_train, y_train, batch_size = args.batch_size, 
                    epochs = args.epochs)
    score = model.evaluate(x_test, y_test)
    
    print('Loss: ', score[0])
    print('Accuracy: ', score[1])
    
    model.save(os.path.join(args.sm_model_dir, "000000001"))