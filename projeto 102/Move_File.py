import os
import shutil

from_dir = "C:/Users/MIRIA/Downloads"
to_dir = "C:/Users/MIRIA/Desktop/Arquivos_Documentos"

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for Arquivos_Documentos in list_of_files:
    name,extension = os.path.splitext(Arquivos_Documentos)
    #print (name)
    #print (extension) 
    if extension == '':
        continue
        if extension in [ ".txt", ".doc", ".docx," ".pdf"]:
            path1 = from_dir + '/' + Arquivos_Documentos
            path2 = to_dir + '/' + "Arquivos_Imagem"
            path3 = to_dir + '/' + "Arquivos_Imagem" + '/' + Arquivos_Documentos

        if os.path.exists(path2):
            print("movendo"+Arquivos_Documentos+"...")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("movendo"+Arquivos_Documentos+"...")
            shutil.move(path1,path3)