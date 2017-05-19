<h1>About</h1>

<p>This is my submission for Project P4: Tournament Database, part of Udacity's Full Stack Web Developer Nanodegree.</p>
<p>The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.</p>

<p>This project has two parts: defining the database schema (SQL table definitions), and writing the code that will use it.</p>

<h1>Code Templates</h1>

<p>The templates for this project are in the tournament subdirectory of your VM’s /vagrant directory. You’ll find three files there: tournament.sql, tournament.py, and tournament_test.py.</p>
<ul>
<li>The template file tournament.sql is where you will put the database schema, in the form of SQL create table commands. Give your tables names that make sense to you, and give the columns descriptive names. You'll also need to create the database itself</li>

<li>The template file tournament.py is where you will put the code of your module. In this file you’ll see stubs of several functions. Each function has a docstring that says what it should do.</li>

<li>Finally, the file tournament_test.py contains unit tests that will test the functions you’ve written in tournament.py. You can run the tests from the command line, using the command python tournament_test.py.</li>
</ul>

<h1>Functions in tournament.py</h1>
<h3>registerPlayer(name)</h3>

<p>Adds a player to the tournament by putting an entry in the database. The database should assign an ID number to the player. Different players may have the same names but will receive different ID numbers.</p>
<h3>countPlayers()</h3>

<p>Returns the number of currently registered players. This function should not use the Python len() function; it should have the database count the players.</p>

<h3>deletePlayers()</h3>

<p>Clear out all the player records from the database.</p>
<h3>reportMatch(winner, loser)</h3>

<p>Stores the outcome of a single match between two players in the database.</p>
<h3>deleteMatches()</h3>

<p>Clear out all the match records from the database.</p>
<h3>playerStandings()</h3>

<p>Returns a list of (id, name, wins, matches) for each player, sorted by the number of wins each player has.</p>
<h3>swissPairings()</h3>

<p>Given the existing set of registered players and the matches they have played, generates and returns a list of pairings according to the Swiss system. Each pairing is a tuple (id1, name1, id2, name2), giving the ID and name of the paired players. For instance, if there are eight registered players, this function should return four pairings. This function should use playerStandings to find the ranking of players.</p>

<h1>How to Run</h1>
<ol>
<li>Install Vagrant and VirtualBox</li>
<li>Launch the Vagrant VM</li>
<li>run python tournament_test.py</li>
</ol>
