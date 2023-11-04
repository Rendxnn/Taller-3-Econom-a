from matplotlib import pyplot as plt
import csv


# Análisis PIB

def analisis_PIB_anos():
    with open('PIB-Amazonas.csv', 'r') as archivo_pib:
        lineas_archivo = (archivo_pib.readlines())
        anos = lineas_archivo[10].split(',')[7:]
        pib_amazonas_anos = list(map(int, lineas_archivo[12].split(',')[7:]))

        pib_maximo = max(pib_amazonas_anos)
        ano_maximo_pib = anos[pib_amazonas_anos.index(pib_maximo)]
        print(f'El PIB maximo fue: {pib_maximo}')
        print(f'El año con el pib máximo fue: {ano_maximo_pib}')

        plt.bar(anos, pib_amazonas_anos)
        plt.title('PIB - Amazonas. Por años')
        plt.xlabel('Años')
        plt.ylabel('PIB (miles de millones de pesos)')
        plt.show()

        archivo_pib.close()


def analisis_tasa_crecimiento():
    with open('PIB-Amazonas.csv', 'r') as archivo_pib:
        lineas_archivo = (archivo_pib.readlines())
        anos = lineas_archivo[10].split(',')[6:]
        pib_amazonas_anos = list(map(int, lineas_archivo[12].split(',')[6:]))
        tasas_crecimiento = [0] * len(pib_amazonas_anos)
        for i in range(1, len(pib_amazonas_anos)):
            pib_actual = pib_amazonas_anos[i]
            pib_anterior = pib_amazonas_anos[i - 1]
            tasas_crecimiento[i] = (pib_actual - pib_anterior) / pib_anterior * 100

        max_crecimiento = max(tasas_crecimiento)
        min_crecimiento = min(tasas_crecimiento)

        max_ano_crecimiento = anos[tasas_crecimiento.index(max_crecimiento)]
        min_ano_crecimiento = anos[tasas_crecimiento.index(min_crecimiento)]

        print(f'El mayor crecimiento fue de {round(max_crecimiento, 2)} y fue en {max_ano_crecimiento}')
        print(f'El menor crecimiento fue de {round(min_crecimiento, 2)} y fue en {min_ano_crecimiento}')

        plt.title('Tasa de crecimiento PIB por año. Amazonas')
        plt.xlabel('Años')
        plt.ylabel('Tasa de crecimiento PIB')
        plt.plot(anos[1:], tasas_crecimiento[1:])
        plt.show()


def analisis_sectores():
    with open('actividad economica.csv', 'r') as archivo_sectores:
        lector = csv.reader(archivo_sectores)
        sectores = {}
        for linea in lector:
            if linea[0] == 'Producto Interno Bruto por departamento - Base 2015':
                sector = next(lector)[0].split('\n')[0]
            if linea[1] == 'Amazonas':
                valor_2010, valor_2022 = linea[7], linea[19]
                sectores[sector.strip()] = (int(valor_2010), int(valor_2022))
        lista_sectores_2010 = sorted(list(sectores.items()), key=lambda s: s[1][0])
        lista_sectores_2022 = sorted(list(sectores.items()), key=lambda s: s[1][1])

        print('----LISTA SECTORES 2010 AMAZONAS----')
        for sector, valores in lista_sectores_2010[:-1]: print(f'{sector}: {valores[0]}')
        print()
        print('----LISTA SECTORES 2022 AMAZONAS----')
        for sector, valores in lista_sectores_2022[:-1]: print(f'{sector}: {valores[1]}')


def analisis_poblacion():
    poblacion_total = 66056
    hombres = 34422
    mujeres = 31634

    plt.pie([hombres, mujeres], labels=['Masculino', 'Femenino'], autopct='%1.1f%%')
    plt.title('Distribución poblacional por sexo. Amazonas')
    plt.show()

    poblacion_edades = "7073 7705 8564 8521 5763 5091 4543 4040 3257 2844 2363 1979 1486 1109 660 592 256 210".split()
    edades = ['0 a 4', '5 a 9', '10 a 14', '15 a 19', '20 a 24', '25 a 29', '30 a 34', '35 a 39', '40 a 44', '45 a 49',
              '50 a 54', '55 a 59', '60 a 64', '65 a 69', '70 a 74', '75 a 79', '80 a 84', '85 y más']

    plt.bar(edades, list(map(int, poblacion_edades)))
    plt.title('Distribución poblacional por edades. Amazonas')
    plt.show()


def analisis_desempleo():
    anos = "2014-1	2014-2	2015-1 2015-2 2016-1	2016-2	2017-1	2017-2	2018-1	2018-2	2019-1	2019-2	2020-1	2020-2	2021-1	2021-2	2022-1 2022-2".split()
    poblacion_total = "380	382	385	389	392	396	400	404	409	416	424	431	438	443	447	450	453	456".split()
    poblacion_edad_trabajar = "270	273	276	279	283	286	290	294	300	306	312	319	324	329	332	336	339	341".split()
    desocupados = "19	16	19	17	24	22	27	26	28	28	32	30	38	43	40	34	37	35".split()
    tasas_desempleo = []
    for i in range(len(desocupados)):
        tasas_desempleo.append(round(int(desocupados[i]) / int(poblacion_edad_trabajar[i]) * 100, 2))
    plt.plot(anos, tasas_desempleo)
    plt.title('Tasas de desempleo Orinoquía, Amazonía e Insular')
    plt.xlabel('Años')
    plt.ylabel('Tasas de desempleo (%)')
    plt.show()


analisis_desempleo()
