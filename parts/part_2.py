from nicegui import ui
from random import shuffle

# TODO 1: Create list of 8 unique emojis, duplicate, and shuffle
EMOJIS = ['🐶', '🐱', '🐭', '🐹', '🐰', '🦊', '🐻', '🐼']
EMOJIS = EMOJIS * 2
shuffle(EMOJIS)

buttons = []
opened = [] # indices of currently flipped cards
matched = [] # indices of solved cards

# TODO 2: Write function to flip non-matching cards back
def reset_pair(i, j):
    buttons[i].set_text('')
    buttons[j].set_text('')
    opened.clear()

# TODO 3: Write click handler
def handle_click(idx):
    if idx in matched or idx in opened:
        return

    # If no cards open, open the first
    if len(opened) == 0:
        buttons[idx].set_text(EMOJIS[idx])
        opened.append(idx)

    # If one card open, open the second
    elif len(opened) == 1:
        buttons[idx].set_text(EMOJIS[idx])
        opened.append(idx)
        i, j = opened
        # Check for match
        if EMOJIS[i] == EMOJIS[j]:
            matched.extend([i, j])
            opened.clear()
            if len(matched) == len(EMOJIS):
                ui.label("You win!").classes('text-3xl text-center font-bold mt-4')
        # No match, schedule flip-back
        else:
            ui.timer(0.5, lambda i=i, j=j: reset_pair(i, j), once=True)

# Build 4x4 grid
with ui.grid(columns=4):
    # TODO 4: Create 16 buttons
    for i in range(16):
        button = ui.button('', on_click=lambda idx=i: handle_click(idx)).classes('w-20 h-20 text-3xl')
        buttons.append(button)

ui.run(title='Memory Game')
