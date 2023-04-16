# Avaliação Sprint 5 - Programa de Bolsas Compass UOL / AWS e Univesp

Avaliação da quinta sprint do programa de bolsas Compass UOL para formação em machine learning para AWS.

***
## Grupo 4

[Carlos Roberto de Souza Camilo ](https://github.com/crobertocamilo)

[Kelly Patricia Lopes Silva](https://github.com/KellyPLSilva)

[Luiz Renato Sassi](https://github.com/luizrsassi)

[Viviane Silva Alves ](https://github.com/Vivianes86)

*****
## Introdução 

Nessa Sprint, foram abordados os assuntos sobre o uso básico de redes neurais com Python, e uso de machine learning na AWS com o recursos do [Amazon SageMaker](https://aws.amazon.com/pt/pm/sagemaker/) para treinar modelos.  

Aprendemos os conceitos teóricos/matemáticos, os fundamentos e excecutamos o treinamento de um dataset. 

O grupo fez o planejamento do projeto atráves de reuniões de alinhamento do contéudo no qual procuramos entender sobre os passos a passos, pesquisas e testes que iriamos trazer para o projeto. Subdividimos as tarefas em readme, analise (deploy e previsões), notebook na AWS e a disponibilização do modelo. 
***
## Objetivo 

Treinarmento de um dataset para posterior reconhecimento.

***

## Escopo

Dataset escolhido foi [CIFAR10]() (Canadian Institute for Advanced Research, 10 classes) é um subconjunto de imagens e contém 60.000 imagens coloridas de 32x32. 
Estão rotuladas em 10 classes mutuamente exclusivas: Avião, Automóvel, Pássaro, Gato, Veado, Cachorro, Sapo, Cavalo, Navio e Caminhão.


![imagemCifar10port](https://user-images.githubusercontent.com/88354075/232254787-6c5a4277-3d83-4e33-a7a8-bafb5f1ff1c4.png)

Etapas do processo para treinamento do dataset

1. Coleta de dados, através de imagens com 10 categorias. 

2. Pré - Processamento de dados, onde ocorre o preparo para o treinamento. 

Inclue as tarefas como normalização, redimensionamento de imagens. 

3. Divisão de dados, é dividido em conjunto de treinamento, validação e teste. 

Ocorre aqui os ajustes dos hiperparâmentos do modelo e o conjunto de teste é usado para avaliar o desempenho final do modelo. 


4. Escolha do Algoritmo e ou modelo, que será usado para treinar os dados. 

Pode variar pois vai depender do tipo de reconhecimento que o conjunto de dados estiver disponível. 


5. Treinamento do modelo
Ajusta os parâmetros para minimizar a diferença entre as previsões e os rótulos verdadeiros do conjunto. 


6. Avaliação do modelo
Foi feito para evitar que o modelo se ajuste demais aos dados de treinamento e não generalize bem para novos dados. 

7. Teste final do modelo 
Avaliação no conjunto de teste para avaliar o desempenho.

8. Implantação do modelo


## Casos de teste
Separamos os caso de testes ......

Buscamos trazer prioridades aos temas abordados nos cursos desta Sprint.


2cnn+256+256_dropout

2cnn+512_0dropout

2cnn+512_10dropout

2cnn+512_20dropout

2cnn+51+2562_50dropout

2cnn+1024_50dropout

3cnn+512_50dropout

3cnn-128-128-128-50dropout-sigmoid

![3cnn-128-128-128-50dropout-sigmoid](https://user-images.githubusercontent.com/88354075/232256066-de6b7240-747c-4102-b9d6-1b1ad13b5214.png)

Os testes realizados, abordam os seguintes ....

## Dificuldades conhecidas


## Como utilizar o sistema

* 

## Referências

[Cifar-10](https://paperswithcode.com/dataset/cifar-10)


  - 
  - 


**Especificações**:

* Com base no notebook apresentado neste tutorial do Tensorflow: <https://www.tensorflow.org/tutorials/keras/classification> (outros padrões como scikit-learn e pytorch também podem ser usados, no caso de exemplos equivalentes);
* Trocar por outro dataset para treinamento, e **verificar se já não foi escolhido por outro grupo**. Pode ser usado qualquer dataset do Tensorflow (ou similar de outro padrão), conforme mostra esta listagem: <https://www.tensorflow.org/datasets/catalog/overview>;
* Armazenar o modelo treinado e o dataset de inferência (se desejado ou necessário, de treino/teste também) em bucket S3;
* Carregar o modelo armazenado para reconhecer um novo exemplo. Observe o exemplo de reconhecimento na seção "Fazendo Previsões" do notebook citado neste capítulo de ebook: <https://www.deeplearningbook.com.br/reconhecimento-de-imagens-com-redes-neurais-convolucionais-em-python-parte-4/>

***





## pendencias

- Projeto em produção na AWS - *verificar imagem Luis*
- Arquivos de configuração utilizados - *verificar*
- Notebook Python desenvolvido *verificar*




***
