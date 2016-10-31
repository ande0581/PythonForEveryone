# 563 should the count for the org with the most messages
import sqlite3

conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

input_file = raw_input('Enter file name: ')
if len(input_file) < 1:
    input_file = 'mbox.txt'

fh = open(input_file)
for line in fh:
    if not line.startswith("From: "):
        continue
    pieces = line.split()
    email = pieces[1]
    domain = email.split('@')[1]  # Split the email to get just the domain name
    cur.execute('SELECT count from Counts WHERE org = ? ', (domain, ))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain, ))
    else:
        cur.execute('UPDATE Counts SET count=count+1 WHERE org = ?', (domain, ))

conn.commit()

sqlstr = 'SELECT org, count FROM counts ORDER BY count DESC LIMIT 10'
print('\nCounts from DB:')
for row in cur.execute(sqlstr):
    print("{} {}".format(row[0], row[1]))




