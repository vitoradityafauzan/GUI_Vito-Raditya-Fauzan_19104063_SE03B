from PyQt5.QtSql import *

def connectdb():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('testdb')
    if db.open():
        print('koneksi telah dibuat')
        query = QSqlQuery()
        sql = '''Create table phonebook(
        id integer not null primary key,
        nama varchar(25),
        nohp varchar(25)
        )'''
        query.exec_(sql)
        if (query.exec_):
            print('Berhasil membuat tabel')
    else:
        print('ERROR: ' + db.lastError().text())

connectdb()
