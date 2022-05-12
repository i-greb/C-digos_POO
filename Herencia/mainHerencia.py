from herencia import*

def main():

    print("Distancia Recorrida")
    resultadoss = movimientoRectilieoUniforme(40,62)
    print(resultadoss.getDistanciaRecorrida())

    print("Aceleración y Distancia Recorrida ")
    resultados2= movimientoRectilineoUniformementeVariado(40,62,96)
    print(resultados2.getAceleracion())

    resultados3 = movimientoRectilineoUniformementeVariado(40,62,96)
    print(resultados3.getDistanciaRecorrida())



if __name__ == "__main__":
    main()



