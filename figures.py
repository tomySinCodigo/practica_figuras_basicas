class Line:
    def __init__(self, char:str):
        self.char = char

    def horizontal(self, num:int) -> str:
        return self.char * num
    

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
        '''draw rectangle'''
        fig = Rectangle(width, height, self.char)
        return fig.outline() if outline else fig.fill()

    

if __name__ == '__main__':
    draw = Draw()
    # print(draw.line.horizontal(6))
    print(draw.rectangle())