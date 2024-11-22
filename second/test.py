from tkinter import Tk
import pytest
from engine import Engine2D, Circle, Triangle, Rectangle, compare_images

def test_compare_screenshots():
    root = Tk()
    engine = Engine2D(root, name='test')
    engine.set_color('black')
    engine.add_shape(Circle(200, 200, 60))
    engine.draw()
    engine.add_shape(Triangle(300, 100, 100, 300, 500, 300))
    engine.draw()
    engine.add_shape(Rectangle(50, 50, 150, 150))
    engine.draw()
    engine.add_shape(Rectangle(0, 0, 0, 0))
    engine.draw()
    root.mainloop()
    root.destroy()
    assert compare_images("screenshot_check.png", "test.png")
    # delete test.png

def test_engine_draw(capsys):
    root = Tk()
    engine = Engine2D(root)
    engine.set_color('light salmon')
    engine.add_shape(Circle(200, 200, 60))
    engine.add_shape(Triangle(300, 100, 100, 300, 500, 300))
    engine.add_shape(Rectangle(50, 50, 150, 150))
    engine.draw()
    root.mainloop()
    root.destroy()
    captured = capsys.readouterr()
    assert "Drawing Circle: (200, 200) with radius 60, color: light salmon" in captured.out
    assert "Drawing Triangle: [(300, 100), (100, 300), (500, 300)], color: light salmon" in captured.out
    assert "Drawing Rectangle: (50, 50, 150, 150), color: light salmon" in captured.out
    assert engine.shapes == []

@pytest.mark.parametrize("color", ["red", "blue", "green"])
def test_set_color(color):
    root = Tk()
    engine = Engine2D(root)
    engine.set_color(color)
    assert engine.current_color == color
    root.destroy()

def test_circle_draw(capsys):
    root = Tk()
    engine = Engine2D(root)
    circle = Circle(0, 0, 5)
    circle.draw('blue', engine.canvas)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Drawing Circle: (0, 0) with radius 5, color: blue"
    root.destroy()

def test_triangle_draw(capsys):
    root = Tk()
    engine = Engine2D(root)
    triangle = Triangle(0, 0, 1, 1, 1, 0)
    triangle.draw("green", engine.canvas)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Drawing Triangle: [(0, 0), (1, 1), (1, 0)], color: green"
    root.destroy()

def test_rectangle_draw(capsys):
    root = Tk()
    engine = Engine2D(root)
    rectangle = Rectangle(0, 0, 2, 3)
    rectangle.draw("yellow", engine.canvas)
    captured = capsys.readouterr()
    assert captured.out.strip() == "Drawing Rectangle: (0, 0, 2, 3), color: yellow"