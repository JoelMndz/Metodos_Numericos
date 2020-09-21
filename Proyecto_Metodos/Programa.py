from guizero import *
from Clases.MetodoEstadistico import MetodoEstadistico
from Clases.AreaIntegrales import AreaIntegrales
from Clases.FalsaPosicion import FalsaPosicion
from Clases.Gauss import Gauss
from Clases.GaussSeidel import GaussSeidel
from Clases.NewthonRaphson import NewthonRaphson
from Clases.RaizCuadratica import RaizCuadratica
from Clases.Ruffini import Ruffini

# -------------------Métodos-------------------------------
# Todas las ventanas lo utilizan
def regresar(v):
    v.hide()
    app.show()

# Metodos de Raíz cuadrática
def calcular_raiz_cuadratica(a,b,c,respuesta):
    try:
        r_c=RaizCuadratica()
        r_c.set_variables(a,b,c)
        respuesta.enable()
        respuesta.clear()
        raices=r_c.get_calcular()
        if r_c.get_calcular()=="Error":
            raise ValueError
        for i in range(len(raices)):
            respuesta.append("x"+str(i+1)+" "+str(raices[i]))
        respuesta.disable()
    except:
        warn('Error',"Datos incorrectos")

def graficar_raiz_cuadratica(a,b,c):
    try:
        r_c=RaizCuadratica()
        r_c.set_variables(a,b,c)
        r_c.get_graficar()
    except:
        warn('Error',"Datos incorrectos")

# Metodos de Newthon Raphson
def calcular_newthon_raphson(funcion, xi, respuesta, p1, p2):
    try:
        n_r=NewthonRaphson()
        n_r.set_ecuacion(funcion)
        n_r.set_xi(xi)
        n_r.set_rango(p1,p2)
        respuesta.enable()
        respuesta.clear()
        respuesta.append(n_r.get_resultado())
        respuesta.disable()
        n_r.get_grafica_resultado()
    except :
        warn('Error',"Datos incorrectos, llene todos los campos")

def graficar_newthon_raphson(funcion, p1, p2):
    try:
        n_r=NewthonRaphson()
        n_r.set_ecuacion(funcion)
        n_r.set_rango(p1,p2)
        n_r.get_grafica_inicial()

    except :
        warn('Error',"Datos incorrectos, llene todos los campos")

# metodos de metodo estadistico
def grafica_lineal(ejex, ejey, p1, p2):
    try:
        m_e=MetodoEstadistico()
        m_e.set_datos(ejex, ejey)
        m_e.set_rango(p1, p2)
        m_e.get_grafica_lineal()
    except:
        warn('Error',"Datos incorrectos, llene todos los campos")

def grafica_cuadratica(ejex, ejey, p1, p2):
    try:
        m_e=MetodoEstadistico()
        m_e.set_datos(ejex, ejey)
        m_e.set_rango(p1, p2)
        m_e.get_grafica_cuadratica()
        
    except:
        warn('Error',"Datos incorrectos, llene todos los campos")

def aprox_lineal(ejex, ejey, aprox, respuesta):
    try:
        m_e=MetodoEstadistico()
        m_e.set_datos(ejex, ejey)
        m_e.set_aproximacion(aprox)
        respuesta.enable()
        respuesta.clear()
        respuesta.append(m_e.get_aprox_lin())
        respuesta.disable()
    except:
        warn('Error',"Datos incorrectos, llene todos los campos")

def aprox_cuadratica(ejex, ejey, aprox, respuesta):
    try:
        m_e=MetodoEstadistico()
        m_e.set_datos(ejex, ejey)
        m_e.set_aproximacion(aprox)
        respuesta.enable()
        respuesta.clear()
        respuesta.append(m_e.get_aprox_cuad())
        respuesta.disable()
    except:
        warn('Error',"Datos incorrectos, llene todos los campos")

# Metodos de Area Integral
def calcular_area(funcion, lim_s, lim_i, p1, p2, respuesta):
    try:
        a_i=AreaIntegrales()
        a_i.set_ecuacion(funcion)
        a_i.set_datos(lim_s, lim_i)
        a_i.set_rango(p1, p2)
        respuesta.enable()
        respuesta.clear()
        respuesta.append(a_i.get_resultado())
        respuesta.disable()
        a_i.get_grafica_resultado()
    except:
        warn('Error',"Datos incorrectos, llene todos los campos")

def graficar_area_integral(funcion, p1, p2):
    try:
        a_i=AreaIntegrales()
        a_i.set_ecuacion(funcion)
        a_i.set_rango(p1, p2)
        a_i.get_grafica_inicial()
    except:
        warn('Error',"Datos incorrectos, llene todos los campos")

# Metodos de Falsa Posición
def calcular_f_p(funcion, x0, delta, p1, p2 , respuesta):
    try:
        f_p=FalsaPosicion()
        f_p.set_ecuacion(funcion)
        f_p.set_x0_delta(x0, delta)
        f_p.set_rango(p1, p2)
        respuesta.enable()
        respuesta.clear()
        respuesta.append(f_p.get_resultado())
        respuesta.disable()
        f_p.get_grafica_resultado()
    except :
        warn('Error',"Datos incorrectos, llene todos los campos")

def graficar_f_p(funcion, p1, p2):
    try:
        f_p=FalsaPosicion()
        f_p.set_ecuacion(funcion)
        f_p.set_rango(p1, p2)
        f_p.get_grafica_inicial()
    except :
        warn('Error',"Datos incorrectos, llene todos los campos")

# Metodos de eliminacion de Gauss
def modelo_matriz(n,matriz,vector):
    matriz.clear()
    vector.clear()
    # Craer modelo
    for i in range(0,int(n[0])):
        fila="" 
        for j in range(0,int(n[2])):
            fila+="0,"
        matriz.append(fila[:-1])
        vector.append(0)
    matriz.disable()
    vector.disable()

def calcular_matriz(matriz, vector, n, matriz_r, ov, respuesta):
    try:
        # Extraer datos
        matrix1=matriz.value.strip().split('\n')
        for i in range(len(matrix1)):
            matrix1[i]=matrix1[i].strip()

        vec=vector.value.strip().split("\n")
        for i in range(len(vec)):
            vec[i]=vec[i].strip()

        lista1=[]
        for i in range(len(matrix1)):
            fila=matrix1[i].split(',')
            lista1.append(fila)
        
        lista2=[]
        for i in range(len(vec)):
            lista2.append(float(vec[i]))
        
        for i in range(len(lista1)):
            for j in range(len(lista1)):
                lista1[i][j]=float(lista1[i][j])
        
        g=Gauss()
        g.set_datos(lista1, lista2, n[0], n[2])

        matriz_r.enable()
        ov.enable()
        respuesta.enable()

        matriz_r.clear()
        ov.clear()
        respuesta.clear()
        
        mat=g.get_matriz()
        vect=g.get_vector()
        raiz=g.get_x()
        

        for i in range(0,int(n[0])):
            fila="" 
            for j in range(0,int(n[2])):
                fila+=str(mat[i,j])+", "
            ov.append(vect[i])
            matriz_r.append(fila)
            respuesta.append("x"+str(i+1)+" "+str(round(raiz[i],2)))

        matriz_r.disable()
        ov.disable()
        respuesta.disable()

    except:
        warn('Error',"Datos incorrectos, llene todos los campos")


# Metodos de causs seidel
def calcular_matriz_seidel(matriz, vector, n, respuesta):
    try:
        # Extraer datos
        matrix1=matriz.value.strip().split('\n')
        for i in range(len(matrix1)):
            matrix1[i]=matrix1[i].strip()

        vec=vector.value.strip().split("\n")
        for i in range(len(vec)):
            vec[i]=vec[i].strip()

        lista1=[]
        for i in range(len(matrix1)):
            fila=matrix1[i].split(',')
            lista1.append(fila)
        
        lista2=[]
        for i in range(len(vec)):
            lista2.append(float(vec[i]))
        
        for i in range(len(lista1)):
            for j in range(len(lista1)):
                lista1[i][j]=float(lista1[i][j])
        # print(lista1)
        # print(lista2)
        # Calculo la Matriz
        # lista1=[[1.0, 1.0, 1.0], [1.0, 5.0, 3.0], [3.0, 2.0, 4.0]]
        # lista2=[45.0, 145.0, 140.0]
        g_s=GaussSeidel()
        g_s.set_datos(lista1, lista2, n[0], n[2])

        respuesta.enable()
        respuesta.clear()
               
        raiz=g_s.get_raices()

        for i in range(0,int(n[0])):
            respuesta.append("x"+str(i+1)+" "+str(round(raiz[i],2)))

        respuesta.disable()

    except:
        warn('Error',"Datos incorrectos, llene todos los campos")
        

# metodos de Ruffini
def modelo_coeficientes(n, respuesta):
    try:
        respuesta.clear()
        for i in range(int(n[3])+1):
            if int(n[3])+1==i+1:
                 respuesta.append("0")
            else:
                respuesta.append("0,")
        
    except:
        warn('Error',"Datos incorrectos, llene todos los campos")

def calcular_raices(input, respuesta):
    try:
        r=Ruffini()
        lista=input.value.split(",")
        for i in range(len(lista)):
            lista[i]=lista[i].strip()
        respuesta.enable()
        respuesta.clear()
        r.set_polinomios(lista)
        if r.get_respuesta()==[]:
            warn('Error','No hay solución')
        for i in r.get_respuesta():
            respuesta.append(i)
        respuesta.disable()
    except:
        warn('Error',"Datos incorrectos, llene todos los campos")
               
# --------------------------------Ventanas de los métodos---------------------------------------
def v_r_c():
    app.hide()
    v_r_c=App(title="Raíz Cuadrática",width=720, height=400,layout='grid')
    v_r_c.font="Calisto MT"
    v_r_c.bg=(176, 196, 222)
    label_titulo=Text(v_r_c,text="Raíz Cuadrática",height=2,size=28,grid=[2,2,20,1])

    boton_regresar=PushButton(v_r_c, text="Regresar", command=lambda:regresar(v_r_c), grid=[1,1])
    boton_regresar.bg=(101, 177, 245)

    label=Text(v_r_c,height=2, grid=[1,3])
    label=Text(v_r_c,height=1, grid=[1,7])
    label=Text(v_r_c,width=6, grid=[4,4])
    label=Text(v_r_c,width=6, grid=[7,4])

    label_a=Text(v_r_c,text="a(x**2):",align='left',grid=[2,4])
    input_a=TextBox(v_r_c,text="1",grid=[3,4])
    input_a.text_size=12
    input_a.bg='white'
    label_b=Text(v_r_c,text="b(x):", height=2,align='left',grid=[2,5])
    input_b=TextBox(v_r_c,text="2",grid=[3,5])
    input_b.text_size=12
    input_b.bg='white'
    label_c=Text(v_r_c,text="c:",align='left',grid=[2,6])
    input_c=TextBox(v_r_c,text="-2",grid=[3,6])
    input_c.text_size=12
    input_c.bg='white'
    boton_calcular=PushButton(v_r_c,text="Calcular",grid=[2,8,2,1],command=lambda:calcular_raiz_cuadratica(input_a.value,
                                                                                                           input_b.value,
                                                                                                           input_c.value,
                                                                                                           input_respuesta))
    boton_calcular.text_size=12
    boton_graficar=PushButton(v_r_c,text="Graficar",grid=[5,5],command=lambda:graficar_raiz_cuadratica(input_a.value,
                                                                                                           input_b.value,
                                                                                                           input_c.value))
    boton_graficar.text_size=12
    label_respuesta=Text(v_r_c,text="Respuesta:",grid=[8,4])
    label_respuesta.text_size=14
    input_respuesta=TextBox(v_r_c,multiline=True,height=3,width=20,grid=[8,5])
    input_respuesta.text_size=12
    input_respuesta.bg='white'
    v_r_c.display()

def v_n_r():
    app.hide()
    v_n_r=App(title="Newthon  Raphson",width=720, height=400,layout='grid')
    v_n_r.font="Calisto MT"
    v_n_r.bg=(176, 196, 222)
    label_titulo=Text(v_n_r,text="Newthon  Raphson",height=2,size=28,grid=[2,2,20,1])

    boton_regresar=PushButton(v_n_r, text="Regresar", command=lambda:regresar(v_n_r), grid=[1,1])
    boton_regresar.bg=(101, 177, 245)

    label=Text(v_n_r,height=2, grid=[1,3])
    label=Text(v_n_r,height=1, grid=[1,7])
    label=Text(v_n_r,width=6, grid=[4,4])
    label=Text(v_n_r,width=6, grid=[7,4])

    label_funcion=Text(v_n_r,text="función:",align='left',grid=[2,5])
    input_funcion=TextBox(v_n_r,text="x**3-30*x**2+2552", width=20,grid=[3,5])
    input_funcion.text_size=12
    input_funcion.bg='white'
    label_xi=Text(v_n_r,text="xi:", height=2,align='left',grid=[2,6])
    input_xi=TextBox(v_n_r,text="10", align='left',grid=[3,6])
    input_xi.text_size=12
    input_xi.bg='white'
    boton_calcular=PushButton(v_n_r,text="Calcular",grid=[2,8,2,1],command=lambda:calcular_newthon_raphson(input_funcion.value,
                                                                                                          input_xi.value,
                                                                                                          input_respuesta,
                                                                                                          input_p1.value,
                                                                                                          input_p2.value))
    boton_calcular.text_size=12
    label_rango=Text(v_n_r, text="Rango:", grid=[5,4,2,1])
    label_p1=Text(v_n_r, text="p1:", align='left',grid=[5,5])
    input_p1=TextBox(v_n_r, text="-10", grid=[6,5])
    input_p1.text_size=12
    input_p1.bg='white'
    label_p2=Text(v_n_r, text="p2:", align='left',grid=[5,6])
    input_p2=TextBox(v_n_r, text="15", grid=[6,6])
    input_p2.text_size=12
    input_p2.bg='white'
    boton_graficar=PushButton(v_n_r,text="Graficar",grid=[5,8,2,1],command=lambda:graficar_newthon_raphson(input_funcion.value,
                                                                                                           input_p1.value,
                                                                                                           input_p2.value))
    boton_graficar.text_size=12
    label_respuesta=Text(v_n_r,text="Respuesta:",grid=[8,4])
    label_respuesta.text_size=14
    input_respuesta=TextBox(v_n_r,multiline=True, width=20,height=2,grid=[8,5])
    input_respuesta.text_size=12
    input_respuesta.bg='white'

    v_n_r.display()

def v_m_e():
    app.hide()
    v_m_e=App(title="Método Estadístico",width=940, height=560,layout='grid')
    v_m_e.font="Calisto MT"
    v_m_e.bg=(176, 196, 222)
    label_titulo=Text(v_m_e,text="Método Estadístico",height=2,size=28,grid=[2,2,20,1])

    boton_regresar=PushButton(v_m_e, text="Regresar", command=lambda:regresar(v_m_e), grid=[1,1])
    boton_regresar.bg=(101, 177, 245)

    label=Text(v_m_e,height=1, grid=[1,3])
    label=Text(v_m_e,height=1, grid=[1,7])
    label=Text(v_m_e,width=6, grid=[5,4])
    label=Text(v_m_e,height=1, grid=[1,11])

    label_x=Text(v_m_e,text="x:",align='left',grid=[2,5])
    input_x=TextBox(v_m_e,text="1,2,3,4,5", width=50,grid=[3,5,2,1])
    input_x.text_size=12
    input_x.bg='white'
    label_y=Text(v_m_e,text="y:", height=2,align='left',grid=[2,6])
    input_y=TextBox(v_m_e,text="10,30,50,60,80", align='left', width=50,grid=[3,6,2,1])
    input_y.text_size=12
    input_y.bg='white'
    boton_lineal=PushButton(v_m_e,text="Regresión Lineal",grid=[3,8],command=lambda:grafica_lineal(input_x.value,
                                                                                                   input_y.value,
                                                                                                   input_p1.value,
                                                                                                   input_p2.value))
    boton_lineal.text_size=12
    boton_cuadratica=PushButton(v_m_e,text="Regresión cuadrática",grid=[4,8],command=lambda:grafica_cuadratica(input_x.value,
                                                                                                   input_y.value,
                                                                                                   input_p1.value,
                                                                                                   input_p2.value))
    boton_cuadratica.text_size=12
    label_rango=Text(v_m_e, text="Rango:", grid=[6,4,2,1])
    label_p1=Text(v_m_e, text="p1:", align='left',grid=[6,5])
    input_p1=TextBox(v_m_e, text="-10", grid=[7,5])
    input_p1.text_size=12
    input_p1.bg='white'
    label_p2=Text(v_m_e, text="p2:", align='left',grid=[6,6])
    input_p2=TextBox(v_m_e, text="15", grid=[7,6])
    input_p2.text_size=12
    input_p2.bg='white'
    label_respuesta=Text(v_m_e,text="Respuesta:",grid=[6,8,3,1])
    label_respuesta.text_size=14
    input_respuesta=TextBox(v_m_e,multiline=True,height=2,width=30,grid=[6,9,3,1])
    input_respuesta.text_size=12
    input_respuesta.bg='white'
    label_aproximacion=Text(v_m_e, text="Aproximación:", height= 2,grid=[2,10,2,1])
    label_aproximacion.text_size=12
    input_aprox=TextBox(v_m_e, align='left', grid=[4,10])
    input_aprox.text_size=12
    input_aprox.bg='white'
    boton_lineal=PushButton(v_m_e,text="Aproximación Lineal",grid=[2,12,2,1],command=lambda:aprox_lineal(input_x.value,
                                                                                                         input_y.value,
                                                                                                         input_aprox.value,
                                                                                                         input_respuesta))
    boton_lineal.text_size=12
    boton_cuadratica=PushButton(v_m_e,text="Aproximación cuadrática",grid=[4,12],command=lambda:aprox_cuadratica(input_x.value,
                                                                                                         input_y.value,
                                                                                                         input_aprox.value,
                                                                                                         input_respuesta))
    boton_cuadratica.text_size=12

    v_m_e.display()

def v_a_i():
    app.hide()
    v_a_i=App(title="Área Integral",width=760, height=400,layout='grid')
    v_a_i.font="Calisto MT"
    v_a_i.bg=(176, 196, 222)
    label_titulo=Text(v_a_i,text="Área Integral",height=2,size=28,grid=[2,2,20,1])

    boton_regresar=PushButton(v_a_i, text="Regresar", command=lambda:regresar(v_a_i), grid=[1,1])
    boton_regresar.bg=(101, 177, 245)

    label=Text(v_a_i,height=2, grid=[1,3])
    label=Text(v_a_i,height=1, grid=[1,7])
    label=Text(v_a_i,width=5, grid=[4,4])
    label=Text(v_a_i,width=6, grid=[7,4])

    label_funcion=Text(v_a_i,text="Funcion:",align='left',grid=[2,4])
    input_funcion=TextBox(v_a_i,text="-10+(35+10)/(1+(x/4)**3)",width=25,grid=[3,4])
    input_funcion.text_size=12
    input_funcion.bg='white'
    label_limsup=Text(v_a_i,text="lim sup:", height=2,align='left',grid=[2,5])
    input_limsup=TextBox(v_a_i,text="6",align='left',grid=[3,5])
    input_limsup.text_size=12
    input_limsup.bg='white'
    label_liminf=Text(v_a_i,text="lim inf:",align='left',grid=[2,6])
    input_liminf=TextBox(v_a_i,text="0",align='left',grid=[3,6])
    input_liminf.text_size=12
    input_liminf.bg='white'
    boton_calcular=PushButton(v_a_i,text="Calcular",grid=[2,8,2,1],command=lambda:calcular_area(input_funcion.value,
                                                                                                input_limsup.value,
                                                                                                input_liminf.value,
                                                                                                input_p1.value,
                                                                                                input_p2.value,
                                                                                                input_respuesta))
    boton_calcular.text_size=12
    label_rango=Text(v_a_i, text="Rango:", grid=[5,4,2,1])
    label_p1=Text(v_a_i, text="p1:", align='left',grid=[5,5])
    input_p1=TextBox(v_a_i, text="-1", grid=[6,5])
    input_p1.text_size=12
    input_p1.bg='white'
    label_p2=Text(v_a_i, text="p2:", align='left',grid=[5,6])
    input_p2=TextBox(v_a_i, text="7", grid=[6,6])
    input_p2.text_size=12
    input_p2.bg='white'
    boton_graficar=PushButton(v_a_i,text="Graficar",grid=[5,8,2,1],command=lambda:graficar_area_integral(input_funcion.value,
                                                                                                input_p1.value,
                                                                                                input_p2.value))
    boton_graficar.text_size=12
    label_respuesta=Text(v_a_i,text="Respuesta:",grid=[8,4])
    label_respuesta.text_size=14
    input_respuesta=TextBox(v_a_i,multiline=True,height=2, width=20,grid=[8,5])
    input_respuesta.text_size=12
    input_respuesta.bg='white'

    v_a_i.display()


def v_f_p():
    app.hide()
    v_f_p=App(title="Falsa Posición",width=720, height=400,layout='grid')
    v_f_p.font="Calisto MT"
    v_f_p.bg=(176, 196, 222)
    label_titulo=Text(v_f_p,text="Falsa Posición",height=2,size=28,grid=[2,2,20,1])

    boton_regresar=PushButton(v_f_p, text="Regresar", command=lambda:regresar(v_f_p), grid=[1,1])
    boton_regresar.bg=(101, 177, 245)

    label=Text(v_f_p,height=2, grid=[1,3])
    label=Text(v_f_p,height=1, grid=[1,7])
    label=Text(v_f_p,width=5, grid=[4,4])
    label=Text(v_f_p,width=6, grid=[7,4])

    label_funcion=Text(v_f_p,text="Funcion:",align='left',grid=[2,4])
    input_funcion=TextBox(v_f_p,text="x**3-30*x**2+2552",width=20,grid=[3,4])
    input_funcion.text_size=12
    input_funcion.bg='white'
    label_x0=Text(v_f_p,text="x0:", height=2,align='left',grid=[2,5])
    input_x0=TextBox(v_f_p,text="10",align='left',grid=[3,5])
    input_x0.text_size=12
    input_x0.bg='white'
    label_delta=Text(v_f_p,text="Delta:",align='left',grid=[2,6])
    input_delta=TextBox(v_f_p,text="10",align='left',grid=[3,6])
    input_delta.text_size=12
    input_delta.bg='white'
    boton_calcular=PushButton(v_f_p,text="Calcular",grid=[2,8,2,1],command=lambda:calcular_f_p(input_funcion.value,
                                                                                        input_x0.value,
                                                                                        input_delta.value,
                                                                                        input_p1.value,
                                                                                        input_p2.value,
                                                                                        input_respuesta))    
    boton_calcular.text_size=12
    label_rango=Text(v_f_p, text="Rango:", grid=[5,4,2,1])
    label_p1=Text(v_f_p, text="p1:", align='left',grid=[5,5])
    input_p1=TextBox(v_f_p, text="-10", grid=[6,5])
    input_p1.text_size=12
    input_p1.bg='white'
    label_p2=Text(v_f_p, text="p2:", align='left',grid=[5,6])
    input_p2=TextBox(v_f_p, text="15", grid=[6,6])
    input_p2.text_size=12
    input_p2.bg='white'
    boton_graficar=PushButton(v_f_p,text="Graficar",grid=[5,8,2,1],command=lambda:graficar_f_p(input_funcion.value,
                                                                                        input_p1.value,
                                                                                        input_p2.value))
    boton_graficar.text_size=12
    label_respuesta=Text(v_f_p,text="Respuesta:",grid=[8,4])
    label_respuesta.text_size=14
    input_respuesta=TextBox(v_f_p,multiline=True,height=2, width=20,grid=[8,5])
    input_respuesta.text_size=12
    input_respuesta.bg='white'
    v_f_p.display()


def v_g():
    app.hide()
    v_g=App(title="Eliminación Gauseana",width=960, height=480,layout='grid')
    v_g.font="Calisto MT"
    v_g.bg=(176, 196, 222)
    label_titulo=Text(v_g,text="Eliminación Gauseana",height=2,size=28,grid=[2,2,20,1])

    boton_regresar=PushButton(v_g, text="Regresar", command=lambda:regresar(v_g), grid=[1,1])
    boton_regresar.bg=(101, 177, 245)

    label=Text(v_g,height=1, grid=[1,3])
    label=Text(v_g,height=1, grid=[1,7])
    label=Text(v_g,width=5, grid=[1,5])
    label=Text(v_g,width=5, grid=[5,4])
    label=Text(v_g,width=5, grid=[9,4])

    label_funcion=Text(v_g,text="Matriz:",align='left',grid=[2,4])
    combo=Combo(v_g, options=["2x2","3x3","4x4","5x5"],align="left",grid=[3,4],command=lambda:modelo_matriz(combo.value,
                                                                                                            input_matriz,
                                                                                                            input_vector))
    combo.text_size=12
    input_matriz= TextBox(v_g,width=30,height=6,multiline=True,grid=[2,6,2,1])
    input_matriz.text_size=12
    input_matriz.bg='white'
    input_vector= TextBox(v_g,width=5,height=6,multiline=True,grid=[4,6])
    input_vector.text_size=12
    input_vector.bg='white'
    label_matriz=Text(v_g,text="Matriz Resultante:",align='left',grid=[6,4])
    output_matriz= TextBox(v_g,width=30,height=6,multiline=True,grid=[6,6,2,1])
    output_matriz.text_size=12
    output_matriz.bg='white'
    output_vector= TextBox(v_g,width=5,height=6,multiline=True,grid=[8,6])
    output_vector.text_size=12
    output_vector.bg='white'
    label_resultado=Text(v_g,text="Respuesta:",align='left',grid=[10,4])
    output_respuesta= TextBox(v_g,width=20,height=6,multiline=True,grid=[10,6])
    output_respuesta.text_size=12
    output_respuesta.bg='white'
    boton_calcular=PushButton(v_g,text="Calcular",grid=[2,8,2,1],command=lambda:calcular_matriz(input_matriz,
                                                                                               input_vector,
                                                                                               combo.value,
                                                                                               output_matriz,
                                                                                               output_vector,
                                                                                               output_respuesta))
    boton_calcular.text_size=12

    v_g.display()

def v_g_s():
    app.hide()
    v_g_s=App(title="Gauss Seidel",width=720, height=480,layout='grid')
    v_g_s.font="Calisto MT"
    v_g_s.bg=(176, 196, 222)
    label_titulo=Text(v_g_s,text="Gauss Seidel",height=2,size=28,grid=[2,2,20,1])

    boton_regresar=PushButton(v_g_s, text="Regresar", command=lambda:regresar(v_g_s), grid=[1,1])
    boton_regresar.bg=(101, 177, 245)

    label=Text(v_g_s,height=1, grid=[1,3])
    label=Text(v_g_s,height=1, grid=[1,7])
    label=Text(v_g_s,width=5, grid=[1,5])
    label=Text(v_g_s,width=5, grid=[9,4])

    label_funcion=Text(v_g_s,text="Matriz:",align='left',grid=[2,4])
    combo=Combo(v_g_s, options=["2x2","3x3","4x4","5x5"],align="left", grid=[3,4],command=lambda:modelo_matriz(combo.value,
                                                                                                            input_matriz,
                                                                                                            input_vector))
    combo.text_size=12
    input_matriz= TextBox(v_g_s,width=30,height=6,multiline=True,grid=[2,6,2,1])
    input_matriz.text_size=12
    input_matriz.bg='white'
    input_vector= TextBox(v_g_s,width=5,height=6,multiline=True,grid=[4,6])
    input_vector.text_size=12
    input_vector.bg='white'
    label_raices=Text(v_g_s,text="Raices:",align='left',grid=[10,4])
    output_raices= TextBox(v_g_s,width=20,height=6,multiline=True,grid=[10,6])
    output_raices.text_size=12
    output_raices.bg='white'
    boton_calcular=PushButton(v_g_s,text="Calcular", grid=[2,8,2,1],command=lambda:calcular_matriz_seidel(input_matriz,
                                                                                               input_vector,
                                                                                               combo.value,
                                                                                               output_raices))
    boton_calcular.text_size=12

    v_g_s.display()

def v_r():
    app.hide()
    v_r=App(title="Método de Ruffini",width=720, height=400,layout='grid')
    v_r.font="Calisto MT"
    v_r.bg=(176, 196, 222)
    label_titulo=Text(v_r,text="Método de Ruffini",height=2,size=28,grid=[2,2,20,1])

    boton_regresar=PushButton(v_r, text="Regresar", command=lambda:regresar(v_r), grid=[1,1])
    boton_regresar.bg=(101, 177, 245)
    label=Text(v_r,height=1, grid=[1,3])
    label=Text(v_r,height=1, grid=[1,7])
    label=Text(v_r,width=5, grid=[1,5])
    label=Text(v_r,width=5, grid=[9,4])

    label_funcion=Text(v_r,text="Grado:",align='left',grid=[2,4])
    combo=Combo(v_r, options=["x**2","x**3","x**4","x**5","x**6"],align="left",grid=[3,4], command=lambda:modelo_coeficientes(combo.value,
                                                                                                                       input_coeficientes))
    combo.text_size=12
    input_coeficientes= TextBox(v_r,width=40,height=6,grid=[2,6,2,1])
    input_coeficientes.text_size=12
    input_coeficientes.bg='white'
    label_raices=Text(v_r,text="Raices:",align='left',grid=[10,4])
    output_raices= TextBox(v_r,width=20,height=6,multiline=True,scrollbar=True,grid=[10,6,6,8])
    output_raices.text_size=12
    output_raices.bg='white'
    boton_calcular=PushButton(v_r,text="Calcular",grid=[2,8,2,1],command=lambda:calcular_raices(input_coeficientes,output_raices))
    boton_calcular.text_size=12

    v_r.display()
# Ventana Principal
app=App(title='Métodos numéricos',width=720, height=480,layout='grid')
app.font="Calisto MT"
app.bg=(176, 196, 222)
label_titulo=Text(app,text="Métodos Numéricos",height=2,size=28,grid=[2,1,20,1])

label=Text(app,width=5,height=2, grid=[1,2])
label=Text(app,width=5,height=1, grid=[1,4])
label=Text(app,width=5,height=1, grid=[1,6])
label=Text(app,width=5,height=1, grid=[1,8])
label=Text(app,width=10,height=1, grid=[3,4])
label=Text(app,width=5,height=1, grid=[1,10])


boton_Raiz_cuadratica=PushButton(app,text="Raíz Cuadrática",width=20,command=v_r_c, grid=[2,3])
boton_Raiz_cuadratica.text_size=12
boton_Gauss=PushButton(app,text="Eliminacion Gaussiana",width=20,command=v_g, grid=[2,5])
boton_Gauss.text_size=12
boton_GaussSeidel=PushButton(app,text="Gauss Seidel",width=20,command=v_g_s, grid=[2,7])
boton_GaussSeidel.text_size=12
boton_Ruffini=PushButton(app,text="Ruffini",width=20,command=v_r, grid=[2,9])
boton_Ruffini.text_size=12
boton_NewthonRaphson=PushButton(app,text="Newthon Raphson",width=20,command=v_n_r, grid=[4,3])
boton_NewthonRaphson.text_size=12
boton_MetodoEstadistico=PushButton(app,text="Método Estadístico",width=20,command=v_m_e, grid=[4,5])
boton_MetodoEstadistico.text_size=12
boton_AreaIntegral=PushButton(app,text="Área Integral",width=20,command=v_a_i, grid=[4,7])
boton_AreaIntegral.text_size=12
boton_FalsaPosicion=PushButton(app,text="Falsa Posición",width=20,command=v_f_p, grid=[4,9])
boton_FalsaPosicion.text_size=12

autor=Text(app,text="Luis Joel Méndez Loor",grid=[1,11,2,1])
curso=Text(app,text="4to 'A'",grid=[3,11])
uleam=Text(app,text="ULEAM",grid=[4,11])

app.display()