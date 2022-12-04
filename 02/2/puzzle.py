def parsePlayer1PlayType(encodedPlayType: str) -> str:
    if encodedPlayType == 'A':
        return 'Rock'
    if encodedPlayType == 'B':
        return 'Paper'
    if encodedPlayType == 'C':
        return 'Scissors'
    raise NameError('Unknown value')

def parsePlayer2PlayType(player1PlayType: str, encodedPlayType: str) -> str:
    if encodedPlayType == 'X':
        if player1PlayType == 'Rock':
            return 'Scissors'
        elif player1PlayType == 'Paper':
            return 'Rock'
        else:
            return "Paper"
    if encodedPlayType == 'Y':
        return player1PlayType
    if encodedPlayType == 'Z':
        if player1PlayType == 'Rock':
            return 'Paper'
        elif player1PlayType == 'Paper':
            return 'Scissors'
        else:
            return "Rock"
    raise NameError('Unknown value')

def parseGameMove(gameLine: str) -> dict[str,str]:
    player1 = parsePlayer1PlayType(gameLine[0])
    return {"player1": player1, "player2": parsePlayer2PlayType(player1, gameLine[2])}

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

def playGame(game: dict[str, str]):
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

def getPlayer2Scores(result: dict[str,int]) -> int:
    return result["player2Score"]

with open('data.txt') as f:
    games = list(map(parseGameMove, f.read().splitlines()))
    results =  list(map(playGame, games))
    player2Score = list(map(getPlayer2Scores, results))

print(sum(player2Score))