import cx_Oracle

con = cx_Oracle.connect('jenkins', 'jenkins', 'localhost:49161/XE')
cursor = con.cursor()
cursor.execute('SELECT EMPLOYEE_ID, FIRST_NAME, LAST_NAME, EMAIL, PHONE_NUMBER, HIRE_DATE, JOB_ID, SALARY, COMMISSION_PCT, MANAGER_ID, DEPARTMENT_ID FROM TEST.EMPLOYEES WHERE EMPLOYEE_ID = 100')
row = cursor.fetchone()
assert row[1] == 'Steven'