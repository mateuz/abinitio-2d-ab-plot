import sys
import csv

from src.plotter import Plotter


def load_csv(filename):
    data = []

    with open(filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            x = float(row[0])
            y = float(row[1])
            kind = 'a' == row[2].lower()

            data.append((x, y, kind))

    return data


def main(filename):
    data = load_csv(filename)

    plotter = Plotter(data)

    plotter.ball_radius = 8
    plotter.a_color = (1, 1, 1)
    plotter.b_color = (0, 0, 0)
    plotter.line_width = 3
    plotter.line_color = (0.486, 0.486, 0.529)

    plotter.render()
    plotter.save(name='prot.png')


if __name__ == "__main__":
    filename = sys.argv[1]
    main(filename)
