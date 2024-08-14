import pandas as pd
import matplotlib.pyplot as plt

file_path = '/home/mijael/CityWeather/Proyecto-final/clima-Beijing-hoy.csv'

df = pd.read_csv(file_path)

sample_df = df.sample(n=10)
print("Muestra aleatoria de 10 datos:")
print(sample_df)

df['fecha y hora del reporte (UTC)'] = pd.to_datetime(df['fecha y hora del reporte (UTC)'])

# Graficar temperatura vs. tiempo
#plt.figure(figsize=(12, 6))
#plt.plot(df['fecha y hora del reporte (UTC)'], df['temperatura actual (°C)'], marker='o', linestyle='-')
#plt.title('Temperatura Actual vs. Tiempo')
#plt.xlabel('Fecha y Hora del Reporte (UTC)')
#plt.ylabel('Temperatura Actual (°C)')
#plt.xticks(rotation=45)
#plt.tight_layout()

"""plt.figure(figsize=(12, 6))
plt.plot(df['fecha y hora del reporte (UTC)'], df['humedad (%)'], marker='o', linestyle='-', color='b')
plt.title('Humedad vs. Tiempo')
plt.xlabel('Fecha y Hora del Reporte (UTC)')
plt.ylabel('Humedad (%)')
plt.xticks(rotation=45)
plt.tight_layout()"""

plt.figure(figsize=(12, 6))
plt.plot(df['fecha y hora del reporte (UTC)'], df['velocidad del viento (m/s)'], marker='o', linestyle='-', color='r')
plt.title('Velocidad del Viento vs. Tiempo')
plt.xlabel('Fecha y Hora del Reporte (UTC)')
plt.ylabel('Velocidad del Viento (m/s)')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig('wind_speed_vs_time.png')

plt.show()
