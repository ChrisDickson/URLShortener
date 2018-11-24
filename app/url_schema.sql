DROP TABLE IF EXISTS url;

CREATE TABLE urls (
  id INTEGER PRIMARY KEY auto_increment,
  url varchar(200) UNIQUE NOT NULL,
  short TEXT NOT NULL
);