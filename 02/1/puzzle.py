def parsePlayType(encodedPlayType: str) -> str:
    if encodedPlayType == 'A' or encodedPlayType == 'X':
        return 'Rock'
    if encodedPlayType == 'B' or encodedPlayType == 'Y':
        return 'Paper'
    if encodedPlayType == 'C' or encodedPlayType == 'Z':
        return 'Scissors'
    raise NameError('Unknown value')

def parseGameMove(gameLine: str) -> dict[str, str]:
    return {"player1": parsePlayType(gameLine[0]), "player2": parsePlayType(gameLine[2])}

def getScore(player: int, winner: int, played: str) -> int:
    
    if player == winner:
        winScore = 6
    elif winner == 0:
        winScore = 3
    else:
        winScore = 0

    if played == 'Rock':
        playedScore = 1
    elif played == 'Paper':
        playedScore = 2
    else:
        playedScore = 3

    return winScore + playedScore

def playGame(game:dict[str, str]) -> dict[str, int]:
    if game["player1"] == game["player2"]:
        winner = 0
# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock
    elif game["player1"] == 'Rock' and game["player2"] == 'Scissors':
         winner = 1
    elif game["player1"] == 'Scissors' and game["player2"] == 'Paper':
         winner = 1
    elif game["player1"] == 'Paper' and game["player2"] == 'Rock':
         winner = 1
    else:
        winner = 2

    return {
        "player1Score": getScore(1, winner, game["player1"]),
        "player2Score": getScore(2, winner, game["player2"]) 
    }

def getPlayer2Scores(result: dict[str, int]) -> int:
    return result["player2Score"]

with open('data.txt') as f:
    games = list(map(parseGameMove, f.read().splitlines()))
    results =  list(map(playGame, games))
    player2Score = list(map(getPlayer2Scores, results))

print(sum(player2Score))