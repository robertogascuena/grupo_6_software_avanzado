1- Descargar el servidor de Apache y MySQL, para ello se usa el entorno XAMPP:
https://www.apachefriends.org/es/index.html

2- Una vez descargado, al instalar seleccionar los componentes: 
Apache, MySQL, PHP, phpMyAdmin

3- Copiar en la carpeta de instalacion de XAMPP la pagina web, para ello ir a
xampp\htdocs y añadir la carpeta profesores que se encuentra en la carpeta pagina_web

4- Iniciar los servidores de Apache y MySQL, se pueden iniciar ejecutando xampp-control.exe dentro de la carpeta de instalacion de XAMMP

Ahora se podrá acceder al login de los profesores accediendo desde el navegador a la página http://localhost/profesores

5- Para importar la base de datos acceder a http://localhost/phpmyadmin/ . En la pestaña importar seleccionar el archivo
127_0_0_1.sql.zip que se encuentra en la carpeta base_de_datos

6- Arrancar el servidor del API Rest para ello ir a la carpeta python-flask-server y ejecutar el comando:
python -m swagger_server
Se puede acceder al API Rest desde la página: http://localhost:8080/profesores/ui/

7- Ahora se podrá entrar con un usuario de profesor, por ejemplo "juan.antonio" y acceder la calificación de su asignatura que es Algoritmia desde la página 
http://localhost/profesores

