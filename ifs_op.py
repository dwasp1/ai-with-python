import turtle as tu
import random as r
def triangle():
    t.color(colors_p.pop(r.randint(0, len(colors_p) - 1)))
    t.begin_fill()
    t.fillcolor(colors_f.pop(r.randint(0, len(colors_p) - 1)))
    for i in range(3):
        t.forward(20)
        t.right(120)
    t.end_fill()
t = tu.Turtle()

colors_p = ["red","orange","blue","purple","pink","black","green"]
colors_f = ["red","orange","blue","purple","pink","black","green"]

triangle()

t.penup()
t.forward(30)
t.pendown()

triangle()

tu.done()
