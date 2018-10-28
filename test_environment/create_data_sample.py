import cx_Oracle

con = cx_Oracle.connect('jenkins', 'jenkins', 'localhost:49161/XE')
cursor = con.cursor()
cursor.execute('DROP USER test CASCADE')
cursor.execute('CREATE USER test IDENTIFIED BY test')
cursor.execute('GRANT ALL PRIVILEGES TO test')

cursor.execute('CREATE TABLE test.employees AS SELECT * FROM prod.employees');
