"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import re
import pandas as pd
from datetime import datetime


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";", index_col = 0)
    df.dropna(axis = 0, inplace = True)
    

    df['monto_del_credito'] = df['monto_del_credito'].str.replace("\$[\s*]|,|\.00", "", regex= True)
    df = df.astype({ "monto_del_credito": int, "comuna_ciudadano": float})

    df[["sexo", "tipo_de_emprendimiento","idea_negocio","barrio","línea_credito"]]=df[["sexo", "tipo_de_emprendimiento","idea_negocio","barrio","línea_credito"]].apply(lambda x: x.astype(str).str.lower())
    for i in ['tipo_de_emprendimiento', 'idea_negocio', 'línea_credito', 'barrio']:
        df[i] = df[i].apply(lambda x: x.translate(x.maketrans("-_","  ")))

    df['fecha_de_beneficio'] = df['fecha_de_beneficio'].apply(lambda x: datetime.strptime(x, "%Y/%m/%d") if (len(re.findall("^\d+/", x)[0]) - 1) == 4 else datetime.strptime(x, "%d/%m/%Y"))
    df.drop_duplicates(inplace = True)
    return df
