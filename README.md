# Tabelas - PostgreSQL

## Tabela **Produtos**
* ID - Serial
* Nome - TEXT
* Created at
* Estoque - INT
* Preço - FLOAT

## Tabela **Vendas**
* Id - Serial
* Produtos - Lista com os ids dos produtos vendidos
* Pagamento (Foreign Keys da tabela de métodos de pagamento. DEVE SER O NOME, NÃO O ID)

## Tabela **Métodos de Pagamento**
* Id - Serial
* Nome - TEXT

# Tarefas

## Cadastro de produtos
Será um INSERT na tabela de Produtos. Deve-se passar:

* Nome
* Estoque inicial (isso deve criar uma linha na tabela de Estoque)
* Preço inicial (isso deve criar uma linha na tabela de Preço)

## Lançamento de vendas

* Cadastrar a venda na tabela de Vendas passando os **produtos** e a **forma de pagamento** (pode ser por ID mesmo)
* Atualizar estoque - Reduzir estoque do produto que foi vendido

# Restrições

* Não deve ser permitido registrar a venda de um produto não registrado ou sem estoque
* Atualizar o preço do produto não deve influenciar nas vendas já realizadas