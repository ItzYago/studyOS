##Lógica do terminal
from rich import print
import sys
"""
  File "c:\Users\use\OneDrive\Documentos\studyOS\terminal\quest.py", line 3, in <module>
    from terminal.logic_terminal import terminal_logic
  File "c:\Users\use\OneDrive\Documentos\studyOS\terminal\logic_terminal.py", line 21
    elif user == "exit":
    ^^^^
SyntaxError: invalid syntax
"""
from terminal.decoracao import decoracao

def terminal_logic(user):

    if user == "help":
        return decoracao()
    print("[bold green]Comandos disponíveis:" \
        "\n""[/bold green]")
    print("[bold green]Português[/bold green]" \
        "\n[bold green]Matemática[/bold green]" \
        "\n[bold green]Química[/bold green]" \
        "\n[bold green]Física[/bold green]" \
        "\n[bold green]História[/bold green]" \
        "\n[bold green]Espanhol[/bold green]")
    return terminal_logic(input(">"))

    elif user == "exit":
    return print("[italic red]Saindo do terminal[/italic red]") or sys.exit(0)
    else:
        print("[italic red]Comando não encontrado.\n"
        "Digite 'help' para ver a lista de comandos disponíveis.[/italic red]")
        return terminal_logic(input(">"))