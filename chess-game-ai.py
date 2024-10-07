import pygame
import chess
import chess.engine

pygame.init()

WIDTH = 1000
HEIGHT = 900
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Chess Game with AI!')
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 28)
big_font = pygame.font.Font('freesansbold.ttf', 30)
timer = pygame.time.Clock()
fps = 60

# Game variables
board = chess.Board()
selection = None
game_over = False
winner = ''
valid_moves = []

# AI variables
engine = chess.engine.SimpleEngine.popen_uci("D:\stockfish\stockfish-windows-x86-64-avx2.exe")
ai_thinking = False
play_as_white = True
game_mode = ''

# Load piece images
piece_images = {}
for color in ['white', 'black']:
    for piece in ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']:
        image = pygame.image.load(f'pieces/{color} {piece}.png')
        piece_images[f'{color}_{piece}'] = pygame.transform.scale(image, (80, 80))
        piece_images[f'{color}_{piece}_small'] = pygame.transform.scale(image, (45, 45))

def draw_board():
    for row in range(8):
        for col in range(8):
            color = 'white' if (row + col) % 2 == 0 else 'gray'
            pygame.draw.rect(screen, color, [col * 100, row * 100, 100, 100])
    
    pygame.draw.rect(screen, 'gray', [0, 800, WIDTH, 100])
    pygame.draw.rect(screen, 'gold', [0, 800, WIDTH, 100], 5)
    pygame.draw.rect(screen, 'gold', [800, 0, 200, HEIGHT], 5)
    
    turn_text = "White's Turn" if board.turn == chess.WHITE else "Black's Turn"
    screen.blit(big_font.render(turn_text, True, 'black'), (20, 820))

def draw_pieces():
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is not None:
            x = chess.square_file(square) * 100
            y = (7 - chess.square_rank(square)) * 100
            color = 'white' if piece.color == chess.WHITE else 'black'
            piece_type = chess.piece_name(piece.piece_type)
            screen.blit(piece_images[f'{color}_{piece_type}'], (x + 10, y + 10))

def draw_valid_moves():
    if selection is not None:
        for move in board.legal_moves:
            if move.from_square == selection:
                x = chess.square_file(move.to_square) * 100 + 50
                y = (7 - chess.square_rank(move.to_square)) * 100 + 50
                pygame.draw.circle(screen, 'red', (x, y), 5)

def draw_captured():
    white_captured = []
    black_captured = []
    
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece is None:
            expected_white = chess.Board().piece_at(square)
            expected_black = chess.Board().piece_at(chess.square_mirror(square))
            
            if expected_white and expected_white.color == chess.WHITE:
                white_captured.append(chess.piece_name(expected_white.piece_type))
            if expected_black and expected_black.color == chess.BLACK:
                black_captured.append(chess.piece_name(expected_black.piece_type))
    
    for i, piece in enumerate(white_captured):
        screen.blit(piece_images[f'white_{piece}_small'], (825, 5 + 50 * i))
    for i, piece in enumerate(black_captured):
        screen.blit(piece_images[f'black_{piece}_small'], (925, 5 + 50 * i))

def draw_check():
    if board.is_check():
        king_square = board.king(board.turn)
        x = chess.square_file(king_square) * 100
        y = (7 - chess.square_rank(king_square)) * 100
        pygame.draw.rect(screen, 'dark red', [x, y, 100, 100], 5)

def draw_game_over():
    pygame.draw.rect(screen, 'black', [200, 200, 400, 70])
    screen.blit(font.render(f'{winner} Won!', True, 'white'), (220, 210))
    screen.blit(font.render('Press ENTER to Restart!', True, 'white'), (220, 240))

def draw_mode_selection():
    screen.fill('gray')
    screen.blit(big_font.render('Select Game Mode:', True, 'black'), (350, 300))
    pygame.draw.rect(screen, 'light gray', [300, 350, 400, 50])
    pygame.draw.rect(screen, 'light gray', [300, 450, 400, 50])
    screen.blit(font.render('Play against AI', True, 'black'), (410, 365))
    screen.blit(font.render('Two Player Mode', True, 'black'), (410, 465))

def draw_color_selection():
    screen.fill('gray')
    screen.blit(big_font.render('Select Your Color:', True, 'black'), (350, 300))
    pygame.draw.rect(screen, 'white', [300, 350, 400, 50])
    pygame.draw.rect(screen, 'black', [300, 450, 400, 50])
    screen.blit(font.render('Play as White', True, 'black'), (410, 365))
    screen.blit(font.render('Play as Black', True, 'white'), (410, 465))

def make_ai_move():
    global ai_thinking
    ai_thinking = True
    result = engine.play(board, chess.engine.Limit(time=2.0))
    board.push(result.move)
    ai_thinking = False

def reset_game():
    global board, selection, game_over, winner, valid_moves
    board = chess.Board()
    selection = None
    game_over = False
    winner = ''
    valid_moves = []

# Main game loop
run = True
mode_selected = False
color_selected = False

while run:
    timer.tick(fps)
    screen.fill('gray')

    if not mode_selected:
        draw_mode_selection()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 300 <= event.pos[0] <= 700:
                    if 350 <= event.pos[1] <= 400:
                        game_mode = 'ai'
                        mode_selected = True
                    elif 450 <= event.pos[1] <= 500:
                        game_mode = 'two_player'
                        mode_selected = True
                        color_selected = True
    elif game_mode == 'ai' and not color_selected:
        draw_color_selection()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 300 <= event.pos[0] <= 700:
                    if 350 <= event.pos[1] <= 400:
                        play_as_white = True
                        color_selected = True
                    elif 450 <= event.pos[1] <= 500:
                        play_as_white = False
                        color_selected = True
                        make_ai_move()  # AI plays first as White
    else:
        draw_board()
        draw_pieces()
        draw_captured()
        draw_check()
        draw_valid_moves()
        
        if game_over:
            draw_game_over()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if not game_over:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x = event.pos[0] // 100
                    y = event.pos[1] // 100
                    square = chess.square(x, 7 - y)

                    if game_mode == 'ai':
                        if (play_as_white and board.turn == chess.WHITE) or \
                           (not play_as_white and board.turn == chess.BLACK):
                            if selection is None:
                                piece = board.piece_at(square)
                                if piece is not None and piece.color == board.turn:
                                    selection = square
                            else:
                                move = chess.Move(selection, square)
                                if move in board.legal_moves:
                                    board.push(move)
                                    selection = None
                                    if not board.is_game_over():
                                        make_ai_move()
                                    else:
                                        game_over = True
                                        winner = "White" if board.turn == chess.BLACK else "Black"
                                else:
                                    selection = None
                    
                    elif game_mode == 'two_player':
                        if selection is None:
                            piece = board.piece_at(square)
                            if piece is not None and piece.color == board.turn:
                                selection = square
                        else:
                            move = chess.Move(selection, square)
                            if move in board.legal_moves:
                                board.push(move)
                                if board.is_game_over():
                                    game_over = True
                                    winner = "White" if board.turn == chess.BLACK else "Black"
                            selection = None

            if event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_RETURN:
                    reset_game()

    pygame.display.flip()

pygame.quit()
engine.quit()
