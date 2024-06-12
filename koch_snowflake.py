from turtle import *
def koch(comprimento, ordem):
    if ordem > 0:
        comprimento /= 3.0
        # forward(comprimento / 3)  
        koch(comprimento, ordem - 1)
        left(60)
        koch(comprimento, ordem - 1)
        right(120)
        koch(comprimento, ordem - 1)
        left(60)
        koch(comprimento, ordem - 1)
    else:
        forward(comprimento)
        return


pencolor("blue")
width(2)
speed(10)

def estrela(tamanho):
    for i in range(3):
        koch(tamanho, 3) 
        right(120)

def inicial():
    koch(600 , 3)


#inicial()
estrela(600)
exitonclick()