# Avaliação Sprint 5 - Programa de Bolsas Compass UOL / AWS e Univesp

Avaliação da [quinta sprint][sprint5main] do programa de bolsas [Compass UOL][compass] para formação em machine learning para [AWS][aws].

***

Este é um projeto de machine learning que usa o conjunto de dados MNIST para treinar um modelo de classificação de imagens de dígitos manuscritos de 0 a 9. O modelo foi treinado usando o Amazon SageMaker.

## Conjunto de Dados MNIST
O conjunto de dados MNIST consiste em 70.000 imagens de dígitos manuscritos (0 a 9) com um tamanho de 28x28 pixels cada. O conjunto de dados é amplamente utilizado para treinar e testar algoritmos de reconhecimento de padrões e classificação de imagens. 

O conjunto de dados pode ser baixado diretamente do site do MNIST: http://yann.lecun.com/exdb/mnist/

![MNIST](https://upload.wikimedia.org/wikipedia/commons/2/27/MnistExamples.png)


## Ambiente
O projeto foi desenvolvido utilizando o ambiente AWS. Os seguintes serviços da AWS foram usados:

- Amazon S3: para armazenar o conjunto de dados
- Amazon SageMaker: para treinar e implantar o modelo ML


## Modelo
O modelo de ML usado neste projeto é uma Rede Neural Convolucional (CNN). A CNN foi desenvolvida usando a biblioteca Keras e treinada usando o TensorFlow. O modelo alcançou uma precisão de 93,2% no conjunto de teste.

## Arquivos do Projeto
- README.md: Este arquivo README.
- mnist.ipynb: O notebook Jupyter que contém o código para carregar o conjunto de dados, treinar o modelo e avaliar a precisão do modelo.
- requirements.txt: Arquivo com as dependências necessárias para executar o notebook.

## Como Executar o Projeto
1 - Faça o login na sua conta do Amazon SageMaker.
2 - Crie um novo notebook instance e selecione o tipo de instância e a imagem de ambiente que deseja usar.
3 - Faça o upload do arquivo mnist.ipynb para o notebook instance.
4 - Abra o notebook e execute as células de código na ordem indicada.

## Referências
- Conjunto de dados MNIST: http://yann.lecun.com/exdb/mnist/
- Amazon SageMaker: https://aws.amazon.com/sagemaker/
- JupyterLab Notebook: https://jupyter.org/


## Dificuldades
- XXXXXXX.
- XXXXXX.

***


## Desenvolvedores do projeto
| [<img src="https://avatars.githubusercontent.com/u/25699466?v=4" width=115><br><sub>Bruno Monserrat Perillo</sub>](https://github.com/brunoperillo) | [<img src="https://avatars.githubusercontent.com/u/124359272?v=4" width=115><br><sub>Irati Gonçalves Maffra</sub>](https://github.com/IratiMaffra) | [<img src="https://avatars.githubusercontent.com/u/35769020?v=4" width=115><br><sub>Marcio Lima Brunelli</sub>](https://github.com/ml-brunelli) | [<img src="https://avatars.githubusercontent.com/u/73674662?v=4" width=115><br><sub>Marcos Vinicios Nativo de Carvalho</sub>](https://github.com/onativo) | [<img src="https://avatars.githubusercontent.com/u/94749597?v=4" width=115><br><sub>O'Dhara Maggi</sub>](https://github.com/odharamaggi) |
| :---: | :---: | :---: |:---: |:---: |


***
   [kernel]: <https://pt.wikipedia.org/wiki/N%C3%BAcleo_(sistema_operacional)>
   [compass]: <https://compass.uol/en/home/>
   [aws]: <https://aws.amazon.com/pt/>
   [sprint5main]: <https://github.com/Compass-pb-aws-2023-Univesp/sprint-5-pb-aws-univesp>
   [endpoint]: <http://54.163.32.88:9000/>
