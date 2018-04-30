import sqlite3


def Main():
    try:
        con = sqlite3.connect('test.db')
        cur = con.cursor()
        cur.executescript("""DROP TABLE IF EXISTS Pets;
        create table Pets(id int, Name text, price int);
        insert into Pets values (1,"Cat",400);
        insert into Pets  values (2,"Dog",200);""")
        pets = ((3,"Parot",300),
                (4,"Bird",100),
                (5,"Fish",30))
        cur.executemany("insert into pets values(?,?,?)",pets)

        con.commit()

        cur.execute('select * from Pets')
        data = cur.fetchall()

        for row in data:
            print(row)

    except sqlite3.Error as er:
        if con:

            print ('Hata Bağlanamadım er:',er.args[0])
            con.rollback()
    finally:
        if con:
            con.close()


if __name__ == '__main__':
    Main()
