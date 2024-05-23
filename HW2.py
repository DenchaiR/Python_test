import turtle

tao = turtle.Pen()
tao1 = turtle.Pen()
tao2 = turtle.Pen()
taolist = []
taolist.clear()
taolist.append(tao)
taolist.append(tao1)
taolist.append(tao2)
taolist[0].shape('turtle')
taolist[1].shape('turtle')
taolist[2].shape('turtle')
taolist[0].color('green')
taolist[1].color('red')
taolist[2].color('blue')
taolist[1].up()
taolist[1].goto(30,30)
taolist[1].down()
taolist[2].up()
taolist[2].goto(-30,-30)
taolist[2].down()
for t in taolist:
    for i in range(10):
        t.forward(50)
        t.left(45)
