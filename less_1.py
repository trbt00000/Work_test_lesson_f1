import math
pi = math.pi

def corner (inp1,inp2,inp3):
    type_corner = "неопределенного"
    inp1 = int(inp1)
    inp2 = int(inp2)
    inp3 = int(inp3)

    if inp1 > inp2 and inp1 > inp3:
        if inp1 * inp1 == (inp2 * inp2) + (inp3 * inp3):
            type_corner = "прямоугольного"
        elif inp1 * inp1 > (inp2 * inp2) + (inp3 * inp3):
            type_corner = "тупоугольного"
        else:
            type_corner = "остроугольного"
    elif inp2 > inp1 and inp2 > inp3:
        if inp2 * inp2 == (inp1 * inp1) + (inp3 * inp3):
            type_corner = "прямоугольного"
        elif inp2 * inp2 > (inp1 * inp1) + (inp3 * inp3):
            type_corner = "тупоугольныого"
        else:
            type_corner = "остроугольного"
    elif inp3 > inp1 and inp3 > inp2:
        if inp3 * inp3 == (inp2 * inp2) + (inp1 * inp1):
            type_corner = "прямоугольного"
        elif inp3 * inp3 > (inp2 * inp2) + (inp1 * inp1):
            type_corner = "тупоугольного"
        else:
            type_corner = "остроугольного"
    else:
        print("Ошибка: невозможно определить тип угла.")

    #print(f"{inp1}, {inp2}, {inp3} - {type_corner}")
    return type_corner

def ring(radius): # Функция расчета площади круга
    pl_k=pi*(int(radius)*int(radius))
    print(f'Площадь круга: {pl_k}')

def triangle(inp1,inp2,inp3): # Функция расчета площади/типа треугольника

    #----Нахождение площади треугольника----
    inp1 = int(inp1)
    inp2 = int(inp2)
    inp3 = int(inp3)
    pp=(inp1+inp2+inp3)/2
    pl_tr=pp*(pp-inp1)*(pp-inp2)*(pp-inp3)
    pl_tr_full=math.sqrt(pl_tr)
    # ----Нахождение типа треугольника----
    if inp1==inp2==inp3:
        type="равностороннего"
    elif inp1==inp2 or inp2==inp3 or inp1==inp3:
        type = "равнобедренного"
    elif inp1!=inp2!=inp3:
        type = "разностороннего"

    type_corner = corner(inp1, inp2, inp3)

    print(f'Площадь {type} {type_corner} треугольника: {pl_tr_full:.2f}')



name = input("Введите название фигуры: ")

if name=="круг" or name=="Круг" or name=="ring" or name=="Ring":
    radius = input("Введите радиус круга: ")
    ring(radius)

elif name=="треугольник" or name=="Треугольник"or name=="triangle" or name=="Triangle":
    inp1 = input("Введите сторону треугольника 1: ")
    inp2 = input("Введите сторону треугольника 2: ")
    inp3 = input("Введите сторону треугольника 3: ")
    triangle(inp1, inp2, inp3)


else:
    print("Фигура не определена")