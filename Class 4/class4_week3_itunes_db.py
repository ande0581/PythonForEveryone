import xml.etree.ElementTree as ET
import sqlite3


def create_db(cur):

    # Make some fresh tables using executescript()
    cur.executescript('''
    DROP TABLE IF EXISTS Artist;
    DROP TABLE IF EXISTS Genre;
    DROP TABLE IF EXISTS Album;
    DROP TABLE IF EXISTS Track;

    CREATE TABLE Artist (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );

    CREATE TABLE Genre (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );

    CREATE TABLE Album (
        id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id  INTEGER,
        title   TEXT UNIQUE
    );

    CREATE TABLE Track (
        id  INTEGER NOT NULL PRIMARY KEY
            AUTOINCREMENT UNIQUE,
        title TEXT  UNIQUE,
        album_id  INTEGER,
        genre_id INTEGER,
        len INTEGER, rating INTEGER, count INTEGER
    );
    ''')


def lookup(d, key):
    """
    <key>Track ID</key><integer>369</integer>
    <key>Name</key><string>Another One Bites The Dust</string>
    <key>Artist</key><string>Queen</string>
    :param d: The dictionary
    :param key: The key in the dictionary we are trying to match on
    :return: If found return text, else None
    """
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None


def main():

    # Instantiate DB Cursor
    conn = sqlite3.connect('trackdb.sqlite')
    cur = conn.cursor()

    # Create DB
    create_db(cur)

    # Prompt of filename or default to 'Library.xml'
    fname = raw_input('Enter file name: ')
    if len(fname) < 1:
        fname = 'Library.xml'

    stuff = ET.parse(fname)
    all = stuff.findall('dict/dict/dict')
    print 'Dict count:', len(all)
    for entry in all:
        if lookup(entry, 'Track ID') is None:
            continue

        name = lookup(entry, 'Name')
        artist = lookup(entry, 'Artist')
        genre = lookup(entry, 'Genre')
        album = lookup(entry, 'Album')
        count = lookup(entry, 'Play Count')
        rating = lookup(entry, 'Rating')
        length = lookup(entry, 'Total Time')

        if name is None or artist is None or album is None or genre is None:
            continue

        #print name, artist, album, count, rating, length

        cur.execute('''INSERT OR IGNORE INTO Artist (name)
            VALUES ( ? )''', (artist, ))
        cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist, ))
        artist_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Genre (name) VALUES ( ? )''', (genre, ))
        cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre, ))
        genre_id = cur.fetchone()[0]

        cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id)
            VALUES ( ?, ? )''', (album, artist_id))
        cur.execute('SELECT id FROM Album WHERE title = ? ', (album, ))
        album_id = cur.fetchone()[0]

        cur.execute('''INSERT OR REPLACE INTO Track
            (title, album_id, genre_id, len, rating, count)
            VALUES ( ?, ?, ?, ?, ?, ? )''',
            (name, album_id, genre_id, length, rating, count))

        conn.commit()
    conn.close()


def display_results():
    conn = sqlite3.connect('trackdb.sqlite')
    cur = conn.cursor()

    sql = """
    SELECT Track.title, Artist.name, Album.title, Genre.name
    FROM Track JOIN Genre JOIN Album JOIN Artist
    ON Track.genre_id = Genre.ID and Track.album_id = Album.id
        AND Album.artist_id = Artist.id
    ORDER BY Artist.name, Track.title LIMIT 3
    """

    results = cur.execute(sql)
    results = results.fetchall()

    for result in results:
        print("{} |\t{} |\t{} |\t{}".format(result[0], result[1], result[2], result[3]))

    conn.close()

if __name__ == '__main__':
    main()
    display_results()
