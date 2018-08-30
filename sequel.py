import mysql.connector
cnx = mysql.connector.connect(user="root", database="test_env",password="password",
								auth_plugin='mysql_native_password')
cursor = cnx.cursor()

add_record = ("INSERT INTO mailchimp_data "
			"(id, lastname, email, client, avg_open, avg_click) "
			"VALUES (%s, %s, %s, %s, %s, %s)")