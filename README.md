<div align="center">

<h1>⚡ ForceNet</h1>

<p>
	Simulador web para calcular la fuerza electrica neta sobre una carga objetivo
	mediante la Ley de Coulomb en 2D, con visualizacion grafica interactiva.
</p>

<p>
	<img alt="Python" src="https://img.shields.io/badge/Python-3.10+-1f2937?style=for-the-badge&logo=python&logoColor=ffd43b">
	<img alt="Flask" src="https://img.shields.io/badge/Flask-3.1-111827?style=for-the-badge&logo=flask&logoColor=white">
	<img alt="Vue" src="https://img.shields.io/badge/Vue-3-0f172a?style=for-the-badge&logo=vuedotjs&logoColor=42b883">
	<img alt="Tailwind" src="https://img.shields.io/badge/TailwindCSS-UI-0b1324?style=for-the-badge&logo=tailwindcss&logoColor=38bdf8">
</p>

</div>

---

## Tabla de Contenido

1. [🌐 Vista General](#vista-general)
2. [🧪 Demo Funcional](#demo-funcional)
3. [✨ Capacidades Principales](#capacidades-principales)
4. [🏗️ Arquitectura](#arquitectura)
5. [📐 Modelo Fisico](#modelo-fisico)
6. [🔌 API REST](#api-rest)
7. [⚙️ Instalacion](#instalacion)
8. [🚀 Guia de Uso](#guia-de-uso)
9. [✅ Calidad Tecnica](#calidad-tecnica)
10. [🛣️ Roadmap](#roadmap)
11. [📄 Licencia](#licencia)

## 🌐 Vista General

ForceNet esta disenada para entornos academicos y practicas de fisica aplicada donde se requiere:

1. Definir una carga objetivo en coordenadas cartesianas.
2. Agregar un conjunto arbitrario de cargas puntuales.
3. Obtener el vector de fuerza resultante con precision numerica.
4. Interpretar visualmente la direccion y magnitud del vector neto.

La aplicacion separa claramente la capa visual, la capa API y el dominio de calculo.

## 🧪 Demo Funcional

<table>
	<tr>
		<td><b>📝 Entrada</b></td>
		<td>Configuracion de carga objetivo y cargas puntuales en tiempo real</td>
	</tr>
	<tr>
		<td><b>📊 Salida</b></td>
		<td>Componentes <code>Fx</code>, <code>Fy</code> y magnitud <code>|F|</code></td>
	</tr>
	<tr>
		<td><b>🎯 Visualizacion</b></td>
		<td>Canvas responsivo con cargas, ejes y vector de fuerza neta</td>
	</tr>
</table>

## ✨ Capacidades Principales

1. Backend en Flask con endpoint REST para calculo.
2. Frontend reactivo con Vue 3 y feedback UX con SweetAlert2.
3. UI moderna basada en Tailwind CSS.
4. Motor de calculo orientado a objetos, desacoplado de la vista.
5. Manejo de errores para entradas invalidas y singularidades fisicas.
6. Diseno responsive adaptado a desktop, tablet y movil.

## 🏗️ Arquitectura

```text
ForceNet/
|-- app.py                # Enrutamiento web y endpoint API
|-- models.py             # Dominio fisico: vectores, cargas y calculadora
|-- requirements.txt      # Dependencias Python
|-- templates/
|   |-- index.html        # Interfaz Vue + Tailwind + Canvas
|-- README.md
```

### 🧩 Componentes del Dominio

1. Vector2D: modelo de vector en 2D con operacion de magnitud.
2. PointCharge: entidad de carga puntual con posicion cartesiana.
3. ForceCalculator: servicio de dominio que aplica Coulomb y suma vectorial.

## 📁 Documentacion por Archivo

### `app.py`

1. Rol: punto de entrada del servidor Flask.
2. Expone dos rutas:
	- `/`: renderiza la UI.
	- `/api/calculate`: recibe datos de cargas y responde `fx`, `fy`, `magnitude`.
3. Valida estructura del JSON y maneja errores de entrada/singularidad.

### `models.py`

1. Rol: capa de dominio fisico (sin dependencias de UI).
2. Define:
	- `Vector2D`: vector cartesiano y magnitud.
	- `PointCharge`: carga puntual con posicion.
	- `ForceCalculator`: sumatoria vectorial usando ley de Coulomb.
3. Lanza `ValueError` si dos cargas coinciden en la misma posicion (caso no acotado).

### `templates/index.html`

1. Rol: interfaz web reactiva (Vue 3 + Tailwind + Canvas).
2. Permite crear escenario fisico, enviar calculo al backend y visualizar resultados.
3. Incluye:
	- formularios para carga objetivo y cargas puntuales,
	- vista grafica con ejes y vector neto,
	- feedback de UX mediante SweetAlert2.

### `requirements.txt`

1. Rol: congelar dependencias Python necesarias para ejecutar el backend.
2. Uso recomendado:

```bash
pip install -r requirements.txt
```

### `README.md`

1. Rol: guia principal del proyecto.
2. Contiene instalacion, arquitectura, API, modelo fisico y flujo de uso.

## 📐 Modelo Fisico

Se usa la forma vectorial:

$$
\vec{F}_{12} = k \cdot q_1 q_2 \cdot \frac{\vec{r}_1 - \vec{r}_2}{\left|\vec{r}_1 - \vec{r}_2\right|^3}
$$

Con:

1. $k = 8.99 \times 10^9\; \text{N m}^2 / \text{C}^2$
2. Fuerza neta total: $\vec{F}_{net} = \sum_i \vec{F}_i$
3. Restriccion fisica: si $r^2 \approx 0$, se rechaza el caso para evitar una fuerza no acotada.

## 🔌 API REST

### 📍 Endpoint

```http
POST /api/calculate
Content-Type: application/json
```

### 📥 Request

```json
{
	"target": { "q": 0.000001, "x": 0, "y": 0 },
	"charges": [
		{ "q": 0.000002, "x": 1, "y": 0 },
		{ "q": -0.000001, "x": -1, "y": 2 }
	]
}
```

### ✅ Response Exitosa

```json
{
	"success": true,
	"fx": 12.345678,
	"fy": -4.210987,
	"magnitude": 13.043210
}
```

### ❌ Response con Error

```json
{
	"success": false,
	"error": "Mensaje de error"
}
```

## ⚙️ Instalacion

### 📌 Requisitos

1. Python 3.10 o superior.
2. pip actualizado.

### 🪜 Pasos

1. Clonar repositorio.

```bash
git clone <url-del-repositorio>
cd ForceNet
```

2. Crear entorno virtual.

Windows (PowerShell):

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instalar dependencias.

```bash
pip install -r requirements.txt
```

4. Iniciar servidor (desarrollo).

```bash
py .\app.py
```

Produccion con Gunicorn (Linux/macOS o contenedor):

```bash
gunicorn -w 2 -b 0.0.0.0:5000 app:app
```

5. Abrir en navegador.

```text
http://127.0.0.1:5000
```

### ☁️ Despliegue en Render

Este proyecto incluye `Procfile` con:

```text
web: gunicorn app:app
```

Pasos rapidos en Render:

1. Crea un nuevo **Web Service** desde tu repositorio.
2. Runtime: **Python 3**.
3. Build Command: `pip install -r requirements.txt`.
4. Start Command: `gunicorn app:app`.
5. Deploy.

## 🚀 Guia de Uso

1. Ingresa datos de la carga objetivo: $q_0$, $x$, $y$.
2. Registra una o mas cargas puntuales con coordenadas.
3. Ejecuta el calculo desde el boton principal.
4. Analiza componentes, magnitud y direccion del vector dibujado.

## ✅ Calidad Tecnica

1. Separacion de responsabilidades entre presentacion, API y dominio.
2. Validaciones para entradas incompletas y casos degenerados.
3. Respuestas JSON estandarizadas para consumo frontend.
4. Codigo orientado a extension para nuevas funcionalidades.

## 🛣️ Roadmap

1. Suite de pruebas unitarias para ForceCalculator.
2. Selector de unidades electricas (C, mC, uC).
3. Exportacion/importacion de escenarios en JSON.
4. Visualizacion de campo electrico y lineas equipotenciales.

## 📄 Licencia

Proyecto de uso academico y educativo.
Puedes adaptarlo libremente segun los requerimientos de tu curso o institucion.
