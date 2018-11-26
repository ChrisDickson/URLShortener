# URLShortener
#### Author: Christopher Dickson   
#### GitHub Repo: https://github.com/ChrisDickson/URLShortener

The application requires a MySQL database. A script to create the required table can be found in:
`instance/url_schema.sql`

To run this service you should:

1. Clone the git repo, or otherwise download the files. 
2. In a command line, point to the location the of the repo.    
e.g., `C:\PythonCode\URLShortener`
3. Enter the command: `set FLASK_APP=app`
4. Enter the command: `flask run`
5. JSON data should be sent to `http://127.0.0.1:5000/short_url` in the format:    
`{    
        "url":"www.example-url.com"
 }`