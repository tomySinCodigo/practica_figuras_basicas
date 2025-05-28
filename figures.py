"""
figures
DESCRIPCION
modulo para graficar figuras basicas con prints
por medio de la clase Draw

Draw tiene los metodos:
 - line
 - rectangle
 - square

 line tiene sus propios metodos:
 - horizontal
 - vertical
 - diagonal

diagonal tiene el parametro:
num: para indicarle la longitud de la linea
asc=True por defecto para que la linea oblicua sea ascedente con False sera descendente

para rectangle y square se pasan directamente los parametros
width: para el ancho
height: para el alto (solo para el rectangulo)
outline: True para inidicar si la grafica solo muestre el borde o False para llenar la grafica

width, height son enteros y outline es boleano

USO:
por ejemplo para graficar una diagonal:

draw = Draw('-') # instanciamos la clase y podemos pasarle un caracter, por defecto es '*'
fig = draw.line.diagonal(3, asc=False)
print(fig)

producira lo siguiente
*
  *
    *

puedes ver mas ejemplos de su uso en le archivo test.py
"""

__author__ = 'tomySinCodigo'
__version__ = '1.0.0'
__web__ = 'https://github.com/tomySinCodigo/practica_figuras_basicas'
__status__ = 'Development'


class Line:
    def __init__(self, char:str):
        self.char = char
        self._ = '  '

    def horizontal(self, num:int) -> str:
        '''retorna un string, una linea horizontal de longitud num'''
        return self.char * num

    def vertical(self, num:int) -> str:
        '''retorna un string, una linea vertical de longitud num'''
        return '\n'.join([self.char]*num)
    
    def diagonal(self, num:int, asc=True) -> str:
        '''retorna un string, una linea diagonal de longitud num'''
        rg = range(num-1, -1, -1) if asc else range(num)
        return '\n'.join([f'{self._*i}{self.char}' for i in rg])
    

class Rectangle:
    def __init__(self, width:int, height:int, char:str='*'):
        self.width = width
        self.height = height
        self.char = f'{char} '

    def _content(self, ichar='  ') -> str:
        return f'{self.char}{ichar*(self.width-2)}{self.char}\n' * \
        (self.height-2)

    def base(self) -> str:
        return self.char * self.width
    
    def outline(self) -> str:
        return f'{self.base()}\n{self._content()}{self.base()}'
    
    def fill(self) -> str:
        return f'{self.base()}\n{self._content(self.char)}{self.base()}'


class Draw:
    """draw figures:
    
    line:
    - vertical
    - horizontal
    - diagonal

    rectangle, square (outline or fill)
    """
    def __init__(self, char:str='*'):
        self.char = char
        self.line = Line(char=char)

    def rectangle(self, width:int=8, height=6, outline=True) -> str:
        '''retorna un string, de un rectangulo,
        
        con outline: True o False puede estar lleno o solo borde'''
        fig = Rectangle(width, height, self.char)
        return fig.outline() if outline else fig.fill()

    def square(self, width:int=6, outline=True) -> str:
        '''retorna un string, de un cuadrado
        
        con outline: True o False puede estar lleno o solo borde'''
        return self.rectangle(width, width, outline)
    

# if __name__ == '__main__':
#     draw = Draw()
    # print(draw.line.horizontal(6))
    # print(draw.rectangle())
    # print(draw.line.diagonal(3))
    # print(draw.line.diagonal(7, asc=False))
