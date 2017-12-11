<html>
 <head>
  <title>Calificacion</title>
  <script>
    function update(num){
		document.getElementById("checkbox"+num).checked = true;
	}
  </script>
  <style>
	  table, th, td {
		border: 1px solid black;
	}
  </style>
 </head>
 <body>
<?php 
	$usuario = $_POST['usuario'];
	$password = $_POST['password'];
	$servidor = "localhost";
	$BD = "universidad";
	
	$mysqli = new mysqli($servidor, $usuario, $password, $BD);

	if ($mysqli->connect_errno) {
		if($mysqli->connect_errno == 1045){
			header("Location: index.php/?ci=1", true, 301);
			exit;
		}
		echo "Lo sentimos, este sitio web está experimentando problemas.<br>";
		echo "Error: Fallo al conectarse a MySQL debido a: <br>";
		echo "Errno: " . $mysqli->connect_errno . "<br>";
		echo "Error: " . $mysqli->connect_error . "<br>";
		exit;
	}
	//Si hay que actualizar
	if(isset($_GET["a"]) && trim($_GET["a"]) == 1){
		if(!isset($_POST['actualizar'])){
			echo "<p style='color:red;'>No se actualizaron calificaciones</p>";
		}else{
			$filActualizar = $_POST['actualizar'];
			$N = count($filActualizar);
			$dni = $_POST['dni'];
			$nota = $_POST['nota'];
			$idAsig = $_POST['idAsignatura'];
			echo("<p>Se actualizan ".$N." filas</p>");
			for($i=0; $i < $N; $i++){
				$sql = "UPDATE `calificacion` SET `nota` = ".$nota[$filActualizar[$i]]." "
				."WHERE `calificacion`.`id_asignatura` = '".$idAsig."' AND `calificacion`.`dni_alumno` = '".$dni[$filActualizar[$i]]."'";
				if ($mysqli->query($sql) === FALSE) {
					echo "<p style='color:red;'>Error al actualizar al alumno con dni ".$dni[$filActualizar[$i]]." en la asignatura ".$idAsig."</p>";
				}
			}
		}	
	}
	//Consultar las notas
	$sql = "SELECT `asignatura`.`id`, `asignatura`.`nombre` AS \"nombasig\", `alumno`.`dni`, `alumno`.`nombre`, `calificacion`.`nota`\n"

    . "FROM `alumno` \n"

    . "	INNER JOIN `calificacion` ON `alumno`.`dni` = `calificacion`.`dni_alumno`\n"

    . "    INNER JOIN `asignatura` ON `calificacion`.`id_asignatura` = `asignatura`.`id`\n"

    . "    INNER JOIN `profesor` ON `asignatura`.`dni_profesor` = `profesor`.`dni`\n"

    . "WHERE `profesor`.`nombre_usuario` = \"".$usuario."\"";
	if (!$resultado = $mysqli->query($sql)) {
		echo "Lo sentimos, este sitio web está experimentando problemas.\n";
		echo "Error: La ejecución de la consulta falló debido a: \n";
		echo "Query: " . $sql . "\n";
		echo "Errno: " . $mysqli->errno . "";
		echo "Error: " . $mysqli->error . "\n";
		exit;
	}else{
		//Mostrar tabla con las notas
		$alumno = $resultado->fetch_assoc();
		echo "<p>Asignatura de " . $alumno['nombasig'] . "</p>";
		echo "<form name='actualizar' method='post' action='/profesores/calificacion.php/?a=1'>";
		echo '<input type="hidden" name="usuario" value="'.$usuario.'"/>';
		echo '<input type="hidden" name="password" value="'.$password.'"/>';
		echo '<input type="hidden" name="idAsignatura" value="'.$alumno['id'].'"/>';
		echo "<table><tr><th>DNI Alumno</th><th>Nombre</th><th>Calificacion</th><th>Actualizar</th></tr>";
		$cont = 0;
		do {
			echo "<tr><td><input type='text' name='dni[]' value='".$alumno['dni']."' readonly/></td>
			<td>".$alumno['nombre']."</td>
			<td><input type='number' name='nota[]' value='".$alumno['nota']."' min='0' max='10' step='.01' oninput='update(".$cont.")'/></td>
			<td><input type='checkbox' id='checkbox".$cont."' name='actualizar[]' value='".$cont."'/></td></tr>";
			$cont++;
		}while($alumno = $resultado->fetch_assoc());
		echo "</table>";
		echo "<input type='submit' name='submit' value='Actualizar'><input type='reset' value='Reiniciar'></form>";
	}
	$resultado->free();
	$mysqli->close();
?>
 </body>
</html>