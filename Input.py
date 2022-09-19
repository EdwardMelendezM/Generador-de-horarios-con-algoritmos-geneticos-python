from pandas import read_csv
def InputCsv(path_local): #Pasamos como parametro el path
    #Creamos Nuestro Diccionario
    Asignaturas={}
    # Cargamos los archivos
    path=read_csv(path_local,header=None) # 'NOMBRE'

    # Codigo - Nombre - Dias - Horas - Creditos - Semestre 
    #    0   -   1    -  2   -  3    -    4     -    5
    for valor in range(len(path[0])):
        if(valor!=0):
            Codigo=str(path[0][valor])
            Nombre=str(path[1][valor])
            Dias=path[2][valor].split(",")
            Horas=path[3][valor].split(",") 
            Creditos=int(path[4][valor])
            Semestre=int(path[5][valor])
            # ['7-9','7-9','7-8'] -> Horas
            for indice in range(len(Horas)):
                Horas[indice]=Horas[indice].split("-")
                Horas[indice][0],Horas[indice][1]=int(Horas[indice][0]),(int(Horas[indice][1])-1)
                if(Horas[indice][0]==Horas[indice][1]):
                    Horas[indice].pop(0)
            #dict[key] = value
            Asignaturas[Codigo]=[Dias,Horas,Nombre,Creditos,Semestre]
    return Asignaturas

