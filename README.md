# Online Shop

Proyecto con Django para construir una tienda online


## Configuración Inicial

### Configuración del entorno virtual

1.  Crear entorno virtual
    ``` bash
    # venv online shop

    python -m venv venv
    ```

2. Iniciar el entorno virtual
    ``` bash
    # Activar entorno virtual

    source venv/bin/activate
    ```

    ```bash
    # Desactivar entorno virtual

    deactivate
    ```

3. Instalar dependencias
    ```bash
    # Ejecutar el comando pip

    pip install -r requirements.txt
    ```

## Ejecutar la applicación

1. Ejecutar las migraciones

    ```bash
    # Ejecutar la opción migrate

    python manage.py migrate 
    ```

2. Para ejecutar el proyecto podemos ejecutar el siguiente comando:

    ```bash
    # Cambiar de ubicacion en la terminal a la carpeta src

    cd src

    # Ejecutar aplicación

    python manage.py runserver 
    ```

3. Finalmente abrir un navegador en la dirección **[localhos:8000](http://localhost:8000/)**
