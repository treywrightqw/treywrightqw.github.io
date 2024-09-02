from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/square_button_clicked', methods=['POST'])
def square_button_clicked():
    print("Square button clicked!")
    return 'Square button clicked!'

@app.route('/rounded_button_clicked', methods=['POST'])
def rounded_button_clicked():
    print("Rounded button clicked!")
    return 'Rounded button clicked!'

@app.route('/triangle_button_clicked', methods=['POST'])
def triangle_button_clicked():
    print("Triangle button clicked!")
    return 'Triangle button clicked!'

@app.route('/playgame', methods=['GET', 'POST'])
def playgame():
    return render_template('playgame.html')

@app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run()

"""import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to generate a random color
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Function to draw a random shape at a random position
def draw_random_shape(surface, rect_list):
    shape_type = random.choice(["rectangle", "circle", "triangle"])

    if shape_type == "rectangle":
        rect_width = random.randint(20, 100)
        rect_height = random.randint(20, 100)
        rect = pygame.Rect(random.randint(0, WIDTH - rect_width), random.randint(0, HEIGHT - rect_height), rect_width, rect_height)
        pygame.draw.rect(surface, random_color(), rect)
        rect_list.append(rect)
    elif shape_type == "circle":
        circle_radius = random.randint(10, 50)
        circle_pos = (random.randint(circle_radius, WIDTH - circle_radius), random.randint(circle_radius, HEIGHT - circle_radius))
        pygame.draw.circle(surface, random_color(), circle_pos, circle_radius)
        rect_list.append(pygame.Rect(circle_pos[0] - circle_radius, circle_pos[1] - circle_radius, circle_radius * 2, circle_radius * 2))
    elif shape_type == "triangle":
        x1, y1 = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        x2, y2 = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        x3, y3 = random.randint(0, WIDTH), random.randint(0, HEIGHT)
        pygame.draw.polygon(surface, random_color(), [(x1, y1), (x2, y2), (x3, y3)])
        min_x = min(x1, x2, x3)
        max_x = max(x1, x2, x3)
        min_y = min(y1, y2, y3)
        max_y = max(y1, y2, y3)
        rect_list.append(pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y))

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Randomly Generated Shapes")
clock = pygame.time.Clock()

# List to store rectangles representing shapes
rectangles = []

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click is inside any shape
            mouse_pos = pygame.mouse.get_pos()
            for rect in rectangles:
                if rect.collidepoint(mouse_pos):
                    print("Clicked on a shape!")

    # Fill the background with white
    screen.fill(WHITE)

    # Draw randomly generated shapes to fill the entire window
    draw_random_shape(screen, rectangles)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
sys.exit()"""
