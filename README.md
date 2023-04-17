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

Utilizando o Sagemaker 

Atráves desse serviço é possível preparar, criar, treinar e implantar modelos de machine learning de alta qualidade rapidamente, reunindo um amplo conjunto de recursos criados especificamente para machine learning. Fornece um conjunto de soluções para os casos de uso mais comuns e que podem ser implantadas prontamente com apenas alguns cliques.


## Casos de teste

Separamos os caso de testes a partir dos cenários identificados para montar uma tabela de casos de teste, onde a quantidade de casos de testes varia de acordo com as validações existentes nos cenários. A união das informações desta tabela como os passos percorridos nos fluxos do casos de usos (resultado da tabela gerada na segunda etapa) produzindo assim a planilha de especificação de Testes.

![WhatsApp Image 2023-04-17 at 08 34 59](https://user-images.githubusercontent.com/88354075/232473930-50b87837-0d9b-42a2-961b-bbce5b30e5ac.jpeg)

* Teste Final

![WhatsApp Image 2023-04-17 at 08 36 34](https://user-images.githubusercontent.com/88354075/232474361-83614e5f-2df6-4fed-b314-f2d95af214c9.jpeg)


Testes realiazados: 

2cnn+128+128+128_20dropout

2cnn+128+128+128_20dropout

2cnn+128+128+128_50dropout-0dropout-cnn

2cnn+512+256_50dropout

2cnn+256+256_dropout

2cnn+512_0dropout

2cnn+512_10dropout

2cnn+512_20dropout

2cnn+51+2562_50dropout

2cnn+1024_50dropout

3cnn+512_50dropout

3cnn-128-128-128-50dropout-sigmoid

![imageconvergir](https://user-images.githubusercontent.com/88354075/232477314-a6847bc4-2f99-4fad-809f-453871a88488.jpeg)


Os testes realizados, abordam os seguintes ....

## Dificuldades conhecidas

* Familiaridade com SageMaker, Tensorflow e Kaggle. 

* Montagem do modelo para treinar os testes.

## Como utilizar o sistema

Entrar na sua conta do Amazon SageMaker, criar um novo notebook selecionando o tipo de instância e ambiente que irá usar. 
Na sequência fazer o upload do arquivo [Cifar-10](https://www.tensorflow.org/api_docs/python/tf/keras/datasets/cifar10/load_data). 
As instalações e importações de biblioteca já estão no modelo. 
Precisará executar as cédulas de código e aguardar o sistema rodar. 

***
## Ferramentas e Tecnologias Utilizadas 

[Visual Studio Code](https://code.visualstudio.com/)

[Amazon Sagemaker](https://aws.amazon.com/pt/sagemaker/)

[Kaggle](https://www.kaggle.com/datasets)

[Google colab](https://colab.research.google.com/)

[Python](https://www.python.org/)
## Referências

[Cifar-10](https://paperswithcode.com/dataset/cifar-10)

Livros: 
* Redes Neurais - Simon Haykin

* Preparação e Análise Exploratória de Dados - Rafael G. C. Ferreira; Leandro B. A. de Miranda; Rafael A. Pinto; et al.

* Python Para Data Science - Netto, Amilcar; Neto, Francisco

****




