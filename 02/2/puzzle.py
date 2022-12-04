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
        
def parsePlayer1PlayType(encodedPlayType: str) -> PlayType:
    if encodedPlayType == 'A':
        return PlayType.ROCK
    if encodedPlayType == 'B':
        return PlayType.PAPER
    if encodedPlayType == 'C':
        return PlayType.SCISSORS
    raise NameError('Unknown value')

def parsePlayer2PlayType(player1PlayType: PlayType, encodedPlayType: str) -> PlayType:
    if encodedPlayType == 'X':
        if player1PlayType == PlayType.ROCK:
            return PlayType.SCISSORS
        elif player1PlayType == PlayType.PAPER:
            return PlayType.ROCK
        else:
            return PlayType.PAPER
    if encodedPlayType == 'Y':
        return player1PlayType
    if encodedPlayType == 'Z':
        if player1PlayType == PlayType.ROCK:
            return PlayType.PAPER
        elif player1PlayType == PlayType.PAPER:
            return PlayType.SCISSORS
        else:
            return PlayType.ROCK
    raise NameError('Unknown value')

def parseGameMove(gameLine: str) -> Game:
    player1 = parsePlayer1PlayType(gameLine[0])
    return Game(player1, parsePlayer2PlayType(player1, gameLine[2]))

def getScore(player: int, winner: int, played: PlayType) -> int:
    
    if player == winner:
        winScore = 6
    elif winner == 0:
        winScore = 3
    else:
        winScore = 0

    return winScore + played.value

def playGame(game: Game) -> Result:
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

    return Result(getScore(1, winner, game.player1), getScore(2, winner, game.player2))

def getPlayer2Scores(result: Result) -> int:
    return result.player2Score

with open('data.txt') as f:
    games = list(map(parseGameMove, f.read().splitlines()))
    results =  list(map(playGame, games))
    player2Score = list(map(getPlayer2Scores, results))

print(sum(player2Score))