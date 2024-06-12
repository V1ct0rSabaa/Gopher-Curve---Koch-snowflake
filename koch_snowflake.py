from turtle import forward, right, left, pencolor, width, speed, exitonclick
# from turtle import *

def koch(comprimento: float, ordem: int) -> None:
    if ordem > 0:
        comprimento /= 3.0
        # forward(comprimento / 3)  
        koch(comprimento, ordem - 1)
        left(60)
        koch(comprimento, ordem - 1)
        right(60 * 2)
        koch(comprimento, ordem - 1)
        left(60)
        koch(comprimento, ordem - 1)
    else:
        forward(comprimento)
        return


pencolor("blue")
width(2)
speed(10)

def estrela(tamanho) -> None:
    complexidade: int = 3
    for i in range(complexidade):
        koch(tamanho, complexidade) 
        right(120)

def inicial(): koch(600 , 3)

#inicial()
estrela(600)
exitonclick()