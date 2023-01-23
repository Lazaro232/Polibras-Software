# API - Teste Back-End

Essa API é responsável pelo gerenciamento de um pequeno mercado. Através dela, é possível cadastrar produtos, realizar vendas e obter um relatório de fechamento de caixa, que consiste no somatório do montante vendido por dia.

## Configurações Iniciais

A API foi construída utilizando o Django Rest Framework (**DRF**). Além disso, utiliza-se a biblioteca **pipenv** para gerenciar o ambiente virtual em que o projeto está contido.

Para instalar as dependências utilizando o **pipenv**:

                pipenv install

Caso as dependências não sejam instaladas de forma automática, usa-se o seguinte comando para sincronizar as dependências.

                pipenv sync

Para ativar o ambiente virtual:

                pipenv shell

Para rodar comandos sem precisar ativar o ambiente virtual:

                pipenv run <comando>

## Rodando o Servidor

Os comandos a seguir irão considerar que o ambiente virtual está ativo, não sendo necessário invocar o comando *pipenv run* como prefixo. Ademais, a API conta com uma camada de autenticação. Tal camada é baseada em um **Token JWT**.

Para realizar qualquer requisição para a API é preciso ter um token e passá-lo como ***Bearer Token*** no *header* da requisição. Para tanto, é necessário criar um *super usuário*, que terá o privilégio de criar tokens de acesso.

Para criar o super usuário. Será pedido para informar o usuário, email e senha para o super usuário.

                python manage.py createsuperuser


Possuindo tal usuário, é possível rodar o servidor e realizar as requisições.

                python manage.py runserver

## Gerando o Token de Acesso

Para gerar o token de acesso, é preciso realizar uma requisição do tipo *POST* para o *endpoint* **.../token/**, passando *username* e *password* no corpo da requisição. A requisição retornará o token de acesso e o token para atualizar o token de acesso em caso de expiração. Possuindo o token, é possível realizar as demais requisições.

