import pygame
from chess.board import Board

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BROWN = (240, 217, 181)
DARK_BROWN = (181, 136, 99)
HIGHLIGHT_COLOR = (50, 205, 50, 128)
CAPTURE_COLOR = (255, 0, 0, 128)

# Load images
def load_piece_images():
    images = {}
    for color in ['white', 'black']:
        for piece in ['pawn', 'rook', 'knight', 'bishop', 'queen', 'king']:
            path = f'assets/{color}_{piece}.png'
            images[(color, piece)] = pygame.image.load(path)
    return images

piece_images = load_piece_images()

# Initialize Board
board = Board()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Chess")

selected_piece = None
valid_moves = []

# Draw Board
def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Draw Pieces
def draw_pieces():
    for row in range(ROWS):
        for col in range(COLS):
            piece = board.board[row][col]
            if piece:
                image = piece_images[(piece.color, piece.__class__.__name__.lower())]
                screen.blit(image, (col * SQUARE_SIZE, row * SQUARE_SIZE))

# Highlight Moves
def highlight_moves(moves):
    for row, col in moves:
        pygame.draw.circle(screen, HIGHLIGHT_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2), 15)

# Main Game Loop
running = True
while running:
    screen.fill(WHITE)
    draw_board()
    draw_pieces()
    highlight_moves(valid_moves)
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            row, col = y // SQUARE_SIZE, x // SQUARE_SIZE
            
            if selected_piece:
                if (row, col) in valid_moves:
                    board.make_move(selected_piece, (row, col))
                selected_piece = None
                valid_moves = []
            else:
                piece = board.board[row][col]
                if piece and piece.color == board.current_turn:
                    selected_piece = (row, col)
                    valid_moves = piece.valid_moves((row, col), board)
                    valid_moves = [move for move in valid_moves if board.is_valid_move((row, col), move)]
    
    if board.is_checkmate(board.current_turn):
        print(f"{board.current_turn} is in checkmate! Game over.")
        running = False
    elif board.is_in_check(board.current_turn):
        print(f"{board.current_turn} is in check!")

pygame.quit()
