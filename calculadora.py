import numpy as np
import numba
from bokeh.models import ColumnDataSource, Plot, LinearAxis, Grid
from bokeh.models.markers import Circle
from bokeh.io import curdoc, show
from bokeh.plotting import figure, output_file, show
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_html_components as html
import dash_core_components as dcc
#import plotly.express as px


def obtener_matriz(data):
    matriz=[]
    if len(data)!=len(data[1]):
        print("Debe ser una matriz cuadrada")
    else:
        for fila in data:
            lista=list(fila.values())
            matriz.append(lista)
        final=np.array(matriz)
        print(final)
        return final
def Greshgorin_calcule(matrix):
    n=matrix.shape[1]
    radios=[]
    centros=[]
    solutio='la solución es la siguiente: \t'
    for i in range(n-1):
        i_=i+1
        ce=matrix[i][i]
        centro_coordenadas=[ce.real,ce.imag]
        radio=np.sum(abs(matrix[i]))-abs(ce)
        radios.append(radio)
        centros.append(centro_coordenadas)
        solutio+=f"el centro del diso {i_} es {centro_coordenadas} y su radio es {radio}\t"
         #'Route distance: {}metros\n'.format(route_distance)
    centros=np.array(centros)
    return [radios,centros],solutio

def grafica(lista):
    centros=list(lista[1].T)
    radios=lista[0]
    #print(centros,radios)
    output_file("toolbar.html")

    # create a new plot with the toolbar below
    p = figure(plot_width=700, plot_height=600,
               title='Greshgorin Circles', toolbar_location="left", x_range=(0, 40), y_range=(0, 40))

    p.circle(centros[0], centros[1], radius=radios)

    show(p)

    #guardar en .html y crear una funcion que mande un div y despliegue la grafica
#mat=[{'column-1': 0, 'column-2': 5, 'column-3': 10, 'column-4': 15}, {'column-1': 1, 'column-2': 6,
 #'column-3': 11, 'column-4': 16}, {'column-1': 2, 'column-2': 7, 'column-3': 12, 'column-4': 17}, {'column-1': 3, 'column-2': 8, 'column-3': 13, 'column-4': 18}]
#matriz=obtener_matriz(mat)
#datos=Greshgorin_calcule(matriz)

#grafica(datos)

def calculadora(matrix):
    matriz=obtener_matriz(matrix)
    datos,solutio=Greshgorin_calcule(matriz)
    grafica(datos)

    return  html.Div([
            html.H5("La solución de la Matriz es:"),





                html.Hr(),  # horizontal line
                html.Div([
                                   dcc.Markdown(solutio)
                        ]),

                html.Iframe(id='map',srcDoc=open('toolbar.html','r').read(),width='75%',height='550'),


            ])
if __name__ == '__calculadora__':
    calculadora()
