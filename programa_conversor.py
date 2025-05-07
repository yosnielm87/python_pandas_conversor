import pandas as pd


def conv_a_pulgadas(cm):
    return cm / 2.54


# Leer el archivo excel....

df = pd.read_excel("muebles_medidas.xlsx")

# Añadir una columnas al dataframe que sea en pulgadas, y se llene haciendo el calculo de cm a pulgadas cm/2.54

df["Pulgadas"] = df["Centimetros:"].apply(conv_a_pulgadas)

df.to_excel("mueble_medidas_convertidas.xlsx", index=False)

print(
    "Conversion completada satisfactoriamente y se ha guardado en un nuevo fichero llamado: 'mueble_medidas_convertidas.xlsx'"
)
