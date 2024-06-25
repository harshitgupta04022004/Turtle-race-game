import turtle as t
import random as r

screen = t.Screen()
screen.setup(width=700, height=500)
win = t.textinput("Make Your Bet", "Who will win the race")

y = (-100)


class Race:
    def __init__(self, turtle):
        self.t = turtle
        self.dis = 0

    def motion(self):
        i = r.randint(0, 10)
        self.t.fd(i)
        self.dis += i
        return self.dis

    def features(self, y, color):
        self.t.penup()
        self.t.shape("turtle")
        self.t.goto(x=-330, y=y)
        self.t.color(color)


color_list = ["red", "blue", "green", "yellow", "orange", "indigo", "violet"]
turtle_list = []
for t_i in range(0, 6):
    tim = t.Turtle()
    tim_race = Race(tim)
    tim_race.features(y=y, color=color_list[t_i])
    turtle_list.append(tim_race)
    y += 40

max = 0
index = 0
while max < 650:
    j = 0
    for _ in turtle_list:
        check = _.motion()
        if check > max:
            max = check
        if max > 650:
            index = j
            break
        j += 1
        
if turtle_list[index].t.color()[0] == win:
    print("You win the bet")
else:
    print("You loses the bet")

screen.exitonclick()
