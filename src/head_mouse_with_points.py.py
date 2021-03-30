import numpy as np
import cv2
import dlib
import pyautogui as pag
#import imutils los movimietnos del mouese
from utils import *
#-------------------------------------------------------------------------------
#                           variables
#-------------------------------------------------------------------------------
#cuadro limite
anchor_punto=(360,290)
#click con la boca
abertura_boca=0.52
abertura_boca_envideo=6
#doble lick con el ojo derecho
abertura_ojo=0.22
abertura_ojo_envideo=6
#click derecho
cejas_levantadas=0.36
cejas_levantadas_envideo=6
cont=0
#deslizar
modo_scroll=False
boca_scroll=0.28
boca_scroll_envideo=6
#-------------------------------------------------------------------------------
#                           video y base de datos
#-------------------------------------------------------------------------------
capturar=cv2.VideoCapture(0)
detector=dlib.get_frontal_face_detector()#detector de  caras
#ahora lo que voy hacer es cargar el predictor del dlib
predictor=dlib.shape_predictor('data/shape_predictor_68_face_landmarks.dat')
while True:
    valor, text_imag=capturar.read()
#   invierto la imagen
    text_imag = cv2.flip(text_imag, 1)
#   conversion a escala de grises
    gris=cv2.cvtColor(text_imag,cv2.COLOR_BGR2GRAY)
#   detectar los rostros
    caras=detector(gris)
#    print(caras)
#-------------------------------------------------------------------------------
#               detecto los rostros y coloco una referencia visual
#-------------------------------------------------------------------------------
#   al hacer el recorrido la funcion me permite detectar los puntos
#   de la esquina superior izquierda y la inferiror derecha
    for rostro in caras:
#       extraigo cda posicon de cada puntos
        x1=rostro.left()
        x2=rostro.right()
        y1=rostro.top()
        y2=rostro.bottom()
#       como ya conozco los datos ahora voy a dibujar un rectagulo
        cv2.rectangle(text_imag,(x1,y1),(x2,y2),(117, 234, 20),2)
#       ahora lo que se hace es hacer es colocar 68 puntos en toda la cara
#       para ello recoor todas las posiciones
#-------------------------------------------------------------------------------
#               contorno de cara
#-------------------------------------------------------------------------------
        for punto in range(0,67):
            puntos_refencia_contorno=predictor(gris,rostro)
            xc=puntos_refencia_contorno.part(punto).x
            yc=puntos_refencia_contorno.part(punto).y
#            coloco los puntos de referencia en el video, las posiciones tomadas
#            la cantidad de pilexes 3 color verde y el grosro de -1
            cv2.circle(text_imag,(xc,yc),3,(0, 5, 139),-1)
#-------------------------------------------------------------------------------
#               deteccion ojos
#-------------------------------------------------------------------------------
        # for punto in range(36,47):
        #     puntos_refencia_ojos=predictor(gris,rostro)
        #     xo=puntos_refencia_ojos.part(punto).x
        #     yo=puntos_refencia_ojos.part(punto).y
        #     cv2.circle(text_imag,(xo,yo),2,(238,18,137),-1)
        puntos_refencia_ojos=predictor(gris,rostro)
        p42=puntos_refencia_ojos.part(42).x,puntos_refencia_ojos.part(42).y
        p43=puntos_refencia_ojos.part(43).x,puntos_refencia_ojos.part(43).y
        p44=puntos_refencia_ojos.part(44).x,puntos_refencia_ojos.part(44).y
        p45=puntos_refencia_ojos.part(45).x,puntos_refencia_ojos.part(45).y
        p46=puntos_refencia_ojos.part(46).x,puntos_refencia_ojos.part(46).y
        p47=puntos_refencia_ojos.part(47).x,puntos_refencia_ojos.part(47).y
#       Ecuacion EARR=eye_aspect_ratio_right relacion de aspecto del ojo derecho
        Aod = np.linalg.norm(np.array(p43)-np.array(p47))
        Bod = np.linalg.norm(np.array(p44)-np.array(p46))
        Cod = np.linalg.norm(np.array(p42)-np.array(p45))
        EARR=(Aod+Bod)/(2*Cod)
        #print("EARR: ",EARR)
#-------------------------------------------------------------------------------
#               deteccion cejas
#-------------------------------------------------------------------------------
        # for punto in range(17,27):
        #     puntos_refencia_cejas=predictor(gris,rostro)
        #     xce=puntos_refencia_cejas.part(punto).x
        #     yce=puntos_refencia_cejas.part(punto).y
        #     cv2.circle(text_imag,(xce,yce),2,(255,0,0),-1)
#-------------------------------------------------------------------------------
#               deteccion nariz
#-------------------------------------------------------------------------------
        # for punto in range(27,36):
        #     puntos_refencia_naris=predictor(gris,rostro)
        #     xn=puntos_refencia_naris.part(punto).x
        #     yn=puntos_refencia_naris.part(punto).y
        #     cv2.circle(text_imag,(xn,yn),2,(205,102,0),-1)
        punro_refencia_n=predictor(gris,rostro)
        x_n=punro_refencia_n.part(30).x
        y_n=punro_refencia_n.part(30).y
        nariz=(x_n,y_n)
        #print(nariz)
#-------------------------------------------------------------------------------
#               deteccion boca
#-------------------------------------------------------------------------------
        # for punto in range(48,68):
        #     puntos_refencia_boca=predictor(gris,rostro)
        #     xb=puntos_refencia_boca.part(punto).x
        #     yb=puntos_refencia_boca.part(punto).y
        #     cv2.circle(text_imag,(xb,yb),2,(220,20,60),-1)
        puntos_refencia_boca=predictor(gris,rostro)
        p60=puntos_refencia_boca.part(60).x,puntos_refencia_boca.part(60).y
        p61=puntos_refencia_boca.part(61).x,puntos_refencia_boca.part(61).y
        p62=puntos_refencia_boca.part(62).x,puntos_refencia_boca.part(62).y
        p63=puntos_refencia_boca.part(63).x,puntos_refencia_boca.part(63).y
        p64=puntos_refencia_boca.part(64).x,puntos_refencia_boca.part(64).y
        p65=puntos_refencia_boca.part(65).x,puntos_refencia_boca.part(65).y
        p66=puntos_refencia_boca.part(66).x,puntos_refencia_boca.part(66).y
        p67=puntos_refencia_boca.part(67).x,puntos_refencia_boca.part(67).y
#       ecuacion MAR a para obtener MAR=mounth mouth_aspect_ratio, ralacioon de aspectro de la boca
        Ab = np.linalg.norm(np.array(p61)-np.array(p67))
        Bb = np.linalg.norm(np.array(p62)-np.array(p66))
        Cb = np.linalg.norm(np.array(p63)-np.array(p65))
        Db = np.linalg.norm(np.array(p60)-np.array(p64))
        MAR=(Ab+Bb+Cb)/(2*Db)
        #print("MAR: ", MAR)

#-------------------------------------------------------------------------------
#               click derecho con la boca
#-------------------------------------------------------------------------------
        if MAR>abertura_boca:
            cont+=1
            if cont>abertura_boca_envideo:
                pag.click(button='right')
                cont = 0
                print('Click Derecho')
#-------------------------------------------------------------------------------
#               click izquierdo con las cejas
#-------------------------------------------------------------------------------
        elif EARR>cejas_levantadas:
            cont+=1
            if cont>cejas_levantadas_envideo:
                pag.click(button='left')
                cont = 0
                print('Click izquierdo')
#-------------------------------------------------------------------------------
#              doble click izquierdo con los ojos
#-------------------------------------------------------------------------------
        elif EARR<abertura_ojo:
            cont+=1
            if cont>abertura_ojo_envideo:
                pag.doubleClick(button='left')
                cont = 0
                print('doubleClick')
#-------------------------------------------------------------------------------
#              activacion de scroll
#-------------------------------------------------------------------------------
        elif (MAR>boca_scroll)and(MAR<abertura_boca):
            cont+=1
            if cont>boca_scroll_envideo:
                modo_scroll=not modo_scroll
                cont=0
                print('modo scroll')
        else:
            cont=0
#-------------------------------------------------------------------------------
#               movimietno mouse
#-------------------------------------------------------------------------------
        cv2.putText(text_imag, "actvado!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)
        x, y = anchor_punto
        nx, ny = nariz
        w, h = 34,20
        wh, hh=52,32
        multiple = 1
        cv2.rectangle(text_imag, (x - w, y - h), (x + w, y + h), (0,255,0), 2)
        cv2.rectangle(text_imag,(x - wh, y - hh), (x + wh, y + hh), (139,0,0), 2)
        cv2.line(text_imag, anchor_punto, nariz, (255,97,3), 2)

        dir = direction(nariz, anchor_punto, w, h,wh, hh)
        cv2.putText(text_imag, dir.upper(), (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)
        drag_leto = 16
        drag_rapido=40
#-------------------------------------------------------------------------------
#               movimietno mouse lento
#-------------------------------------------------------------------------------
        if dir == 'Derecha_lenta':
            pag.moveRel(drag_leto, 0)
        elif dir == 'izquierda_lenta':
            pag.moveRel(-drag_leto, 0)
        elif dir == 'Arriba_lento':
            if modo_scroll:
                pag.scroll(40)
            else:
                pag.moveRel(0, -drag_leto)
        elif dir == 'Abajo_lento':
            if modo_scroll:
                pag.scroll(-40)
            else:
                pag.moveRel(0, drag_leto)
#-------------------------------------------------------------------------------
#               movimietno mouse rapido
#-------------------------------------------------------------------------------
        elif dir == 'Derecha_rapida':
            pag.moveRel(drag_rapido, 0)
        elif dir == 'izquierda_rapida':
            pag.moveRel(-drag_rapido, 0)
        elif dir == 'Arriba_rapido':
            if modo_scroll:
                pag.scroll(40)
            else:
                pag.moveRel(0, -drag_rapido)
        elif dir == 'Abajo_rapido':
            if modo_scroll:
                pag.scroll(-40)
            else:
                pag.moveRel(0, drag_rapido)
        if modo_scroll:
            cv2.putText(text_imag, 'modo scroll ON!', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,150), 2)
#   muestro lo que estoy capturando constantemente
    cv2.imshow("img",text_imag)
#-------------------------------------------------------------------------------
#                      tecla para cerrar la ventana
#-------------------------------------------------------------------------------
    if(cv2.waitKey(30) & 0xFF == ord ('q')):
        break
