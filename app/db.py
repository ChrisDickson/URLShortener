from flaskext.mysql import MySQL

mysql = MySQL()


def init_db(app):
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'urlshorten'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    mysql.init_app(app)


def insert_urls(short, url):
    con = mysql.connect()
    cur = con.cursor()
    q = """INSERT INTO urls (url, short) VALUES (%s, %s)"""
    values = (url, short)
    cur.execute(q, values)
    con.commit()

    cur.close()
    con.close()


def check_url_in_db(url):
    url_flag = False
    con = mysql.connect()
    cur = con.cursor()
    q = """SELECT * FROM urlshorten.urls WHERE url = %s"""
    cur.execute(q, (url,))
    count = cur.rowcount
    if count == 0:
        url_flag = True

    cur.close()
    con.close()

    return url_flag


def get_short(url):
    con = mysql.connect()
    cur = con.cursor()
    query = """SELECT short FROM urlshorten.urls WHERE url = %s"""
    cur.execute(query, (url, ))
    short = cur.fetchone()

    cur.close()
    con.close()

    return short[0]


def get_original(short):
    con = mysql.connect()
    cur = con.cursor()
    query = """SELECT url FROM urls WHERE urls.short = %s"""
    cur.execute(query, (short, ))
    original = cur.fetchone()

    cur.close()
    con.close()

    return original[0]
