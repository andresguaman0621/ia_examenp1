# Regresión Lineal Simple para Predicción de Ventas

# Importar las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importar el dataset
dataset = pd.read_csv('data_1.csv')
X = dataset.iloc[:, :-1].values  # Variable independiente (Advertising_Spend)
y = dataset.iloc[:, -1].values   # Variable dependiente (Sales)

# Dividir el dataset en conjunto de entrenamiento y conjunto de prueba
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=0)

# Entrenar el modelo de Regresión Lineal Simple con el conjunto de entrenamiento
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Predecir los resultados del conjunto de prueba
y_pred = regressor.predict(X_test)

# Calcular métricas de evaluación
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f'Coeficiente: {regressor.coef_[0]:.4f}')
print(f'Término independiente: {regressor.intercept_:.4f}')
print(f'Ecuación del modelo: Sales = {regressor.coef_[0]:.4f} * Advertising_Spend + {regressor.intercept_:.4f}')
print(f'R²: {r2:.4f}')
print(f'Error Absoluto Medio (MAE): {mae:.4f}')
print(f'Error Cuadrático Medio (RMSE): {rmse:.4f}')

# Visualizar los resultados del conjunto de entrenamiento
plt.figure(figsize=(10, 6))
plt.scatter(X_train, y_train, color='red', label='Datos reales (entrenamiento)')
plt.plot(X_train, regressor.predict(X_train), color='blue', label='Línea de regresión')
plt.title('Ventas vs Gasto en Publicidad (Conjunto de Entrenamiento)')
plt.xlabel('Gasto en Publicidad ($)')
plt.ylabel('Ventas ($)')
plt.legend()
plt.grid(True)
plt.show()

# Visualizar los resultados del conjunto de prueba
plt.figure(figsize=(10, 6))
plt.scatter(X_test, y_test, color='red', label='Datos reales (prueba)')
plt.plot(X_train, regressor.predict(X_train), color='blue', label='Línea de regresión')
plt.title('Ventas vs Gasto en Publicidad (Conjunto de Prueba)')
plt.xlabel('Gasto en Publicidad ($)')
plt.ylabel('Ventas ($)')
plt.legend()
plt.grid(True)
plt.show()

# Análisis adicional: Visualizar residuos
residuos = y_test - y_pred
plt.figure(figsize=(10, 6))
plt.scatter(X_test, residuos, color='green')
plt.axhline(y=0, color='red', linestyle='-')
plt.title('Residuos vs Gasto en Publicidad')
plt.xlabel('Gasto en Publicidad ($)')
plt.ylabel('Residuos')
plt.grid(True)
plt.show()

# Crear histograma de residuos
plt.figure(figsize=(10, 6))
plt.hist(residuos, bins=15, color='skyblue', edgecolor='black')
plt.axvline(x=0, color='red', linestyle='-')
plt.title('Distribución de Residuos')
plt.xlabel('Residuos')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.show()

# Realizar predicciones para diferentes niveles de gasto en publicidad
gasto_publicidad = np.array([1000, 2000, 3000, 4000, 5000]).reshape(-1, 1)
predicciones = regressor.predict(gasto_publicidad)
for i, gasto in enumerate(gasto_publicidad):
    print(f'Gasto en publicidad: ${gasto[0]:.2f} → Ventas estimadas: ${predicciones[i]:.2f}')
