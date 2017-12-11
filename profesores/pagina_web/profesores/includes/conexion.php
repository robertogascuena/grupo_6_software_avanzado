<?php
	$servidor = "localhost";
	$usuario = "prueba1";
	$password = "prueba1234";
	$BD = "universidad";
	
	$mysqli = new mysqli($servidor, $usuario, $password, $BD);

	if ($mysqli->connect_errno) {
		echo "Lo sentimos, este sitio web está experimentando problemas.<br>";
		echo "Error: Fallo al conectarse a MySQL debido a: <br>";
		echo "Errno: " . $mysqli->connect_errno . "<br>";
		echo "Error: " . $mysqli->connect_error . "<br>";
		exit;
	}
	$sql = "SELECT * FROM `alumno`";
	if (!$resultado = $mysqli->query($sql)) {
		echo "Lo sentimos, este sitio web está experimentando problemas.\n";
		echo "Error: La ejecución de la consulta falló debido a: \n";
		echo "Query: " . $sql . "\n";
		echo "Errno: " . $mysqli->errno . "";
		echo "Error: " . $mysqli->error . "\n";
		exit;
	}else{
		while ($alumno = $resultado->fetch_assoc()){
			echo "<p>El alumno " . $alumno['nombre'] . " con dni " . $alumno['dni'] . " esta vivo</p>";
		}
	}
	$resultado->free();
	$mysqli->close();
?>