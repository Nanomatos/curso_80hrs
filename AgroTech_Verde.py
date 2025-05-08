import pandas as pd
import numpy as np

np.random.seed(42)
n = 1000

data = {
    'tipo_de_cultivo': np.random.choice(['maiz', 'trigo', 'arroz', 'soja', 'naranjas','uva','lentejas', 'zanahoria'], n),
    'tipo_de_suelo': np.random.choice(["arcilloso", "arenoso", "limoso", "rocoso"], n),
    'ph': np.round(np.random.uniform(5.8, 6.8, n), 2),
    'humedad': np.round(np.random.uniform(0, 100, n), 2),
    'temperatura': np.round(np.random.uniform(0, 40, n)),
    'precipitacion': np.round(np.random.uniform(0, 300, n), 2),
    'horas_de_sol': np.round(np.random.uniform(0, 16, n), 1),
    'temporada': np.random.choice(['verano', 'otoño', 'invierno','primavera'], n),
    
}

df = pd.DataFrame(data)
print(df.head())

df.to_csv('agrotech_data.csv', index=False)
#comentario: Genera un dataset ficticio para el proyecto AgroTech Verde, con 1000 filas y 8 columnas.