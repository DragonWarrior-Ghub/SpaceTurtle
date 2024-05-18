# Импорты
import turtle
from random import randint

# Переменная нужна для бесконечного цикла при поражении, чтобы застопить игру
# Другими словами, пока не нажмёшь пробел, который обнуляет игру, она застрянет на одном цикле
useless = turtle.Turtle()
useless.hideturtle()
useless.up()

# Текст
text = turtle.Turtle()
text.up()
text.hideturtle()
text.goto(-170, -90)
text.pencolor('white')
text2 = turtle.Turtle()
text2.up()
text2.hideturtle()
text2.goto(60, -90)
text2.pencolor('white')
text3 = turtle.Turtle()
text3.up()
text3.hideturtle()
text3.goto(-150, -150)
text3.pencolor('white')
text4 = turtle.Turtle()
text4.up()
text4.hideturtle()
text4.goto(-50, -65)
text4.pencolor('white')

# Создание игрока
pl = turtle.Turtle(shape='turtle')
pl.color('gray')
pl.shapesize(3, 3)
pl.speed(0)
pl.left(90)
pl.penup()

window = turtle.Screen()  # Создание окна
window.setup(500, 700)  # Создание размеров окна
window.bgcolor('black')  # Цвет окна
window.title('SpaceTurtle')  # Название окна

# Создание границ путей
line = turtle.Turtle()
line.speed(1000)
line.hideturtle()
line.penup()
line.goto(-50, 350)


# Создание звёзд
star0 = turtle.Turtle(shape='circle')  # Форма круга
star0.shapesize(0.3, 0.3)  # Размер
star0.speed(10000)  # Моментальное перемещение на точку
star0.color('white')
star0.penup()
star0.goto(randint(-250, -160), randint(-350, 350))  # Рандомные координаты по x и y
star1 = turtle.Turtle(shape='circle')
star1.shapesize(0.3, 0.3)
star1.speed(10000)
star1.color('white')
star1.penup()
star1.goto(randint(-250, -160), randint(-350, 350))
star2 = turtle.Turtle(shape='circle')
star2.shapesize(0.3, 0.3)
star2.speed(10000)
star2.color('white')
star2.penup()
star2.goto(randint(-250, -160), randint(-350, 350))
star3 = turtle.Turtle(shape='circle')
star3.shapesize(0.3, 0.3)
star3.speed(10000)
star3.color('white')
star3.penup()
star3.goto(randint(-250, -160), randint(-350, 350))
star4 = turtle.Turtle(shape='circle')
star4.shapesize(0.3, 0.3)
star4.speed(10000)
star4.color('white')
star4.penup()
star4.goto(randint(-250, -160), randint(-350, 350))
star5 = turtle.Turtle(shape='circle')
star5.shapesize(0.3, 0.3)
star5.speed(10000)
star5.color('white')
star5.penup()
star5.goto(randint(160, 250), randint(-350, 350))  # Координаты по X изменены (звёзды идут на другую сторону)
star6 = turtle.Turtle(shape='circle')
star6.shapesize(0.3, 0.3)
star6.speed(10000)
star6.color('white')
star6.penup()
star6.goto(randint(160, 250), randint(-350, 350))
star7 = turtle.Turtle(shape='circle')
star7.shapesize(0.3, 0.3)
star7.speed(10000)
star7.color('white')
star7.penup()
star7.goto(randint(160, 250), randint(-350, 350))
star8 = turtle.Turtle(shape='circle')
star8.shapesize(0.3, 0.3)
star8.speed(10000)
star8.color('white')
star8.penup()
star8.goto(randint(160, 250), randint(-350, 350))
star9 = turtle.Turtle(shape='circle')
star9.shapesize(0.3, 0.3)
star9.speed(10000)
star9.color('white')
star9.penup()
star9.goto(randint(160, 250), randint(-350, 350))

# Создание врагов
ship0 = turtle.Turtle()
ship1 = turtle.Turtle()
ship2 = turtle.Turtle()
ship3 = turtle.Turtle()
ship4 = turtle.Turtle()
ship5 = turtle.Turtle()
ship6 = turtle.Turtle()
ship7 = turtle.Turtle()
ship8 = turtle.Turtle()
ship9 = turtle.Turtle()
ship10 = turtle.Turtle()
ship11 = turtle.Turtle()
ship12 = turtle.Turtle()
ship13 = turtle.Turtle()
ship14 = turtle.Turtle()

# Добавление всех врагов в список
ships = [ship0, ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9, ship10, ship11, ship12, ship13,
         ship14]
# Обработка врагов
for i in range(0, 15):
    ships[i].hideturtle()
    ships[i].shapesize(6, 3)
    ships[i].speed(10000)
    ships[i].up()
    ships[i].right(90)
    ships[i].color('grey')

# Ешки нужны где-то в цикле но мне лень разбираться зачем они вообще были нужны
# Одно ясно точно - без них работать не будет, если не переделать врагов наполовину
e0 = turtle.Turtle()
e1 = turtle.Turtle()
e2 = turtle.Turtle()
e3 = turtle.Turtle()
e4 = turtle.Turtle()
e5 = turtle.Turtle()
e6 = turtle.Turtle()
e7 = turtle.Turtle()
e8 = turtle.Turtle()
e9 = turtle.Turtle()
e10 = turtle.Turtle()
dif = 0  # Сложность
record = 0  # Рекорд
lose = 1  # Поражение
count = 0  # Кол-во врагов


# Движение влево
def pl_left():
    plx, ply = pl.pos()  # Определение координат
    if plx == -100:  # Ограничение на движение
        pass
    else:
        pl.goto(plx-100, ply)  # Передвижение на координату по x


# Движение вправо
def pl_right():
    plx, ply = pl.pos()
    if plx == 100:
        pass
    else:
        pl.goto(plx+100, ply)


# Созданеи новой игры
def new_game():
    global dif  # Глобализация переменных
    global lose
    if lose == 1:  # Обнуление переменных
        dif = 0
        lose = 0


# Привязка функций к кнопкам
window.onkey(pl_left, 'Left')
window.onkey(pl_right, 'Right')
window.onkey(new_game, 'space')
window.listen()

# Создание текста на экране
text.write('Движение вправо-влево на стрелочки', font='TimesNewRoman 15')
text3.write('Нажмите на пробел что бы начать', font='TimesNewRoman 15')

# Остановка игры до нажатия пробела
while lose == 1:
    useless.forward(1)


# Создание игрвого пространста
while True:

    # Обнуление текста
    text.clear()
    text2.clear()
    text3.clear()
    text4.clear()

    # Прорисовка путей
    line.pencolor('white')
    line.pendown()
    line.goto(-50, -350)
    line.penup()
    line.goto(50, 350)
    line.pendown()
    line.goto(50, -350)

    # Перемещение игрока
    pl.goto(0, -300)
    pl.showturtle()

    # Цикл идёт пока сложность не поднимется до 200
    # Остальные циклы почти такие же, поэтому комментов там будет куда меньше, чем в первом
    while dif < 200 and lose != 1:  # Проверка условия поражения
        record = 1
        if dif % 20 == 0:  # Каждые 20 тиков происходит написанный ниже алгоритм

            # Выбор случайного врага
            enemy = randint(0, 14)
            while ships[enemy] == e0 or ships[enemy] == e1 or ships[enemy] == e2:
                enemy = randint(0, 14)

            # Выбор пути врагом
            road = randint(1, 3)
            if road == 1:
                ships[enemy].goto(-100, 370)
            elif road == 2:
                ships[enemy].goto(0, 370)
            else:
                ships[enemy].goto(100, 370)
            ships[enemy].showturtle()

            # Присваивание к доп. переменной
            if count == 0:
                e0 = ships[enemy]
            elif count == 1:
                e1 = ships[enemy]
            elif count == 2:
                e2 = ships[enemy]
                count = -1
            count += 1

        # Движение врагов (скорость в скорбках меняется от сложности)
        e0.forward(13)
        e1.forward(13)
        e2.forward(13)

        dif += 1  # Нарастает сложность
        x, y = pl.pos()  # Получение координат игрока

        # Проверка столкновения на каждого врага. Кривые хитбоксы находятся именно тут.
        xe, ye = e0.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e1.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e2.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

    # Цикл следующего уровня сложности. Начинается лишь когда сложность доходит до 200 и кончается когда будет 400.
    # Также работает и со следующими циклами, поэтому комментов там почти не будет
    while dif < 400 and lose != 1:
        if dif % 18 == 0:
            enemy = randint(0, 14)
            road = randint(1, 3)
            while ships[enemy] == e0 or ships[enemy] == e1 or ships[enemy] == e2:
                enemy = randint(0, 14)
            if road == 1:
                ships[enemy].goto(-100, 370)
            elif road == 2:
                ships[enemy].goto(0, 370)
            else:
                ships[enemy].goto(100, 370)

            ships[enemy].showturtle()
            if count == 0:
                e0 = ships[enemy]
            elif count == 1:
                e1 = ships[enemy]
            elif count == 2:
                e2 = ships[enemy]
                count = -1
            count += 1

        # Враги ускорились
        e0.forward(18)
        e1.forward(18)
        e2.forward(18)

        dif += 1
        x, y = pl.pos()

        xe, ye = e0.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e1.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e2.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

    while dif < 700 and lose != 1:
        if dif % 15 == 0:
            enemy = randint(0, 14)
            road = randint(1, 3)
            while ships[enemy] == e0 or ships[enemy] == e1 or ships[enemy] == e2:
                enemy = randint(0, 14)
            if road == 1:
                ships[enemy].goto(-100, 370)
            elif road == 2:
                ships[enemy].goto(0, 370)
            else:
                ships[enemy].goto(100, 370)
            ships[enemy].showturtle()
            if count == 0:
                e0 = ships[enemy]
            elif count == 1:
                e1 = ships[enemy]
            elif count == 2:
                e2 = ships[enemy]
                count = -1
            count += 1

        e0.forward(21)
        e1.forward(21)
        e2.forward(21)

        dif += 1
        x, y = pl.pos()

        xe, ye = e0.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e1.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e2.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

    while dif < 900 and lose != 1:
        if dif % 50 == 0:
            # Цикл работает дважды для создания двух врагов за 50 тиков
            for i in range(2):
                enemy = randint(0, 14)
                road = randint(1, 3)
                while ships[enemy] == e0 or ships[enemy] == e1 or ships[enemy] == e2 or ships[enemy] == e3:
                    enemy = randint(0, 14)
                if road == 1:
                    ships[enemy].goto(-100, 370)
                elif road == 2:
                    ships[enemy].goto(0, 370)
                else:
                    ships[enemy].goto(100, 370)
                ships[enemy].showturtle()
                if count == 0:
                    e0 = ships[enemy]
                elif count == 1:
                    e1 = ships[enemy]
                elif count == 2:
                    e2 = ships[enemy]
                elif count == 3:
                    e3 = ships[enemy]
                    count = -1
                count += 1

        e0.forward(15)
        e1.forward(15)
        e2.forward(15)
        e3.forward(15)

        dif += 1

        x, y = pl.pos()

        xe, ye = e0.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e1.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e2.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e3.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

    while dif < 1300 and lose != 1:
        if dif % 15 == 0:
            for i in range(2):
                enemy = randint(0, 14)
                road = randint(1, 3)
                while ships[enemy] == e0 or ships[enemy] == e1 or ships[enemy] == e2 or ships[enemy] == e3 \
                        or ships[enemy] == e4 or ships[enemy] == e5:
                    enemy = randint(0, 14)
                if road == 1:
                    ships[enemy].goto(-100, 370)
                elif road == 2:
                    ships[enemy].goto(0, 370)
                else:
                    ships[enemy].goto(100, 370)
                ships[enemy].showturtle()
                if count == 0:
                    e0 = ships[enemy]
                elif count == 1:
                    e1 = ships[enemy]
                elif count == 2:
                    e2 = ships[enemy]
                elif count == 3:
                    e3 = ships[enemy]
                elif count == 4:
                    e4 = ships[enemy]
                elif count == 5:
                    e5 = ships[enemy]
                    count = -1
                count += 1

        e0.forward(21)
        e1.forward(21)
        e2.forward(21)
        e3.forward(21)
        e4.forward(21)
        e5.forward(21)
        dif += 1

        x, y = pl.pos()

        xe, ye = e0.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e1.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e2.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e3.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e4.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e5.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

    while dif < 1700 and lose != 1:
        if dif % 10 == 0:
            for i in range(2):
                enemy = randint(0, 14)
                road = randint(1, 3)
                while ships[enemy] == e0 or ships[enemy] == e1 or ships[enemy] == e2 or ships[enemy] == e3 \
                        or ships[enemy] == e4 or ships[enemy] == e5:
                    enemy = randint(0, 14)
                if road == 1:
                    ships[enemy].goto(-100, 370)
                elif road == 2:
                    ships[enemy].goto(0, 370)
                else:
                    ships[enemy].goto(100, 370)
                ships[enemy].showturtle()
                if count == 0:
                    e0 = ships[enemy]
                elif count == 1:
                    e1 = ships[enemy]
                elif count == 2:
                    e2 = ships[enemy]
                elif count == 3:
                    e3 = ships[enemy]
                elif count == 4:
                    e4 = ships[enemy]
                elif count == 5:
                    e5 = ships[enemy]
                    count = -1
                count += 1

        e0.forward(30)
        e1.forward(30)
        e2.forward(30)
        e3.forward(30)
        e4.forward(30)
        e5.forward(30)
        dif += 1

        x, y = pl.pos()

        xe, ye = e0.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e1.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e2.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e3.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e4.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e5.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

    while dif < 2100 and lose != 1:
        if dif % 7 == 0:
            for i in range(2):
                enemy = randint(0, 14)
                road = randint(1, 3)
                while ships[enemy] == e0 or ships[enemy] == e1 or ships[enemy] == e2 or ships[enemy] == e3 \
                        or ships[enemy] == e4 or ships[enemy] == e5 or ships[enemy] == e6 or ships[enemy] == e7 \
                        or ships[enemy] == e8:
                    enemy = randint(0, 14)
                if road == 1:
                    ships[enemy].goto(-100, 370)
                elif road == 2:
                    ships[enemy].goto(0, 370)
                else:
                    ships[enemy].goto(100, 370)
                ships[enemy].showturtle()
                if count == 0:
                    e0 = ships[enemy]
                elif count == 1:
                    e1 = ships[enemy]
                elif count == 2:
                    e2 = ships[enemy]
                elif count == 3:
                    e3 = ships[enemy]
                elif count == 4:
                    e4 = ships[enemy]
                elif count == 5:
                    e5 = ships[enemy]
                elif count == 6:
                    e6 = ships[enemy]
                elif count == 7:
                    e7 = ships[enemy]
                elif count == 8:
                    e8 = ships[enemy]
                    count = -1
                count += 1

        e0.forward(45)
        e1.forward(45)
        e2.forward(45)
        e3.forward(45)
        e4.forward(45)
        e5.forward(45)
        e6.forward(45)
        e7.forward(45)
        e8.forward(45)

        dif += 1
        x, y = pl.pos()

        xe, ye = e0.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e1.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e2.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e3.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e4.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e5.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e6.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e7.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e8.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

    # Последний цикл (максимальная сложность).
    while dif > 1 and lose != 1:
        if dif % 4 == 0:
            for i in range(2):
                enemy = randint(0, 14)
                road = randint(1, 3)
                while ships[enemy] == e0 or ships[enemy] == e1 or ships[enemy] == e2 or ships[enemy] == e3 \
                        or ships[enemy] == e4 or ships[enemy] == e5 or ships[enemy] == e6 or ships[enemy] == e7 \
                        or ships[enemy] == e8 or ships[enemy] == e9 or ships[enemy] == e10:
                    enemy = randint(0, 14)
                if road == 1:
                    ships[enemy].goto(-100, 370)
                elif road == 2:
                    ships[enemy].goto(0, 370)
                else:
                    ships[enemy].goto(100, 370)
                ships[enemy].showturtle()
                if count == 0:
                    e0 = ships[enemy]
                elif count == 1:
                    e1 = ships[enemy]
                elif count == 2:
                    e2 = ships[enemy]
                elif count == 3:
                    e3 = ships[enemy]
                elif count == 4:
                    e4 = ships[enemy]
                elif count == 5:
                    e5 = ships[enemy]
                elif count == 6:
                    e6 = ships[enemy]
                elif count == 7:
                    e7 = ships[enemy]
                elif count == 8:
                    e8 = ships[enemy]
                elif count == 9:
                    e9 = ships[enemy]
                elif count == 10:
                    e10 = ships[enemy]
                    count = -1
                count += 1
        e0.forward(60)
        e1.forward(60)
        e2.forward(60)
        e3.forward(60)
        e4.forward(60)
        e5.forward(60)
        e6.forward(60)
        e7.forward(60)
        e8.forward(60)
        e9.forward(60)
        e10.forward(60)

        dif += 1
        x, y = pl.pos()

        xe, ye = e0.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e1.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e2.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e3.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e4.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e5.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e6.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e7.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e8.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e9.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

        xe, ye = e10.pos()
        if y + 60 >= ye >= y - 90 and x - 50 <= xe <= x + 50:
            lose = 1

    # Скрытие игрока
    pl.hideturtle()

    # Скрытие врагов
    e0 = useless
    e1 = useless
    e2 = useless
    e3 = useless
    e4 = useless
    e5 = useless
    e6 = useless
    e7 = useless
    e8 = useless
    e9 = useless
    e10 = useless

    # Скрытие путей и врагов
    for i in range(0, 15):
        ships[i].hideturtle()
    line.pencolor('black')
    line.goto(50, 350)
    line.penup()
    line.goto(-50, -350)
    line.pendown()
    line.goto(-50, 350)

    # Запись рекорда и других сообщений (сейва нет, рекорд сохраняется лишь до выключения игры)
    if record > 0:
        text.goto(-100, -90)
        text.write('Лучший рекорд:', font='TimesNewRoman 15')
        if record < dif:
            record = dif
        text2.write(str(record), font='TimesNewRoman 15')
        text3.write('Нажмите пробел для новой игры', font='TimesNewRoman 15')

    # Игра стопится до перезапуска
    while lose == 1:
        useless.forward(1)
