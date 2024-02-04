from flask import render_template_string
def gen_login(flask_auth_path):
    return render_template_string(f"""
	<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Login</title>
    <style>
        body {{
            color: green;
            background-color: black;
		}}
							   
		input {{
			color: green; /* Text color for input */
			background-color: black; /* Background color for input */
			border: 1px solid green; /* Border color for input */
			padding: 5px; /* Padding for input */
			margin: 5px; /* Margin for input */
			}}
		button {{
			color: green; /* Text color for input */
			background-color: black; /* Background color for input */
			border: 1px solid green; /* Border color for input */
			padding: 5px; /* Padding for input */
			margin: 5px; /* Margin for input */
			}}

	</style>
	</head>
	<body>
	<pre>
	Welcome!
							   
	Please Authenticate to Continue.
	</pre>
	<form action="{flask_auth_path}" method="post">
		<label for="username">Username:</label>
		<input type="text" id="username" name="username">
		</br>
		</br>
		<label for="password">Password:</label>
		<input type="password" id="password" name="password">
		</br>
		</br>
        <label for="2fa">2FA:</label>
		<input type="password" id="2fa" name="2fa">
		</br>
		</br>
		<button type="submit">Login</button>
	</body>
	""")
