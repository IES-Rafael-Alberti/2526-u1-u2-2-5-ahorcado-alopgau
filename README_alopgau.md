# AHORCADO - Juego de adivinanza de palabras

> Juego del **ahorcado** que utiliza una **API de palabras aleatorias** para seleccionar términos en español.

> **Interfaz visual con dibujo progresivo del ahorcado según los fallos**

---

## Índice

1. [Descripción del módulo](#1-descripción-del-módulo)
2. [Requisitos](#2-requisitos)
3. [Instalación](#3-instalación-de-python-y-dependencias)
   - 3.1 [Instalación de Python](#31-instalación-de-python)
   - 3.2 [Instalación de dependencias](#32-instalación-de-dependencias)
   - 3.3 [Entorno virtual](#33-entorno-virtual-opcional-recomendado)
4. [Ejecución](#4-ejecución-del-juego)
   - 4.1 [Sintaxis general](#sintaxis-general)
   - 4.2 [Ejemplos de ejecución](#ejemplos-de-ejecución)
5. [Funcionalidades](#5-funcionalidades)
   - 5.1 [Obtención de palabras](#obtención-de-palabras)
   - 5.2 [Validación de entrada](#validación-de-entrada)
   - 5.3 [Interfaz visual](#interfaz-visual)
   - 5.4 [Gestión del juego](#gestión-del-juego)
6. [Estructura del código](#6-estructura-del-código)
   - 6.1 [Funciones principales](#funciones-principales)
   - 6.2 [Funciones de dibujo](#funciones-de-dibujo)
   - 6.3 [Utilidades](#utilidades)
7. [Mensajes y errores](#7-mensajes-y-errores)
8. [Problemas frecuentes](#8-problemas-frecuentes-faq)
9. [API utilizada](#9-api-utilizada)
10. [Evidencias de depuración](#10-evidencias-de-depuración)  
## 1) Descripción del módulo

Este proyecto implementa el **juego clásico del ahorcado** donde el jugador debe adivinar una palabra letra por letra.

- La **palabra objetivo** se obtiene automáticamente desde una API externa de palabras aleatorias en español.
- El programa **valida las entradas** del usuario y controla el progreso del juego.
- Se muestra un **dibujo progresivo del ahorcado** según la cantidad de errores cometidos.

El juego sigue estas reglas:
- Máximo **6 fallos** permitidos
- Se muestran las **letras ya intentadas**
- La palabra se representa con guiones que se revelan progresivamente
- Al final de cada partida, se pregunta si se desea continuar jugando

---

## 2) Requisitos

- **Python 3.6 o superior**.
- **Dependencia externa**: `requests` (para conexión con la API).
- **Sistema operativo**: Windows, Linux o macOS.
- **Conexión a Internet** (para obtener palabras de la API).

---

## 3) Instalación de Python y dependencias

### 3.1 Instalación de Python

#### Linux

```bash
# Debian/Ubuntu
sudo apt update
sudo apt install -y python3 python3-pip

# Fedora
sudo dnf install -y python3 python3-pip

# Arch/Manjaro
sudo pacman -S --needed python python-pip
```

#### Windows

1. Descargar desde **[https://www.python.org/downloads/](https://www.python.org/downloads/)** 
2. **Marcar** "**Add Python to PATH**" durante la instalación.
3. Verificar en PowerShell:
```powershell
py --version
py -m pip --version
```

### 3.2 Instalación de dependencias

```bash
# Instalar la librería requests
pip install requests

# O usando el módulo pip de Python
python -m pip install requests
```

### 3.3 Entorno virtual (opcional recomendado)

```bash
# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
# Linux/macOS:
source .venv/bin/activate
# Windows:
# .\.venv\Scripts\Activate.ps1

# Instalar dependencias en el entorno virtual
pip install requests
```

---

## 4) Ejecución del juego

### Sintaxis general

```bash
python ahorcado.py
```

> En Windows puedes usar `py` en lugar de `python`.

> En Linux, si conviven varias versiones, usa `python3`.

---

### Ejemplos de ejecución

**Inicio del juego**

```bash
# Linux/macOS
python3 ahorcado.py
# Windows
python ahorcado.py

# Salida esperada inicial
==================================================
------------------AHORCADO-------------------
==================================================
Ingresa una letra: 
```

**Durante el juego**

```
Fallos: 1/6
------
Letras introducidas:  ['A', 'E', 'I']

Ingresa una letra: 
```

**Victoria**

```
Ganaste! La palabra era programación
¿Quieres seguir jugando? (S/N)
```

**Derrota**

```
Has perdido... La palabra era elefante
¿Quieres seguir jugando? (S/N)
```

---

## 5) Funcionalidades

### Obtención de palabras

- Utiliza **Random Word API** (`https://random-word-api.herokuapp.com/word?lang=es&number=1`)
- Retorna palabras aleatorias en español
- Una palabra por ronda

### Validación de entrada

- Comprueba que la entrada sea **una sola letra**
- Verifica que **no se haya introducido antes**
- Acepta tanto mayúsculas como minúsculas
- Rechaza números, símbolos y entradas múltiples

### Interfaz visual

- **Dibujo progresivo del ahorcado** según los fallos:
  - 1 fallo: cabeza
  - 2 fallos: cuerpo
  - 3 fallos: pierna izquierda
  - 4 fallos: ambas piernas
  - 5 fallos: brazo izquierdo
  - 6 fallos: brazo derecho (juego perdido)

- **Palabra oculta** mostrada con guiones
- **Letras intentadas** visibles en todo momento
- **Contador de fallos** actualizado

### Gestión del juego

- **Limpieza de pantalla** entre intentos
- **Sistema de rondas** continuas
- **Opción para reiniciar** o finalizar después de cada partida

---

## 6) Estructura del código

### Funciones principales:

- `procesarjuego()`: Coordina la preparación y ejecución del juego
- `procesarronda()`: Gestiona una ronda completa del juego
- `procesarletra()`: Valida y procesa la entrada del usuario
- `comprobarintento()`: Evalúa si el intento es correcto
- `anadirletra()`: Revela las letras acertadas en la palabra
- `dibujarahorcado()`: Controla el dibujo progresivo del ahorcado
- `preguntacontinuar()`: Gestiona la continuación del juego

### Funciones de dibujo:

- `dibujarcabeza()`
- `dibujarcuerpoybrazos()`
- `dibujarpiernas()`
- `dibujarpiernaizquierda()`

### Utilidades:

- `elegirpalabra()`: Obtiene palabra de la API
- `limpiarpantalla()`: Limpia la consola

---

## 7) Mensajes y errores

- **Entrada inválida**: "La letra X ya ha sido introducida, o no es una letra sino varias, o es un número"
- **Letra incorrecta**: "La letra X no se encuentra en la palabra"
- **Victoria**: "Ganaste! La palabra era [PALABRA]"
- **Derrota**: "Has perdido... La palabra era [PALABRA]"
- **Continuación**: "¿Quieres seguir jugando? (S/N)"

---

## 8) Problemas frecuentes (FAQ)

- **"ModuleNotFoundError: No module named 'requests'"** → Instala la dependencia con `pip install requests`
- **Error de conexión** → Verifica tu conexión a Internet (la API requiere conexión)
- **"python: command not found"** → Instala Python o ajusta el **PATH**
- **Caracteres especiales no mostrados correctamente** → Asegúrate de que la terminal soporte UTF-8
- **La API no responde** → El servicio podría estar temporalmente fuera de línea

---

## 9) API utilizada

- **Nombre**: Random Word API
- **URL**: `https://random-word-api.herokuapp.com/word`
- **Parámetros**: `lang=es` (español), `number=1` (una palabra)
- **Formato respuesta**: JSON array con una palabra

---
## 10) Evidencias de depuración 

He usado el depurador múltiples veces durante el proceso de desarrollo, pero me centraré en la última vez que lo he usado:

Durante la implementación del dibujo, me di cuenta que ocurría lo siguiente:

![](demostracionahorcado1.png)
Como vemos, con 4 fallos se pintan la cabeza, el cuerpo y ambas piernas, sin embargo, al 5º fallo:

![](demostracionahorcado2.png)
vemos que, como correspondería, se pinta el brazo izquierdo, sin embargo, ambas piernas han desaparecido.

Asi que añadiendo un breakpoint en la entrada de la función que dibuja las piernas: ![](breakpoint.png)
y cambiando desde el depurador la variable fallos a 4, que es justo antes de que se dibuje el 1º brazo, comencé a ejecutar paso a paso
![](variablefallos.png)
Una vez entre dentro de la función `dibujarpiernas()` con `F10` vi el `elif` de aquí, encargado de mostrar ambas piernas:
![](demostracionbug.png)
tenía == en lugar de >= lo que hacia que las piernassolo se imprimiesen puntualmente en el fallo 4. Al cambiar el operador, vemos que todo funcionaba correctamente:
![](capturas/Pasted%20image%2020251109012657.png)
Como vemos, ahora al 5º fallo se mantienen las piernas, tal como buscabamos