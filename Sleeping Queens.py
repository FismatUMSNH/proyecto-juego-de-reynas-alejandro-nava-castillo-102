#Este Juego Fue Programado Por:
#Alejandro Nava Castillo
#Estudiante De 1er Semestre de
import random
import sys
print "Bienvenido al juego Sleeping Queens!".center(0," ")
c=raw_input("Conoces Las Reglas De este Juego(Enter si/n no)")
if c=="no" or c=="n":
  print '''

  Este Juego Fue Programado Por Alejandro Nava Castillo
  Estudiante De Primer Semestre(102) De La Facultad FISMAT De La UMSH Como Proyecto Final Del Curso De Programacion

  Los Derechos De Este Juego Pertenecen a Gamewright y Solo Han Sido Replicados Sin Fines De Lucro '''
  raw_input
  print '''
  Este es un juego para 2-5 jugadores, que trabaja con una baraja modificada,con cartas con efectos diversos como seran descritos a continuacion, y que esta conformada por:

  12 Reinas:Son cartas que se apartan del mazo y se colocan "Dormidas" bocabajo, el objetivo del juego es conseguir "Despertarlas"
  8 reyes: Tienen el poder de despertar una reina durmiente.
  4 Caballeros:  Roban una reina de tu oponente.
  3 Dragones:(CARTA REACCION)  Enfrentan a los caballeros evitando que roben una de tus reinas.
  4 Pociones de dormir:  Pone a dormir una reina de tu oponente.
  3 Varitas magicas:(CARTA REACCION)  Te defiende de la Pocion de Dormir.
  5 Bufones:(CARTA DE RIESGO)  Deberas robar la siguiente carta del mazo. Si es una carta con algun efecto la conservas y obtienes un turno extra, si es un numero se cuenta empezando contigo hacia la izquierda. El ultimo jugador en ser contado podra despertar una reina.
  Cartas con numeros:  El juego contiene cuatro grupos de cartas numeradas del 1 al 10, Las cuales pueden ser descartadas en pares, tercios, o como sumas utilizando las cartas como sumandos y resultado, en cuyo caso se pueden bajar tantas como sea posible
  '''
  raw_input("Instrucciones")
  print '''
  Al empezar el juego, se colocan las reinas bocabajo, y se reparten 5 cartas a cada jugador, despues de lo cual, el juegos comienza.

  Al empezar el turno, el jugador utilizara alguna de sus cartas para usar su efecto, en cuyo caso debera elegir como o contra quien usarla, y despues de resolver los efectos pertinentes, tomara otra carta(en caso de no haberse topado con alguna resistencia).

  Si el jugador intenta robar o dormir una reina rival, el contrario podra defenderse si tiene la carta de reaccion correcta, despues de lo cual ambos descartaran sus cartas y tomaran una nueva.

  O descartara cartas numericas de acuerdo a las condiciones dadas antes con el fin de tomar el mismo numero de cartas desde el mazo
  '''
  raw_input("Fin Del Juego")
  print '''
  El juego concluye cuando alguno de los jugadores optiene 5 reinas o 50 puntos si se juega de 2-3 personas; Y 4 reinas o 40 puntos si son de 4-5 personas

  El juego termina en el instante en el que algun jugador cumple con las condiciones establecidas arriba, sin poder hacerse nada al respecto de no haberse hecho antes
  '''
  raw_input("Condiciones Especiales")
  print '''
  Durante el juego, el mazo terminara acabandose. En tal caso, solo se necesita volver a barajar las cartas restantes y volver a repartirlas.

  Pueden ocurrir casos como ser atacado y contratacar con un dragon, ser dormido y contrarestar con varita o las condiciones propias del bufon, pero hay 2 casos en que despertar una reina activara un efecto

  1.-Si se logra despertar a la Reina Rosa, esta podra traes consigo a otra reina durmiente. Este efecto no aplica si la reina es robada, pero puede aplicarse si es dormida y vuelta a despertar

  2.-Si se despierta a la Reina Perro teniendo previamente a la Reina Gato, esta ultima debera volver a ponerse bocabajo, puesto que los gatos y los perros no se llevan bien. Lo mismo ocurrira a la inversa
  '''
  raw_input("Conclusiones")
  print '''
  Sleeping Queens es un juego original y muy divertido, comprobado por alumnos de la calse 2 de la facultad de Ciencias Fisico-Matematicas y por muchos jugadores a lo largo del mundo. Espero que esta version, aunque imperfecta y digital pueda entretenerte tanto como a nosotros

    Asi que a fin de cuentas...Destruye A Tus Rivales!, Hurta El Fruto De Su Fortuna Y Miralos Llorar Y Retorcerse En Su Impotencia! Pero Cuidado, podrian estar pensando en hacerte lo mismo a ti...
    '''
lista_jugadores=["j1","j2","j3","j4","j5"]
reinas=["Reina Arcoiris","Reina Pastel","Reina Starfish","Reina Rosa","Reina Mariquita","Reina Girasol","Reina Pavo","Reina Luna","Reina Gato","Reina Perro","Reina Panqueque","Reina Corazon"]
reinas_value=[5,5,5,5,10,10,10,10,15,15,15,20]
#datos para robos
reinasc=["Reina Arcoiris","Reina Pastel","Reina Starfish","Reina Rosa","Reina Mariquita","Reina Girasol","Reina Pavo","Reina Luna","Reina Gato","Reina Perro","Reina Panqueque","Reina Corazon"]
reinas_valuec=[5,5,5,5,10,10,10,10,15,15,15,20]
numericas=range(1,11)
carta=[]
for i in (4*(range(1,11))):
  x=i
  carta.append(x)
rey=["rey","rey","rey","rey","rey","rey","rey","rey"]
bufon=["bufon","bufon","bufon","bufon","bufon"]
caballero=["caballero","caballero","caballero","caballero"]
pocion=["pocion","pocion","pocion","pocion",]
varita=["varita","varita","varita"]
dragon=["dragon","dragon","dragon"]
baraja=carta+rey+bufon+caballero+pocion+varita+dragon
mazo=[]
while len(baraja)>0:
  y=random.choice(baraja)
  baraja.remove(y)
  mazo.append(y)
#enlistar jugadores
lista_jugadores=["j1","j2","j3","j4","j5"]
lj=["J1","J2","J3","J4","J5"]
nj=input("Este juego trabaja con 2-5 jugadores, Cuantos Jugadores Participaran?")
while nj<2:
  print "No son suficientes judadores"
  nj=input("Por favor, ingrese otro numero")
  while nj>5:
    print "El numero de jugadores excede el permitido"
    nj=input("Por favor, ingrese otro numero")
while nj>5:
  print "El numero de jugadores excede el permitido"
  nj=input("Por favor, ingrese otro numero")
  while nj<2:
    print "No son suficientes judadores"
    nj=input("Por favor, ingrese otro numero")
print nj
jitinerable=range(0,nj)
#Dar Mano
mano1=[]
mano2=[]
mano3=[]
mano4=[]
mano5=[]
manos=[mano1,mano2,mano3,mano4,mano5]
eliminardemano=5-nj
if eliminardemano==0:
  manos=[mano1,mano2,mano3,mano4,mano5]
if eliminardemano==1:
  manos=[mano1,mano2,mano3,mano4]
if eliminardemano==2:
  manos=[mano1,mano2,mano3]
if eliminardemano==3:
  manos=[mano1,mano2]
#tpa no trabaja adecuadamente, remplazo
tbj=[1,2,3,4,5]
tba=[]
for i in range(0,nj):
  x=tbj[i]
  tba.append(x)
#Def de juego
def gameover(x):
  if nj<4:
    if jp[x]>=50:
      print "**********MUCHAS FELICIDADES Al Jugador".center(0," ")+str(tj[0]), "POR HABER CONSEGUIDO 50 PUNTOS Y GANAR EL JUEGO!!!!**********"
      raw_input("Pulsa Cualquir Tecla Para Finalizar")
      sys.exit(0)
    if jr[x].count(0)==0:
      print "**********MUCHAS FELICIDADES Al Jugador".center(0," ")+str(tj[0]), "POR HABER CONSEGUIDO 5 REINAS Y GANAR EL JUEGO!!!!**********"
      raw_input("Pulsa Cualquir Tecla Para Finalizar")
      sys.exit(0)
    else:
      nada="nada"
  if nj<6:
    if jp[x]>=40:
      print "**********MUCHAS FELICIDADES Al Jugador".center(0," ")+str(tj[0]), "POR HABER CONSEGUIDO 40 PUNTOS Y GANAR EL JUEGO!!!!**********"
      raw_input("Pulsa Cualquir Tecla Para Finalizar")
      sys.exit(0)
    if jr[x].count(0)==1:
      print "**********MUCHAS FELICIDADES Al Jugador".center(0," ")+str(tj[0]), "POR HABER CONSEGUIDO 4 REINAS Y GANAR EL JUEGO!!!!**********"
      raw_input("Pulsa Cualquir Tecla Para Finalizar")
      sys.exit(0)
    else:
      nada="nada"
def tienes(x):
  print "No Tienes Esa Carta, Por Favor Ingrese Una Valida"
  print " "
  print "Tu Mano Tiene",manos[0]
  print " "
  eleccionj=input(panel)
  eleccionf(eleccionj)
def sacar(x):
  y=mazo[0]
  x.append(y)
  cartasrestantes=len(mazo)
  if cartasrestantes==0:
    baraja=carta+rey+bufon+caballero+pocion+varita+dragon
    while len(baraja)>0:
      y=random.choice(baraja)
      baraja.remove(y)
      mazo.append(y)
def dar_mano(x):
  while len(x)<5:
    y=mazo[0]
    x.append(y)
    mazo.remove(y)
for i in range(0,nj):
  dar_mano(manos[i])
print len(mazo)
def sacarm(x):
  y=random.choice(mazo)
  manos[x].append(y)
  mazo.remove(y)   #Cuidado con este bastardo
  cartasrestantes=len(mazo)
  if cartasrestantes==0:
    baraja=carta+rey+bufon+caballero+pocion+varita+dragon
    for i in range(0,len(manos)):
      manoaromever=manos[i]
      for i in range(0,len(manoaromever)):
        cartaaremover=manoaromever[i]
        baraja.remove(cartaaremover)
    while len(baraja)>0:
      y=random.choice(baraja)
      baraja.remove(y)
      mazo.append(y)
#4 paneles de eleccion principal y basico
panel='''Oprima El Boton Indicado Para Ejecutar Accion
Usar Rey       (1)
Usar Caballero (2)
Usar Bufon     (3)
Usar Pocion    (4)
Tirar Cartas   (5)
Tirar Dragon   (6)
Tirar Varita   (7)
Ver Reinas     (8)
'''
paneltirar='''Oprima El Boton Indicado Para Ejecutar Accion
Tirar 1 sola carta        (1)
Tirar Un Par              (2)
Tirar Una Tercia          (3)
Tirar 4 Cartas Iguales    (4)
Tirar Una Operacion       (5)
Matematica
O Puedes Tirar Una Carta  (6)
Sin Usar Su Efecto
'''
panelcaballero='''A Quien Robaras?(No Podras Robar Si No Esta Jugando)'''
panelpocion='''Contra Quien La Usaras?(No Podras Robar Si No Esta Jugando)'''
panelvarita='''Usar Varita?
Si(1)
No(2)'''
paneldragon='''Usar Dragon?
Si(1)
No(2)'''
#propiedades de los jugadores--------------------------
T1="Es el turno del jugador 1"
T2="Es el turno del jugador 2"
T3="Es el turno del jugador 3"
T4="Es el turno del jugador 4"
T5="Es el turno del jugador 5"
j1r=[0,0,0,0,0]
j2r=[0,0,0,0,0]
j3r=[0,0,0,0,0]
j4r=[0,0,0,0,0]
j5r=[0,0,0,0,0]
j1p=0
j2p=0
j3p=0
j4p=0
j5p=0
jr=[j1r,j2r,j3r,j4r,j5r]
jp=[j1p,j2p,j3p,j4p,j5p]
tjbb=[1,2,3,4,5]
#Propiedades Grupales---------------------------
#robar=raw_input(panelcaballero)
#respuestavarita=raw_input("Intentan Dormir A Tu " + reinadormida+" "+(panelvarita))
#respuestacaballero=raw_input("Intentan Robar A Tu " + reinaurtada+" "+(paneldragon))
#
#comandos de batalla
def card(nj):
  while nj<1 and nj<7:
    print "No es una opcion valida1"
    nj=input("Por favor, ingrese otra")
  while nj>1 and nj>7:
    print "No es una opcion valida3"
    nj=input("Por favor, ingrese otra")
  while nj<1 and nj<7:
    print "No es una opcion valida4"
    nj=input("Por favor, ingrese otra")
  while nj>=1 and nj<=7:
    return nj
#
def menudedevolucion(x):
  print '''
  En Tu Mano Hay''', manos[x]
  eleccionj=input(panel)
  eleccionj=card(eleccionj)
  eleccionf(eleccionj)
  eleccion(eleccionj)
#
def reyf(x):
  if len(reinas)==0:
    print "No Hay Reinas Por Despertar", lj[x],"Pierde A Su Rey"
    manos[x].remove("rey")
  else:
    awake=random.choice(reinas)
    print "Has Despertado A", awake
    nawake=reinas.index(awake)
    wpoint=reinas_value[nawake]
    reinas.remove(awake)
    jr[0].append(awake)
    jr[0].remove(0)
    jp[0]=jp[0]+wpoint
    reinas_value.remove(wpoint)
    if awake=="Reina Gato":
      if "Reina Perro" in jr[0]:
        print '''Oh no!, Tu Reina Perro Ataco a tu Reina Gato! Tuviste que volver a dormir a tu Reina Gato...'''
        jr[0].remove("Reina Gato")
        jr[0].append(0)
        reinas.append("Reina Gato")
        jp[0]=jp[0]-wpoint
        reinas_value.append(15)
        print "Tus reinas ahora son: ",jr[0]
        print "Actualmente tienes", jp[0], "puntos"
        return jp[0]
      else:
        nada="nada"
    if awake=="Reina Perro":
      if "Reina Gato" in jr[0]:
        print '''Oh no!, Tu Reina Gato Ataco a tu Reina Perro! Tuviste que volver a dormir a tu Reina Perro...'''
        jr[0].remove("Reina Perro")
        jr[0].append(0)
        reinas.append("Reina Perro")
        jp[0]=jp[0]-wpoint
        reinas_value.append(15)
        print "Tus reinas ahora son: ",jr[0]
        print "Actualmente tienes", jp[0], "puntos"
        return jp[0]
      else:
        nada="nada"
    if awake=="Reina Rosa":
      print "La Gran Reina Rosa Te Permite Despertar otra Reina!"
      manos[0].append("rey")
      jp[0]=reyf(0)+5
    print "Tus reinas ahora son: ",jr[0]
    print "Actualmente tienes", jp[0], "puntos"
    manos[0].remove("rey")
    sacarm(0)
    gameover(0)
    return jp[0]
#
def reyfb(x):
  if len(reinas)==0:
    print "No Hay Reinas Por Despertar", lj[x], "Pierde A Su Oportunidad"
  else:
    awake=random.choice(reinas)
    print "Has Despertado A", awake
    nawake=reinas.index(awake)
    wpoint=reinas_value[nawake]
    reinas.remove(awake)
    jr[0].append(awake)
    jr[0].remove(0)
    jp[0]=jp[0]+wpoint
    reinas_value.remove(wpoint)
    if awake=="Reina Gato":
      if "Reina Perro" in jr[0]:
        print '''Oh no!, Tu Reina Perro Ataco a tu Reina Gato! Tuviste que volver a dormir a tu Reina Gato...'''
        jr[0].remove("Reina Gato")
        jr[0].append(0)
        reinas.append("Reina Gato")
        jp[0]=jp[0]-wpoint
        reinas_value.append(15)
        print "Tus reinas ahora son: ",jr[0]
        print "Actualmente tienes", jp[0], "puntos"
        return jp[0]
      else:
        nada="nada"
    if awake=="Reina Perro":
      if "Reina Gato" in jr[0]:
        print '''Oh no!, Tu Reina Gato Ataco a tu Reina Perro! Tuviste que volver a dormir a tu Reina Perro...'''
        jr[0].remove("Reina Perro")
        jr[0].append(0)
        reinas.append("Reina Perro")
        jp[0]=jp[0]-wpoint
        reinas_value.append(15)
        print "Tus reinas ahora son: ",jr[0]
        print "Actualmente tienes", jp[0], "puntos"
        return jp[0]
      else:
        nada="nada"
    if awake=="Reina Rosa":
      print "La Gran Reina Rosa Te Permite Despertar otra Reina!"
      jp[0]=reyfb(0)+5
    print "Tus reinas ahora son: ",jr[0]
    print "Actualmente tienes", jp[0], "puntos"
    gameover(0)
    return jp[0]
#
def robarmando(x):
  for i in range(0,len(tj)-1):
    print "Las Reinas Del Jugador", tj[i+1],"Son", jr[i+1],"(",(i+1),")"
  print " "
  robar=input(panelcaballero)
  print " "
  if robar==robar:
    porrobar=input("En que lugar esta la reina a robar?")
    conteo=(jr[robar].count(0))
    ultimorobo=jr[robar][porrobar-1]
    if ultimorobo==0:
      print "No Hay Ninguna Reina Ahi, Tu Caballero Se Perdio En El Camino"
      manos[x].remove("caballero")
      sacarm(x)
    else:
      if "dragon" in manos[robar]:
        print "Jugador",tj[robar], "Tenia un Dragon, no pudiste robar"
        manos[x].remove("caballero")
        sacarm(x)
        manos[robar].remove("dragon")
        sacarm(robar)
      elif conteo<5:
        robolugar=reinasc.index(ultimorobo)
        robopoint=reinas_valuec[robolugar]
        jp[x]=jp[x]+robopoint
        jp[robar]=jp[robar]-robopoint
        jr[robar][porrobar-1]=0
        jr[x].insert(0,ultimorobo)
        jr[x].remove(0)
        print "           Has Robado Exitosamente a", ultimorobo+"!"
        manos[x].remove("caballero")
        sacarm(x)
        print "J"+str(tj[robar]), "Ahora tiene:"
        print jr[robar], "Reinas"
        print "Y", jp[robar], "Puntos"
        print "J"+str(tj[x]),"Ahora Tiene"
        print jr[x], "Reinas"
        print "Y", jp[x], "Puntos"
        gameover(0)
      else:
        print "No habia reina, no pudiste robar"
#
def bufonf(x):
  cantidad=len(tpa)
  manos[x].remove("bufon")
  sacarm(x)
  bufada=manos[x][4]
  print "Has Sacado", bufada
  neoj=[]
  if bufada in range(1,11):
    print "Es de Numero"
    print " "
    for i in range(0,len(tpa)):
      x=(i+1)
      neoj.append(x)
    for i in range(0,bufada-1):
      sacar=neoj.pop(0)
      neoj.append(sacar)
    buforeina=neoj[0]
    if buforeina==1:
      print "El Jugador", tjbb[buforeina-1], "Despierta A Una Reina Gracias Al bufon!"
      reyfb(x)
      print " "
    if buforeina!=1:
      print "El Jugador", tjbb[buforeina-1], "Despierta A Una Reina Gracias Al bufon!"
      reynf(buforeina-1)
      print " "
  elif bufada!=1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
    print "No es un Numero"
    print "Has Conseguido", bufada, "Obtienes Otro Turno"
    menudedevolucion(x)
def pocionf(x):
  for i in range(0,len(tj)-1):
    print "Las Reinas Del Jugador", tj[i+1],"Son", jr[i+1],"(",(i+1),")"
  dormir=input(panelpocion)
  if dormir==dormir:
    pordormir=input("En Que Lugar Esta La Reina A Dormir?")
    conteo=(jr[dormir].count(0))
    ultimodormir=jr[dormir][pordormir-1]
    if ultimodormir==0:
      print "No Hay Ninguna Reina Ahi, Tu Pocion Se Te Cae De Las Manos"
      manos[x].remove("pocion")
      sacarm(x)
    else:
      if "varita" in manos[dormir]:
        print "Jugador",tj[dormir], "Tenia Una Varita, No Pudiste Dormir Su Reina"
        manos[x].remove("pocion")
        sacarm(x)
        manos[dormir].remove("varita")
        sacarm(dormir)
      elif conteo<5:
        dormirlugar=reinasc.index(ultimodormir)
        dormirpoint=reinas_valuec[dormirlugar]
        jp[dormir]=jp[dormir]-dormirpoint
        jr[dormir][pordormir-1]=0
        print "           Has Dormido Exitosamente a", ultimodormir+"!"
        manos[x].remove("pocion")
        sacarm(x)
        print "J"+str(tj[dormir]), "Ahora tiene:"
        print jr[dormir], "Reinas"
        print "Y", jp[dormir], "Puntos"
      else:
        print "No Habia Reina, No Pudiste Dormirla"
#
#
def tirarf(x):
  qtiro=input(paneltirar)
  if qtiro==1:
    atirar=input("Que Carta Tiraras?")
    if manos[x].count(atirar)>=1:
      for i in range(0,1):
        manos[x].remove(atirar)
        sacarm(x)
      print manos[x]
    else:
      print "Esa No Es Una Opcion Valida, Seras Devuelto Al Panel Anterior"
      menudedevolucion(x)
  if qtiro==2:
    atirar=input("Que Cartas Tiraras?")
    if manos[x].count(atirar)>=2:
      for i in range(0,2):
        manos[x].remove(atirar)
        sacarm(x)
      print manos[x]
    else:
      print "No Tienes Tantas Cartas De Ese Tipo"
      print "Seras Devuelto Al Panel Anterior"
      menudedevolucion(x)
  if qtiro==3:
    atirar=input("Que Cartas Tiraras?")
    if manos[x].count(atirar)>=3:
      for i in range(0,3):
        manos[x].remove(atirar)
        sacarm(x)
      print manos[x]
    else:
      print "No Tienes Tantas Cartas De Ese Tipo"
      print "Seras Devuelto Al Panel Anterior"
      menudedevolucion(x)
  if qtiro==4:
    atirar=input("Que Cartas Tiraras?")
    if manos[x].count(atirar)>=4:
      for i in range(0,4):
        manos[x].remove(atirar)
        sacarm(x)
      print manos[x]
    else:
      print "No Tienes Tantas Cartas De Ese Tipo"
      print "Seras Devuelto Al Panel Anterior"
      menudedevolucion(x)
  if qtiro==5:
    atirar1=input("Cual Es La Primera Carta?")
    atirar2=input("Cual Es La segunda Carta?")
    sumaqtiro=atirar1+atirar2
    if manos[x].count(atirar1)>=1 and manos[x].count(atirar2)>=1 and manos[x].count(sumaqtiro)>=1:
      print "No mames, salio!"
      manos[x].remove(atirar1)
      manos[x].remove(atirar2)
      manos[x].remove(sumaqtiro)
      sacarm(x)
      sacarm(x)
      sacarm(x)
    else:
      print '''
      No Tienes Las Cartas Que Representan Los Sumandos O El Resultado De Tu Operacion, Por Favor Revisa Tu Mano
      Seras Devuelto Al Panel Anterior
      '''
      menudedevolucion(x)
  if qtiro==6:
    cartanoquerida=raw_input("Por Favor Escriba Que Carta Tirara(Su Efecto No Sera Usado, Cartas De Respuesta Pueden Ser Tiradas Desde Sus Respectivas Opciones)")
    if manos[x].count(cartanoquerida)>=1:
      manos[x].remove(cartanoquerida)
      print "Tiro", cartanoquerida
      sacarm(x)
    else:
      print '''No Tienes Ese Tipo De Carta
      Seras Devuelto Al Panel Anterior'''
      menudedevolucion(x)
def dragonf(x):
  if manos[x].count("dragon")>=1:
    print "Has Tirado Un Dragon"
    manos[x].remove("dragon")
    sacarm(x)
  else:
      print '''No Tienes Ese Tipo De Carta
      Seras Devuelto Al Panel Anterior'''
      menudedevolucion(x)
def varitaf(x):
  if manos[x].count("varita")>=1:
    print "Has Tirado Una Varita"
    manos[x].remove("varita")
    sacarm(x)
  else:
      print '''No Tienes Ese Tipo De Carta
      Seras Devuelto Al Panel Anterior'''
      menudedevolucion(x)
def eleccion(e):
  if e==1:
    print lj[0], "Uso Rey"
  if e==2:
    print lj[0], "Eligio Caballero"
  if e==3:
    print lj[0], "Eligio Bufon"
  if e==4:
    print lj[0], "Eligio Pocion"
  if e==5:
    print lj[0], "Tiro Cartas"
  if e==6:
    print lj[0], "Tiro Dragon"
  if e==7:
    print lj[0], "Tiro Varita"
  if e==8:
    print "Aun Faltan Por Despertar", len(reinas), "Reinas"
    print " "
    for i in range(0,nj):
      print "Reinas Del Jugador", tj[i], jr[i]
      print "Y Tiene", jp[i], "Puntos"
      print " "
    print " "
    if raw_input("Necesita Ver El Valor De Las Reinas?(S/Enter)")=="s":
      print " "
      for i in range(0,12):
        print reinas[i], str(reinas_value[i]),"Puntos"
    print '''
    En Tu Mano Hay'''
    print manos[0]
    eleccionj=input(panel)
    card(eleccionj)
    eleccionf(eleccionj)
    eleccion(eleccionj)
#
def eleccionf(eleccionj):
  if eleccionj==1:
    if "rey" in manos[0]:
      reyf(0)
    else:
      tienes(0)
  elif eleccionj==2:
    if "caballero" in manos[0]:
      robarmando(0)
    else:
      tienes(0)
  elif eleccionj==3:
    if "bufon" in manos[0]:
      bufonf(0)
    else:
     tienes(0)
  elif eleccionj==4:
    if "pocion" in manos[0]:
      pocionf(0)
    else:
      tienes(0)
  elif eleccionj==5:
    if "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" or "10" in manos[0]:
      tirarf(0)
    else:
      tienes(0)
  elif eleccionj==6:
    if "dragon" in manos[0]:
      dragonf(0)
    else:
      tienes(0)
  elif eleccionj==7:
    if "varita" in manos[0]:
      varitaf(0)
    else:
      tienes(0)
#Elecciones Enemigas
def ahoran(x):
  print lj[x], "Ahora Tiene"
  print jr[x], "Reinas"
  print "Y", jp[x], "Puntos"
def reyn(x):
  print "El Jugador", tjbb[x], "Usa A Un Rey"
  if len(reinas)==0:
    print "No Hay Reinas Por Despertar", lj[x],"Pierde A Su Rey"
    manos[x].remove("rey")
  else:
    awake=random.choice(reinas)
    print lj[x], "Ha Despertado A", awake
    nawake=reinas.index(awake)
    wpoint=reinas_value[nawake]
    reinas.remove(awake)
    jr[x].append(awake)
    jr[x].remove(0)
    jp[x]=jp[x]+wpoint
    reinas_value.remove(wpoint)
    if awake=="Reina Gato":
      if "Reina Perro" in jr[x]:
        print '''Oh no!, Su Reina Perro Ataco a Su Reina Gato! Tuvo Que Volver A Dormir A Su Reina Gato...'''
        jr[x].remove("Reina Gato")
        jr[x].append(0)
        reinas.append("Reina Gato")
        jp[x]=jp[x]-wpoint
        reinas_value.append(15)
        manos[x].remove("rey")
        print "Sus Reinas Ahora Son: ",jr[x]
        print "Actualmente Tiene", jp[x], "Puntos"
        gameover(x)
        return jp[x]
      else:
        nada="nada"
    if awake=="Reina Perro":
      if "Reina Gato" in jr[x]:
        print '''Oh no!, Su Reina Gato Ataco a Su Reina Perro! Tuvo que volver a dormir a Su Reina Perro...'''
        jr[x].remove("Reina Perro")
        jr[x].append(0)
        reinas.append("Reina Perro")
        jp[x]=jp[x]-wpoint
        manos[x].remove("rey")
        reinas_value.append(15)
        print "Sus Reinas Ahora Son: ",jr[x]
        print "Actualmente Tiene", jp[x], "Puntos"
        gameover(x)
        return jp[x]
      else:
        nada="nada"
    if awake=="Reina Rosa":
      print "La Gran Reina Rosa Le Permite Despertar otra Reina!"
      manos[x].append("rey")
      jp[x]=reyn(x)+5
    gameover(x)
    print "Sus Reinas Ahora Son: ",jr[x]
    print "Actualmente Tiene", jp[x], "Puntos"
    return jp[x]
def reynf(x):  #necesario para el funcionamiento del bufon aliado
    if len(reinas)==0:
      print "No Hay Reinas Por Despertar", lj[x],"Pierde A Su Oportunidad"
    else:
        awake=random.choice(reinas)
        print lj[x], "Ha Despertado A", awake
        nawake=reinas.index(awake)
        wpoint=reinas_value[nawake]
        reinas.remove(awake)
        jr[x].append(awake)
        jr[x].remove(0)
        jp[x]=jp[x]+wpoint
        reinas_value.remove(wpoint)
        if awake=="Reina Gato":
          if "Reina Perro" in jr[x]:
            print '''Oh no!, Su Reina Perro Ataco a Su Reina Gato! Tuvo Que Volver A Dormir A Su Reina Gato...'''
            jr[x].remove("Reina Gato")
            jr[x].append(0)
            reinas.append("Reina Gato")
            jp[x]=jp[x]-wpoint
            reinas_value.append(15)
            print "Sus Reinas Ahora Son: ",jr[x]
            print "Actualmente Tiene", jp[x], "Puntos"
            gameover(x)
            return jp[x]
          else:
            nada="nada"
        if awake=="Reina Perro":
          if "Reina Gato" in jr[x]:
            print '''Oh no!, Su Reina Gato Ataco a Su Reina Perro! Tuvo que volver a dormir a Su Reina Perro...'''
            jr[x].remove("Reina Perro")
            jr[x].append(0)
            reinas.append("Reina Perro")
            jp[x]=jp[x]-wpoint
            reinas_value.append(15)
            print "Sus Reinas Ahora Son: ",jr[x]
            print "Actualmente Tiene", jp[x], "Puntos"
            gameover(x)
            return jp[x]
          else:
            nada="nada"
        if awake=="Reina Rosa":
          print "La Gran Reina Rosa Le Permite Despertar otra Reina!"
          jp[x]=reynf(x)+5
        gameover(x)
        print "Sus Reinas Ahora Son: ",jr[x]
        print "Actualmente Tiene", jp[x], "Puntos"
        return jp[x]
def caballeron(x):
    print "El Jugador",lj[x],"Le hecho El Ojo A tu Reina"
    robarmachin=jr[0][4]
    if robarmachin==0:
      robarmachin=jr[0][3]
      if robarmachin==0:
        robarmachin=jr[0][2]
        if robarmachin==0:
          robarmachin=jr[0][1]
          if robarmachin==0:
            robarmachin=jr[0][0]
    lugarurto=jr[0].index(robarmachin)
    if "dragon" in manos[0]:
      print "Intentan Robar A Tu Reina!"
      eleccionf=raw_input(paneldragon)
      if eleccionf=="2":
        robolugar=reinasc.index(robarmachin)
        robopoint=reinas_valuec[robolugar]
        jp[x]=jp[x]+robopoint
        jp[0]=jp[0]-robopoint
        jr[0][lugarurto]=0
        jr[x].insert(0,robarmachin)
        jr[x].remove(0)
        print "     Te Han Robado A", robarmachin
        manos[x].remove("caballero")
        sacarm(x)
        print " "
        print lj[0], "Ahora tiene:"
        print jr[0], "Reinas"
        print "Y", jp[0], "Puntos"
        print " "
        print lj[x], "Ahora Tiene"
        print jr[x], "Reinas"
        print "Y", jp[x], "Puntos"
        print " "
        gameover(x)
      if eleccionf=="1":
        print "Usaste un Dragon, No Te Pudieron Robar"
        manos[x].remove("caballero")
        sacarm(x)
        manos[0].remove("dragon")
        sacarm(0)
    else:
      robolugar=reinasc.index(robarmachin)
      robopoint=reinas_valuec[robolugar]
      jp[x]=jp[x]+robopoint
      jp[0]=jp[0]-robopoint
      jr[0][lugarurto]=0
      jr[x].insert(0,robarmachin)
      jr[x].remove(0)
      print "     Te Han Robado Sin Que Pudieras Defender a", robarmachin
      manos[x].remove("caballero")
      sacarm(x)
      print " "
      print lj[0], "Ahora tiene:"
      print jr[0], "Reinas"
      print "Y", jp[0], "Puntos"
      print " "
      print lj[x], "Ahora Tiene"
      print jr[x], "Reinas"
      print "Y", jp[x], "Puntos"
      print " "
      gameover(x)
def bufonn(x):
  print "El Jugador", tjbb[x], "Usa Un Bufon"
  cantidad=len(tba)
  manos[x].remove("bufon")
  sacarm(x)
  bufada=manos[x][4]
  neoj=tba
  if bufada in range(1,11):
    print "Ha Sacado", bufada
    for i in range(0,bufada-1):
      sacar=neoj.pop(0)
      neoj.append(sacar)
    buforeina=neoj[0]
    if buforeina==1:
      print "El Jugador", tjbb[buforeina-1], "Despierta A Una Reina Gracias Al bufon!"
      reyfb(x)
    if buforeina!=1:
      print "El Jugador", tjbb[buforeina-1], "Despierta A Una Reina Gracias Al bufon!"
      reynf(buforeina-1)
  elif bufada!=1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 or 10:
    print "No es un Numero"
    print tjbb[x], "Ha Conseguido", bufada, "Obtiene Otro Turno"
    if "rey" in manos[x] and len(reinas)!=0:
      reyn(x)
      if "rey" in manos[x]:
        manos[x].remove("rey")
        sacarm(x)
    elif "caballero" in manos[x] and (jr[0][4] or jr[0][3] or jr[0][2] or jr[0][1] or jr[0][0])!=0:
      caballeron(x)
    elif "pocion" in manos[x] and (jr[0][4] or jr[0][3] or jr[0][2] or jr[0][1] or jr[0][0])!=0:
      pocionn(x)
    elif "bufon" in manos[x]:
      bufonn(x)
    else:
      asacar(x)
def pocionn(x):
    print "Al Jugador", lj[x], "No Le Agrada tu Reina"
    robarmachin=jr[0][4]
    if robarmachin==0:
      robarmachin=jr[0][3]
      if robarmachin==0:
        robarmachin=jr[0][2]
        if robarmachin==0:
          robarmachin=jr[0][1]
          if robarmachin==0:
            robarmachin=jr[0][0]
    lugarurto=jr[0].index(robarmachin)
    if "varita" in manos[0]:
      print "Intentan Dormir A Tu Reina!"
      eleccionf=raw_input(panelvarita)
      if eleccionf=="2":
        robolugar=reinasc.index(robarmachin)
        robopoint=reinas_valuec[robolugar]
        jp[0]=jp[0]-robopoint
        jr[0][lugarurto]=0
        print "     Han Dormido A Tu", robarmachin
        manos[x].remove("pocion")
        sacarm(x)
        print " "
        print lj[0], "Ahora tiene:"
        print jr[0], "Reinas"
        print "Y", jp[0], "Puntos"
        print " "
      if eleccionf=="1":
        print "Usaste una Varita, No Pudieron Dormir Tu Reina"
        manos[x].remove("pocion")
        sacarm(x)
        manos[0].remove("varita")
        sacarm(0)
    else:
      robolugar=reinasc.index(robarmachin)
      robopoint=reinas_valuec[robolugar]
      jp[0]=jp[0]-robopoint
      jr[0][lugarurto]=0
      print "     Han Dormido A Tu", robarmachin
      manos[x].remove("pocion")
      sacarm(x)
      print " "
      print lj[0], "Ahora tiene:"
      print jr[0], "Reinas"
      print "Y", jp[0], "Puntos"
      print " "
def asacar(x):
  oldcard=random.choice(manos[x])
  manos[x].remove(oldcard)
  sacarm(x)
  print lj[x], "Tira y Roba Una Carta"
contador=1
tpj=[1,2,3,4,5]
tpa=[]
for i in range(0,nj):
  x=tpj[i]
  tpa.append(x)
tj=tpa
print tj
def card(nj):
  while nj<1 and nj<8:
    print "No es una opcion valida1"
    nj=input("Por favor, ingrese otra")
  while nj>1 and nj>8:
    print "No es una opcion valida3"
    nj=input("Por favor, ingrese otra")
    while nj<1 and nj<8:
      print "No es una opcion valida4"
      nj=input("Por favor, ingrese otra")
  while nj>=1 and nj<=8:
    return nj
espacio= "*****************************************************".center(70,"*")
if c=="ylasreinas":
  reinas=["Reina Perro", "Reina Gato"]
while tj[0]==1:
  print T1.center(60," ")
  if c=="realeza":
      manos[0]=["rey","rey","dragon","caballero","caballero"]
  if c=="mat":
      manos[0]=[2,2,4,6,8]
  if c=="mago":
    manos[0]=["pocion","varita","rey","caballero","caballero"]
  if c=="seacabo":
    mazo=["rey"]
  if c=="joker":
    manos[0]=["bufon","bufon","rey","bufon","caballero"]
  print "En tu mano hay", manos[0]
  eleccionj=input(panel)
  eleccionj=card(eleccionj)
  eleccionf(eleccionj)
  eleccion(eleccionj)
  sacar=tj.pop(0)
  tj.append(sacar)
  sacara=tba.pop(0)
  tba.append(sacar)
  print mano1
  print len(mazo)
  print espacio
  raw_input()
  print tj
  while tj[0]==2:
    print T2.center(60," ")
    if "rey" in manos[1] and len(reinas)!=0:
      reyn(1)
      if "rey" in manos[1]:
        manos[1].remove("rey")
        sacarm(1)
    elif "caballero" in manos[1] and (jr[0][4] or jr[0][3] or jr[0][2] or jr[0][1] or jr[0][0])!=0:
      caballeron(1)
    elif "pocion" in manos[1] and (jr[0][4] or jr[0][3] or jr[0][2] or jr[0][1] or jr[0][0])!=0:
      pocionn(1)
    elif "bufon" in manos[1]:
      bufonn(1)
    else:
      asacar(1)
    sacar=tj.pop(0)
    tj.append(sacar)
    sacara=tba.pop(0)
    tba.append(sacar)
    print espacio
    raw_input()
    print tj
    while tj[0]==3:
      print T3.center(60," ")
      if "rey" in manos[2] and len(reinas)!=0:
        reyn(2)
        if "rey" in manos[2]:
          manos[2].remove("rey")
          sacarm(2)
      elif "caballero" in manos[2] and (jr[0][4] or jr[0][3] or jr[0][2] or jr[0][1] or jr[0][0])!=0:
        caballeron(2)
      elif "pocion" in manos[2] and (jr[0][4] or jr[0][3] or jr[0][2] or jr[0][1] or jr[0][0])!=0:
        pocionn(2)
      elif "bufon" in manos[2]:
        bufonn(2)
      else:
        asacar(2)
      sacar=tj.pop(0)
      tj.append(sacar)
      sacara=tba.pop(0)
      tba.append(sacar)
      print espacio
      raw_input()
      print tj
      while tj[0]==4:
        print T4.center(60," ")
        if "rey" in manos[3] and len(reinas)!=0:
          reyn(3)
          if "rey" in manos[3]:
            manos[3].remove("rey")
            sacarm(3)
        elif "caballero" in manos[3] and (jr[0][4] or jr[0][3] or jr[0][2] or jr[0][1] or jr[0][0])!=0:
          caballeron(3)
        elif "pocion" in manos[3] and (jr[0][4] or jr[0][3] or jr[0][2] or jr[0][1] or jr[0][0])!=0:
          pocionn(3)
        elif "bufon" in manos[3]:
          bufonn(3)
        else:
          asacar(3)
        sacar=tj.pop(0)
        tj.append(sacar)
        sacara=tba.pop(0)
        tba.append(sacar)
        print espacio
        raw_input()
        print tj
        while tj[0]==5:
          print T5.center(60," ")
          if "rey" in manos[4] and len(reinas)!=0:
            reyn(4)
            if "rey" in manos[4]:
              manos[4].remove("rey")
              sacarm(4)
          elif "caballero" in manos[4] and (jr[0][4] or jr[0][3] or jr[0][2] or jr[0][1] or jr[0][0])!=0:
            caballeron(4)
          elif "pocion" in manos[4] and (jr[0][4] or jr[0][3] or jr[0][2] or jr[0][1] or jr[0][0])!=0:
            pocionn(4)
          elif "bufon" in manos[4]:
            bufonn(4)
          else:
            asacar(4)
          sacar=tj.pop(0)
          tj.append(sacar)
          sacara=tba.pop(0)
          tba.append(sacar)
          print espacio
          raw_input()
          print tj
