# Usa Alpine como imagen base
FROM alpine:3.14

# Actualiza la lista de paquetes e instala las herramientas necesarias
RUN apk update && \
    apk add --no-cache python3-dev py3-pip && \
    pip3 install --upgrade pip

# Instala las dependencias necesarias para mysqlclient
# RUN apk --no-cache add mariadb-connector-c-dev build-base

RUN apk add mariadb-dev

RUN apk add mariadb-connector-c-dev build-base

# Establece el directorio de trabajo
WORKDIR /app

# Copia el código de la aplicación al contenedor
COPY . /app

# Instala las dependencias de Python
RUN pip3 --no-cache-dir install -r requirements.txt

# Especifica el comando para ejecutar tu aplicación
CMD ["python3", "app.py"]

# apk add mariadb-dev
# apk add mariadb-connector-c-dev build-base
# pip3 install -r requirements.txt