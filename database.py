import sqlite3 as sql
db=sql.connect('data.db',check_same_thread=False)
def create(id=1,income=0):

    db.execute('''CREATE TABLE IF NOT EXISTS salary(
    ID INT PRIMARY KEY NOT NULL
    ,INCOME INT NOT NULL
    )''')
    theincome=select()
    if theincome != 0:
        income=theincome
    db.execute('''
     INSERT OR REPLACE INTO salary(ID,INCOME) VALUES(?,?)''',(id,income))
    db.commit()

def create_for_expences():
    db.execute('''CREATE TABLE IF NOT EXISTS expensess(
    EXPENSES TEXT PRIMARY KEY NOT NULL,
    EXPENSE INT NOT NULL
    )''')

def income(incom,id=1):
        db.execute('''
         REPLACE INTO salary(id,INCOME) VALUES(?,?)''',(id,incom,))
        db.commit()
def select():
    income=db.execute('''
    SELECT INCOME FROM salary WHERE ID=1
    ''')
    theincome=""
    for item in income:
        theincome=item[0]
    #print("+++++++++++++++++++++++++++++++++")
    #print(theincome)
    return theincome
def insert_expense(expenses,expense):
    db.execute('''
    INSERT OR REPLACE INTO expensess(EXPENSES,EXPENSE) VALUES(?,?)
    ''',(expenses,expense,))
    db.commit()
def get_the_money(expense):
    theexpense=db.execute('''SELECT EXPENSE FROM expensess WHERE EXPENSES=?
    ''',(expense,))#?
    money=""
    for item in theexpense:
        money=item[0]
    return money
def select_all_transcation():
    data=db.execute('''
    SELECT * FROM expensess
''')
    inst={}
    for item in data:
        inst[item[0]]=item[1]
    return inst
