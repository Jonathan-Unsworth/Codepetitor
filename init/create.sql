CREATE TABLE `player_stats` (
  `player_stats_id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `level` INTEGER NOT NULL,
  `elo_rating` INTEGER NOT NULL,
  `wins` INTEGER NOT NULL,
  `loses` INTEGER NOT NULL,
  `win_lost_ratio` DOUBLE NOT NULL
);

CREATE TABLE `player` (
  `player_id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `player_stats_id` INTEGER NOT NULL,
  `username` VARCHAR(16) UNIQUE NOT NULL,
  `password` VARCHAR(16) NOT NULL
);

CREATE INDEX `idx_player__player_stats_id` ON `player` (`player_stats_id`);

ALTER TABLE `player` ADD CONSTRAINT `fk_player__player_stats_id` FOREIGN KEY (`player_stats_id`) REFERENCES `player_stats` (`player_stats_id`);

CREATE TABLE `task` (
  `task_id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `task_description` VARCHAR(255) NOT NULL
);

CREATE TABLE `games_played` (
  `game_id` INTEGER PRIMARY KEY AUTO_INCREMENT,
  `winner_id` INTEGER NOT NULL,
  `loser_id` INTEGER NOT NULL,
  `winners_code` VARCHAR(255) NOT NULL,
  `task_id` INTEGER NOT NULL,
  `losers_code` VARCHAR(255) NOT NULL
);

CREATE INDEX `idx_games_played__loser_id` ON `games_played` (`loser_id`);

CREATE INDEX `idx_games_played__task_id` ON `games_played` (`task_id`);

CREATE INDEX `idx_games_played__winner_id` ON `games_played` (`winner_id`);

ALTER TABLE `games_played` ADD CONSTRAINT `fk_games_played__loser_id` FOREIGN KEY (`loser_id`) REFERENCES `player` (`player_id`) ON DELETE CASCADE;

ALTER TABLE `games_played` ADD CONSTRAINT `fk_games_played__task_id` FOREIGN KEY (`task_id`) REFERENCES `task` (`task_id`) ON DELETE CASCADE;

ALTER TABLE `games_played` ADD CONSTRAINT `fk_games_played__winner_id` FOREIGN KEY (`winner_id`) REFERENCES `player` (`player_id`) ON DELETE CASCADE