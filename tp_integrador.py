import pandas as pd

# 1) Lectura y Exploración de Datos
excel_file = "movies.xls"

df_1900s = pd.read_excel(excel_file, sheet_name="1900s")
df_2000s = pd.read_excel(excel_file, sheet_name="2000s")
df_2010s = pd.read_excel(excel_file, sheet_name="2010s")

print("Primeras 5 filas de 2000s: \n", df_2000s.head(5))

print("\nCantidad de filas en 2010s:", len(df_2010s))


# 2) Unificación de Datos
df_movies = pd.concat([df_1900s, df_2000s, df_2010s], ignore_index=True)

primeras_10 = df_movies.head(10)
print("\nPrimeras 10 filas de df_movies: \n", primeras_10)


# 3) Análisis
# Películas por país
pelis_por_pais = df_movies["Country"].value_counts()
print("\nPelículas por país: \n", pelis_por_pais)

# Top 5 directores 2010s
top5_directores = df_2010s["Director"].value_counts().head(5)
print("\nTop 5 directores 2010s: \n", top5_directores)


# Ordenar por IMDB Score
top5_score = df_movies.sort_values(by="IMDB Score", ascending=False).head(5)
print("\nTop 5 películas por IMDB Score:")
print(top5_score[["Title", "IMDB Score"]])


# Agrupación
# Promedio IMDB por país
promedio_pais = df_movies.groupby("Country")["IMDB Score"].mean()
print("\nPromedio IMDB por país: \n", promedio_pais)

# Cantidad de películas por década
df_movies["Decade"] = (df_movies["Year"] // 10) * 10
pelis_por_decada = df_movies["Decade"].value_counts().sort_index()
print("\nPelículas por década: \n", pelis_por_decada)


# 5) Limpieza y Exportación
print("\nInformación general del DataFrame: \n", df_movies.info())

# Eliminar filas con valores vacíos en IMDB Score
df_limpio = df_movies.dropna(subset=["IMDB Score"])

# Exportar
df_limpio.to_excel("movies_limpio.xlsx", index=False)
print("\nArchivo movies_limpio.xlsx exportado correctamente.")
