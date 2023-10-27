import turtle as tu
colors = input()
def ident():
    t.penup()
    t.forward(30)
    t.pendown()
def shapes():
    for i in range(4):
        t.forward(20)
        t.right(90)
    ident()
    t.circle(20)
    ident()
    for i in range(3):
        t.forward(20)
        t.right(120)
t = tu.Turtle()

try:
    t.color(colors)
    shapes()
except:
    print("Цвет не определён")
    shapes()

tu.done()
