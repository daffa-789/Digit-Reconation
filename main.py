import tkinter as tk
from PIL import Image, ImageOps, ImageDraw
import numpy as np
import tensorflow as tf

# Load model yang sudah dilatih
try:
    model = tf.keras.models.load_model('digit_model.keras')
except Exception as e:
    print("Error: File 'digit_model.keras' tidak ditemukan! Jalankan 'train.py' terlebih dahulu.")
    exit()

class SmoothDigitRecognizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Digit Recognizer - Smooth Brush")
        self.root.resizable(False, False)

        self.canvas_size = 280
        
        # UI Canvas (Latar putih)
        self.canvas = tk.Canvas(root, width=self.canvas_size, height=self.canvas_size, bg='white', cursor='pencil')
        self.canvas.pack(pady=10)

        # Background image internal PIL
        self.image = Image.new("L", (self.canvas_size, self.canvas_size), "white")
        self.draw = ImageDraw.Draw(self.image)

        # Variabel untuk melacak posisi mouse terakhir (Biar jadi kuas mulus)
        self.last_x, self.last_y = None, None

        # Bind Event Mouse
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw_smooth_lines)

        # Tombol Predict
        self.btn_predict = tk.Button(root, text="Predict", font=("Arial", 12, "bold"), command=self.predict_digit, bg='#4CAF50', fg='white', width=10)
        self.btn_predict.pack(side=tk.LEFT, padx=30, pady=10)

        # Tombol Clear
        self.btn_clear = tk.Button(root, text="Clear", font=("Arial", 12, "bold"), command=self.clear_canvas, bg='#f44336', fg='white', width=10)
        self.btn_clear.pack(side=tk.RIGHT, padx=30, pady=10)

        # Label Output Hasil
        self.lbl_result = tk.Label(root, text="Silahkan gambar angka...", font=("Arial", 16))
        self.lbl_result.pack(pady=20)

    def start_draw(self, event):
        # Catat titik awal saat klik pertama kali
        self.last_x, self.last_y = event.x, event.y

    def draw_smooth_lines(self, event):
        x, y = event.x, event.y
        brush_width = 18 # Ketebalan kuas ideal untuk MNIST

        if self.last_x and self.last_y:
            # Menggambar garis kontinu yang menghubungkan titik lama ke titik baru (Anti patah-patah)
            self.canvas.create_line(self.last_x, self.last_y, x, y, width=brush_width, fill="black", capstyle=tk.ROUND, smooth=True)
            self.draw.line([self.last_x, self.last_y, x, y], fill="black", width=brush_width, joint="round")
            
        self.last_x, self.last_y = x, y

    def clear_canvas(self):
        self.canvas.delete("all")
        self.image = Image.new("L", (self.canvas_size, self.canvas_size), "white")
        self.draw = ImageDraw.Draw(self.image)
        self.last_x, self.last_y = None, None
        self.lbl_result.config(text="Silahkan gambar angka...", fg="black")

    def predict_digit(self):
        # 1. Invert warna terlebih dahulu karena getbbox mencari objek non-hitam
        img_inverted = ImageOps.invert(self.image)
        bbox = img_inverted.getbbox()
        
        if bbox:
            # 2. [FITUR CERDAS] Auto-Crop area angka yang digambar saja
            cropped = img_inverted.crop(bbox)
            
            # 3. Buat persegi proporsional dengan padding agar posisi angka seimbang
            w, h = cropped.size
            max_dim = max(w, h) + 40
            square_img = Image.new("L", (max_dim, max_dim), "black")
            square_img.paste(cropped, ((max_dim - w) // 2, (max_dim - h) // 2))
            
            # 4. Resize ke 20x20 (ukuran inti tulisan MNIST) lalu taruh di tengah kanvas 28x28
            digit_20x20 = square_img.resize((20, 20), Image.Resampling.LANCZOS)
            final_img = Image.new("L", (28, 28), "black")
            final_img.paste(digit_20x20, (4, 4))
            
            # 5. Normalisasi dan Reshape untuk input Keras Model
            img_array = np.array(final_img) / 255.0
            img_input = img_array.reshape(1, 28, 28, 1)

            # 6. Prediksi lewat model
            prediction = model.predict(img_input)
            predicted_digit = np.argmax(prediction)
            confidence = np.max(prediction) * 100

            # Tampilkan hasil
            self.lbl_result.config(text=f"Prediksi: {predicted_digit} ({confidence:.2f}%)", fg="#4CAF50")
        else:
            self.lbl_result.config(text="Kanvas kosong! Silahkan gambar dulu.", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = SmoothDigitRecognizerApp(root)
    root.mainloop()