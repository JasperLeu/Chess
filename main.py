import chess
game = chess.Game()
running = True
print(game.board.getBestMove(4, "white"))
while running:
    running = not game.refresh()