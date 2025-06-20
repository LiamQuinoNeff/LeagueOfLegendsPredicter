# Importar librerías
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
import tkinter as tk
from customtkinter import CTk, CTkLabel, CTkEntry, CTkButton
import random
import os

# 1. Cargar el dataset
data = pd.read_csv('C:/Users/PC/Downloads/TF_Meza_Quino/data/data_normalizado_limpio.csv')

# 2. Definir las variables predictoras (X) y la variable objetivo (y)
X = data.drop(columns=['blueWins'])
y = data['blueWins']

# 3. Dividir el dataset en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Verificar si el modelo ya está guardado
model_path = 'neural_network_model.h5'
if not os.path.exists(model_path):
    # 4. Implementar la Red Neuronal Artificial (RNA)
    def build_neural_network():
        model = Sequential()
        model.add(Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
        model.add(Dense(32, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))  # Salida binaria
        model.compile(optimizer=Adam(learning_rate=0.001), loss='binary_crossentropy', metrics=['accuracy'])
        return model

    # Entrenar la RNA
    nn_model = build_neural_network()
    nn_model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=1)
    
    # Guardar el modelo RNA entrenado
    nn_model.save(model_path)
else:
    # Cargar el modelo RNA guardado
    nn_model = load_model(model_path)

# Evaluar la RNA
nn_loss, nn_accuracy = nn_model.evaluate(X_test, y_test)
print(f"RNA Accuracy: {nn_accuracy:.4f}")

#-----------------------------------------
# Interfaz de usuario con CustomTkinter

# Extraer los nombres de las características desde X
model_features = X.columns.tolist()

# Función para generar valores aleatorios para las características faltantes
def generate_random_values():
    # Definir los rangos de valores típicos para cada variable
    random_values = {
        "blueKills": random.randint(0, 10),
        "blueGoldDiff": random.randint(-2000, 2000),
        "blueTowersDestroyed": random.randint(0, 3),
        "blueDragons": random.randint(0, 2),
        "redKills": random.randint(0, 10),
        "redGoldDiff": random.randint(-2000, 2000)
    }
    return random_values

# Función para validar la entrada
def validar_entrada(valor):
    try:
        # Elimina espacios adicionales
        valor = valor.strip()
        # Intenta convertir el valor a un número
        float(valor)
        return True
    except ValueError:
        # Si ocurre un error, el valor no es numérico
        return False

# Función para hacer la predicción
def make_prediction():
    try:
        # Crear un diccionario para almacenar los valores ingresados o aleatorios
        features_dict = {feature: 0.0 for feature in model_features}

        # Rellenar features_dict con los valores del usuario para las características importantes
        for i, entry in enumerate(entries):
            value = entry.get().strip()
            feature_name = important_features[i]
            if validar_entrada(value):
                features_dict[feature_name] = float(value)
            else:
                random_value = generate_random_values().get(feature_name, 0.0)
                features_dict[feature_name] = random_value
                entry.delete(0, tk.END)
                entry.insert(0, str(random_value))

        # Convertir el diccionario a un DataFrame con el orden correcto de columnas
        input_features = pd.DataFrame([features_dict])[model_features]

        # Hacer la predicción con el modelo RNA
        prediction = nn_model.predict(input_features)[0][0]
        result_text = "Victoria" if prediction >= 0.5 else "Derrota"
        result_label.configure(text=f"Predicción: {result_text} del equipo azul")
    except ValueError as e:
        result_label.configure(text="Error: Asegúrese de ingresar valores numéricos.")
        print(f"Detalle del error: {e}")

# Configuración de la ventana principal
root = CTk()
root.title("Predicción de Victoria de League of Legends")
root.geometry("400x600")

# Mostrar el porcentaje de acierto del modelo RNA
accuracy_label = CTkLabel(root, text=f"RNA Accuracy: {nn_accuracy:.4f}", font=("Arial", 12))
accuracy_label.pack(pady=10)

# Etiquetas e entradas de datos para las variables más importantes
important_features = ["blueKills", "blueGoldDiff", "blueTowersDestroyed", "blueDragons", "redKills", "redGoldDiff"]
entries = []
for feature in important_features:
    label = CTkLabel(root, text=f"{feature}:")
    label.pack()
    entry = CTkEntry(root)
    entry.pack()
    entries.append(entry)

# Botón para hacer la predicción
predict_button = CTkButton(root, text="Predecir", command=make_prediction)
predict_button.pack(pady=20)

# Etiqueta para mostrar el resultado
result_label = CTkLabel(root, text="Predicción: ", font=("Arial", 16))
result_label.pack()

# Ejecutar la ventana principal
root.mainloop()
