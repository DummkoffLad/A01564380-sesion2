# 1.1.1 Entorno de programación: GitHub Codespaces con VS Code

## Introducción
**GitHub Codespaces** te ofrece un entorno de desarrollo completo basado en **VS Code en la nube**, ligado a tu repositorio. No necesitas instalar Python localmente: el contenedor ya trae intérprete, extensiones y dependencias reproducibles mediante configuración.

---

## Características
- **VS Code en el navegador** (o app) con terminal, extensiones y depuración.
- **Entorno reproducible** por repo usando `.devcontainer/`.
- **Integración total con Git y GitHub** (branches, PRs, Issues).
- **Configurable**: versiones de Python, paquetes, herramientas (linters, formatters, etc.).
- **Soporte Jupyter** dentro de VS Code (notebooks `.ipynb`).

### Limitaciones
- Requiere conexión estable a Internet.
- Los recursos de cómputo dependen del plan de GitHub.
- El contenedor “duerme” si no lo usas por un tiempo (se reactiva rápido).

---

## Requisitos previos
- Cuenta en **GitHub** con acceso a **GitHub Codespaces**.
- Un repositorio (por ejemplo, `python-ciencia-datos`) con permisos para abrir Codespaces.

---

## Primeros pasos (crear y abrir un Codespace)
1. Entra a tu repo en GitHub.
2. Haz clic en **Code → Codespaces → Create codespace on main** (o la rama que prefieras).
3. Espera 1–2 minutos a que se construya el contenedor e instale extensiones.
4. Se abrirá **VS Code Web** con el repo listo para trabajar (explorador, terminal, etc.).

> Tip: si tienes extensión de **GitHub Codespaces** instalada en VS Code de escritorio, puedes “**Open in VS Code**”.

---

## Hola Mundo (archivo `.py`)
1. Crea un archivo `hello.py` en la raíz del repo:
   ```python
   print("Hola mundo desde Codespaces 👋")
   ```
   
Abre la Terminal en VS Code y ejecuta:

```bash
python hello.py
```

Verás la salida en la terminal.


Notas: 
-Si el repo incluye requirements.txt, se instalarán automáticamente tras crear el Codespace.
- Si modificas requirements.txt y ya está creado el Codespace abre la Terminal en VS Code y ejecuta:
```bash


# Introducción a la Programación en Python  
**Curso:** Computer Science – Primer semestre  
**Tema:** Fundamentos de programación y cálculos en Python  

## 1. Algoritmos
Un **algoritmo** es una secuencia de pasos lógicos y bien definidos que se siguen para resolver un problema o realizar una tarea. En programación, los algoritmos son la base de todo programa.

**Características de un buen algoritmo:**
- **Preciso:** cada paso es claro y sin ambigüedades.
- **Definido:** el mismo problema siempre produce el mismo resultado.
- **Finito:** tiene un número limitado de pasos.

**Ejemplo de algoritmo para sumar dos números:**
1. Leer el primer número.
2. Leer el segundo número.
3. Sumar ambos números.
4. Mostrar el resultado.

## 2. Elementos básicos de un programa en Python
Un programa en Python suele incluir:

- **Variables:** espacios en memoria para guardar información.  
  ```python
  edad = 20
  ```
- **Operadores:** símbolos que realizan operaciones (+, -, *, /, %, **).  
  ```python
  total = precio * cantidad
  ```
- **Entrada y salida:** interacción con el usuario.  
  ```python
  nombre = input("Escribe tu nombre: ")
  print("Hola,", nombre)
  ```
- **Estructuras de control:** deciden el flujo del programa (`if`, `for`, `while`).
- **Funciones:** bloques de código reutilizables.  
  ```python
  def saludar():
      print("Hola mundo")
  ```

## 3. Orden en que se ejecutan las operaciones
Python sigue **reglas de precedencia** para decidir qué operación ejecutar primero.

**Orden común de ejecución (de mayor a menor prioridad):**
1. **Paréntesis** `()`
2. **Potencias** `**`
3. **Multiplicación, división, módulo** `*`, `/`, `%`
4. **Suma y resta** `+`, `-`
5. **Comparaciones** (`>`, `<`, `==`, `!=`, etc.)
6. **Operadores lógicos** (`and`, `or`, `not`)

**Ejemplo:**
```python
resultado = 3 + 2 * (5 ** 2)  
# 5 ** 2 = 25  
# 2 * 25 = 50  
# 3 + 50 = 53
print(resultado)  # Muestra 53
```

## 4. Actividad en clase: Construcción de programas con cálculos
**Objetivo:** aplicar variables, operadores, entrada/salida y orden de operaciones.

**Instrucciones:**
1. Crear un programa que:
   - Pida al usuario el precio de un producto y la cantidad.
   - Calcule el subtotal.
   - Calcule el IVA (16%).
   - Calcule el total.
2. Mostrar todos los resultados de forma clara.

**Ejemplo de solución:**
```python
# Solicitar datos al usuario
precio = float(input("Ingresa el precio del producto: "))
cantidad = int(input("Ingresa la cantidad: "))

# Cálculos
subtotal = precio * cantidad
iva = subtotal * 0.16
total = subtotal + iva

# Mostrar resultados
print("Subtotal:", subtotal)
print("IVA:", iva)
print("Total a pagar:", total)
```

**📌 Nota para estudiantes:**  
Antes de programar, piensa siempre el **algoritmo**. Un buen plan evita errores y facilita el desarrollo.
