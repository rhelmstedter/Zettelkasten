from datetime import datetime
from collections import Counter
import os
import re
from rich import print
import plotext as plt


def parse_notes():
    files = os.listdir("./zettel")
    note_format = re.compile(r"\d{12}(?:[a-z])?\.md")
    notes = [note.strip("a.md") for note in files if note_format.match(note)]
    return [datetime.strptime(note, "%Y%m%d%H%M") for note in sorted(notes)]


def build_axes(time_series):
    count_by_month = Counter(
        [note.strftime("%b %Y") for note in sorted(time_series)]
    )
    x_axis = []
    y_axis = []
    for date, count in count_by_month.items():
        x_axis.append(date)
        y_axis.append(count)
    return x_axis, y_axis


def plotter(x, y, foreground_color, background_color):
    plt.datetime.set_datetime_form(date_form="%b %Y")
    plt.plot_date(x, y, marker="dot", color=foreground_color)
    plt.ticks_color(foreground_color)
    plt.plotsize(88, 30)
    plt.canvas_color(background_color)
    plt.axes_color(background_color)


if __name__ == "__main__":
    notes = parse_notes()
    x_axis, y_axis = build_axes(notes)
    print(f"\nYour Zettelkasten contains [b]{len(notes)}[/b] notes.\n\n")
    plt.clp()
    plotter(x_axis, y_axis, "black", "yellow")
    plt.title("Notes Written Per Month")
    plt.xlabel("Date")
    plt.show()
