Requisitos:

- python 3
- Instalar locust y dotenv

```
pip3 install python-dotenv
pip3 install locust
```

Para pode rusar esta herramienta, se necesita crear un nuevo archivo .env usando como ejemplo el archivo example.env

Luego de estp, necesita crear un .locust.conf usando como ejemplo el archivo example.locust.conf

dentro de locustfile.py, puede configurar a gusto el request que desea hacer, incluso llenar un body en la variable body

Luego de tener esto, tiene que generar el archivo sqlite con el comando

```
python3 manage.py migrate
```

y ya con esto, puede empezar con el comando.

```
locust --config .locust.conf
```

Tambien puede usar el comando

```
./run.sh
```

Si cumple las siguientes condiciones:

1: Tiene creado en su base de datos postgresql un usuario con permisos de super que tenga el mismo nombre del su usuario en el equipo.
2: Modifico el resetData.sql con los querys necesarios para limpiar su base de datos y en el run.sh modifico el nombre de la base de datos a la que desea apuntar

Esto porque el primer comando, directamente corre el sql del archivo en la base a la que este apuntando y al momento de hacerlo, usara el nombre de su usuario como el usuario que solicita el query
