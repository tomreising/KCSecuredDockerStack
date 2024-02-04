"""
Module for Login Page
"""
from flask import render_template_string
def gen_success():
    """
    Generate Login Page
    """
    return render_template_string("""
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Home Login</title>
<style>
	body {
		color: green;
		background-color: black;
	}
							
	input {
		color: green; /* Text color for input */
		background-color: black; /* Background color for input */
		border: 1px solid green; /* Border color for input */
		padding: 5px; /* Padding for input */
		margin: 5px; /* Margin for input */
		}
	button {
		color: green; /* Text color for input */
		background-color: black; /* Background color for input */
		border: 1px solid green; /* Border color for input */
		padding: 5px; /* Padding for input */
		margin: 5px; /* Margin for input */
		}

</style>
</head>
<body>
<pre>
	You have been authenticated!
	Please try your request again.
</pre>
</body>
	""")
