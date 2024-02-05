from pyglet.window import Window
from pyglet.app import run
from pyglet.shapes import Circle, Rectangle
from pyglet.graphics import Batch
from pyglet import clock
import math

def hex_to_rgb(hex_color):
    return int(hex_color[1:3],16), int(hex_color[3:5],16),int(hex_color[5:7],16), 255

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

class Renderer(Window):
    def __init__(self):
        super().__init__(950, 950, "Merge Sort")
        self.batch = Batch()
        self.x = [6, 4, 7, 1, 5, 3, 2, 8] 
        self.colors = ["#F3D6B8", "#F0C6D4", "#EAAAC4", "#E08BB2", "#D26A9D", "#BD3376", "#A61C4F", "#912239"]
        self.bars = []

        for e, i in enumerate(self.x):
            if i < len(self.colors):
                color = self.colors[i]
                rgb_color = hex_to_rgb(color)
                self.bars.append(Rectangle(100 + e * 100, 100, 80, i * 100, color=rgb_color, batch=self.batch))

    def merge_sort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2  
            L = arr[:mid]  
            R = arr[mid:] 

            self.merge_sort(L)
            self.merge_sort(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

    def on_update(self, deltatime):
        self.merge_sort(self.x)
        self.update_bars()

    def update_bars(self):
        self.bars = []
        for e, i in enumerate(self.x):
            if i < len(self.colors):
                color = self.colors[i]
                rgb_color = hex_to_rgb(color)
                self.bars.append(Rectangle(100 + e * 100, 100, 80, i * 100, color=rgb_color, batch=self.batch))

    def on_draw(self):
        self.clear()
        self.batch.draw()

renderer = Renderer()
clock.schedule_interval(renderer.on_update, 3)
run()