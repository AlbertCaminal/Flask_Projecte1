def buildCountryList():
    file = open("./assets/world-data-2023-CLEAN.csv", "r", encoding="utf-8")
    dataset = file.read()
    file.close()

    filas = dataset.split("\n")
    encabezado, *registros = filas
    columnas = encabezado.split(",")

    paises = []
    for registro in registros:
        infoPais = registro.split(",")
        pais = {}
        for columna,dato in zip (columnas, infoPais):
            pais[columna] = dato
        paises.append(pais)
    return paises

def getCountryData(country):
    paises = buildCountryList()
    for pais in paises:
        if (pais["Country"] == country):
            return pais



def getCountryNames(): 
    paises = buildCountryList()
    nombresPaises = []
    for pais in paises:
        nombresPaises.append(pais["Country"])
    return nombresPaises

def parseValue(value_str):
    if not value_str or value_str.strip() == '':
        return 0
    try:
        # Eliminar $, espacios, comas y otros caracteres
        cleaned = value_str.replace('$', '').replace(',', '').replace(' ', '').replace('%', '')
        return float(cleaned)
    except:
        return 0

def filterCountriesByVariable(variable, min_value, max_value):
    paises = buildCountryList()
    paisesFiltrados = []
    
    # Mapeo de variables a columnas del CSV
    columnas = {
        'GDP': 'GDP',
        'Population': 'Population',
        'Life expectancy': 'Life expectancy',
        'Land Area(Km2)': 'Land Area(Km2)'
    }
    
    columna = columnas.get(variable)
    if not columna:
        return []
    
    for pais in paises:
        valor_str = pais.get(columna, '0')
        valor = parseValue(valor_str)
        
        if valor >= min_value and valor <= max_value:
            paisesFiltrados.append(pais["Country"])
    
    return paisesFiltrados

