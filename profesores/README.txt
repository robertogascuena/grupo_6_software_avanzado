1- Descargar el servidor de Apache y MySQL, para ello se usa el entorno XAMPP:
https://www.apachefriends.org/es/index.html

2- Una vez descargado, al instalar seleccionar los componentes: 
Apache, MySQL, PHP, phpMyAdmin

3- Copiar en la carpeta de instalacion de XAMPP la pagina web, para ello ir a
xampp\htdocs y añadir la carpeta profesores que se encuentra en la carpeta pagina_web

4- Iniciar los servidores de Apache y MySQL, se pueden iniciar ejecutando xampp-control.exe dentro de la carpeta de instalacion de XAMMP

Ahora se podra acceder al login de los profesores accediendo desde el navegador a la página http://localhost/profesores

5- Para importar la base de datos acceder a http://localhost/phpmyadmin/ . En la pestaña importar seleccionar el archivo
127_0_0_1.sql.zip que se encuentra en la carpeta base_de_datos

6- Una vez importada la base de datos se han de crear los usuarios de los profesores para acceder a la calificación.
En http://localhost/phpmyadmin/ seleccionar la base de datos universidad.
Seleccionar la pestaña privilegios
Pulsar a Agregar cuenta de usuario
El nombre de usuario tiene que ser el mismo que aparece en la columna 'nombre_usuario' de la tabla profesor
-Ej: Nombre de usuario: juan.antonio Contraseña: antonio
Seleccionar los privilegios de datos y darle a continuar

7- Ahora se podra entrar con el usuario juan.antonio y acceder la calificacion de su asignatura que es Algoritmia desde la página 
http://localhost/profesores

