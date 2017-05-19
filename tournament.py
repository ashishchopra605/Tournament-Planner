#!/usr/bin/env python
# tournament.py -- implementation of a Swiss-system tournament

import psycopg2
import bleach

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    conn = db.cursor()
    conn.execute("delete from matches;")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    conn = db.cursor()
    conn.execute("delete from players;")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    conn = db.cursor()
    conn.execute("select count(*) from players")
    count = conn.fetchone()
    db.close()
    return count[0]


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    conn = db.cursor()
    query = "insert into players (name) values(%s);"
    conn.execute(query, (name,))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place,or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    conn = db.cursor()
    conn.execute("select * from standings;")
    # return all rows in standings view
    result = conn.fetchall()
    db.close()
    return result


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    conn = db.cursor()
    query = ("INSERT INTO matches(winner, loser) VALUES (%s, %s);")
    conn.execute(query, (winner, loser,))
    db.commit()
    db.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    db = connect()
    c = db.cursor()
    # fetch id,name of players acc. to total matches win in descending order
    c.execute("SELECT id, name FROM standings ORDER BY total_wins DESC;")
    rows = c.fetchall()

    pairs = []
    # checks if there is even number of players
    if len(rows) % 2 == 0:
        for i in range(0, len(rows), 2):
            players = rows[i][0], rows[i][1], rows[i+1][0], rows[i+1][1]
            pairs.append(players)
        return pairs

    else:
        print "There are uneven number of players in the tournament"

    db.close()
