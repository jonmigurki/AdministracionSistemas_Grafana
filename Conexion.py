from pytrends.request import TrendReq
from crate import client
import time


#time.sleep(15)


pytrend = TrendReq()



# +----------------------------------------------------------------------------+
# |       BÚSQUEDA 1: INTERÉS POR TIEMPO DE "CORONAVIRUS" EN GOOGLE            |
# +----------------------------------------------------------------------------+

pytrend.build_payload(kw_list=['coronavirus'])
interest_over_time_df = pytrend.interest_over_time()
tabla = interest_over_time_df

lista=[[],[],[],[],[],[],[],[],[],[],[],[]]

for index,row in tabla.iterrows():

    annio_actual = (str(index)[:4])
    if(annio_actual=='2020'):
        mes_actual = str(index)[5]+str(index)[6]
        if(int(mes_actual)<10):
            mes_actual = mes_actual[1:]

        lista[int(mes_actual)-1].append(row['coronavirus'])



connection = client.connect("localhost:4200")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS busquedas_mes_coronavirus")

cursor.execute("""CREATE TABLE busquedas_mes_coronavirus (mes VARCHAR(20), busquedas INT, PRIMARY KEY (mes))""")

sql = """INSERT INTO busquedas_mes_coronavirus(mes, busquedas) VALUES (?, ?)"""

meses = ["01 Enero", "02 Febrero", "03 Marzo", "04 Abril", "05 Mayo", "06 Junio", "07 Julio", "08 Agosto", "09 Septiembre", "10 Octubre", "11 Noviembre", "12 Diciembre"]

for x in range(0,len(lista)):
    lista[x] = sum(lista[x])/len(lista[x])

    datos=(str(meses[x]), lista[x])
    cursor.execute(sql, datos)


print("--> Búsqueda 1 realizada")



# +----------------------------------------------------------------------------+
# |           BÚSQUEDA 2: INTERÉS POR TIEMPO DE "COVID" EN GOOGLE              |
# +----------------------------------------------------------------------------+

pytrend.build_payload(kw_list=['covid'])
interest_over_time_df = pytrend.interest_over_time()
tabla = interest_over_time_df

lista=[[],[],[],[],[],[],[],[],[],[],[],[]]

for index,row in tabla.iterrows():

    annio_actual = (str(index)[:4])
    if(annio_actual=='2020'):
        mes_actual = str(index)[5]+str(index)[6]
        if(int(mes_actual)<10):
            mes_actual = mes_actual[1:]

        lista[int(mes_actual)-1].append(row['covid'])



connection = client.connect("localhost:4200")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS busquedas_mes_covid")

cursor.execute("""CREATE TABLE busquedas_mes_covid (mes VARCHAR(20), busquedas INT, PRIMARY KEY (mes))""")

sql = """INSERT INTO busquedas_mes_covid(mes, busquedas) VALUES (?, ?)"""

meses = ["01 Enero", "02 Febrero", "03 Marzo", "04 Abril", "05 Mayo", "06 Junio", "07 Julio", "08 Agosto", "09 Septiembre", "10 Octubre", "11 Noviembre", "12 Diciembre"]

for x in range(0,len(lista)):
    lista[x] = sum(lista[x])/len(lista[x])

    datos=(str(meses[x]), lista[x])
    cursor.execute(sql, datos)


print("--> Búsqueda 2 realizada")



# +----------------------------------------------------------------------------+
# |          BÚSQUEDA 3: INTERÉS POR TIEMPO DE "VACUNA" EN GOOGLE              |
# +----------------------------------------------------------------------------+

pytrend.build_payload(kw_list=['vacuna'])
interest_over_time_df = pytrend.interest_over_time()
tabla = interest_over_time_df

lista=[[],[],[],[],[],[],[],[],[],[],[],[]]

for index,row in tabla.iterrows():

    annio_actual = (str(index)[:4])
    if(annio_actual=='2020'):
        mes_actual = str(index)[5]+str(index)[6]
        if(int(mes_actual)<10):
            mes_actual = mes_actual[1:]

        lista[int(mes_actual)-1].append(row['vacuna'])



connection = client.connect("localhost:4200")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS busquedas_mes_vacuna")

cursor.execute("""CREATE TABLE busquedas_mes_vacuna (mes VARCHAR(20), busquedas INT, PRIMARY KEY (mes))""")

sql = """INSERT INTO busquedas_mes_vacuna(mes, busquedas) VALUES (?, ?)"""

meses = ["01 Enero", "02 Febrero", "03 Marzo", "04 Abril", "05 Mayo", "06 Junio", "07 Julio", "08 Agosto", "09 Septiembre", "10 Octubre", "11 Noviembre", "12 Diciembre"]

for x in range(0,len(lista)):
    lista[x] = sum(lista[x])/len(lista[x])

    datos=(str(meses[x]), lista[x])
    cursor.execute(sql, datos)


print("--> Búsqueda 3 realizada")



# +----------------------------------------------------------------------------+
# |          BÚSQUEDA 4: INTERÉS POR TIEMPO DE "VACCINE" EN GOOGLE             |
# +----------------------------------------------------------------------------+

pytrend.build_payload(kw_list=['vaccine'])
interest_over_time_df = pytrend.interest_over_time()
tabla = interest_over_time_df

lista=[[],[],[],[],[],[],[],[],[],[],[],[]]

for index,row in tabla.iterrows():

    annio_actual = (str(index)[:4])
    if(annio_actual=='2020'):
        mes_actual = str(index)[5]+str(index)[6]
        if(int(mes_actual)<10):
            mes_actual = mes_actual[1:]

        lista[int(mes_actual)-1].append(row['vaccine'])



connection = client.connect("localhost:4200")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS busquedas_mes_vaccine")

cursor.execute("""CREATE TABLE busquedas_mes_vaccine (mes VARCHAR(20), busquedas INT, PRIMARY KEY (mes))""")

sql = """INSERT INTO busquedas_mes_vaccine(mes, busquedas) VALUES (?, ?)"""

meses = ["01 Enero", "02 Febrero", "03 Marzo", "04 Abril", "05 Mayo", "06 Junio", "07 Julio", "08 Agosto", "09 Septiembre", "10 Octubre", "11 Noviembre", "12 Diciembre"]

for x in range(0,len(lista)):
    lista[x] = sum(lista[x])/len(lista[x])

    datos=(str(meses[x]), lista[x])
    cursor.execute(sql, datos)


print("--> Búsqueda 4 realizada")



# +----------------------------------------------------------------------------+
# |         BÚSQUEDA 5: INTERÉS POR TIEMPO DE "MASCARILLA" EN GOOGLE           |
# +----------------------------------------------------------------------------+

pytrend.build_payload(kw_list=['mascarilla'])
interest_over_time_df = pytrend.interest_over_time()
tabla = interest_over_time_df

lista=[[],[],[],[],[],[],[],[],[],[],[],[]]

for index,row in tabla.iterrows():

    annio_actual = (str(index)[:4])
    if(annio_actual=='2020'):
        mes_actual = str(index)[5]+str(index)[6]
        if(int(mes_actual)<10):
            mes_actual = mes_actual[1:]

        lista[int(mes_actual)-1].append(row['mascarilla'])



connection = client.connect("localhost:4200")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS busquedas_mes_mascarilla")

cursor.execute("""CREATE TABLE busquedas_mes_mascarilla (mes VARCHAR(20), busquedas INT, PRIMARY KEY (mes))""")

sql = """INSERT INTO busquedas_mes_mascarilla(mes, busquedas) VALUES (?, ?)"""

meses = ["01 Enero", "02 Febrero", "03 Marzo", "04 Abril", "05 Mayo", "06 Junio", "07 Julio", "08 Agosto", "09 Septiembre", "10 Octubre", "11 Noviembre", "12 Diciembre"]

for x in range(0,len(lista)):
    lista[x] = sum(lista[x])/len(lista[x])

    datos=(str(meses[x]), lista[x])
    cursor.execute(sql, datos)


print("--> Búsqueda 5 realizada")



# +----------------------------------------------------------------------------+
# |            BÚSQUEDA 6: INTERÉS POR TIEMPO DE "MASK" EN GOOGLE              |
# +----------------------------------------------------------------------------+

pytrend.build_payload(kw_list=['mask'])
interest_over_time_df = pytrend.interest_over_time()
tabla = interest_over_time_df

lista=[[],[],[],[],[],[],[],[],[],[],[],[]]

for index,row in tabla.iterrows():

    annio_actual = (str(index)[:4])
    if(annio_actual=='2020'):
        mes_actual = str(index)[5]+str(index)[6]
        if(int(mes_actual)<10):
            mes_actual = mes_actual[1:]

        lista[int(mes_actual)-1].append(row['mask'])



connection = client.connect("localhost:4200")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS busquedas_mes_mask")

cursor.execute("""CREATE TABLE busquedas_mes_mask (mes VARCHAR(20), busquedas INT, PRIMARY KEY (mes))""")

sql = """INSERT INTO busquedas_mes_mask(mes, busquedas) VALUES (?, ?)"""

meses = ["01 Enero", "02 Febrero", "03 Marzo", "04 Abril", "05 Mayo", "06 Junio", "07 Julio", "08 Agosto", "09 Septiembre", "10 Octubre", "11 Noviembre", "12 Diciembre"]

for x in range(0,len(lista)):
    lista[x] = sum(lista[x])/len(lista[x])

    datos=(str(meses[x]), lista[x])
    cursor.execute(sql, datos)


print("--> Búsqueda 6 realizada")



# +----------------------------------------------------------------------------+
# |        BÚSQUEDA 7: PALABRAS MÁS BUSCADAS EN ESPAÑA DURANTE 2020            |
# +----------------------------------------------------------------------------+

tabla = pytrend.top_charts(2020, hl='FGS', tz=300, geo='ES')
lista = []

for index,row in tabla.iterrows():

    lista.append(row['title'])


connection = client.connect("localhost:4200")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS top_busquedas_espana_2020")

cursor.execute("""CREATE TABLE top_busquedas_espana_2020 (top INT, busqueda VARCHAR(50), PRIMARY KEY (top))""")

sql = """INSERT INTO top_busquedas_espana_2020(top, busqueda) VALUES (?, ?)"""

for x in range(0,len(lista)):
    datos=(x+1, lista[x])
    cursor.execute(sql, datos)


print("--> Búsqueda 7 realizada")



# +----------------------------------------------------------------------------+
# |         BÚSQUEDA 8: PALABRAS MÁS BUSCADAS EN EEUU DURANTE 2020             |
# +----------------------------------------------------------------------------+

tabla = pytrend.top_charts(2020, hl='FGS', tz=300, geo='US')
lista = []

for index,row in tabla.iterrows():

    lista.append(row['title'])


connection = client.connect("localhost:4200")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS top_busquedas_eeuu_2020")

cursor.execute("""CREATE TABLE top_busquedas_eeuu_2020 (top INT, busqueda VARCHAR(50), PRIMARY KEY (top))""")

sql = """INSERT INTO top_busquedas_eeuu_2020(top, busqueda) VALUES (?, ?)"""

for x in range(0,len(lista)):
    datos=(x+1, lista[x])
    cursor.execute(sql, datos)


print("--> Búsqueda 8 realizada")


# +----------------------------------------------------------------------------+
# |        BÚSQUEDA 9: PALABRAS MÁS BUSCADAS EN ITALIA DURANTE 2020            |
# +----------------------------------------------------------------------------+

tabla = pytrend.top_charts(2020, hl='FGS', tz=300, geo='IT')
lista = []

for index,row in tabla.iterrows():

    lista.append(row['title'])


connection = client.connect("localhost:4200")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS top_busquedas_italia_2020")

cursor.execute("""CREATE TABLE top_busquedas_italia_2020 (top INT, busqueda VARCHAR(50), PRIMARY KEY (top))""")

sql = """INSERT INTO top_busquedas_italia_2020(top, busqueda) VALUES (?, ?)"""

for x in range(0,len(lista)):
    datos=(x+1, lista[x])
    cursor.execute(sql, datos)


print("--> Búsqueda 9 realizada")




# +----------------------------------------------------------------------------+
# |         BÚSQUEDA 10: COMPARATIVA DE INTERÉS POR SEMANA DE "COVID"          |
# |                    Y "CORONAVIRUS" EN ESTADOS UNIDOS                       |
# +----------------------------------------------------------------------------+

list = ['Coronavirus', 'Covid']
pytrends = TrendReq(hl='en-US', tz=360)
pytrends.build_payload(list, cat=0, timeframe='today 12-m', geo='US')
df = pytrends.interest_over_time()
df = df.drop('isPartial', axis = 1)

semanas = []
coronavirus = []
covid = []

for index,row in df.iterrows():

    semanas.append(str(index)[0:10])
    coronavirus.append(str(row['Coronavirus']))
    covid.append(str(row['Covid']))


connection = client.connect("localhost:4200")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS coronavirus_vs_covid_eeuu")

cursor.execute("""CREATE TABLE coronavirus_vs_covid_eeuu (fecha VARCHAR(20), coronavirus INT, covid INT, PRIMARY KEY (fecha))""")

sql = """INSERT INTO coronavirus_vs_covid_eeuu(fecha, coronavirus, covid) VALUES (?, ?, ?)"""

for x in range(0,len(semanas)):
    datos=(semanas[x], coronavirus[x], covid[x])
    cursor.execute(sql, datos)


print("--> Búsqueda 10 realizada")



# +----------------------------------------------------------------------------+
# |         BÚSQUEDA 11: COMPARATIVA DE INTERÉS POR SEMANA DE "COVID"          |
# |                        Y "CORONAVIRUS" EN ESPAÑA                           |
# +----------------------------------------------------------------------------+

list = ['Coronavirus', 'Covid']
pytrends = TrendReq(hl='ES', tz=360)
pytrends.build_payload(list, cat=0, timeframe='today 12-m', geo='ES')
df = pytrends.interest_over_time()
df = df.drop('isPartial', axis = 1)

semanas = []
coronavirus = []
covid = []

for index,row in df.iterrows():

    semanas.append(str(index)[0:10])
    coronavirus.append(str(row['Coronavirus']))
    covid.append(str(row['Covid']))


connection = client.connect("localhost:4200")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS coronavirus_vs_covid_espana")

cursor.execute("""CREATE TABLE coronavirus_vs_covid_espana (fecha VARCHAR(20), coronavirus INT, covid INT, PRIMARY KEY (fecha))""")

sql = """INSERT INTO coronavirus_vs_covid_espana(fecha, coronavirus, covid) VALUES (?, ?, ?)"""

for x in range(0,len(semanas)):
    datos=(semanas[x], coronavirus[x], covid[x])
    cursor.execute(sql, datos)


print("--> Búsqueda 11 realizada")



# +----------------------------------------------------------------------------+
# |           BÚSQUEDA 12: BÚSQUEDA DE "CONFINAMIENTO" EN ESPAÑA               |
# +----------------------------------------------------------------------------+

lista = ['confinamiento', 'confinamientos']
pytrends = TrendReq(hl='ES', tz=360)
pytrends.build_payload(lista, cat=0, timeframe='today 12-m', geo='ES')
df = pytrends.interest_over_time()
df = df.drop('isPartial', axis = 1)

semanas = []
confinamiento = []

for index,row in df.iterrows():

    semanas.append(str(index)[0:10])
    confinamiento.append(str(row['confinamiento']))


connection = client.connect("localhost:4200")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS busqueda_confinamiento_espana")

cursor.execute("""CREATE TABLE busqueda_confinamiento_espana (fecha VARCHAR(20), confinamiento INT, PRIMARY KEY (fecha))""")

sql = """INSERT INTO busqueda_confinamiento_espana(fecha, confinamiento) VALUES (?, ?)"""

for x in range(0,len(semanas)):
    datos=(semanas[x], confinamiento[x])
    cursor.execute(sql, datos)


print("--> Búsqueda 12 realizada")



# +----------------------------------------------------------------------------+
# |          BÚSQUEDA 13: BÚSQUEDA DE "TOQUE DE QUEDA" EN ESPAÑA               |
# +----------------------------------------------------------------------------+

lista = ['toque de queda', 'toques de queda']
pytrends = TrendReq(hl='ES', tz=360)
pytrends.build_payload(lista, cat=0, timeframe='today 12-m', geo='ES')
df = pytrends.interest_over_time()
df = df.drop('isPartial', axis = 1)

semanas = []
toquequeda = []

for index,row in df.iterrows():

    semanas.append(str(index)[0:10])
    toquequeda.append(str(row['toque de queda']))


connection = client.connect("localhost:4200")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS busqueda_toque_queda_espana")

cursor.execute("""CREATE TABLE busqueda_toque_queda_espana (fecha VARCHAR(20), toquequeda INT, PRIMARY KEY (fecha))""")

sql = """INSERT INTO busqueda_toque_queda_espana(fecha, toquequeda) VALUES (?, ?)"""

for x in range(0,len(semanas)):
    datos=(semanas[x], toquequeda[x])
    cursor.execute(sql, datos)


print("--> Búsqueda 13 realizada")



# +----------------------------------------------------------------------------+
# |              BÚSQUEDA 14: BÚSQUEDA DE "ERTE" EN ESPAÑA                     |
# +----------------------------------------------------------------------------+

lista = ['ERTE', 'ERTES']
pytrends = TrendReq(hl='ES', tz=360)
pytrends.build_payload(lista, cat=0, timeframe='today 12-m', geo='ES')
df = pytrends.interest_over_time()
df = df.drop('isPartial', axis = 1)

semanas = []
erte = []

for index,row in df.iterrows():

    semanas.append(str(index)[0:10])
    erte.append(str(row['ERTE']))


connection = client.connect("localhost:4200")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS busqueda_erte_espana")

cursor.execute("""CREATE TABLE busqueda_erte_espana (fecha VARCHAR(20), erte INT, PRIMARY KEY (fecha))""")

sql = """INSERT INTO busqueda_erte_espana(fecha, erte) VALUES (?, ?)"""

for x in range(0,len(semanas)):
    datos=(semanas[x], erte[x])
    cursor.execute(sql, datos)


print("--> Búsqueda 14 realizada")



# +----------------------------------------------------------------------------+
# |           BÚSQUEDA 15: BÚSQUEDA DE "SINTOMAS" EN ESPAÑA                    |
# +----------------------------------------------------------------------------+

lista = ['sintomas', 'sint']
pytrends = TrendReq(hl='ES', tz=360)
pytrends.build_payload(lista, cat=0, timeframe='today 12-m', geo='ES')
df = pytrends.interest_over_time()
df = df.drop('isPartial', axis = 1)

semanas = []
sintomas = []

for index,row in df.iterrows():

    semanas.append(str(index)[0:10])
    sintomas.append(str(row['sintomas']))


connection = client.connect("localhost:4200")

cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS busqueda_sintomas_espana")

cursor.execute("""CREATE TABLE busqueda_sintomas_espana (fecha VARCHAR(20), sintomas INT, PRIMARY KEY (fecha))""")

sql = """INSERT INTO busqueda_sintomas_espana(fecha, sintomas) VALUES (?, ?)"""

for x in range(0,len(semanas)):
    datos=(semanas[x], sintomas[x])
    cursor.execute(sql, datos)


print("--> Búsqueda 15 realizada")