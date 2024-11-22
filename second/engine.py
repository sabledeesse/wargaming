from tkinter import Canvas, Tk
from PIL import Image, ImageGrab
import numpy as np


class Engine2D:
    def __init__(self, root, name: str = None):
        self.root = root
        self.name = name
        self.canvas = Canvas(root, bg='misty rose', width=720, height=720, name=self.name)
        self.canvas.pack()
        self.shapes = []
        self.current_color = "black"

    def set_color(self, color):
        self.current_color = color

    def add_shape(self, shape):
        self.shapes.append(shape)

    def draw(self):
        for shape in self.shapes:
            shape.draw(self.current_color, self.canvas)
        self.shapes.clear()
        self.root.update()
        if self.name:
            self.save_canvas_screenshot(self.name)
        self.root.after(2000, self.root.quit)

    def save_canvas_screenshot(self, filename):
        x = self.root.winfo_x() + self.canvas.winfo_x()
        y = self.root.winfo_y() + self.canvas.winfo_y()
        x2 = x + self.canvas.winfo_width()
        y2 = y + self.canvas.winfo_height()
        ImageGrab.grab(xdisplay=":0").crop((x, y, x2, y2)).save(filename + '.png')


class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self, color, canvas):
        print(f"Drawing Circle: ({self.x}, {self.y}) with radius {self.radius}, color: {color}")
        canvas.create_oval(self.x - self.radius, self.y - self.radius, self.x + self.radius,
                           self.y + self.radius,
                           fill=color,
                           outline=color,
                           width=3)

class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3

    def draw(self, color, canvas):
        print(f"Drawing Triangle: [({self.x1}, {self.y1}), ({self.x2}, {self.y2}), ({self.x3}, {self.y3})], color: {color}")
        canvas.create_polygon(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3,
                              outline=color,
                              fill=color,
                              width=4)

class Rectangle:
    def __init__(self, x0, y0, x1, y1):
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1

    def draw(self, color, canvas):
        print(f"Drawing Rectangle: ({self.x0}, {self.y0}, {self.x1}, {self.y1}), color: {color}")
        canvas.create_rectangle(self.x0, self.y0, self.x1, self.y1,
                                outline=color,
                                fill=color,
                                width=4)

def compare_images(img1_path, img2_path):
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)
    arr1 = np.array(img1)
    arr2 = np.array(img2)
    return np.array_equal(arr1, arr2)

if __name__ == "__main__":
    # I added 'fill' parameter cuz its beautiful this way
    root = Tk()
    engine = Engine2D(root)
    engine.set_color('light salmon')
    engine.add_shape(Circle(200, 200, 60))
    engine.draw()
    engine.set_color('coral')
    engine.add_shape(Triangle(300, 100, 100, 300, 500, 300))
    engine.draw()
    engine.set_color('red')
    engine.add_shape(Rectangle(50, 50, 150, 150))
    engine.draw()
    engine.add_shape(Rectangle(0, 0, 0, 0))
    engine.draw()
    root.mainloop()
    root.destroy()

