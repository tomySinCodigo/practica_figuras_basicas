from figures import __author__, Draw


def test() -> str:
    draw = Draw(char='+')
    text = 'TEST\n'
    text += f'autor: {__author__}\n\n'
    text += f'Linea horizontal:\n{draw.line.horizontal(8)}\n\n'
    text += f'Linea vertical:\n{draw.line.vertical(8)}\n\n'
    text += f'Rectangulo:\n{draw.rectangle(width=10, height=4, outline=False)}\n\n'
    text += f'Cuadrado:\n{draw.square(width=8, outline=True)}\n\n'
    text += f'Linea diagonal ascendente:\n{draw.line.diagonal(3)}\n\n'
    text += f'Linea diagonal descendente:\n{draw.line.diagonal(5, asc=False)}\n\n'
    return text

def escribeArchivo(text:str):
    with open('salida_test.txt', 'w') as file:
        file.write(text)

if __name__ == '__main__':
    escribeArchivo(test())
