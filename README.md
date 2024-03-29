
# Proyecto de Clasificación de Gafas con FastAPI

Este proyecto utiliza FastAPI para exponer un modelo de inteligencia artificial que puede clasificar si una persona en una foto proporcionada está usando gafas. El modelo se basa en el dataset Olivetti Faces y ha sido entrenado para reconocer la presencia de gafas en imágenes faciales.

## Características Adicionales

- **Logging de aplicación**: Registro completo de eventos de la aplicación en `/logs/app.log`, facilitando el seguimiento y la depuración.
- **Autenticación**: Autenticación segura mediante tokens JWT. La autenticación se realiza a través de un Bearer Token para proteger las rutas críticas.
- **Manejo de excepciones**: Un módulo de excepciones personalizadas que captura y registra errores, mejorando la fiabilidad y mantenibilidad del código.
- **Modelo de token**: Uso del modelo Pydantic para la validación de tokens y datos entrantes, asegurando la integridad de los datos a través de la aplicación.
- **Configuración centralizada**: Un módulo de configuración inicializa valores críticos de la aplicación al arranque, asegurando que todos los componentes estén correctamente configurados.
- **Pruebas integradas**: Pruebas unitarias y de integración para modelos y rutas utilizando `pytest`, garantizando la calidad del código y facilitando la integración continua.
- **Rutas API**: Dos rutas principales, `/token` para la generación de tokens de autenticación y `/predict` para la clasificación de imágenes, asegurando una interfaz clara y funcional para los usuarios de la API.

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

## Uso de Swagger UI con Autenticación OAuth2

Una vez que el servidor FastAPI esté en ejecución, puedes utilizar Swagger UI para interactuar con la API, incluyendo las rutas protegidas mediante autenticación OAuth2. Sigue estos pasos para autenticarte:

1. Abre Swagger UI accediendo a [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) en tu navegador.

2. Haz clic en el botón `Authorize` que encontrarás en la parte superior derecha de la página de Swagger UI.

3. Se abrirá una ventana emergente de autenticación. Aquí deberás introducir tus credenciales de usuario (`username` y `password`) en los campos correspondientes.

    - **Nota:** Debes usar las credenciales válidas que tu API espera. Por ejemplo, si tienes un usuario administrador, podrías necesitar introducir `username: admin` y `password: tu_contraseña`.

4. Después de llenar los campos con tus credenciales, haz clic en el botón `Authorize` dentro de la ventana emergente para enviar la solicitud de token.

5. Una vez autenticado exitosamente, puedes cerrar la ventana emergente. Swagger UI utilizará el token de acceso obtenido para todas las solicitudes subsiguientes a rutas protegidas.

6. Para cerrar la sesión en Swagger UI y eliminar el token de acceso, puedes hacer clic en el botón `Logout` situado junto al botón `Authorize`.

Ahora estás listo para probar las rutas protegidas en tu API directamente desde Swagger UI, con cada solicitud incluyendo automáticamente el token de acceso requerido.

## Uso de CURL para Autenticación y Acceso a Rutas Protegidas

Para interactuar con rutas protegidas desde la línea de comandos, puedes usar `curl` para primero obtener un token de acceso y luego incluir este token en tus solicitudes subsiguientes.

### Obtener Token de Acceso

1. Usa el siguiente comando `curl` para obtener un token de acceso. Reemplaza `tu_usuario` y `tu_contraseña` con tus credenciales válidas.

    ```bash
    curl -X 'POST' \
      'http://localhost:8000/token' \
      -H 'Content-Type: application/x-www-form-urlencoded' \
      -d 'username=tu_usuario&password=tu_contraseña'
    ```

    Este comando enviará tus credenciales a la ruta `/token` y, si son válidas, recibirás una respuesta que incluye un token de acceso.

2. Copia el token de acceso desde la respuesta. Lo necesitarás para realizar solicitudes a rutas protegidas.

### Hacer una Solicitud a una Ruta Protegida

Con tu token de acceso, puedes ahora hacer solicitudes a rutas protegidas utilizando `curl`. A continuación, se muestra cómo hacer una solicitud a la ruta `/predict/`, incluyendo el token de acceso en el encabezado `Authorization`.

1. Reemplaza `TU_TOKEN_DE_ACCESO` en el siguiente comando con el token de acceso que obtuviste en el paso anterior. Asegúrate de incluir la palabra `Bearer` antes de tu token en el encabezado `Authorization`.

    ```bash
    curl -X 'POST' \
      'http://localhost:8000/predict/' \
      -H 'accept: application/json' \
      -H 'Authorization: Bearer TU_TOKEN_DE_ACCESO' \
      -H 'Content-Type: multipart/form-data' \
      -F 'file=@sample_face01.png;type=image/png'
    ```

    Este comando envía una solicitud POST a la ruta `/predict/`, incluyendo el archivo `sample_face01.png` como parte del cuerpo de la solicitud. La autenticación se maneja mediante el encabezado `Authorization`, que incluye el token de acceso obtenido previamente.

Recuerda reemplazar `sample_face01.png` con la ruta correcta al archivo de imagen que deseas enviar en tu solicitud. Si todo es correcto, recibirás una respuesta de la API basada en la lógica implementada para la ruta `/predict/`.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.
