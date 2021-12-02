from tkinter import *
from tkinter import ttk
import random
from sortingVisualized import *
from colors import *


#Main Window

window = Tk()
window.title("Visualization of Sorting Algorithms")
window.maxsize(1000,700)
window.config(bg=WHITE)

algo_name = StringVar()
algo_list = ["Bucket Sort","Bubble Sort","Counting Sort","Heap Sort","Insertion Sort",
    "Merge Sort","Quick Sort","Radix Sort","Selection Sort","Shell Sort"]

speed = StringVar()
speed_list = ["Fast","Medium","Slow"]


#To be filled with random values
data = []


#display data to the screen
def drawData(data, colorArray):
    canvas.delete("all")
    canvas_width = 800
    canvas_height = 400
    x_width = canvas_width / (len(data) + 1)
    offset = 4
    spacing = 2
    normalizedData = [i / max(data) for i in data]

    for i, height in enumerate(normalizedData):
        x0 = i * x_width + offset + spacing
        y0 = canvas_height - height * 390
        x1 = (i + 1) * x_width + offset
        y1 = canvas_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])

    window.update_idletasks()


#generate array values to be sorted
def generate():
    global data

    data = []
    for i in range(0, 100):
        random_value = random.randint(1, 150)
        data.append(random_value)

    drawData(data, [BLUE for x in range(len(data))])


#set sorting speed
def set_speed():
    if speed_menu.get() == 'Slow':
        return 0.3
    elif speed_menu.get() == 'Medium':
        return 0.1
    else:
        return 0.001


#call the selected sorting algorithm
def sort():
    global data
    timeTick = set_speed()
    
    if algo_menu.get() == 'Bubble Sort':
        bubble(data, drawData, timeTick)
        drawData(data, [LIGHT_GREEN for x in range(len(data))])
        
    elif algo_menu.get() == 'Merge Sort':
        merge(data, 0,len(data)-1,drawData, timeTick)
        drawData(data, [LIGHT_GREEN for x in range(len(data))])

    elif algo_menu.get() == 'Quick Sort':
        quick(data, 0,len(data)-1,drawData, timeTick)
        drawData(data, [LIGHT_GREEN for x in range(len(data))])

    elif algo_menu.get() == 'Heap Sort':
        heap(data, drawData, timeTick)
        drawData(data, [LIGHT_GREEN for x in range(len(data))])

    elif algo_menu.get() == 'Selection Sort':
        selection(data, drawData, timeTick)
        drawData(data, [LIGHT_GREEN for x in range(len(data))])

    elif algo_menu.get() == 'Insertion Sort':
        insert(data, drawData, timeTick)
        drawData(data, [LIGHT_GREEN for x in range(len(data))])

    elif algo_menu.get() == 'Counting Sort':
        counting(data, drawData, timeTick)
        drawData(data, [LIGHT_GREEN for x in range(len(data))])

    elif algo_menu.get() == 'Shell Sort':
        shell(data, drawData, timeTick)
        drawData(data, [LIGHT_GREEN for x in range(len(data))])

    elif algo_menu.get() == 'Radix Sort':
        radix(data, drawData, timeTick)
        drawData(data, [LIGHT_GREEN for x in range(len(data))])

    elif algo_menu.get() == 'Bucket Sort':
        bucket(data, drawData, timeTick)
        drawData(data, [LIGHT_GREEN for x in range(len(data))])




#--------User Interface----------

UI_frame = Frame(window, width= 900, height=300, bg=WHITE)
UI_frame.grid(row=0, column=0, padx=10, pady=5)

# dropdown to select sorting algorithm 
l1 = Label(UI_frame, text="Algorithm: ", bg=WHITE)
l1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
algo_menu = ttk.Combobox(UI_frame, textvariable=algo_name, values=algo_list)
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

# dropdown to select sorting speed 
l2 = Label(UI_frame, text="Sorting Speed: ", bg=WHITE)
l2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
speed_menu = ttk.Combobox(UI_frame, textvariable=speed, values=speed_list)
speed_menu.grid(row=1, column=1, padx=5, pady=5)
speed_menu.current(0)

# sort button 
b1 = Button(UI_frame, text="Sort", command=sort, bg=BLUE)
b1.grid(row=2, column=1, padx=5, pady=5)

# button for generating array 
b3 = Button(UI_frame, text="Generate Array", command=generate, bg=BLUE)
b3.grid(row=2, column=0, padx=5, pady=5)

# canvas to draw our array 
canvas = Canvas(window, width=800, height=400, bg=WHITE)
canvas.grid(row=1, column=0, padx=10, pady=5)


window.mainloop()