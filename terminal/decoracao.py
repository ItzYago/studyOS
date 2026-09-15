##adicionar o código do terminal aqui
from rich import print
from rich.console import Console

def decoracao():

    console = Console()
    console.print(r"""
[bold cyan]
╔══════════════════════════════════════════════════╗
║                                                  ║
║              ███████╗████████╗██╗   ██╗         ║
║              ██╔════╝╚══██╔══╝╚██╗ ██╔╝         ║
║              ███████╗   ██║    ╚████╔╝          ║
║              ╚════██║   ██║     ╚██╔╝           ║
║              ███████║   ██║      ██║            ║
║              ╚══════╝   ╚═╝      ╚═╝            ║
║                                                  ║
║                 S T U D Y   O S                  ║
║                                                  ║
╚══════════════════════════════════════════════════╝
[/bold cyan]
""")

    print("[bold green]Bem-vindo ao terminal do studyOS![/bold green]")
    print("[bold blue]Digite 'help' para ver os comandos disponíveis.[/bold blue]")