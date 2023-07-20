import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the window dimensions (scaled by 3x)
window_width, window_height = 720, 480
scale_factor = 3
window = pygame.display.set_mode((window_width * scale_factor, window_height * scale_factor))
pygame.display.set_caption("Maze Game")

# Define colors
BLACK = (0, 0, 0)
NEON_GREEN = (0, 255, 0)
RED = (255, 0, 0)
ORANGISH_YELLOW = (255, 200, 0)
BRIGHT_YELLOW = (255, 255, 0)
PURPLISH_BLUE = (128, 0, 128)
MIDTONE_GREEN = (0, 128, 0)

# Create the maze using a 2D array (scaled by 3x)
maze = [
    [1, 4, 1, 4, 1, 4, 1, 4, 1, 1, 4, 1, 4, 1, 1, 4, 1, 4, 1, 1, 1, 1, 1, 4, 1, 4, 4, 1, 1, 1],
    [1, 3, 4, 4, 1, 4, 1, 4, 1, 1, 4, 4, 4, 1, 1, 4, 1, 4, 1, 1, 1, 1, 1, 4, 1, 4, 1, 4, 4, 1],
    [1, 1, 1, 1, 1, 4, 1, 4, 1, 4, 4, 1, 1, 1, 1, 4, 1, 4, 1, 1, 1, 4, 4, 4, 1, 4, 1, 1, 1, 1],
    [1, 4, 1, 4, 1, 1, 1, 4, 1, 1, 1, 1, 4, 1, 1, 4, 1, 4, 1, 1, 4, 4, 1, 1, 1, 4, 1, 4, 4, 1],
    [1, 4, 1, 1, 1, 4, 4, 4, 4, 4, 1, 4, 4, 4, 1, 4, 1, 4, 4, 4, 1, 1, 1, 1, 1, 4, 4, 4, 1, 1],
    [1, 1, 1, 4, 1, 1, 1, 4, 1, 1, 1, 1, 2, 4, 1, 4, 1, 1, 1, 1, 4, 1, 1, 4, 1, 1, 1, 4, 1, 1],
    [1, 1, 1, 1, 1, 4, 4, 4, 4, 1, 4, 4, 4, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 1],
    [1, 1, 1, 4, 1, 4, 1, 1, 1, 1, 1, 1, 4, 1, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 4, 1],
    [1, 4, 1, 4, 1, 4, 1, 4, 4, 1, 4, 1, 4, 1, 1, 4, 1, 4, 1, 4, 1, 1, 1, 4, 1, 1, 1, 4, 1, 1],
    [1, 4, 4, 4, 1, 1, 1, 1, 4, 4, 4, 1, 4, 1, 1, 4, 4, 4, 4, 4, 1, 4, 4, 4, 1, 4, 1, 4, 4, 1],
    [1, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 1, 1, 1, 1]
    
   ]


# Define player position and size (scaled by 3x)
player_size = 20 * scale_factor
player_x, player_y = 20 * scale_factor, 20 * scale_factor

# Winning message
font = pygame.font.SysFont("", 90)
win_message_text = "333KA06071968"
win_message = font.render(win_message_text, True, RED)

# Define player win status
player_win = False

# ... (previous code)

# Function to handle touch events
def handle_touch_events():
    global player_x, player_y, start_x, start_y, player_win  # Declare player_x and player_y as global variables
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            start_x, start_y = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if not player_win:  # Only handle touch events if the player has not won
                end_x, end_y = event.pos
                # Calculate swipe distance and direction
                swipe_x = end_x - start_x
                swipe_y = end_y - start_y
                # Check if the swipe is vertical or horizontal and move the player accordingly
                if abs(swipe_x) > abs(swipe_y):
                    if swipe_x > 0 and maze[player_y // player_size][(player_x + player_size) // player_size] != 4:
                        player_x += player_size
                    elif swipe_x < 0 and maze[player_y // player_size][(player_x - player_size) // player_size] != 4:
                        player_x -= player_size
                else:
                    if swipe_y > 0 and maze[(player_y + player_size) // player_size][player_x // player_size] != 4:
                        player_y += player_size
                    elif swipe_y < 0 and maze[(player_y - player_size) // player_size][player_x // player_size] != 4:
                        player_y -= player_size

                # Keep the player within the game window boundaries
                player_x = max(player_size, min(player_x, window_width * scale_factor - player_size * 2))
                player_y = max(player_size, min(player_y, window_height * scale_factor - player_size * 2))

# ... (rest of the code)


# Main game loop
while True:
    handle_touch_events()  # Handle touch events

    # Fill the window with the background color
    window.fill(BLACK)

    # Draw the maze (scaled by 3x)
    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == 1:
                # Fill the path with black color
                pygame.draw.rect(window, BLACK, (x * player_size, y * player_size, player_size, player_size))
                # Draw the neon green outline for all cells
                pygame.draw.rect(window, NEON_GREEN, (x * player_size, y * player_size, player_size, player_size), 1)
            elif maze[y][x] == 2:
                # Draw the winning cell with orangish yellow fill and bright yellow outline
                pygame.draw.rect(window, ORANGISH_YELLOW, (x * player_size, y * player_size, player_size, player_size))
                pygame.draw.rect(window, BRIGHT_YELLOW, (x * player_size, y * player_size, player_size, player_size), 1)
            elif maze[y][x] == 3:
                # Draw the starting cell with purplish blue fill and neon green outline
                pygame.draw.rect(window, PURPLISH_BLUE, (x * player_size, y * player_size, player_size, player_size))
                pygame.draw.rect(window, NEON_GREEN, (x * player_size, y * player_size, player_size, player_size), 1)
            elif maze[y][x] == 4:
                # Draw the blockade cell with midtone green fill
                pygame.draw.rect(window, MIDTONE_GREEN, (x * player_size, y * player_size, player_size, player_size))

    # Draw the player as a red square
    pygame.draw.rect(window, RED, (player_x, player_y, player_size, player_size))

    # Check if the player reached the end point
    if (player_y + player_size // 2) // player_size < len(maze) and (player_x + player_size // 2) // player_size < len(maze[0]):
        if maze[(player_y + player_size // 2) // player_size][(player_x + player_size // 2) // player_size] == 2:
            player_win = True  # Player wins, set win status to True

    # If the player wins, display the winning message at the center of the screen
    if player_win:
        win_message_x = (window_width * scale_factor - win_message.get_width()) // 2 - 500
        win_message_y = (window_height * scale_factor - win_message.get_height()) // 2 - -500
        window.blit(win_message, (win_message_x, win_message_y))

    # Update the display
    pygame.display.update()
