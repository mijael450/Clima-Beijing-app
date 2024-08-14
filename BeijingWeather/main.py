import requests
import csv
import os
from datetime import datetime, timezone
import pandas as pd
import matplotlib.pyplot as plt

api_key = "8000de0e0248108140e1bde34fbb45e1"
latitud = "39.907501"
longitud = "116.397232"
base_url = "https://api.openweathermap.org/data/2.5/weather?"
complete_url = f"{base_url}lat={latitud}&lon={longitud}&appid={api_key}&units=metric"
print(complete_url)
response = requests.get(complete_url)

data = response.json()

if response.status_code == 200:
   
    dt = datetime.fromtimestamp(data["dt"], tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S')

    datos = {
        "fecha y hora del reporte (UTC)": dt,
        "longitud": data["coord"]["lon"],
        "latitud": data["coord"]["lat"],
        "estado del cielo": data["weather"][0]["main"],
        "descripción del cielo": data["weather"][0]["description"],
        "temperatura actual (°C)": data["main"]["temp"],
        "temperatura mínima (°C)": data["main"]["temp_min"],
        "temperatura máxima (°C)": data["main"]["temp_max"],
        "presión (hPa)": data["main"]["pressure"],
        "humedad (%)": data["main"]["humidity"],
        "visibilidad (m)": data.get("visibility", "N/A"),  
        "velocidad del viento (m/s)": data["wind"]["speed"],
        "dirección del viento (°)": data["wind"]["deg"],
        "nubes (%)": data["clouds"]["all"],
        "hora del amanecer (UNIX)": data["sys"]["sunrise"],
        "hora del atardecer (UNIX)": data["sys"]["sunset"],
        "zona horaria": data["timezone"],
        "nombre de la ciudad": data["name"],
        "id de la ciudad": data["id"],
    }

   
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

    archivo_existe = os.path.exists("clima-Beijing-hoy.csv")

    with open("clima-Beijing-hoy.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not archivo_existe or os.stat("clima-Beijing-hoy.csv").st_size == 0:
            writer.writerow(datos.keys())
        writer.writerow(datos.values())
    

else:
    print(f"Error: {data['message']}")
