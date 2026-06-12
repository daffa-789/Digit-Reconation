import tensorflow as tf
from tensorflow.keras import layers, models

# 1. Load dataset MNIST
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocessing: Ubah skala pixel ke 0-1 dan sesuaikan dimensi
x_train = x_train.reshape(-1, 28, 28, 1).astype('float32') / 255.0
x_test = x_test.reshape(-1, 28, 28, 1).astype('float32') / 255.0

# 2. Arsitektur Model CNN yang Lebih Stabil
model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.BatchNormalization(),
    layers.MaxPooling2D((2, 2)),
    
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.BatchNormalization(),
    layers.MaxPooling2D((2, 2)),
    
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.3), # Mencegah model terlalu overthinking
    layers.Dense(10, activation='softmax')
])

# 3. Compile Model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 4. Training Model (5 Epochs sudah sangat optimal)
print("=== Memulai Proses Training Model Cerdas ===")
model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))

# 5. Simpan Model
model.save('digit_model.keras')
print("\n[SUKSES] Model berhasil disimpan dengan nama 'digit_model.keras'")