#Precisa ser Salvo como executável e agendado para execução
# nos dias e horários desejáveis:
import os
import glob

py_files = glob.glob('C:\\Users\\Administrador1\\Desktop\\*.*[!lnk]')

for py_file in py_files:
   try:
       os.remove(py_file)
   except OSError as e:
       print(f"Error:{e.strerror}")
