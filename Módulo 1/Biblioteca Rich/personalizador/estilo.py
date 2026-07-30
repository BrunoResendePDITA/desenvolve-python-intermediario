from rich.console import Console
from rich.style import Style


def texto_estilizado(texto, isArquivo):
    """
    Exibe um texto ou o nome e conteúdo de um arquivo de texto.
    Os textos exibidos são estilizados.

    Se isArquivo for True, o parâmetro texto deve ser o caminho de um arquivo. 
    Caso contrário, o texto é exibido diretamente.

    Args:
        texto (str): Texto ou caminho do arquivo.
        isArquivo (bool): Indica se texto é um arquivo.

    Returns:
        None
    """
    console = Console()

    ESTILO_ARQUIVO = Style(color="sky_blue1", bold=True)
    ESTILO_CONTEUDO = Style(color="grey93")
    ESTILO_TEXTO = Style(color="cyan1")

    ESTILO_AVISO = Style(color="red", blink=True, bold=True)
    
    if not isinstance(texto, str):
            console.print("O parâmetro passado não é uma string.", style=ESTILO_AVISO)
            return
    
    if isArquivo:
        try:
            with open(texto, "r", encoding="utf-8") as f:
                conteudo = f.read()
                console.print(f'Arquivo: {texto}', style=ESTILO_ARQUIVO)
                console.print(f'Conteúdo: {conteudo}', style=ESTILO_CONTEUDO)
        except FileNotFoundError:
            console.print("O arquivo não foi encontrado.", style=ESTILO_AVISO)
            return                        
    else:
        console.print(f'Texto: {texto}', style=ESTILO_TEXTO)


def texto_estilizado_2(texto, isArquivo):
    """
    Exibe um texto ou o nome e conteúdo de um arquivo de texto.
    Os textos exibidos são estilizados.

    Se isArquivo for True, o parâmetro texto deve ser o caminho de um arquivo. 
    Caso contrário, o texto é exibido diretamente.

    Args:
        texto (str): Texto ou caminho do arquivo.
        isArquivo (bool): Indica se texto é um arquivo.

    Returns: 
        None: Esta função apenas exibe informações no terminal.
    """
    console = Console()

    ESTILO_ARQUIVO = Style(color="deep_sky_blue1", bold=True)
    ESTILO_CONTEUDO = Style(color="white")
    ESTILO_TEXTO = Style(color="spring_green1")

    
    ESTILO_AVISO = Style(color="red", blink=True, bold=True)
    
    if not isinstance(texto, str):
            console.print("O parâmetro passado não é uma string.", style=ESTILO_AVISO)
            return

    if isArquivo:
            try:
                with open(texto, "r", encoding="utf-8") as f:
                    conteudo = f.read()
                    console.print(f'Arquivo: {texto}', style=ESTILO_ARQUIVO)
                    console.print(f'Conteúdo: {conteudo}', style=ESTILO_CONTEUDO)
            except FileNotFoundError:
                console.print("O arquivo não foi encontrado.", style=ESTILO_AVISO)
                return
    else:
        console.print(f'Texto: {texto}', style=ESTILO_TEXTO)
