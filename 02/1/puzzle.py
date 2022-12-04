from enum import Enum

class PlayType(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

class Game:
    def __init__(self, player1: PlayType, player2: PlayType):
        self.player1 = player1       
        self.player2 = player2

class Result:
    def __init__(self, player1: int, player2: int):
        self.player1Score = player1       
        self.player2Score = player2

def parsePlayType(encodedPlayType: str) -> PlayType:
    if encodedPlayType == 'A' or encodedPlayType == 'X':
        return PlayType.ROCK
    if encodedPlayType == 'B' or encodedPlayType == 'Y':
        return PlayType.PAPER
    if encodedPlayType == 'C' or encodedPlayType == 'Z':
        return PlayType.SCISSORS
    raise NameError('Unknown value')

def parseGameMove(gameLine: str) -> Game:
    return Game(parsePlayType(gameLine[0]), parsePlayType(gameLine[2]))

def getScore(player: int, winner: int, played: PlayType) -> int:
    if player == winner:
        winScore = 6
    elif winner == 0:
        winScore = 3
    else:
        winScore = 0

    return winScore + played.value

def playGame(game:Game) -> Result:
    if game.player1 == game.player2:
        winner = 0

    # Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
    elif game.player1 == PlayType.ROCK and game.player2 == PlayType.SCISSORS:
         winner = 1
    elif game.player1 == PlayType.SCISSORS and game.player2 == PlayType.PAPER:
         winner = 1
    elif game.player1 == PlayType.PAPER and game.player2 == PlayType.ROCK:
         winner = 1
    else:
        winner = 2

    return Result(
        getScore(1, winner, game.player1),
        getScore(2, winner, game.player2)
    )

def getPlayer2Scores(result: Result) -> int:
    return result.player2Score

with open('data.txt') as f:
    games = list(map(parseGameMove, f.read().splitlines()))
    results =  list(map(playGame, games))
    player2Score = list(map(getPlayer2Scores, results))

print(sum(player2Score))