from figures import Draw


def test() -> str:
    draw = Draw(char='+')
    text = 'TEST\n'
    text += f'Linea horizontal:\n{draw.line.horizontal(8)}\n\n'
    text += f'Linea vertical:\n{draw.line.vertical(8)}\n\n'

    return text

def escribeArchivo(text:str):
    with open('salida_test.txt', 'w') as file:
        file.write(text)

if __name__ == '__main__':
    escribeArchivo(test())