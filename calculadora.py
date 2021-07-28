import numpy as np
import numba
from bokeh.models import ColumnDataSource, Plot, LinearAxis, Grid,ColorBar
from bokeh.models.markers import Circle
from bokeh.io import curdoc, show
from bokeh.plotting import figure, output_file, show, save
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
import dash
from dash.dependencies import Input, Output, State, ClientsideFunction
import dash_html_components as html
import dash_core_components as dcc
from bokeh.palettes import Spectral6
from bokeh.transform import linear_cmap
#import plotly.express as px


def obtener_matriz(data):
    matriz=[]
    if len(data)!=len(data[1]):
        print("Debe ser una matriz cuadrada")
    else:
        for fila in data:
            lista=list(fila.values())
            matriz.append(lista)
        #se define en que conjunto de numeros se trabaja
        final=np.array(matriz,dtype='f')

        print(final)
        return final
def Greshgorin_calcule(matrix):
    n=matrix.shape[1]
    radios=[]
    centros=[]
    solutio=['La solución es la siguiente: \n']
    for i in range(n):
        i_=i+1
        ce=matrix[i][i]
        centro_coordenadas=[ce.real,ce.imag]
        centro=(ce.real,ce.imag)
        radio=np.sum(abs(matrix[i]))-abs(ce)
        radios.append(radio)
        centros.append(centro_coordenadas)
        solutio.append(f"el centro del diso {i_} es {centro} y su radio es {radio}\n")
         #'Route distance: {}metros\n'.format(route_distance)
    centros=np.array(centros)
    return [radios,centros],solutio


def grafica(lista):
    centros=list(lista[1].T)
    radios=lista[0]
    x=list(centros[0])
    y=list(centros[1])
    mapper = linear_cmap(field_name='x', palette=Spectral6 ,low=min(x) ,high=max(x))
    TOOLTIPS = [
    ("index", "$index"),
    ("(x,y)", "($x, $y)"),
        ]

    source = ColumnDataSource(dict(x=x,y=y,radios=radios))

    # create a new plot with the toolbar below
    p = figure(plot_width=600, plot_height=600,
               title='Greshgorin Circles', toolbar_location="left", x_range=(0, 40),
                y_range=(0, 40),tools="tap"+",pan,wheel_zoom,box_zoom,reset,save",tooltips=TOOLTIPS)

    p.circle(x='x', y='y', line_color=mapper,color=mapper,radius='radios', fill_alpha=1, size=12, source=source,
    #centros[0], centros[1], radius=radios, color=list_of_colors,
                    selection_color="firebrick",

                       # set visual properties for non-selected glyphs
                       nonselection_fill_alpha=0.2,
                       nonselection_fill_color="blue",
                       nonselection_line_color="firebrick",
                       nonselection_line_alpha=1.0)
    #file_html(p, CDN, "my plot")
    #se crea un archivo .html el cual contiene la grafica
    save(p, "my_plot.html")


def calculadora(matrix):
    matriz=obtener_matriz(matrix)
    datos,solutio=Greshgorin_calcule(matriz)
    grafica(datos)
#re regresa una dicisión en htmal, la cual es mostrada en la interfaz
    return  html.Div([
            html.H5("La solución de la Matriz es:"),


                html.Hr(),  # horizontal line
                html.Div([
                                   dcc.Markdown(solutio)
                        ]),

                html.Iframe(id='map',srcDoc=open('my_plot.html','r').read(),width='75%',height='550'),


            ])
if __name__ == '__calculadora__':
    calculadora()
