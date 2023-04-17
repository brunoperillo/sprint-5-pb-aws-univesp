# Avaliação Sprint 5 - Programa de Bolsas Compass UOL / AWS e Univesp

Avaliação da quinta Sprint do programa de bolsas Compass UOL para formação em machine learning para AWS.

***
## Grupo 3

[Carlos Roberto de Souza Camilo ](https://github.com/crobertocamilo)

[Kelly Patricia Lopes Silva](https://github.com/KellyPLSilva)

[Luiz Renato Sassi](https://github.com/luizrsassi)

[Viviane Silva Alves ](https://github.com/Vivianes86)

*****
## Introdução 

Nessa Sprint, foram abordados os assuntos sobre o uso básico de redes neurais com Python e Tensorflow/Keras, e o estudo de modelos de *machine learning* na AWS com o recurso [Amazon SageMaker](https://aws.amazon.com/pt/pm/sagemaker/) para treinar modelos.  

Aprendemos os conceitos teóricos/matemáticos, os fundamentos e excecutamos o treinamento de um dataset. 

O grupo fez o planejamento do projeto atráves de reuniões de alinhamento do contéudo no qual procuramos entender as etapas de preparação e criação de um modelo de rede neural, pesquisas e testes do que iríamos implementar no projeto. Subdividimos as tarefas em readme, analise (*deploy* e previsões), notebook na AWS e a disponibilização do modelo. 
***
## Objetivo 

Treinamento de uma rede neural utilizando um *dataset* para classificação de imagens, e sua posterior disponibilização para aplicação em imagens nas quais não foi treinado.

***

## Escopo

O *dataset* escolhido foi [CIFAR10]() (Canadian Institute for Advanced Research, 10 classes), que consiste num conjunto 60.000 imagens coloridas em baixa resulção (32x32 pixels). 
As imagens estão rotuladas em 10 classes mutuamente exclusivas: Avião, Automóvel, Pássaro, Gato, Veado, Cachorro, Sapo, Cavalo, Navio e Caminhão.


![imagemCifar10port](https://user-images.githubusercontent.com/88354075/232254787-6c5a4277-3d83-4e33-a7a8-bafb5f1ff1c4.png)

Etapas do processo para treinamento do modelo:

1. Coleta de dados, através de imagens com 10 categorias. 

2. Pré-processamento do dados, onde ocorre o preparo para o treinamento. 

Inclue as tarefas como normalização, redimensionamento das imagens. 

3. Divisão de dados, onde o *dataset* é dividido em conjunto de treino, validação e teste. 

O conjunto de valiação é utilizado para avaliar os hiperparâmetros do modelo a partir da comparação de métricas (acurácia e erro) no conjunto de treino e validação. Já as imagens do conjunto de teste, são utilizadas, após o treinamento, para avaliar a qualidade preditiva do modelo.

4. Escolha do algoritmo e do modelo, que será usado para treinar os dados. 

Pode variar pois vai depender das características do *dataset* utilizado. Apesar de pequenas, as imagens do CIFAR10 são coloridas, sendo requerem a aplicação de camadas convolucionais (CNN).


5. Treinamento do modelo:
Consiste em ajustar os parâmetros livres da rede de forma a minimizar a diferença entre as previsões e os rótulos verdadeiros do conjunto. 


6. Avaliação do modelo:
Feita comparando o resultado no modelo para nos conjuntos de treino e teste. É importante para evitar que o modelo se ajuste demais aos dados de treino (*overfitting*), mas não generalize bem para novos dados. 

7. Teste final do modelo: 
Avaliação da qualidade final no conjunto de teste (10.000 imagens) para avaliar seu desempenho com dados (novas imagens) com as quais não treinou.

8. Implantação do modelo utilizando o Sagemaker 

Atráves desse serviço é possível preparar, criar, treinar e implantar modelos de *machine learning* de alta qualidade rapidamente, reunindo um amplo conjunto de recursos criados especificamente para este tipo de algoritmos. Fornece um conjunto de soluções para os casos de uso mais comuns e que podem ser implantadas prontamente com apenas alguns cliques.


## Desenvolvimento

Para definição da arquitetura da rede neural, foram realizados dezenas de teste, abordando deste o algoritmo de otimização, aplicação e nível do algoritmo de regularização (*dropout*), e outros parâmetros da rede (*batch size*), até a arquitetura da rede em si (número de camadas - CNN e MLP - e quantidade de neurônios). Os resultados dos principais testes é apresentado na pasta [src/tests](https://github.com/Compass-pb-aws-2023-Univesp/sprint-5-pb-aws-univesp/tree/grupo-3/src/tests). 

O principal critério para aprovar ou não uma arquitetura foi a não ocorrência de *overfitting*, mas também a simplicidade do modelo. Ao final, **a rede escolhida foi uma composta por 3 camadas convolucionais e 3 camadas com 128 neurônios cada**. Como mostrado abaixo, esta rede apresentou ótima concordância entre os conjuntos de treino e validação, tanto em acurácia (a portengem de imagens que a rede classifica corretamente) quanto em erro (a "certeza" que a rede tem na classificação que indica).

![imageconvergir](https://user-images.githubusercontent.com/88354075/232477314-a6847bc4-2f99-4fad-809f-453871a88488.jpeg)


**Acurácia do modelo:**
* Treino: 79,8%
* Validação: 78,8%
* Teste: 78,8%


Alguns exemplos da aplicação do modelo treinado às imagens do conjunto de teste:

![WhatsApp Image 2023-04-17 at 08 36 34](https://user-images.githubusercontent.com/88354075/232474361-83614e5f-2df6-4fed-b314-f2d95af214c9.jpeg)


A imagem abaixo mostra a matriz de confusão, comparando a predição do modelo (*predicted label*) e a real classificação da imagem (*true label*). Como pode ser observado, o erro do modelo (ele acertou 7900 imagens, mas classificou 2100 incorretamente) ocorre principalmente em relação à classe "cachorro", frequentemente confundida como sendo "gato".

Uma alternativa para melhorar os resultados do modelo, mantendo a baixa resolução das imagens 32x32, seria aumentar o número de imagens disponíveis para treino, principalmente nas classes "cachorro" e "gato".

![WhatsApp Image 2023-04-17 at 08 34 59](https://user-images.githubusercontent.com/88354075/232473930-50b87837-0d9b-42a2-961b-bbce5b30e5ac.jpeg)



## Dificuldades conhecidas

* Familiaridade com SageMaker, Tensorflow e Kaggle. 

* Montagem e tempo de execução do modelo para treinar os testes.

## Como utilizar o sistema

Abrir o notebook [endpoint_externo_boto3.ipynb](https://github.com/Compass-pb-aws-2023-Univesp/sprint-5-pb-aws-univesp/blob/grupo-3/src/endpoint_externo_boto3.ipynb) no Google Colab. É necessário ter chaves para acesso à conta e o endereço do endpoint. Imagens a serem testadas devem estar no Colab (necessário fazer o upload; há exemplos na pasta assets/)


***
## Ferramentas e Tecnologias Utilizadas 

[Visual Studio Code](https://code.visualstudio.com/)

[Amazon Sagemaker](https://aws.amazon.com/pt/sagemaker/)

[Kaggle](https://www.kaggle.com/datasets)

[Google colab](https://colab.research.google.com/)

[Python](https://www.python.org/)
## Referências

[Cifar-10](https://paperswithcode.com/dataset/cifar-10)

Tutorial:
* https://www.kaggle.com/code/roblexnana/cifar10-with-cnn-for-beginer
  
Livros: 
* Redes Neurais - Simon Haykin

* Preparação e Análise Exploratória de Dados - Rafael G. C. Ferreira; Leandro B. A. de Miranda; Rafael A. Pinto; et al.

* Python Para Data Science - Netto, Amilcar; Neto, Francisco

****




