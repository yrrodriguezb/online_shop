# Online Shop

Proyecto con **[Django](https://www.djangoproject.com/)**. para construir una tienda online


## Configuración Inicial

### Ejecutando la aplicacion en un contenedor con docker

1. Crear la imagen de docker
    ``` bash
    # Crear la imagen con docker

    docker build -t app-online-shop:v1.0.0 .           
    ```

3. Crear un contenedor con la imagen contruida
     ``` bash
    # Crear el contenedor con docker

    docker run -it --name django-online-shop -p 8000:8000 app-online-shop:v1.0.0            
    ``` 

2. Conectarnos al contenedor con el fin de crear un super usuario
    ``` bash
    # Ejecutar comando createsuperuser

    docker exec -it django-online-shop python /app/src/manage.py createsuperuser
    ```

4. Finalmente abrir un navegador en la dirección **[localhost:8000](http://localhost:8000/)**    


**NOTA:** Tener en cuenta que si el contenedor es apagado, los datos en la base de datos se eliminarán, ya que no son persistentes. Para este caso, es necesario manejar los **[Volumenes](https://docs.docker.com/storage/volumes/)** en docker. Ya que este es un ejemplo muy sencillo para manejar contenedores de docker en una aplicación de **[Django](https://www.djangoproject.com/)**.


### Corriendo la aplicación con multiples contenedores (Django - MySQL)

1. Crear la imagen de docker
    ``` bash
    # Crear los servicios con docker compose
    docker-compose up           
    ```

2. Ejecutar las migraciones de Django
     ``` bash
    # ejecjutar comando migrate

    docker-compose run --rm web python src/manage.py migrate      
    ``` 

3. Conectarnos al contenedor con el fin de crear un super usuario
    ``` bash
    # Ejecutar comando createsuperuser

    docker-compose run --rm web python src/manage.py createsuperuser
    ```

4. Servir archivos estaticos
    ``` bash
    # Ejecutar comando collectstatic

    docker-compose run --rm web python src/manage.py collectstatic 
    ```

5. Finalmente abrir un navegador en la dirección **[localhost:8000](http://localhost:8000/)**    

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

4. Configurar variable de entorno
    ```bash
    # Nombre variable DJANGO_SETTINGS_MODULE
    # local
    export DJANGO_SETTINGS_MODULE=shop.settings.local

    # producción
    export DJANGO_SETTINGS_MODULE=shop.settings.production
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

3. Finalmente abrir un navegador en la dirección **[localhost:8000](http://localhost:8000/)**

