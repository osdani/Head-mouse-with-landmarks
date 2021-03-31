# Head-mouse-with-landmarks
Este es un proyecto que consiste en mover el mouse mediante visión por computadora 
## Intalacion de herramientas 
Para este proyecto se utilizo Spyder para windows 10 
* [Anaconda página oficial ](https://www.anaconda.com/distribution/ ) - El IDE de programacion.

    ![Anacoda](https://github.com/osdani/Head-mouse-with-landmarks/blob/main/data/anaconda.png)  ![Spyder](https://github.com/osdani/Head-mouse-with-landmarks/blob/main/data/spyder.png)
### Librerías
_Después de realizar la instalación del IDE se procede a instalar las respectivas librerías, se busca el terminal “anaconda prompt” y lo ejecutamos como administrador. Las librerías para Python es casi lo mismo que en la terminal de linux solo que esta vez se ejecuta en la terminal “anaconda prompt”_

```
pip install NOMBRE-LIBRERIA 
```
Sin embargo, a veces se utilizan otras instrucciones que relacionan a Anaconda debido a que es más fácil instalar la de esta manera, puesto que algunas librerías necesitan de complementos para que estas funciones si se instala por el comando anterior.
#### Instalar Dlib
![Cmake](https://github.com/osdani/Head-mouse-with-landmarks/blob/main/data/cmake.png) ![Dlib](https://github.com/osdani/Head-mouse-with-landmarks/blob/main/data/Dlib.png) 

Para instalar esta librería existen varias maneras la primera opción es mediante el primer ejemplo, sin embargo, se debe instalar [Cmake](https://cmake.org/download/).
```
pip install dlib
```
[Documentación](https://pypi.org/project/dlib/)

Otra opción que puede funcionar es:
```
conda install -c conda-forge dlib=19.18 
```
DESCARGAR base de datos [landmark](https://es.osdn.net/projects/sfnet_dclib/downloads/dlib/v18.10/shape_predictor_68_face_landmarks.dat.bz2/)
