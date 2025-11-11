
> CLI que, **dada una IP, establece si esta es válida  y en caso de serlo muestra su clase**

---
## 1) Descripción del módulo

  

Este proyecto implementa un **comprobador de IPs**.

- La IP se introduce directamente como una cadena de texto

- La IP **debe estar formada por 4 octetos** (dígitos de 0 a 255) separados por punto

Las clases de IP se establecen de la siguiente manera:  

| Clase | Rango de Dirección IP       | Rango del primer octeto | Uso principal                               |
| ----- | --------------------------- | ----------------------- | ------------------------------------------- |
| A     | 0.0.0.0 - 127.255.255.255   | 0 - 127                 | Redes muy grandes (muchos hosts)            |
| B     | 128.0.0.0 - 191.255.255.255 | 128 - 191               | Redes medianas (empresas)                   |
| C     | 192.0.0.0 - 223.255.255.255 | 192 - 223               | Redes pequeñas (LANs)                       |
| D     | 224.0.0.0 - 239.255.255.255 | 224 - 239               | Multicast (transmisión a múltiples hosts)   |
| E     | 240.0.0.0 - 255.255.255.255 | 240 - 255               | Experimental (reservada para investigación) |

---
## 2) Requisitos

- **Python 3.10 o superior**.

- **Sin dependencias externas obligatorias.**
---

## 3) Instalación de Python

### 3.1 Linux

#### Debian/Ubuntu (y derivados)
```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv
python3 --version
python3 -m pip --version
```

#### Fedora
```bash
sudo dnf install -y python3 python3-pip python3-virtualenv
python3 --version
python3 -m pip --version
```

#### Arch/Manjaro
```bash
sudo pacman -S --needed python python-pip
python --version
python -m pip --version
```

> **Entorno virtual (opcional recomendado)**
```bash
python3 -m venv .venv
# Activar:
# Linux/macOS:
source .venv/bin/activate
# (Salir: 'deactivate')
```

### 3.2 Windows

#### Opción A — Microsoft Store
1. Abrir **Microsoft Store**, buscar **Python 3.x** (Python Software Foundation).
2. Instalar y verificar:
```powershell
py --version
py -m pip --version
```

#### Opción B — Instalador oficial
1. Descargar desde **https://www.python.org/downloads/** el instalador de Python 3.x.
2. **Marcar** “**Add Python to PATH**” durante la instalación.
3. Verificar:
```powershell
py --version
py -m pip --version
```

> **Entorno virtual (opcional)**
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
# (Salir: 'deactivate')
```

---

## 4) Ejecución del módulo

  

### Sintaxis general

```bash

python direccionesip.py DIRECCIÓN

```

- `DIRECCIÓN`: **Dirección IP a evaluar**

  

> En Windows puedes usar `py` en lugar de `python`.

> En Linux, si conviven varias versiones, usa `python3`.

---
### Ejemplos

**IP Clase A**

```bash
# Entrada esperada
# Linux/macOS
python3 direccionesip.py 1.1.1.1
# Windows
python direccionesip.py 1.1.1.1
# Salida esperada
IP válida Clase A
```

**IP Clase B**

```bash
# Entrada esperada
# Linux/macOS
python3 direccionesip.py 128.0.0.0
# Windows
python direccionesip.py 128.0.0.0
# Salida esperada
IP válida Clase B
```

**IP Clase C**

```bash
# Entrada esperada
# Linux/macOS
python3 direccionesip.py 192.0.0.0
# Windows
python direccionesip.py 192.0.0.0
# Salida esperada
IP válida Clase C
```

**IP Clase D**

```bash
# Entrada esperada
# Linux/macOS
python3 direccionesip.py 224.0.0.0
# Windows
python direccionesip.py 224.0.0.0
# Salida esperada
IP válida Clase D
```

**IP Clase E**

```bash
# Entrada esperada
# Linux/macOS
python3 direccionesip.py 240.0.0.0
# Windows
python direccionesip.py 240.0.0.0
# Salida esperada
IP válida Clase E
```

**IP errónea**

```bash
# Entrada esperada
# Linux/macOS
python3 direccionesip.py 240.0.0.a
# Windows
python direccionesip.py 240.0.0.a
# Salida esperada
La IP no es válida (hay dígitos menores a 0 o letras)
```


---
## 6) Mensajes de error y códigos de salida

  

- **Octeto inválido** (>255)

- Mensaje: `La IP no es válida (hay digitos mayores a 255)`

- **Octeto inválido** (Negativo o letra)

-  Mensaje: `La IP no es válida (hay dígitos menores a 0 o letras)`

- **Demasiados octetos** o separadores

- Mensaje: `La IP tiene más de 4 octetos`
---
## 7) Problemas frecuentes (FAQ)
- **“python: command not found” / “py no se reconoce”** → Instala Python o ajusta el **PATH** (ver sección 3).
- **“pip no se reconoce”** → Usa `python -m pip` (o `py -m pip` en Windows).
- **Si hay un error, sigue las instrucciones dadas. (asegurándote de que la IP cumple este formato `X.X.X.X`**)
