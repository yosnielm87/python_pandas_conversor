import pandas as pd

# Dataframe es la info basica con el nombre de las piezas y centimetros para poder armar el Excel

data = {
    "Piezas:": ["Pata", "Tablero", "Puertas", "Estantes", "Gaveteros"],
    "Centimetros:": [40, 120, 60, 30, 180],
}


df = pd.DataFrame(data)

# Guardar el Dataframe en un archivo Excel

df.to_excel("muebles_medidas.xlsx", index=False)