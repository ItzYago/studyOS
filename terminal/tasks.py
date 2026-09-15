"""

 Exception has occurred: ModuleNotFoundError
No module named 'logic_termi'
  File "C:\Users\use\OneDrive\Documentos\studyOS\terminal\tasks.py", line 1, in <module>
    from logic_termi import termi_logic
  File "C:\Users\use\OneDrive\Documentos\studyOS\main.py", line 3, in <module>
    from terminal.tasks import tasks
ModuleNotFoundError: No module named 'logic_termi' 


"""


from logic_termi import termi_logic

def tasks():
    user = input(">")
    return termi_logic