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
	    	<h1>Usuarios</h1>
	    	<ul>
	   		 %for r in result:
	        	<li>{{r['_id']}}</li>
	        	<li>{{r['email']}}</li>
	        	<li>{{r['webpage']}}</li>
	        	<li>{{r['credit_card']}}</li>
	        	<li>{{r['password']}}</li>
	        	<li>{{r['name']}}</li>
	        	<li>{{r['surname']}}</li>
	        	<li>{{r['address']}}</li>
            <li>{{r['likes']}}</li>
            <li>{{r['birthdate']}}</li>        	
	    	%end 
	    	</ul>
    	</div>
    </div>
</body>
</html>

