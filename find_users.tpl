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
      <div id="menubar">
        <ul id="menu">
          <li><a href="/find_user">FIND USER</a></li>
          <li><a href="/find_users">FIND USERS</a></li>
          <li><a href="/find_users_or">FIND USERS OR</a></li>
          <li><a href="/find_like">FIND LIKE</a></li>
          <li><a href="/find_country">FIND COUNTRY</a></li>
          <li><a href="/find_email_birthdate">FIND EMAILBIRTHDAY</a></li>
          <li><a href="/find_country_likes_limit_sorted">FIND COUNTRY LIKES LIMIT SORTED</a></li>
        </ul>
      </div>
    </div>
    <div id="site_content">
      	<div id="content">
	    	<h1>Usuarios</h1>
	    	<tr><th>Nombre Usuario</th><th>Email</th><th>Tarjeta</th><th>Pagina Web</th><th>Hash</th><th>Nombre</th>....</tr>
	    	<tr>
	   		 %for r in rows:
	        	<td>{{r}}</td>
	    	%end 
	    	</tr>
    	</div>
    </div>
</body>
</html>

