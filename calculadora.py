import numpy as np
import numba
from bokeh.models import ColumnDataSource, Plot, LinearAxis, Grid
from bokeh.models.markers import Circle
from bokeh.io import curdoc, show

from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html


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
    for i in range(n-1):
        i_=i+1
        ce=matrix[i][i]
        centro_coordenadas=[ce.real,ce.imag]
        radio=np.sum(abs(matrix[i]))-abs(ce)
        radios.append(radio)
        centros.append(centro_coordenadas)
        print(f"el centro del diso {i_} es {centro_coordenadas} y su radio es {radio}")
    centros=np.array(centros)
    return [radios,centros]

def grafica(lista):
    centros=list(lista[1].T)
    radios=lista[0]
    print(centros,radios)

    source = ColumnDataSource(dict(x=centros[0], y=centros[1], radius=radios))
    plot = Plot(
        title='Discos de Greshgorin', plot_width=500, plot_height=500,
        min_border=1, toolbar_location='left')

    glyph = Circle(x="x", y="y",  radius='radius', line_color="#3288bd", fill_color="blue", line_width=3,toolbar_location="left")
    plot.add_glyph(source, glyph)

    xaxis = LinearAxis()
    plot.add_layout(xaxis, 'below')

    yaxis = LinearAxis()
    plot.add_layout(yaxis, 'left')

    plot.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
    plot.add_layout(Grid(dimension=1, ticker=yaxis.ticker))

    curdoc().add_root(plot)
    show(plot)

    #guardar en .html y crear una funcion que mande un div y despliegue la grafica
mat=[{'column-1': 0, 'column-2': 5, 'column-3': 10, 'column-4': 15}, {'column-1': 1, 'column-2': 6,
 'column-3': 11, 'column-4': 16}, {'column-1': 2, 'column-2': 7, 'column-3': 12, 'column-4': 17}, {'column-1': 3, 'column-2': 8, 'column-3': 13, 'column-4': 18}]
matriz=obtener_matriz(mat)
datos=Greshgorin_calcule(matriz)
grafica(datos)
