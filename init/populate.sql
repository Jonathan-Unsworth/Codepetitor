INSERT INTO player_stats (level, elo_rating, wins, loses, win_lost_ratio)
VALUES (5, 1200, 6, 1, 6.0);

INSERT INTO player_stats (level, elo_rating, wins, loses, win_lost_ratio)
VALUES (17, 700, 21, 21, 1.0);

INSERT INTO player (player_stats_id, username, password)
VALUES (1, 'dinJarin', 'yoda');

INSERT INTO player (player_stats_id, username, password)
VALUES (2, 'chief117', 'cortana');

INSERT INTO task (task_description, task_name, task_code)
VALUES ('Write a function to print the first 5 Fibonacci numbers', 'Fibonacci', 'int fibonacci() { }');

INSERT INTO games_played (winner_id, loser_id, winners_code, task_id, losers_code)
VALUES (1, 2, 'int fib(int num) {return n + n-1}', 1, 'dfsfsqewr');games_played