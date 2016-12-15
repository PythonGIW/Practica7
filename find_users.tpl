<!DOCTYPE html>
<html xml:lang="en">

<head>
  <title>Practica7</title>
  <meta http-equiv="content-type" content="text/html; charset=iso-8859-1" />
  <link rel="stylesheet" type="text/css" href="style.css" />
</head>

<body>
  <div id="main">
    <div id="header">
      <div id="logo">
        <h1>BASE DE DATOS DE USUARIOS</h1>
      </div>
    </div>
    <div id="site_content">
      	<div id="content">
        <center><table>
        <tr><th>Nombre usuario</th><th>Email</th><th>Pagina Web</th><th>Tarjeta</th></tr><th>Hash</th></tr><th>Nombre</th></tr><th>Apellido</th></tr><th>Direccion</th></tr><th>Aficiones</th></tr><th>Fecha de nacimiento</th></tr>
        %for row in result:
          <td>{{row}}</td> 
        %end 
        </table></center>
    	</div>
    </div>
</body>
</html>

