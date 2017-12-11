<?php 
	//include("includes/conexion.php"); 
?>
<html>
 <head>
  <title>Login</title>
 </head>
 <body>
  <form name="conectar" method="post" action="/profesores/calificacion.php">
	<p>Nombre de usuario <input type="text" value="juan.antonio" name="usuario" /></p> 
	<p>Contraseña <input type="password" value="juan" name="password" /></p>
	<?php 
		if(isset($_GET["ci"]) && trim($_GET["ci"]) == 1){
			echo "<p style='color:red;'>Contraseña incorrecta</p>";
		}
	?>
	<input type="submit" name="submit" value="Conectar">
  </form>
 
 </body>
</html>