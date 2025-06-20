# Importar librerías
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

# 1. Cargar el dataset
data = pd.read_csv('C:/Users/PC/Downloads/TF_Meza_Quino/data/data_normalizado_limpio.csv')

# 2. Definir las variables predictoras (X) y la variable objetivo (y)
X = data.drop(columns=['blueWins'])
y = data['blueWins']

# 3. Dividir el dataset en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Implementar los modelos

## 4.1 Red Neuronal Artificial (RNA)
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

# Evaluar la RNA
nn_loss, nn_accuracy = nn_model.evaluate(X_test, y_test)
print(f"RNA Accuracy: {nn_accuracy:.4f}")

## 4.2 Random Forest
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)
rf_predictions = rf_model.predict(X_test)

# Evaluar Random Forest
rf_accuracy = accuracy_score(y_test, rf_predictions)
print(f"Random Forest Accuracy: {rf_accuracy:.4f}")
print(confusion_matrix(y_test, rf_predictions))
print(classification_report(y_test, rf_predictions))

## 4.3 Support Vector Machine (SVM)
svm_model = SVC(kernel='linear', probability=True, random_state=42)
svm_model.fit(X_train, y_train)
svm_predictions = svm_model.predict(X_test)

# Evaluar SVM
svm_accuracy = accuracy_score(y_test, svm_predictions)
print(f"SVM Accuracy: {svm_accuracy:.4f}")
print(confusion_matrix(y_test, svm_predictions))
print(classification_report(y_test, svm_predictions))