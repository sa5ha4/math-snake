import tkinter
import random
import operator

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * COLS
WINDOW_HEIGHT = TILE_SIZE * ROWS

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#game window
window = tkinter.Tk()
window.title("snake")
window.resizable(False, False)

canvas = tkinter.Canvas(window, bg = "black", width = WINDOW_WIDTH, height = WINDOW_HEIGHT)
canvas.pack()
window.update()

#center the window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int((screen_width/2) - (window_width/2))
window_y = int((screen_height/2) - (window_height/2))
#format "(w)x(h)+(x)+(y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

#initialize game
snake = Tile(12*TILE_SIZE, 18*TILE_SIZE) #single tile, snake's head
food = Tile(10*TILE_SIZE, 7*TILE_SIZE)
box_1 = Tile(4*TILE_SIZE, 8*TILE_SIZE)
box_2 = Tile(11*TILE_SIZE, 8*TILE_SIZE) 
box_3 = Tile(18*TILE_SIZE, 8*TILE_SIZE) 
snake_body = [] #multiple snake tiles
velocityX = 0
velocityY = 0
game_over = False
score = 0
num_1 = random.randint(1, 10)
num_2 = random.randint(1, 10)
num_3 = random.randint(1, 20)
num_4 = random.randint(1, 20)
operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv,}
operation = random.choice(list(operators.keys()))
answer = operators.get(operation)(num_1, num_2)
variants = {num_3, num_4, answer}
variant1 = random.choice(list(variants))
variant2 = random.choice(list(variants))
variant3 = random.choice(list(variants))

def change_direction(e): #e = event
    # print(e)
    # print(e.keysym)
    global velocityX, velocityY, game_over
    if (game_over):
        return
    
    if (e.keysym == "Up" and velocityY != 1):
        velocityX = 0
        velocityY = -1
    elif (e.keysym == "Down" and velocityY != -1):
        velocityX = 0
        velocityY = 1
    elif (e.keysym == "Left" and velocityX != 1):
        velocityX = -1
        velocityY = 0
    elif (e.keysym == "Right" and velocityX != -1):
        velocityX = 1
        velocityY = 0

def move():
    global snake, food, snake_body, game_over, score, box_1, box_2, box_3, variant1, variant2, variant3
    if (game_over):
        return

    if (snake.x < 0 or snake.x >= WINDOW_WIDTH or snake.y < 0 or snake.y >= WINDOW_HEIGHT):
        game_over = True

    for tile in snake_body:
        if (snake.x == tile.x and snake.y == tile.y):
            game_over = True
            return

     #collision
    if (snake.x == box_1.x, box_2.x, box_3.x == answer and snake.y == box_1.y, box_2.y, box_3.y == answer):
        snake_body.append(Tile(food.x, food.y))
        score += 1
    else:
        snake.x == box_1.x, box_2.x, box_3.x != answer and snake.y == box_1.y, box_2.y, box_3.y != answer
    
    
    #update snake body
    for i in range(len(snake_body)-1, -1, -1):
        tile = snake_body[i]
        if (i == 0):
            tile.x = snake.x
            tile.y = snake.y
        else:
            prev_tile = snake_body[i-1]
            tile.x = prev_tile.x
            tile.y = prev_tile.y

    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE


def draw():
    global snake, food, snake_body, game_over, score, box_1, box_2, box_3, variant1, variant2, variant3
    move()

    canvas.delete("all")

    #draw food
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill = "black")


    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill = "#67c94f")

    #draw problem
    canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/5, font = "ComicNeue 20", text = f'What is {num_1} {operation} {num_2}', fill = "#fff8f0")

    #draw variants
    canvas.create_rectangle(box_1.x, box_1.y, box_1.x + TILE_SIZE*3, box_1.y + TILE_SIZE*3, fill = "red")
    canvas.create_text(box_1.x + TILE_SIZE*1.5, box_1.y + TILE_SIZE*1.5, font = "ComicNeue 20", text = {variant1}, fill = "#fff8f0")

    canvas.create_rectangle(box_2.x, box_2.y, box_2.x + TILE_SIZE*3, box_2.y + TILE_SIZE*3, fill = "red")
    canvas.create_text(box_2.x + TILE_SIZE*1.5, box_2.y + TILE_SIZE*1.5, font = "ComicNeue 20", text = {variant3}, fill = "#fff8f0")

    canvas.create_rectangle(box_3.x, box_3.y, box_3.x + TILE_SIZE*3, box_3.y + TILE_SIZE*3, fill = "red")
    canvas.create_text(box_3.x + TILE_SIZE*1.5, box_3.y + TILE_SIZE*1.5, font = "ComicNeue 20", text = {variant3}, fill = "#fff8f0")

    #draw snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill = "#67c94f")

    if (game_over):
        canvas.create_text(WINDOW_WIDTH/2, WINDOW_HEIGHT/2, font = "ComicNeue 20", text = f"Game Over: {score}", fill = "#fff8f0")
    else:
        canvas.create_text(30, 20, font = "ComicNeue 10", text = f"score: {score}", fill = "#fff8f0")
    


    window.after(100, draw) #100ms = 1/7 second, 7 frames/second

draw()

window.bind("<KeyRelease>", change_direction)

window.mainloop()