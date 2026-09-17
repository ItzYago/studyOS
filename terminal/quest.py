                  ## AQUI FICAM AS PERGUNTAS DO TERMINAL

from terminal.logic_terminal import terminal_logic

def questions():
    user = input(">").upper().lower()
    return terminal_logic(user)