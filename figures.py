class Line:
    def __init__(self, char:str):
        self.char = char

    def horizontal(self, num:int) -> str:
        '''retorna un string horizontal de longitud num'''
        return self.char * num

    def vertical(self, num:int) -> str:
        '''retorna un string vertical de longitud num'''
        return '\n'.join([self.char]*num)
    

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

    

if __name__ == '__main__':
    draw = Draw()
    # print(draw.line.horizontal(6))
    print(draw.line.vertical(7))