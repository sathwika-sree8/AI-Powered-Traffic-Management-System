# Save this as create_dummy_model.py in backend/models
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

model = Sequential([
    Conv2D(8, (3, 3), activation='relu', input_shape=(299, 299, 3)),
    MaxPooling2D(2, 2),
    Flatten(),
    Dense(1, activation='sigmoid')
])
model.save("accident_detection_model.h5")
