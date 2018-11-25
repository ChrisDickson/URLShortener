from flaskext.mysql import MySQL

mysql = MySQL()


def init_db(app):
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'urls'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    mysql.init_app(app)


def insert_urls(short, url):
    con = mysql.connect()
    cur = con.cursor()
    cur.execute("INSERT INTO urls (url, short) VALUES(%s, %s)", url, short)
    con.commit()


def check_url_in_db(url):
    url_flag = True
    con = mysql.connect()
    cur = con.cursor()
    if cur.execute("SELECT * FROM urls.urls WHERE url = %s", url) is None:
        url_flag = False
    return url_flag


def get_short(url):
    con = mysql.connect()
    cur = con.cursor()
    short = cur.execute("SELECT short FROM urls.urls WHERE url = %s", url)
    return short


def get_original(short):
    con = mysql.connect()
    cur = con.cursor()
    original = cur.execute("SELECT url FROM urls WHERE urls.short = %s", short)
    return original
