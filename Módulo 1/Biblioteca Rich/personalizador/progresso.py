import time
from rich.console import Console
from rich.progress import Progress
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel

texto = 'Lista de compras.txt'


def carrega_texto(texto, isArquivo):
    """
    Exibe um texto ou o nome e conteúdo de um arquivo de texto.
    Exibe uma barra indicando que o texto está sendo carregado,
    o carregamento existe apenas para demostrar a funcionalidade da biblioteca rich.
    
    Se isArquivo for True, o parâmetro texto deve ser o caminho de um arquivo. 
    Caso contrário, o texto é exibido diretamente.
    
    Args:
        texto (str): Texto ou caminho do arquivo.
        isArquivo (bool): Indica se texto é um arquivo.
    
    Returns:
        None
    """
    
    console = Console()
    progress = Progress(refresh_per_second=60)

    if not isinstance(texto, str):
        print("O parâmetro passado não é uma string.")
        return

    if isArquivo:
        try:
            with open(texto, "r", encoding="utf-8") as f:
                conteudo = f.read()
        except FileNotFoundError:
            print("O arquivo não foi encontrado.")
            return

        with Progress() as progress:
            task = progress.add_task(f"Carregando conteúdo de {texto}...", total=120)

            progress.refresh()
            for _ in range(60):
                progress.update(task, advance=2)
                time.sleep(0.02)

        console.print(conteudo)

    else:
        with Progress() as progress:
            task = progress.add_task(f"Carregando texto...", total=120)

            progress.refresh()
            for _ in range(60):
                progress.update(task, advance=2)
                time.sleep(0.02)
        
        console.print(texto)

def carrega_caracteres_texto(texto, isArquivo):
    """
    Exibe um texto ou o nome e conteúdo de um arquivo de texto.
    Exibe uma barra indicando que o texto está sendo carregado, 
    os caracteres do texto são renderizados um de cada vez, 
    atualizando o conteúdo do terminal atual.
    
    Se isArquivo for True, o parâmetro texto deve ser o caminho de um arquivo. 
    Caso contrário, o texto é exibido diretamente.
    
    Args:
        texto (str): Texto ou caminho do arquivo.
        isArquivo (bool): Indica se texto é um arquivo.
    
    Returns:
        None
    """

    layout = Layout()
    texto_atualizado = ""

    if not isinstance(texto, str):
        print("O parâmetro passado não é uma string.")
        return

    if isArquivo:
        try:
            with open(texto, "r", encoding="utf-8") as f:
                conteudo = f.read()
        except FileNotFoundError:
            print("O arquivo não foi encontrado.")
            return

        with Live(layout, refresh_per_second=60):
            for letra in conteudo:
                texto_atualizado += letra
                layout.update(Panel(texto_atualizado))
                time.sleep(0.1)

    else:
        with Live(layout, refresh_per_second=60):
            for letra in texto:
                texto_atualizado += letra
                layout.update(Panel(texto_atualizado))
                time.sleep(0.1)
