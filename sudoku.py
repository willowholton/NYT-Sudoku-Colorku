import requests
import json
import matplotlib.pyplot as pyplot


url = "https://www.nytimes.com/puzzles/sudoku/"
page = requests.get(url)
text = page.text
search = "gameData = "
start = text.find(search) + len(search)
obj, end_idx = json.JSONDecoder().raw_decode(text, start)

colors = ['white', 'crimson','orange','gold','limegreen','darkgreen','lightskyblue','mediumblue','mediumpurple','rebeccapurple']
levels = ['easy', 'medium', 'hard']

date = obj['easy']['print_date']
puzzles = {}

for diff in levels:
    puzzles[diff] = [obj[diff]['puzzle_data']['puzzle'][i : i + 9] for i in range(0, 81, 9)]

for diff in levels:
    puzzle = puzzles[diff]
    file_path = 'puzzles/' + date + ' ' + diff + '.png'
    fig, ax = pyplot.subplots(figsize=(11,11))
    ax.set_aspect("equal")
    ax.set_axis_off()
    ax.set_xlim(0, 9)
    ax.set_ylim(0, 9)

    for i in range(10):
        if (i % 3 == 0):
            ax.plot([0,9], [i,i], color="black", linewidth=5)
            ax.plot([i,i], [0,9], color="black", linewidth=5)
        else: 
            ax.plot([0,9], [i,i], color="black", linewidth=1.5)
            ax.plot([i,i], [0,9], color="black", linewidth=1.5)

    for i in range(9):
        for j in range(9):
            value = puzzle[i][j]
            if (value != 0):
                circle = pyplot.Circle(xy=(j+0.5, 9-i-1+0.5), radius=0.25, color=colors[value], fill=True)
                ax.add_patch(circle)

    pyplot.savefig(file_path, bbox_inches='tight', pad_inches=0.25)