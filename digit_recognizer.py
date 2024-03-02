import tkinter as tk
from tkinter import Canvas, Button, messagebox
from tkinter.filedialog import asksaveasfilename
from PIL import Image, ImageDraw
import numpy as np
import pickle
from sklearn import datasets, linear_model, metrics
from sklearn.model_selection import train_test_split

# Load the model
def load_model():
    global reg
    with open('logistic_regression_model.pkl', 'rb') as f:
        reg = pickle.load(f)

# Predict digit
def predict_digit():
    # Get drawn digit
    im = Image.new('L', (8, 8), color='white')
    draw = ImageDraw.Draw(im)
    draw.line(coordinates, fill='black', width=2)
    del draw
    
    # Convert to numpy array
    im_arr = np.array(im)
    
    # Flatten and normalize
    im_arr = im_arr.flatten() / 255.0
    
    # Predict
    prediction = reg.predict(im_arr.reshape(1, -1))
    messagebox.showinfo("Prediction", f"The predicted digit is: {prediction[0]}")

# Clear canvas
def clear_canvas():
    global coordinates
    coordinates = []
    canvas.delete("all")

# Drawing functionality
def start_draw(event):
    global coordinates
    coordinates.append((event.x, event.y))

def draw(event):
    global coordinates
    coordinates.append((event.x, event.y))
    x1, y1 = (event.x - 2), (event.y - 2)
    x2, y2 = (event.x + 2), (event.y + 2)
    canvas.create_oval(x1, y1, x2, y2, fill='black')

# GUI setup
root = tk.Tk()
root.title("Digit Recognizer")

# Load model button
load_button = Button(root, text="Load Model", command=load_model)
load_button.pack()

# Canvas for drawing
canvas = Canvas(root, width=200, height=200, bg='white')
canvas.pack()
canvas.bind("<ButtonPress-1>", start_draw)
canvas.bind("<B1-Motion>", draw)

# Predict button
predict_button = Button(root, text="Predict Digit", command=predict_digit)
predict_button.pack()

# Clear button
clear_button = Button(root, text="Clear", command=clear_canvas)
clear_button.pack()

coordinates = []

root.mainloop()