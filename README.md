# Reconocimiento Facial con OpenCV

Este proyecto utiliza OpenCV para implementar un sistema de reconocimiento facial que permite identificar y almacenar rostros a partir de videos. Se basa en tres scripts principales que abarcan la captura de imágenes, el entrenamiento de un modelo de reconocimiento y la identificación de rostros en tiempo real.

## Descripción de los Scripts

### 1. Captura y Almacenamiento de Imágenes

El primer script se encarga de capturar imágenes de una persona específica desde un video y almacenarlas en una carpeta. Aquí se utilizan técnicas de detección de rostros para extraer y guardar las imágenes.

**Funcionamiento:**
- Se define el nombre de la persona y la ruta de almacenamiento de imágenes.
- Se abre un video, se detectan los rostros y se extraen imágenes de ellos, que se guardan en una carpeta dedicada.

### 2. Entrenamiento del Modelo de Reconocimiento Facial

El segundo script procesa las imágenes almacenadas y entrena un modelo de reconocimiento facial utilizando el método LBPH (Local Binary Patterns Histograms).

**Funcionamiento:**
- Se listan las carpetas de personas y se leen las imágenes desde estas carpetas.
- Se asignan etiquetas a las imágenes y se entrena el reconocedor con los datos obtenidos.
- Finalmente, se guarda el modelo entrenado en un archivo XML para su uso posterior.

### 3. Identificación de Rostros en Tiempo Real

El tercer script utiliza el modelo previamente entrenado para identificar rostros en un nuevo video, mostrando en pantalla el nombre de la persona identificada.

**Funcionamiento:**
- Se lee el modelo entrenado y se procesa un video en tiempo real.
- Para cada cuadro del video, se detectan rostros, se extraen y se identifican utilizando el modelo.
- Se muestra el nombre de la persona sobre el rostro detectado en el video.

## Ejemplo de Uso

1. **Captura de Imágenes:** Ejecuta el primer script para capturar imágenes de una persona de un video.
2. **Entrenamiento del Modelo:** Ejecuta el segundo script para entrenar el modelo con las imágenes capturadas.
3. **Identificación en Tiempo Real:** Ejecuta el tercer script para reconocer rostros en un video.

## Consideraciones

- Asegúrate de tener instalado OpenCV y sus dependencias en tu entorno de Python.
- Los videos utilizados deben estar en un formato compatible y deben tener buena calidad para asegurar una detección precisa de rostros.
- Las imágenes almacenadas deben ser suficientes (idealmente, al menos 300 imágenes) para un entrenamiento efectivo del modelo de reconocimiento facial.

## **Utilidad en Ingeniería de Datos**

**Este código es altamente relevante para la ingeniería de datos ya que:**

- Permite la recopilación de datos de manera estructurada (imágenes de rostros) para entrenar modelos de machine learning.
- Facilita la creación de pipelines de datos al integrar la captura, el procesamiento y el almacenamiento de datos.
- Proporciona un marco para la implementación de técnicas de análisis de datos en tiempo real, lo que es fundamental en aplicaciones de visión por computadora.

Este enfoque se puede extender a otros dominios donde la detección y el reconocimiento de patrones son necesarios, como en la seguridad, el marketing y la interacción humano-computadora.

