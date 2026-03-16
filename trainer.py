import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split

# Sample model training functionality

def train_model(data, labels, model_path='model.h5'):
    # Split data into training and validation sets
    X_train, X_val, y_train, y_val = train_test_split(data, labels, test_size=0.2, random_state=42)

    # Create a simple neural network model
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
        tf.keras.layers.Dropout(0.2),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])

    # Compile the model
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    # Train the model
    model.fit(X_train, y_train, validation_data=(X_val, y_val), epochs=10, batch_size=32)

    # Save the model
    model.save(model_path)
    print(f'Model trained and saved to {model_path}')

# Example usage:
# data = np.random.rand(1000, 10)  # Example data
# labels = np.random.randint(0, 2, size=(1000,))  # Example labels
# train_model(data, labels)