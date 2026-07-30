from rich.console import Console
from rich.layout import Layout
from rich.text import Text


def texto_com_layout(texto, isArquivo):
    """
    Exibe um texto ou o nome e conteúdo de um arquivo de texto.
    O texto ficará dentro de um container equivalente à area do terminal.
    
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
    layout["upper"].size = 2

    if not isinstance(texto, str):
        print("O parâmetro passado não é uma string.")
        return

    if isArquivo:
        try:
            with open(texto, "r", encoding="utf-8") as f:
                conteudo = f.read()

            layout["upper"].update(
                Text(f"Nome do arquivo: {texto}", style="bold sky_blue1"))
            layout["lower"].update(
                Text(f"Conteúdo do arquivo: {conteudo}", style="grey85"))
            console.print(layout)
            
        except FileNotFoundError:
            print("O caminho passado não é um arquivo.")
            return

    else:
        layout["upper"].update(
            Text("Texto comum", style="bold red")
        )

        layout["lower"].update(
            Text(texto, style="grey85")
        )

        console.print(layout)


def texto_com_layout_2(texto, isArquivo):
    """
    Exibe um texto ocupando todo espaço do terminal.
    O texto ficará dentro de um container equivalente à area do terminal.
    
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

            layout.update(
                Text(f"{texto}\n\n{conteudo}", style="grey85")
            )

            console.print(layout)

        except FileNotFoundError:
            print("O caminho passado não é um arquivo.")
            return

    else:
        layout.update(
            Text(texto, style="grey85")
        )

        console.print(layout)
