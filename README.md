# Figuras Basicas

realizando figuras basicas usando python

## Uso

primero importamos la clase `Draw` del modulo `figures`

```python
from figures import Draw
draw = Draw()
```

para dibujar un rectangulo de largo 7 y de alto 3

```python
fig = draw.rectangle(width=7, height=3)
print(fig)
```

produce:

```python
* * * * * * *                            
*           *
* * * * * * *
```

para que este lleno usamo el parametro `outline=False`

```python
fig2 = draw.rectangle(7, 3, outline=False)
print(fig2)
```

produce:

```python
* * * * * * *
* * * * * * *
* * * * * * *
```

mas informacion del proyecto en la [wiki](https://github.com/tomySinCodigo/practica_figuras_basicas/wiki)
