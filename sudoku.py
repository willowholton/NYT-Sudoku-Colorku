import requests
import re
import matplotlib.pyplot as pyplot


url = "https://www.nytimes.com/puzzles/sudoku/"
page = requests.get(url)


gamedata = page.text.split("gameData =")[1].split("}}}</script>")[0]


date = re.search(r'"print_date":"(\d{4}-\d{2}-\d{2})', gamedata).group(1)
puzzles = re.findall(r'"puzzle":\[([\d,]{161})', gamedata)

easy = [int(i) for i in puzzles[0].split(",")]
easy_puzzle = [easy[i : i + 9] for i in range(0, 81, 9)]
medium = [int(i) for i in puzzles[2].split(",")]
medium_puzzle = [medium[i : i + 9] for i in range(0, 81, 9)]
hard = [int(i) for i in puzzles[1].split(",")]
hard_puzzle = [hard[i : i + 9] for i in range(0, 81, 9)]

all_puzzles = [easy_puzzle, medium_puzzle, hard_puzzle]
colors = ['white', 'crimson','orange','gold','limegreen','darkgreen','lightskyblue','mediumblue','mediumpurple','rebeccapurple']
diff = ['easy', 'medium', 'hard']

for i in range(3):
    puzzle = all_puzzles[i]
    file_path = 'puzzles/' + date + ' ' + diff[i] + '.png'
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