from pony.orm import *



db = Database()



class Player(db.Entity):
    player_id = PrimaryKey(int, auto=True)
    player_stats_id = Required('Player_Stats')
    games_won = Set('Games_Played', reverse='winner_id')
    games_lost = Set('Games_Played', reverse='loser_id')
    username = Required(str, 16, unique=True)
    password = Required(str, 16)


class Player_Stats(db.Entity):
    player_stats_id = PrimaryKey(int, auto=True)
    player_id = Optional(Player)
    level = Required(int, default=0)
    elo_rating = Required(int, default=1200)
    wins = Required(int, default=0)
    loses = Required(int, default=0)
    win_lost_ratio = Required(float, default=0)


class Games_Played(db.Entity):
    game_id = PrimaryKey(int, auto=True)
    winner_id = Required(Player, reverse='games_won')
    loser_id = Required(Player, reverse='games_lost')
    winners_code = Required(str)
    task_id = Required('Task')
    losers_code = Required(str)


class Task(db.Entity):
    task_id = PrimaryKey(int, auto=True)
    task_description = Required(str)
    games = Set(Games_Played)

db.bind(host="localhost", provider="mysql", user="root", password="charmander117", db="codepetitor")
db.generate_mapping()