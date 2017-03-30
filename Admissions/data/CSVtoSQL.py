import csv
import sqlite3

con = sqlite3.Connection('admittedDB.sqlite')
cur = con.cursor()
cur.execute('CREATE TABLE "admitted" ("Ucb Level2 Ethnic Rollup Desc" varchar(50), "Gender" varchar(50), "Derived Residency" varchar(50),"College/school" varchar(50), "Applicant Headcounts" varchar(50),"Academic Yr" varchar(50), "Admitted" varchar(20));')

f = open('admitted data.csv')
csv_reader = csv.reader(f, delimiter=',')

cur.executemany('INSERT INTO admitted VALUES (?, ?, ?, ?, ?, ?, ?)', csv_reader)
cur.close()
con.commit()
con.close()
f.close()