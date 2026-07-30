from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout


def texto_com_painel(texto, isArquivo):
    """
    Exibe um texto ou o nome e conteúdo de um arquivo de texto.
    O texto ficará dentro de um container, equivalendo à area do terminal.
    O container é delimitado por uma borda, e é dividido em duas partes, 
    mostrando o nome do arquivo(caso tenha) e o texto.
    
    Se isArquivo for True, o parâmetro texto deve ser o caminho de um arquivo. 
    Caso contrário, o texto é exibido diretamente.
    
    Args:
        texto (str): Texto ou caminho do arquivo.
        isArquivo (bool): Indica se texto é um arquivo.
    
    Returns:
        None
    """

    console = Console()
    layout = Layout()

    layout.split_column(Layout(name="upper"), Layout(name="lower"))
    layout["upper"].size = 3

    if not isinstance(texto, str):
            print("O parâmetro passado não é uma string.")
            return
    
    if isArquivo:        
        try:
            with open(texto, "r", encoding="utf-8") as f:
                conteudo = f.read()
                
                layout["upper"].update(Panel(texto, title='Nome do arquivo', style="sky_blue1"))

                layout["lower"].update(Panel(conteudo, title="Conteúdo do arquivo", style="sky_blue1"))
                console.print(layout)
        except FileNotFoundError:
            print("O caminho passado não é uma string.")
            return

    else:
        layout["upper"].update(Panel("", title='N/A', style="red"))

        layout["lower"].update(Panel(texto, title="Texto", style="grey85"))
        console.print(layout)

def texto_com_painel_2(texto, isArquivo):
    """
    Exibe um texto ou o nome e conteúdo de um arquivo de texto.
    O texto ficará dentro de um container, equivalendo à area do terminal.
    O container mostra o texto e se for um arquivo o nome aparece como título.
    
    Se isArquivo for True, o parâmetro texto deve ser o caminho de um arquivo. 
    Caso contrário, o texto é exibido diretamente.
    
    Args:
        texto (str): Texto ou caminho do arquivo.
        isArquivo (bool): Indica se texto é um arquivo.
    
    Returns:
        None
    """

    console = Console()
    layout = Layout()
    

    if not isinstance(texto, str):
            print("O parâmetro passado não é uma string.")
            return
    
    if isArquivo:        
        try:
            with open(texto, "r", encoding="utf-8") as f:
                conteudo = f.read()
                layout.update(Panel(conteudo, title=texto, style="sky_blue1 "))
                console.print(layout)

        except FileNotFoundError:
            print("O caminho passado não é uma string.")

    else:
        layout.update(Panel(texto, title='Texto comum', style="grey85"))
        console.print(layout)
