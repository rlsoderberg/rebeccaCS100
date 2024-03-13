#embedded sql scripts including show database & add data

#notes:
#it doesn't like comparing None
#list was the key to displaying a list of databases
#i ended up using regular expressions when database items were hard to strip
#use join correctly (it's not the same as append); it helps to use tuples
#correct datatypes also help

#it always puts a b before the value for the last column. wat is this???

#well, i'm having problems with:
#create new column > a. exits the program, when i try to return to COLUMN MENU!
#create new column > b. gets stuck on types[d]????

#well, i was almost able to make a bool(2000), so i'll have to work on that next
#i tried, but it's still not filtering right!!!

#oh yeah, and the main thing is, look at all those variables i'm passing back and forth!!! seems so redundant

#anyway, it's not really doing what i want, but it is kind of limiting range, one way or another, so i'll take it for now

def show_db():

    showdb = "show databases;"
    show = db.cursor()
    show.execute(showdb)
    row_count = show.rowcount
    dblist = []
    for row in show:
        print(row)
        dblist.append(re.sub('[^\w]', '', str(row)))

    if row_count == 0:
        print(f'No databases found.')
    else:
        base = 'null_name'
        while base not in dblist:
            base = input('enter the name of a database to insert data: ')

    show.close()

    return base

def show_tables():

    showtables = "show tables;"
    tables = sdb.cursor()
    tables.execute(showtables)
    row_count = tables.rowcount
    tblist = []
    for row in tables:
        print(row)
        tblist.append(re.sub('[^\w]', '', str(row)))

    if row_count == 0:
        print(f'No tables found.')
    else:
        tabel = 'null_name'
        while tabel not in tblist:
            tabel = input('enter the name of a table to insert data: ')

    tables.close()

    return tabel


def show_columns(tabel):
    
    describen = "select * from " + tabel
    rows = sdb.cursor()
    rows.execute(describen)
    row_count = rows.rowcount
    columns = [name for (name, _, _, _, _, _, _) in rows.description]

    for row in rows:
        rowlist = list(row)
        print(rowlist)

    rows.close()

    return columns, row_count, rowlist

def create_insert(rowlist):
    base1 = "insert into " + tabel + " (`"
    base2 = "`) values ('"
    base3 = "')"

    print('Enter a value for each of these columns, or None for no value: ')
    for e in range(0, len(rowlist)):
        
        item = input(columns[e] + ': ')
        tuple1 = (base1, columns[e])
        if e > 0:
            base1 = "`, `".join(tuple1)
        else: 
            base1 = "".join(tuple1)
        tuple2 = (base2, item)
        if e > 0:
            base2 = "', '".join(tuple2)
        else:
            base2 = "".join(tuple2)
    
    stringtuple = (base1, base2, base3)
    string = "".join(stringtuple)
    strex = sdb.cursor()
    strex.execute(string)
    print('new row created.')

def select_type(length, types, inuse, lens, tabel):
    dt = 0
    while int(dt) == 0:

        print(f'\nSELECT DATA TYPE\ncurrent datatype is {inuse}({length}).')

        select = -1
        valid = False
        while valid == False:
            while int(select) == -1:
                try:
                    print('\navailable datatypes, and their length ranges:')
                    for x in types:
                        print(f'{types.index(x)}. {x} length:  (0, {lens[types.index(x)]})')
                    select = input('enter one of these numbers: ')
                    inuse = types[int(select)]
                    length = lens[types.index(x)]
                    valid = True
                except int(length) not in range(0, lens[types.index(inuse)]): 
                    print(f'current range {length} out of range for data type {inuse}.')
                    print(f'ranges for data types are: ')
                    for x in types:
                        print(f'{types.index(x)}. {x} length:  (0, {lens[types.index(x)]})')
                    select = input('enter one of these numbers: ')
            

        print(f'\nnew datatype & length: {inuse}({length})')
        dt = input('press 0 to select length again, or 1 to return to COLUMN MENU: ')

    if int(dt) == 1:
        column_menu(length, types, inuse, lens, tabel)
    return inuse
    
def set_range(length, types, inuse, lens, tabel):
    rng = 0
    while int(rng) == 0:

        print(f'\nSELECT LENGTH\ncurrent datatype is {inuse}({length}).')

        length = -1
        while int(length) == -1:
            print(f'\navailable length range for data type {inuse}: (0, {lens[types.index(inuse)]})')
            while int(length) not in range(0, lens[types.index(inuse)]):
                valid = False
                while valid == False:
                    try:
                        length = input('set length max: ')
                        valid = True
                    except int(length) not in range(0, lens[types.index(inuse)]):
                        print(f'range {length} out of range for current datatype {inuse}.')
                        print(f'range for data type {inuse} is (0, {lens[types.index(inuse)]}). please select another range. ')

        

        print(f'\nnew datatype & length: {inuse}({length})')
        rng = input('press 0 to select length again, or 1 to return to COLUMN MENU: ')

    if int(rng) == 1:
        column_menu(length, types, inuse, lens, tabel)

    return length

def column_menu(length, types, inuse, lens, tabel):

    print(f'\nCOLUMN MENU\ncurrent datatype is {inuse}({length}).')
    lentype = 'null_name'
    while lentype != 'a' and lentype != 'b' and lentype != 'c':
        lentype = input('press a to select a different length.\npress b to select a different datatype.\npress c to create column. ')


    if lentype == 'a':
        
        length = set_range(length, types, inuse, lens, tabel)

    elif lentype == 'b':

        inuse = select_type(length, types, inuse, lens, tabel)

    elif lentype == 'c':

        if int(length) < 0:
            print('\nyou need to set length first.')
            column_menu(length, types, inuse, lens, tabel)
        else:
            column_name(length, types, inuse, lens, tabel)


def column_name(length, types, inuse, lens, tabel):

    nm = 0
    while int(nm) == 0:

        print('\nSELECT COLUMN NAME')

        valid = False
        while valid == False:
            try:
                cname = input('type name for column, up to 128 characters: ')
                valid = True
            except len(cname) > 128:
                print('Error: column name length exceeds 128 characters. Try again: ')

        nm = input("press 1 to create column '" + cname + "', or 0 to SELECT COLUMN NAME again: ")

    if int(nm) == 1:
        execute_column(length, types, inuse, lens, tabel, cname)


def execute_column(length, types, inuse, lens, tabel, cname):

    newc = f'alter table {tabel} add {cname} {inuse}({length})'
    newcex = sdb.cursor()
    newcex.execute(newc)
    print(f'inserting column {cname} {inuse}({length}) into {tabel}')
    
    showc = 'show columns from ' + tabel
    newcex.execute(showc)
    columns = [(name, type_code) for (name, type_code, _, _, _, _, _) in newcex.description]

    print(f'\nnew columns for table {tabel}: ')
    for l in newcex:
        print(l)
   
    newcex.close()



import pymysql
import re

db = pymysql.connect(host='localhost', user='root', password = '2101')
db.autocommit(True)

#enter the name of a database to insert data
base = show_db()

db.close()


#reconnected at new database?        
sdb = pymysql.connect(host='localhost', user='root', password = '2101', database = base)
sdb.autocommit(True)


input('now in database ' + base + '. press any key to show tables in ' + base + '.')
tabel = show_tables()

input('press any key to see existing columns in ' + tabel)
columns, row_count, rowlist = show_columns(tabel)

length = 255
types = ['varchar', 'int', 'char', 'bool']
inuse = 'varchar'
lens = [65535, 255, 255, 1]

#do you want to a. create new row, or b. create new column?
c = 'null_name'
while c.lower() != 'a' and c.lower() != 'b':
    c = input('\ndo you want to a. create new row, or b. create new column? ')

if c == 'a':
    create_insert(rowlist)

elif c == 'b':
    column_menu(length, types, inuse, lens, tabel)

sdb.close()




