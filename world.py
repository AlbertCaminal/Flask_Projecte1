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

