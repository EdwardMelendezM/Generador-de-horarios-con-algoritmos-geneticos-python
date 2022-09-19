from operator import itemgetter
from random import getrandbits, randint, random, choice
from Input import *

def ConstruirMolecula(individuo,num_cromosomas,cursos_ofrecidos):
    cursos_ofrecidos_binario={}
    def BuscarPoner(codigo,cursos_ofrecidos):
        for keys in cursos_ofrecidos:
            if keys==codigo:
                cursos_ofrecidos_binario[keys]=cursos_ofrecidos[keys]
    def Analizar():
        for valor in individuo:
            if(valor.binario==1):
                BuscarPoner(valor.codigo,cursos_ofrecidos)
    Analizar()
    return cursos_ofrecidos_binario

def ConstruirHorario(ListaCursos): #Recibe como parameto Todos los cursos :dict
    def NuevoHorario():
        horario={
        7:[[],[],[],[],[]]
        ,8:[[],[],[],[],[]]
        ,9:[[],[],[],[],[]],
        10:[[],[],[],[],[]],
        11:[[],[],[],[],[]],
        12:[[],[],[],[],[]],
        13:[[],[],[],[],[]],
        14:[[],[],[],[],[]],
        15:[[],[],[],[],[]],
        16:[[],[],[],[],[]],
        17:[[],[],[],[],[]],
        18:[[],[],[],[],[]],
        19:[[],[],[],[],[]],
        20:[[],[],[],[],[]]
        }
        return horario

    #                    ( matrix , 7        , 0          ,'alg lineal')
    def InsertarElemento(Dicc:dict,numero:int,posicion:int,codigo:str):
        for keys in Dicc:
            if(numero==keys):
                Dicc[keys][posicion].append(codigo)
                break
    
    def DeterminarPosicion(semana:list,dia:str):
        for indice in range(len(semana)):
            if(dia==semana[indice]):
                return indice
    Matrix=NuevoHorario()
    Semana=['lunes','martes','miercoles','jueves','viernes']
    #INICIAMOS AGREGAR TODOS LOS CURSOS
    #'C001' :[ ['lunes','miercoles','viernes']  , [[7,8],[7,8],[7]]      ,'Alg Adva',4]
    #|Keys|   |--------------------------- VALOR --------------------------------------|
    for keys in ListaCursos:
        Dias=ListaCursos[keys][0]  # ['lunes','miercoles','viernes']
        Horas=ListaCursos[keys][1] # [ [7,8] , [7,8] , [7] ]
        Nombre=ListaCursos[keys][2] # 'Alg Adva'
        for indice,valor in enumerate(Semana):
        # Semana=['lunes','martes','miercoles','jueves','viernes']
            if(valor in Dias): # [ [7,8] , [7,8] , [7] ]    
                indiceHoras=DeterminarPosicion(Dias,valor) # 0
                for HorasValor in Horas[indiceHoras]:
                    InsertarElemento(Matrix,HorasValor,indice,Nombre)
                    #               HORARIO,7,0,'Alg Adva'
    return Matrix

class Molecula:  #Objeto Binario
    def __init__(self,codigo,binario):
        self.codigo=codigo
        self.binario=binario

'''=========================================================================='''
'''=============================   RESTRICCION  ============================='''
'''=========================================================================='''
# RESTRICCION DE NO TENER DOS CURSO DEL MISMO NOMBRE
def Restriccion(Dicc:dict): #Recibe como parameto Todos los cursos :dict
    Contador=0
    def ContarIguales(elem):
        return ListaCursos.count(elem)
    #Todos los nombres de los cursos
    ListaCursos=[Dicc[keys][2] for keys in Dicc]
    for valor in ListaCursos:
        if(ContarIguales(valor)>=2):
            return False
    return True


'''=========================================================================='''
'''============================ FUNCION OBJETIVO ============================'''
'''=========================================================================='''
def CursosRetrasados(Dicc:dict):
    ListaSemestres=[]
    for keys in Dicc:
        Semestre=Dicc[keys][4]
        ListaSemestres.append(Semestre)
    Nueva={}
    for indice in range(len(ListaSemestres)):
        if( ListaSemestres[indice] not in  Nueva):
            Nueva[ListaSemestres[indice]]=ListaSemestres.count(ListaSemestres[indice])
    SemestreActual = max(Nueva, key = Nueva.get)
    CursosAdelantados=0
    for keys in Nueva:
        if(keys>SemestreActual):
            CursosAdelantados+=Nueva[keys]
        elif(keys==SemestreActual):
            CursosAdelantados+=Nueva[keys]/10
    return CursosAdelantados
    
def HorasMuertasTurnoMañana(Dicc:dict):
    TiempoPerdido=0
    # 'C001' :[ ['lunes','miercoles','viernes']  , [[7,8],[7,8],[7]]      ,'Alg Adva',4,6]
    for keys in Dicc:
        Horas=Dicc[keys][1] #[[7,8],[7,8],[7]]
        for hora in Horas:
            if(len(hora)==2):
                if(hora[0] not in [7,8,9,10,11,12]):
                    TiempoPerdido+=1
                if(hora[1] not in [7,8,9,10,11,12]):
                    TiempoPerdido+=1
            if(len(hora)==1):
                if(hora[0] not in [7,8,9,10,11,12]):
                    TiempoPerdido+=1

    return TiempoPerdido

def HorasMuertasTurnoTarde(Dicc:dict):
    TiempoPerdido=0
    # 'C001' :[ ['lunes','miercoles','viernes']  , [[7,8],[7,8],[7]]      ,'Alg Adva',4]
    for keys in Dicc:
        Horas=Dicc[keys][1] #[[7,8],[7,8],[7]]
        for hora in Horas:
            if(len(hora)==2):
                if(hora[0] not in [13,14,15,16,17,18,19,20]):
                    TiempoPerdido+=1
                if(hora[1] not in [13,14,15,16,17,18,19,20]):
                    TiempoPerdido+=1
            if(len(hora)==1):
                if(hora[0] not in [13,14,15,16,17,18,19,20]):
                    TiempoPerdido+=1

    return TiempoPerdido

def MaximosCreditos(Dicc:dict,Cmax=26): #Recibe la lista total de cursos
    SumaCreditos=sum( [Dicc[keys][3]  for keys in Dicc] )
    return (SumaCreditos-Cmax)/Cmax if SumaCreditos>Cmax else 0

def MinimosCreditos(Dicc:dict,Cmin=24): #Recibe la lista total de cursos
    SumaCreditos=sum( [Dicc[keys][3]  for keys in Dicc] )
    return (Cmin-SumaCreditos)/Cmin if SumaCreditos<Cmin else 0

def CantidadHorasCruzadas(Dicc:dict): #Recibe EL HORARIO CONSTRUIDO
    ListaHorario=[]
    cant_repetidos=0
    def AgregarListaHorario():
        for indice in range(len(dias)):
            for ind in horas[indice]:
                cadena=dias[indice]+","+str(ind)
                ListaHorario.append(cadena)
    def ContarRepetidos(valor):
        return ListaHorario.count(valor)
    for keys in Dicc:
        dias=Dicc[keys][0]
        horas=Dicc[keys][1]
        AgregarListaHorario()
    for valor in ListaHorario:
        if(ContarRepetidos(valor)>=2):
            cant_repetidos+=1
    return cant_repetidos/24    

def HorasDeAlmuerzo(Dicc:dict): 
    TotalHoraInterrumpidas=0 #Acumulador
    for keys in Dicc: # 'C001' :[ ['lunes','miercoles','viernes']  , [[7,8],[7,8],[7]]      ,'Alg Adva',4]
        Horas=Dicc[keys][1]
        for hora in Horas:
            for aux in hora:
                if(aux==13 or aux==14):
                    TotalHoraInterrumpidas+=1
    return TotalHoraInterrumpidas/10

def FuncionObjetivo(Dicc,turno,MaxCreditos,MinCreditos):
    if(turno==1):  #TURNO MAÑANA
        return 10*MaximosCreditos(Dicc,MaxCreditos)+25*MinimosCreditos(Dicc,MinCreditos)+30*CantidadHorasCruzadas(Dicc)+5*HorasDeAlmuerzo(Dicc)+0*HorasMuertasTurnoTarde(Dicc)+20*HorasMuertasTurnoMañana(Dicc)+10*CursosRetrasados(Dicc)
    elif(turno==2):#TURNO TARDE
        return 10*MaximosCreditos(Dicc)+30*MinimosCreditos(Dicc)+30*CantidadHorasCruzadas(Dicc)+0*HorasDeAlmuerzo(Dicc)+20*HorasMuertasTurnoTarde(Dicc)+0*HorasMuertasTurnoMañana(Dicc)+10*CursosRetrasados(Dicc)
    else:#CASUAL 
        return 30*MaximosCreditos(Dicc)+10*MinimosCreditos(Dicc)+40*CantidadHorasCruzadas(Dicc)+10*HorasDeAlmuerzo(Dicc)+0*HorasMuertasTurnoTarde(Dicc)+0*HorasMuertasTurnoMañana(Dicc)+10*CursosRetrasados(Dicc)
'''=========================================================================='''


'''=========================================================================='''
'''============================= CREAR POBLACION ============================'''
'''=========================================================================='''
def individuoMolecula(numero_cursos_ofrecidos:int,ListaCursosOfrecidos:dict):
    """Crear nueva poblacion"""
    ListaBinario=[]
    Valores=[ getrandbits(1) for x in range(numero_cursos_ofrecidos) ]
    Keys=[x for x in ListaCursosOfrecidos]
    for indice in range(len(Keys)):
        ListaBinario.append(Molecula(Keys[indice],Valores[indice]))
    return ListaBinario

def poblacion(numero_cursos_ofrecidos:int,ListaCursosOfrecidos:dict,NroIndividuos:int):
    return [individuoMolecula(numero_cursos_ofrecidos,ListaCursosOfrecidos) for x in range(NroIndividuos)]
'''=========================================================================='''
def Fitness(individuo,num_cromosomas,cursos_ofrecidos,turno,MaxCreditos,MinCreditos):
    cursos_ofrecidos_binario={}
    def BuscarPoner(codigo,cursos_ofrecidos):
        for keys in cursos_ofrecidos:
            if keys==codigo:
                cursos_ofrecidos_binario[keys]=cursos_ofrecidos[keys]
    def Analizar():
        for valor in individuo:
            if(valor.binario==1):
                BuscarPoner(valor.codigo,cursos_ofrecidos)
    Analizar()
    if(Restriccion(cursos_ofrecidos_binario)):
        return 1/(1+FuncionObjetivo(cursos_ofrecidos_binario,turno,MaxCreditos,MinCreditos))
        #DIVISION 1/(1+FO)

        #MINIMIZAR
        # -FO
        # 1/(1+FO)
    return 1

def NuevaRuleta(pais): #SELECCION DE RULETA
    """Selecciona un padre y una madre según las reglas de la ruleta."""
    def sortear(fitness_total, indice_a_ignorar=-1):
        #2 parámetros garantizan que no seleccionará el mismo elemento
        """Configurar la ruleta para realizar el sorteo"""
        ruleta, acumulado, valor_sorteado = [], 0, random()

        if indice_a_ignorar!=-1: #Deduce del total, la cantidad que se retirará de la ruleta
            fitness_total -= valores[0][indice_a_ignorar]

        for indice, i in enumerate(valores[0]):
            if indice_a_ignorar==indice: #ignorar el valor ya utilizado en la ruleta
                continue
            acumulado += i
            ruleta.append(acumulado/fitness_total)
            if ruleta[-1] >= valor_sorteado:
                return indice
    
    valores = list(zip(*pais)) #crea 2 listas con valores de fitness y cromosomas
    #[(-1, 159, 98, 55, -1), ([1, 0, 1, 0, 1], [0, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1])]

    fitness_total = sum(valores[0])

    indice_padre = sortear(fitness_total) 
    indice_madre = sortear(fitness_total, indice_padre)

    padre = valores[1][indice_padre]
    madre = valores[1][indice_madre]
    
    return padre, madre

def Evolucion(poblacion:list,num_cromosomas:int,cursos_ofrecidos:dict,turno,MaxCreditos:int,MinCreditos:int,mutate=0.08,):
    pais=[ [Fitness(x,num_cromosomas,cursos_ofrecidos,turno,MaxCreditos,MinCreditos),x]for x in poblacion if Fitness(x,num_cromosomas,cursos_ofrecidos,turno,MaxCreditos,MinCreditos)<1]
    sorted(pais , key=itemgetter(0))
    hijos=[]
    while(len(hijos)<num_cromosomas):
        padre,madre=NuevaRuleta(pais)
        mitad=len(padre)//2
        IndividuoNuevo=[]
        for indice in range(len(padre)):
            if(indice<mitad):
                NuevoCromosoma=Molecula(padre[indice].codigo,padre[indice].binario)
                IndividuoNuevo.append(NuevoCromosoma)
            else:
                NuevoCromosoma=Molecula(madre[indice].codigo,madre[indice].binario)
                IndividuoNuevo.append(NuevoCromosoma)
        hijos.append(IndividuoNuevo)
    #MUTACION
    for individuo in hijos:
        if(mutate>random()):
            indice_aleatorio=randint(0, len(individuo)-1)
            if individuo[indice_aleatorio].binario == 1:
                individuo[indice_aleatorio].binario = 0 
            else:
                individuo[indice_aleatorio].binario = 1
    return hijos

def Mostrar(matriz):
    for keys in matriz:
        print(keys,matriz[keys])
#----------------------------------------------------------------------------------------------------------
#---------------------------------------- FUNCION PRINCIPAL ----------------------------------------------
#----------------------------------------------------------------------------------------------------------
def AlgoritmoGenetico(CursosOfrecidos,turno=1,MaxCreditos=22,MinCreditos=24,Cromosomas=450,Generaciones=120):
    Poblacion=poblacion(len(CursosOfrecidos),CursosOfrecidos,Cromosomas)
    #Algoritmo Genetico
    for i in range(Generaciones):
        Poblacion = Evolucion(Poblacion,Cromosomas,CursosOfrecidos,turno,MaxCreditos,MinCreditos)
    for indice in range(5):
        MoleculaIndividual=Poblacion[indice]
        MoleculaDiccionario=ConstruirMolecula(MoleculaIndividual,Cromosomas,CursosOfrecidos)
        Matriz=ConstruirHorario(MoleculaDiccionario)
    OutPut=[['HORAS','LUNES','MARTES','MIERCOLES','JUEVES','VIERNES']]
    for keys in Matriz:
        Aux=[]
        Aux.append(keys)
        for valor in Matriz[keys]:
            if len(valor)>=1:
                Aux.append(valor[0])
            else:
                Aux.append("    ")
        OutPut.append(Aux)
    #[['HORAS','LUNES','MARTES','MIERCOLES','JUEVES','VIERNES']]
    # ['  7  ',' MAT ',' ALG  ','  MAT    ','  ALG ','  MAT  ']
    # ['  8 ',' MAT ',' ALG  ','  MAT    ','  ALG ','  MAT  ']
    # ['  9 ',' MAT ',' ALG  ','  MAT    ','  ALG ','  MAT  ']
    # [' 10 ',' MAT ',' ALG  ','  MAT    ','  ALG ','  MAT  ']]


    return OutPut