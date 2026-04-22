import chess
game = chess.Game()
running = True
while running:
    running = not game.refresh()