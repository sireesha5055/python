from flask import Flask, render_template, request, jsonify
import pyodbc

app = Flask(__name__)

# Database connection configuration
# Connection string
server = 'SIRI'
database = 'Sql'
conn = pyodbc.connect('DRIVER={SQL Server Native Client 11.0};'
                      'SERVER=' + server + ';'
                      'DATABASE=' + database + ';'
                      'Trusted_Connection=yes;')

# Flask route to handle sign-in request and verify user credentials
@app.route('/signin', methods=['POST'])
def signin():
    try:
        # Get form data from the request
        email = request.form['email']
        password = request.form['password']

        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Call the stored procedure to check login credentials
        cursor.execute("EXEC USP_Users_Signin ?, ?, ?", email, password, 0)

        # Fetch the output flag from the stored procedure
        result = cursor.fetchall()
        flag = result[0][0]

        # Close the cursor
        cursor.close()

        # Return the login status to the frontend
        if flag == 1:
            print ('login succesful')
        else:
            return 'Invalid email or password. Please try again.'

    except Exception as e:
        # Handle errors and return an error message to the frontend
        return 'Error: ' + str(e)
