import tkinter as tk
from PIL import Image, ImageDraw, ImageOps
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model # type: ignore



class Draw:


    def __init__(self, root):
        self.root = root
        self.root.title("Draw Digit")

        self.canvas_width = 280
        self.canvas_height = 280
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.canvas.pack()

        self.button = tk.Button(root, text="Predict", command=self.convert_to_28x28)
        self.button.pack()

        self.prediction_label = tk.Label(root, text="Draw a digit and click 'Predict'", font=("Helvetica", 16))
        self.prediction_label.pack()

        self.image = Image.new("RGB", (self.canvas_width, self.canvas_height), (255, 255, 255))
        self.draw = ImageDraw.Draw(self.image)

        self.canvas.bind("<B1-Motion>", self.paint)

        

    def paint(self, event):
        x, y = event.x, event.y
        radius = 6
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill='black')
        self.draw.ellipse([x - radius, y - radius, x + radius, y + radius], fill='black')


    def convert_to_28x28(self):

        gray_image = self.image.convert("L")
        inverted_image = ImageOps.invert(gray_image)
        resized_image = inverted_image.resize((28, 28), Image.Resampling.LANCZOS)
        normalized_array = np.array(resized_image) / 255.0
        input_array = normalized_array.reshape((28, 28, 1))
        input_array = np.expand_dims(input_array, axis=0)

        prediction = model.predict(input_array)
        number = np.argmax(prediction[0])
        percentage = round(max(prediction[0]))*100
        self.prediction_label.config(text=f"{number} by {percentage} % !")



if __name__ == "__main__":

    model = load_model('./models/e10.h5')
    root = tk.Tk()
    app = Draw(root)
    root.mainloop()
