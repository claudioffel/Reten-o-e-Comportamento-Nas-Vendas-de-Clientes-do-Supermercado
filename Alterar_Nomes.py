import pandas as pd
import random

df = pd.read_excel("Tabelas Vendas Clientes.xlsx")


nomes = [
    "Lucas","Miguel","Arthur","Heitor","Theo","Davi","Gabriel","Pedro",
    "Matheus","Rafael","Bruno","Felipe","Gustavo","Daniel","Henrique",
    "Leonardo","Vinicius","Samuel","Caio","Eduardo","Joao","Anderson",
    "Ricardo","Diego","Marcelo","Tiago","Victor","Alex","Carlos","Andre",
    "Mariana","Julia","Beatriz","Larissa","Camila","Amanda","Isabela",
    "Sofia","Valentina","Helena","Clara","Alice","Livia","Fernanda",
    "Patricia","Juliana","Renata","Aline","Vanessa","Natalia","Bianca",
    "Carolina","Paula","Elaine","Gabriela","Monica","Cristina","Tatiane",
    "Bruna","Leticia"
]


sobrenomes = [
    "Silva","Oliveira","Souza","Costa","Santos","Lima","Ferreira",
    "Almeida","Rocha","Barbosa","Martins","Melo","Ribeiro","Nascimento",
    "Cardoso","Araújo","Teixeira","Batista","Correia","Moreira",
    "Freitas","Vieira","Pereira","Carvalho","Monteiro","Dias",
    "Andrade","Moura","Castro","Campos","Pinto","Rezende","Farias",
    "Sales","Peixoto","Machado","Fonseca","Neves","Queiroz","Leite",
    "Nogueira","Miranda","Tavares","Borges","Aguiar","Porto","Macedo",
    "Gomes","Coelho","Alves","Cunha","Ramos","Mendes","Cavalcante",
    "Xavier","Pacheco","Siqueira","Torres","Valente","Prado"
]


nomes_usados = set()

def gerar_nome():

    tentativas = 0

    while tentativas < 1000:

        nome = random.choice(nomes)
        sobrenome = random.choice(sobrenomes)

        nome_completo = f"{nome} {sobrenome}"

        if nome_completo not in nomes_usados:

            nomes_usados.add(nome_completo)

            return nome_completo

        tentativas += 1

   
    return f"{random.choice(nomes)} {random.choice(sobrenomes)}"


df["NOME"] = df["NOME"].apply(
    lambda x: gerar_nome() if pd.notna(x) else x
)


df.to_excel(
    "clientes_anonimizados.xlsx",
    index=False
)

print("Arquivo anonimizado criado")