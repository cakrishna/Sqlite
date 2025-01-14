# run in terminal
import sqlite3
from employee import Employee

# create employee database
# conn = sqlite3.connect("employee.db") 
conn = sqlite3.connect(":memory:") 
# using :memory: we test database on evry run later assaingn to a database or table
# we pass it to database when we done this test with :memory:

# create a cursor to interact with that database
c = conn.cursor()

# 1) create tables once
c.execute("""CREATE TABLE employees (
          first text,
          last text,
          age int,
          pay real
          )""")

# 2) create functions for CRUD context with manages
# here we are creating an application to perform CRUD
# we are also using context managers using with
# context managers used to setup and teardown resources.
# it is used to open close files, commit, automatically
# in sqlite connection onjects used as contect managesrs that auto commit or rollback transactions.
# transactions will be commited if no error, if error auomatically rollback.
def insert_emp(emp):
    with conn: # we can commit insert by using with context manager
        c.execute("INSERT INTO employees VALUES (:first, :last, :age, :pay)", {'first': emp.first, 'last': emp.last, 'age': emp.age, 'pay': emp.pay})

def get_emps_by_name(lastname): # we dont commit select statements so no context manager is need here
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()

def update_age(emp, age):
    with conn: # used Context manager
        c.execute("""UPDATE employees SET age = :age
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'age': age})

def update_pay(emp, pay):
    with conn: # used Context manager
        c.execute("""UPDATE employees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})


def remove_emp(emp):
    with conn: # used Context manager
        c.execute("DELETE from employees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})


# 3) create instances on that Employee class
emp_1=Employee('john','doe', 43, 80000)
emp_2=Employee('tom','doe', 41, 90000)

# 4) insert 
insert_emp(emp_1)
insert_emp(emp_2)

# 5) get
emps = get_emps_by_name('doe')
print(emps)

# 6) update

update_age(emp_2,60)
update_pay(emp_2,99000)

# 7) delete

remove_emp(emp_1)

emps = get_emps_by_name('doe')
print(emps)

conn.close()
# it is a good practice to close