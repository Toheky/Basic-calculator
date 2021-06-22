import time
import pygame as pg
from evaluation import * 
from labels import Label
from buttons import Button
from constants import barrier, S

def buttons_labels(x, y, font, button_group, label_group, symbols, path):
    '''Create buttons and labels.'''
    for row in range(3):
        for col in range(7):
            button = Button(x, y, path)
            label = Label(font, symbols[row][col], (x+12, y+3), (255,255,255))
            button_group.add(button)
            label_group.append(label)
            x += 57.143
        y += 50
        x = 10

def main():
    '''Main function for initializate the interfaces and functions.'''
    pg.init()

    #List with symbols per button
    symbols = [["L", "√", "^", "C", "P", "!", "0"],
               ["s", "c", "t", "g", "l", "m", "<"],
               ["π", "e", "τ", "Σ", "Π", "l", "ƒ"]]

    shortcuts = []
    
    #Screen settings
    W, H = 400, 400 
    screen = pg.display.set_mode((W, H))
    pg.display.set_caption("Calculator")
    running = True

    logo = pg.image.load("imgs/logo.png")
    pg.display.set_icon(logo) 

    base_font = pg.font.SysFont("Consolas", 24)

    #Eval operations
    user_text = ""
    result_text = ""

    #Mark of the display
    dsp = pg.image.load("imgs/display.png").convert()
    input_rect = dsp.get_rect(topleft=(10, 20))

    #Save buttons
    button_group = pg.sprite.Group()

    #Save labels
    label_group = []

    #Button and label generator
    path = "C:/Users/tix4t/Desktop/Projects/Projects/Basic calculator/imgs/sprites_button"
    buttons_labels(10, 250, base_font, button_group, label_group, symbols, path)

    #Flag for keep pressed key
    pressed_back = False
    pressed_right = False
    pressed_left = False

    #Switch button for radians and degrees
    switch_button = Button(10, 200, path)
    button_group.add(switch_button)
    active = 1

    #Label for switch button
    label_switch = Label(base_font, "Θ", (23, 204), (255,255,255))

    #Title convertion
    title_bin = Label(base_font, "BIN", (15, 140), (81, 156, 93))
    switch_conversion = 1

    #Cursor for search mode
    pse_cursor = pg.Rect(15, 26, 13, 30)
    key_cursor = True

    #Save the index position of the cursor
    current_index = 0

    #Save last result
    control = ""

    while running: 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.MOUSEBUTTONDOWN:
                for item in button_group:
                    user_text += item.check_click(event.pos, user_text, control)

                if switch_button.rect.collidepoint(event.pos):
                    switch_button.animate()
                    active = -active    

                if 352 < event.pos[0] < 392 and 350 < event.pos[1] < 383:
                    switch_conversion = -switch_conversion

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    pressed_back = True
                elif event.key == pg.K_RETURN or event.key == pg.K_KP_ENTER:
                    #evaluate and save the result in result_text
                    control = result_text = str(evaluate(user_text, active))

                elif event.key == pg.K_TAB:
                    #active mode search
                    key_cursor = not key_cursor
                elif not key_cursor and event.key == pg.K_RIGHT:
                    #move cursor to the right
                    pressed_right = True
                    
                elif not key_cursor and event.key == pg.K_LEFT:
                    #move cursor to the left
                    pressed_left = True
                    
                elif not key_cursor and event.key == pg.K_DOWN:
                    #delete characters
                    user_text = "".join([user_text[i] for i in range(len(user_text)) if i != current_index])
                    barrier.x -= 13
                elif not key_cursor and barrier.x < 365:
                    #add characters
                    barrier.x += S
                    user_text = user_text[:current_index] + event.unicode + user_text[current_index:]
                    current_index += 1
                    pse_cursor.x += S

                #shortcuts
                elif event.key == pg.K_s and barrier.x < 365:
                    user_text += "sin("
                    barrier.x += S*4
                elif event.key == pg.K_c and barrier.x < 365:
                    user_text += "cos("
                    barrier.x += S*4
                elif event.key == pg.K_t and barrier.x < 365:
                    user_text += "tan("
                    barrier.x += S*4
                elif event.key == pg.K_r and barrier.x < 365:
                    user_text += "√("
                    barrier.x += S*2
                elif event.key == pg.K_g and barrier.x < 365:
                    user_text += "gcd("
                    barrier.x += S*4
                elif event.key == pg.K_l and barrier.x < 365:
                    user_text += "log("
                    barrier.x += S*4
                elif event.key == pg.K_p and barrier.x < 365:
                    user_text += "π"
                    barrier.x += S
                elif event.key == pg.K_z and barrier.x < 365:
                    user_text += "Σ("
                    barrier.x += S*2
                elif event.key == pg.K_f and barrier.x < 365:
                    user_text += "!"
                    barrier.x += S
                elif event.key == pg.K_p and barrier.x < 365:
                    user_text += "π"
                    barrier.x += S
                elif event.key == pg.K_a and barrier.x < 365:
                    user_text += "pow("
                    barrier.x += S*4
                elif event.key == pg.K_x and barrier.x < 365:
                    user_text += "τ"
                    barrier.x += S
                elif event.key == pg.K_q:
                    user_text += ""
                    barrier.x -= 5000

                elif event.key == pg.K_LSHIFT or event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
                    pass
                elif barrier.x < 365:
                    #write text in the screen
                    user_text += event.unicode
                    barrier.x += S
                    
            elif event.type == pg.KEYUP:
                if event.key == pg.K_BACKSPACE:
                    pressed_back = False
                if event.key == pg.K_RIGHT:
                    pressed_right = False
                if event.key == pg.K_LEFT:
                    pressed_left = False

        if pressed_back:
            time.sleep(0.087)
            #clear by one character
            user_text = user_text[:-1]
            barrier.x -= 13
            if barrier.x < pse_cursor.x and pse_cursor.x > 15:
                pse_cursor.x -= 13 
                current_index -= 1
            if user_text == "":
                result_text = ""

        if pressed_right:
            time.sleep(0.087)
            if current_index < len(user_text)-1:
                current_index += 1
                pse_cursor.x += S

        elif pressed_left:
            time.sleep(0.087)
            if current_index > 0:   
                current_index -= 1
                pse_cursor.x -= 13

        if barrier.x < 2:
            #reset screen
            barrier.x = 2
            current_index = 0
            pse_cursor.x = 15
            user_text = ""
            result_text = ""

        screen.fill((49,49,49))

        #display
        screen.blit(dsp, input_rect)

        if switch_conversion < 0:
            screen.blit(title_bin.txt, title_bin.pos)
            if "0b" not in result_text and len(result_text) > 0:
                result_text = bin(int(result_text))
        else:
            if "0b" in result_text and len(result_text) > 0:
                result_text = str(int(result_text[2:], 2))

        if not key_cursor:
            #active pseudo-cursor
            pg.draw.rect(screen, (252, 141, 141), pse_cursor)
        elif barrier.x >= 400:
            barrier.x = len(user_text)*13

        pg.draw.rect(screen, (25, 25, 25), barrier)

        text_surface = base_font.render(user_text, 1, (2,2,2))
        result = base_font.render(result_text, 1, (2,2,2))

        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 8))
        screen.blit(result, (input_rect.x + 5, input_rect.y + 145))

        button_group.draw(screen)
        button_group.update()

        for item in label_group:
            #blit each label
            screen.blit(item.txt, item.pos)

        #screen.blit(switch_button.image, switch_button.rect)
        screen.blit(label_switch.txt, label_switch.pos)

        pg.display.flip() 

if __name__ == "__main__":
    main()