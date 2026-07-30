import argparse
from personalizador.estilo import texto_estilizado, texto_estilizado_2
from personalizador.layout import texto_com_layout, texto_com_layout_2
from personalizador.painel import texto_com_painel, texto_com_painel_2
from personalizador.progresso import carrega_texto, carrega_caracteres_texto

parser = argparse.ArgumentParser()

parser.add_argument("texto", help="Texto ou caminho do arquivo a ser informado")
parser.add_argument("-a", "--arquivo", action="store_true", help="Indica que o texto informado é um caminho de arquivo")
parser.add_argument("-m", "--modulo", choices=["estilo", "layout", "painel", "progresso"], help="Opções: estilo, layout, painel ou progresso", required=True)
parser.add_argument("-f", "--funcao", help="Funções disponíveis: texto_estilizado, texto_estilizado_2, texto_com_layout, texto_com_layout_2, texto_com_painel, texto_com_painel_2, carrega_texto, carrega_caracteres_texto", required=True)

args = parser.parse_args()

modulos = {
    "estilo": {
        "texto_estilizado": texto_estilizado,
        "texto_estilizado_2": texto_estilizado_2
    },
    "layout": {
            "texto_com_layout": texto_com_layout,
            "texto_com_layout_2": texto_com_layout_2
        },
    "painel": {
            "texto_com_painel": texto_com_painel,
            "texto_com_painel_2": texto_com_painel_2
        },
    "progresso": {
            "carrega_texto": carrega_texto,
            "carrega_caracteres_texto": carrega_caracteres_texto
        }
}

funcao_escolhida = modulos[args.modulo][args.funcao]

funcao_escolhida(args.texto, args.arquivo)
