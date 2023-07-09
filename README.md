# Backend do desafio técnico

Contém um aplicativo Flask simples que fornece duas APIs para operações em matrizes.

## Pré-requisitos
- Python 3.x
- Flask
- Flask-Cors
- Flask-Testing (para executar os testes)

## Instalação

Clone este repositório:
````
git clone https://github.com/seu-usuario/seu-repositorio.git
````
````cd seu-repositorio````

Instale as dependências:

````pip install -r requirements.txt````

## Uso

Execute o aplicativo Flask:

````python run.py````

As seguintes rotas estão disponíveis:

/inverte-diagonais: Esta rota recebe uma matriz e retorna a matriz com suas diagonais invertidas.

/conta-submatriz: Esta rota recebe uma matriz e uma submatriz e retorna o número de vezes que a submatriz ocorre na matriz.

Faça uma requisição POST para uma das rotas acima, passando os parâmetros necessários como um objeto JSON no corpo da requisição. A resposta será um objeto JSON contendo os resultados da operação.


### Exemplos
#### Inverter Diagonais

URL: /inverte-diagonais

Método: POST

Corpo da requisição:

{
  "matriz": [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
  ]
}
Resposta:

{
  "matriz_invertida": [
    [3, 2, 1],
    [4, 5, 6],
    [9, 8, 7]
  ]
}
#### Contar Submatriz
URL: /conta-submatriz

Método: POST

Corpo da requisição:

{
  "matriz": [
    [1, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6],
    [4, 5, 6, 7]
  ],
  "submatriz": [
    [3, 4],
    [4, 5]
  ]
}
Resposta:

{
  "contagem": 3
}

### Testes

Este repositório também inclui testes automatizados para as funções de manipulação de matrizes.

Para executar os testes, execute o seguinte comando:

````python tests.py````