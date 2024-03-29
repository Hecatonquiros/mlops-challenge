
# Proyecto de Clasificación de Gafas con FastAPI

Este proyecto utiliza FastAPI para exponer un modelo de inteligencia artificial que puede clasificar si una persona en una foto proporcionada está usando gafas. El modelo se basa en el dataset Olivetti Faces y ha sido entrenado para reconocer la presencia de gafas en imágenes faciales.

## Características

- **FastAPI**: Framework moderno y rápido (de alto rendimiento) para construir APIs con Python 3.7+.
- **Modelo de IA**: Utiliza un modelo SVM entrenado previamente para clasificar imágenes.
- **Swagger UI**: Documentación interactiva de la API y pruebas de endpoints integradas.

## Instalación

Este proyecto requiere Python 3.7+.

1. **Clonar el Repositorio**

   ```bash
   git clone https://github.com/Hecatonquiros/mlops-challenge.git
   cd tu-repositorio
   ```

2. **Crear y Activar un Entorno Virtual (Opcional)**

   ```bash
   python -m venv venv
   # En Windows
   venv\Scripts\activate
   # En Unix o MacOS
   source venv/bin/activate
   ```

3. **Instalar Dependencias**

   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

Para iniciar el servidor FastAPI, ejecuta:

```bash
uvicorn app.main:app --reload
```

El servidor estará disponible en `http://127.0.0.1:8000`. Puedes acceder a la documentación de la API y probar los endpoints directamente a través de Swagger UI en `http://127.0.0.1:8000/docs`.

## Uso

Para usar el endpoint de clasificación de gafas, sigue estos pasos:

1. Accede a Swagger UI en `http://127.0.0.1:8000/docs`.
2. Introduce en el authorize las credenciales (username: admin, password: password)
3. Selecciona el endpoint `/predict/`.
4. Usa el botón "Try it out" para cargar una imagen (hay de ejemplo en la carpeta app/tests/test_files)
5. Haz clic en "Execute" para enviar la imagen y recibir la predicción.

## Docker

Este proyecto se puede ejecutar dentro de un contenedor Docker. Sigue estos pasos para construir y ejecutar el contenedor:

1. **Construir la Imagen de Docker**

   En la raíz del proyecto, ejecuta:

   ```bash
   docker build -t clasificacion-gafas-fastapi .
   ```

   Esto construirá una imagen de Docker con la etiqueta `clasificacion-gafas-fastapi` basada en el `Dockerfile` en la raíz del proyecto.

2. **Ejecutar el Contenedor**

   Una vez construida la imagen, puedes ejecutarla con:

   ```bash
   docker run -d --name myfastapi -p 8000:8000 clasificacion-gafas-fastapi
   ```

   Esto iniciará un contenedor llamado `myfastapi`, exponiendo el servidor FastAPI en el puerto 8000 de tu máquina local.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
