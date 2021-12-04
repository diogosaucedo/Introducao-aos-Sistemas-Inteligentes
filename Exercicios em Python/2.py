"""
2) Faça uma função que receba dois parâmetros: linhas e colunas. A função deve desenhar uma moldura usando os caracteres
 '-', '|' e '*', como abaixo para 1 linha e 3 colunas.

*---*
|     |
*---*

"""


def draw_frame(amount_lines: int, amount_columns: int):
    print("*", amount_columns * "-", "*")
    [print("|", amount_columns * " ", "|") for i in range(amount_lines)]
    print("*", amount_columns * "-", "*")


# receive values
lines = int(input("Amount lines: "))
columns = int(input("Amount columns: "))

draw_frame(lines, columns)
