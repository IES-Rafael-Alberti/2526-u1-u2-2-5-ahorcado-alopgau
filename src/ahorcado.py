import requests
def procesarronda(palabra:str, letras_introducidas:list, guiones:list, fallos:int) -> None:
    """Se encarga de coordinar todos los procesos necesarios para jugar una ronda en específico.

    Args:
        palabra (str): La palabra establecida para la ronda
        letras_introducidas (list): Lista de letras introducidas
        guiones (list): Lista con guiones para representar las letras restantes
        fallos (int): Contador de fallos de la ronda

    Returns:
        None

    """
    while fallos < 6 and "-" in guiones:
        letra = procesarletra(letras_introducidas)
        limpiarpantalla()
        letras_introducidas.append(letra.upper())
        fallos, intentoValido = comprobarintento(palabra, letra, fallos)
        dibujarahorcado(fallos)
        if intentoValido:
            guiones = anadirletra(letra, palabra,guiones)
        else:
            print("\nLa letra", letra, "no se encuentra en la palabra")
        print("Fallos: " + str(fallos) + "/6")
        print("".join(guiones))
        print("Letras introducidas: ", letras_introducidas)
    if fallos < 6:
        print("Ganaste! La palabra era " + palabra)
        preguntacontinuar()
    else:
        print("Has perdido... La palabra era " + palabra)
        preguntacontinuar()
def procesarjuego() -> None:
        """Se encarga de coordinar todos los procesos necesarios para jugar, asi como de los preparativos.

        Returns:
            None

        """
        print("=" * 50)
        print("AHORCADO".center(50, "-"))
        print("=" * 50)
        fallos = 0
        palabra_ronda = elegirpalabra()
        letras_introducidas = []
        guiones = list("-" * len(palabra_ronda))
        procesarronda(palabra_ronda,letras_introducidas,guiones, fallos)

def comprobarintento(palabra:str, letra:str, fallos:int) -> tuple[int, bool]:
    """Comprueba si el intento es fallido o no
    Args:
        palabra (str): La palabra establecida para la ronda
        letra (str): La letra introducida previamente por el usuario
        fallos (int): Contador de fallos de la ronda
    Returns:
        tuple:
            - int: Número de fallos
            - bool: Si el intento es fallido (False) o no (True)
    """
    if letra not in palabra:
        fallos += 1
        return fallos, False
    else:
        return fallos, True



def anadirletra(letra: str, palabra:str, guiones:list) -> list:
    """Se encarga de añadir la letra introducida por el usuario a la palabra, todas las veces que dicha letra aparezca en la misma

    Args:
        letra (str): La letra introducida por el usuario
        palabra (str): La palabra establecida para la ronda
        guiones (list): Lista con guiones para representar las letras restantes

    Returns:
        list: La lista de guiones actualizada, sustituyendo los correspondientes por la letra escogida
    """
    for i in range(len(palabra)):
        if palabra[i].upper() == letra.upper():
            guiones[i] = palabra[i]
    return guiones
def preguntacontinuar() -> None:
    """
    Pregunta al usuario si quiere jugar otra ronda sin detener la ejecución. En caso de que no, termina la misma

    Returns:
        None

    """
    continuar = None
    while continuar != "S" and continuar != "N":
        continuar = input("¿Quieres seguir jugando? (S/N)\n")
        if continuar.upper() == "S":
            procesarjuego()
        elif continuar.upper() == "N":
            print("Gracias por jugar!")




def procesarletra(letras_introducidas:list) -> str:
    """Comprueba si la letra introducida por el usuario no ha sido introducida ya o no es una letra, para asi procesarla o no
    Args:
        letras_introducidas (list): Lista de letras introducidas
    Returns:
        str: La letra introducida por el usuario
    """
    letra = ""
    letraValida = False
    while not letra.isalpha() or not letraValida or not len(letra) == 1:

            letra = input("Ingresa una letra: ")
            if letra not in letras_introducidas and len(letra) == 1 and letra.isalpha():
                return letra
            else:
                print("La letra", letra, "ya ha sido introducida, o no es una letra sino varias, o es un número")
                letraValida = False


def elegirpalabra() -> str:
    """Escoge una palabra aleatoria de la RandomWordAPI para la ronda
    Returns:
            palabra_ronda (str): La palabra escogida para la ronda
    """
    url = "https://random-word-api.herokuapp.com/word?lang=es&number=1"
    palabra_ronda = requests.get(url)

    return palabra_ronda.json()[0]

def dibujarahorcado(fallos:int) -> None:
    """Coordina funciones para dibujar el ahorcado por partes, según el número de fallos
    Args:
     fallos (int): Contador de fallos de la ronda
     Returns:
         None
    """
    if fallos == 1:
        dibujarcabeza()
    if fallos == 2:
        dibujarcabeza()
        dibujarcuerpoybrazos(fallos)
    if 2 < fallos < 5:
        dibujarcabeza()
        dibujarcuerpoybrazos(fallos)
        dibujarpiernas(fallos)
    if fallos >= 5:
        dibujarcabeza()
        dibujarcuerpoybrazos(fallos)
        dibujarpiernas(fallos)

def dibujarcabeza() -> None:
    """Dibuja la cabeza del ahorcado
    Returns:
        None
    """
    for i in range(0, 3):
        print(("#" * 6).center(60))
def dibujarcuerpoybrazos(fallos:int) -> None:
    """Dibuja el cuerpo del ahorcado (y también sus brazos, dependiendo de los fallos)
    Returns:
        None
    """
    for i in range(0, 3):
        if i == 1 and fallos == 5:
            print("----|    |".center(55))
        if i == 1 and fallos == 6:
            print("----|    |----".center(60))
        else:
            print("|    |".center(60))
    print("\\____/".center(60))

def dibujarpiernas(fallos:int) -> None:
    """ Coordina funciones para dibujar las piernas una por una
    Args:
        fallos (int): Contador de fallos de la ronda
    Returns:
        None
    """
    for i in range(0, 3):
        if fallos == 3:
            dibujarpiernaizquierda()
        elif fallos >= 4:
            print("|    |".center(60))

def dibujarpiernaizquierda() -> None:
    """Dibuja la pierna izquierda del ahorcado
    Returns:
        None
    """
    print("|".center(55))
def limpiarpantalla() -> None:
    """Limpia la información de consola
    Returns:
        None
    """
    print("\n" * 50)

def main():
    procesarjuego()

if __name__ == "__main__":
    main()