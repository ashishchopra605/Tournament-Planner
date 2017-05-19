-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


-- tournament database created

CREATE DATABASE tournament;

-- connect to database tournament
\c tournament

-- players table created

CREATE TABLE players(id serial primary key,name varchar(25) NOT NULL);

-- matches table created

CREATE TABLE matches(id serial primary key,winner Integer REFERENCES players(id) NOT NULL,loser Integer REFERENCES players(id) NOT NULL);

-- standings view created

CREATE VIEW standings AS SELECT players.id, players.name, (SELECT count(matches.winner) FROM matches WHERE players.id = matches.winner) AS total_wins, (SELECT count(matches.id) FROM matches WHERE players.id = matches.winner OR players.id = matches.loser) AS total_matches FROM players ORDER BY total_wins DESC, total_matches DESC;





