# 🔢 Digit Recognition (MNIST CNN)

Aplikasi desktop GUI interaktif berbasis Python dan Tkinter untuk menggambar angka (0–9) dan memprediksi angka tersebut secara real-time menggunakan Convolutional Neural Network (CNN) Keras/TensorFlow yang dilatih pada dataset MNIST.

![Python](https://img.shields.io/badge/Python-3.9+-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green)

---

## ✨ Fitur

- 🖌️ **Kanvas Gambar Halus**: Menggambar angka dengan mouse/stylus dengan antialiasing dan ketebalan kuas adaptif.
- 🎯 **Preprocessing Standar MNIST**: Auto-crop bounding box, resize 20×20 dengan aspect ratio dijaga, padding ke 28×28 di tengah kanvas hitam.
- 🧠 **CNN 10 Layer**:
  - `Conv2D (32, 3x3) -> BatchNormalization -> MaxPooling2D (2x2)`
  - `Conv2D (64, 3x3) -> BatchNormalization -> MaxPooling2D (2x2)`
  - `Flatten -> Dense (128, ReLU) -> Dropout (0.3) -> Dense (10, Softmax)`
- 📊 **Tampilan Probabilitas**: Menampilkan angka hasil prediksi beserta persentase confidence.
- 🧹 **Clear Canvas**: Tombol reset kanvas untuk menggambar angka berikutnya.

---

## 🚀 Cara Menjalankan

### 1. Install Dependensi

```bash
pip install -r requirements.txt
```

### 2. Latih Model (Jika belum ada model `.keras`)

Model dilatih pada dataset MNIST (akan otomatis diunduh pada percobaan pertama):

```bash
python train.py
```
Output: file `digit_model.keras`.

### 3. Jalankan Aplikasi GUI

```bash
python main.py
```

---

## 📁 Struktur Berkas

```
Digit Reconation/
├── main.py                    # Aplikasi GUI Tkinter + inference model
├── train.py                   # Script training CNN MNIST & export digit_model.keras
├── requirements.txt           # Daftar dependensi Python
├── Master_Memory_Workflow.md  # Catatan teknis & arsitektur
└── .gitignore                 # Mengabaikan model biner & cache
```
