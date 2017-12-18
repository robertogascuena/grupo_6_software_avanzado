<html>
 <head>
  <title>Calificacion</title>
  <!--<script src="./scripts/actualizarCheckBox.js"></script>-->
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
				$service_url = 'http://localhost:8080/profesores/nota';
				$ch = curl_init($service_url);
				$data = array("dniAlumno" => $dni[$filActualizar[$i]],
							"idAsignatura" => $idAsig,
							"nota" => $nota[$filActualizar[$i]]);
				$data_json = json_encode($data);
				curl_setopt($ch, CURLOPT_HTTPHEADER, array('Content-Type: application/json','Content-Length: ' . strlen($data_json)));
				curl_setopt($ch, CURLOPT_CUSTOMREQUEST, 'PUT');
				curl_setopt($ch, CURLOPT_POSTFIELDS, $data_json);
				curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
				$response = curl_exec($ch);
				if ($response === false) {
					$info = curl_getinfo($ch);
					curl_close($ch);
					die('error occured during curl exec. Additioanl info: ' . var_export($info));
				}
				curl_close($ch);
				$decoded = json_decode($response);
				if (isset($decoded->status) && $decoded->status === 400) {
					die('Error: ' . $decoded->detail);
				}	
			}//fin for
		}
	}//fin actualizar
	$service_url = 'http://localhost:8080/profesores/notas/by-user-profesor/'.$usuario;
	$curl = curl_init($service_url);
	curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
	$curl_response = curl_exec($curl);
	if ($curl_response === false) {
		$info = curl_getinfo($curl);
		curl_close($curl);
		die('error occured during curl exec. Additioanl info: ' . var_export($info));
	}
	curl_close($curl);
	$alumnos = json_decode($curl_response);
	if (isset($alumnos->status) && $alumnos->status === 404) {
		die('Error: ' . $alumnos->detail);
	}else{
		//echo "<p>".$alumno->dniAlumno."</p>";
		//Mostrar tabla con las notas
		echo "<p>Asignatura de ".$alumnos[0]->nombAsignatura."</p>";
		echo "<form name='actualizar' method='post' action='/profesores/calificacion.php/?a=1'>";
		echo '<input type="hidden" name="usuario" value="'.$usuario.'"/>';
		echo '<input type="hidden" name="idAsignatura" value="'.$alumnos[0]->idAsignatura.'"/>';
		echo "<table><tr><th>DNI Alumno</th><th>Nombre</th><th>Calificacion</th><th>Actualizar</th></tr>";
		$cont = 0;
		foreach($alumnos as &$alumno){
			echo "<tr><td><input type='text' name='dni[]' value='".$alumno->dniAlumno."' readonly/></td>
			<td>".$alumno->nombAlumno."</td>";
			if(isset($alumno->nota)){
				echo "<td><input type='number' name='nota[]' value='".$alumno->nota."' min='0' max='10' step='.01' oninput='update(".$cont.")'/></td>";
			}else{
				echo "<td><input type='number' name='nota[]' value='' min='0' max='10' step='.01' oninput='update(".$cont.")'/></td>";
			}
			echo "<td><input type='checkbox' id='checkbox".$cont."' name='actualizar[]' value='".$cont."'/></td></tr>";
			$cont++;
		}
		echo "</table>";
		echo "<input type='submit' name='submit' value='Actualizar'><input type='reset' value='Reiniciar'></form>";
	}
?>
 </body>
</html>