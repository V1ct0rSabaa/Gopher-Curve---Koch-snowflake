from turtle import forward, right, left, bgcolor, color, pensize, speed, left, goto, exitonclick
# from turtle import *

angulo_curva: int = 60
regra_para_a: str = "A-B--B+A++AA+B-"
regra_para_b: str = "+A-BB--B-A++A+B"

def curvaGosper(ordem: int, tamanho: float, regra: str) -> None:
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
curvaGosper(3, 50, "B")
exitonclick()