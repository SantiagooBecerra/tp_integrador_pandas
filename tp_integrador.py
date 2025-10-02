import pandas as pd

# 1) LECTURA Y EXPLORACIÓN
excel_file = "movies.xls"

df_1900s = pd.read_excel(excel_file, sheet_name="1900s")
df_2000s = pd.read_excel(excel_file, sheet_name="2000s")
df_2010s = pd.read_excel(excel_file, sheet_name="2010s")

print("Primeras 5 filas de 2000s:")
print(df_2000s.head())

print("\nCantidad de filas en 2010s:", len(df_2010s))


# 2) UNIFICACIÓN
df_movies = pd.concat([df_1900s, df_2000s, df_2010s], ignore_index=True)

primeras_10 = df_movies.head(10)
print("\nPrimeras 10 filas de df_movies:")
print(primeras_10)


# 3) ANÁLISIS
# Películas por país
pelis_por_pais = df_movies["Country"].value_counts()
print("\nPelículas por país:")
print(pelis_por_pais)

# Top 5 directores 2010s
top5_directores = df_2010s["Director"].value_counts().head(5)
print("\nTop 5 directores 2010s:")
print(top5_directores)

# Ordenar por IMDB Score
top5_score = df_movies.sort_values(by="IMDB Score", ascending=False).head(5)
print("\nTop 5 películas por IMDB Score:")
print(top5_score[["Title", "IMDB Score"]])


# 4) AGRUPACIÓN
# Promedio IMDB por país
promedio_pais = df_movies.groupby("Country")["IMDB Score"].mean()
print("\nPromedio IMDB por país:")
print(promedio_pais)

# Cantidad de películas por década
df_movies["Decade"] = (df_movies["Year"] // 10) * 10
pelis_por_decada = df_movies["Decade"].value_counts().sort_index()
print("\nPelículas por década:")
print(pelis_por_decada)


# 5) LIMPIEZA Y EXPORTACIÓN
print("\nInformación general del DataFrame:")
print(df_movies.info())

# Eliminar filas con valores vacíos en IMDB Score
df_limpio = df_movies.dropna(subset=["IMDB Score"])

# Exportar
df_limpio.to_excel("movies_limpio.xlsx", index=False)
print("\nArchivo movies_limpio.xlsx exportado correctamente.")
