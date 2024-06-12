from turtle import *

angulo_curva = 60
regra_para_a = "A-B--B+A++AA+B-"
regra_para_b = "+A-BB--B-A++A+B"
def curvaGosper(ordem, tamanho, regra):
    if ordem < 1:
        forward(tamanho)
        return
    else:
        if regra == "A":
            regra_escolhida = regra_para_a 
        else:
            regra_escolhida = regra_para_b
        for char in regra_escolhida:
            if char == "A":
                curvaGosper(ordem - 1, tamanho, "A")
            elif char == "A":
                curvaGosper(ordem - 1, tamanho, "B")
            elif char == "-":
                right(angulo_curva)
            elif char == "+":
                left(angulo_curva)

bgcolor("white")
color("white")
pensize(2)
speed(10)
left(90)
goto(-100, -300)
color("purple")
#curvaGosper(1, 50, "B")
#curvaGosper(2, 50, "B")
curvaGosper(3, 50, "B")
exitonclick()