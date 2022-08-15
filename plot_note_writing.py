import os
import re
from collections import Counter
from datetime import datetime

import plotext as plt
from rich import print

MONTH_AND_YEAR = "%b-%y"


def parse_notes() -> list[datetime]:
    """
    Parse the Zettelkasten and convert the zettel filenames to datetime objects.

    :returns: A list of datetime objects created based on the filenames for each zettle.
    """
    files = os.listdir("./zettel")
    note_format = re.compile(r"\d{12}(?:[a-z])?\.md")
    notes = [note.strip("a.md") for note in files if note_format.match(note)]
    return [datetime.strptime(note, "%Y%m%d%H%M") for note in sorted(notes)]


def build_axes(notes_time_series) -> tuple[list, list]:
    """
    Build the axes for the plot based on the month and year each note was written.

    :time_series: A list of datetime objects.
    :returns: A list for the x_axis containing the month and year for the notes in the zettelkasten.
        A list for the y_axis containing the counts of notes written in each month.
    """
    count_by_month = Counter(
        note.strftime(MONTH_AND_YEAR) for note in sorted(notes_time_series)
    )
    x_axis = count_by_month.keys()
    y_axis = count_by_month.values()
    return x_axis, y_axis


def plotter(
    x_axis: list,
    y_axis: list,
    foreground_color: str,
    background_color: str,
) -> None:
    plt.datetime.set_datetime_form(date_form=MONTH_AND_YEAR)
    plt.plot_date(x_axis, y_axis, marker="dot", color=foreground_color)
    plt.ticks_color(foreground_color)
    plt.plotsize(100, 30)
    plt.canvas_color(background_color)
    plt.axes_color(background_color)


if __name__ == "__main__":
    notes_time_series = parse_notes()
    x_axis, y_axis = build_axes(notes_time_series)
    print(f"\nYour Zettelkasten contains [b]{len(notes_time_series)}[/b] notes.\n")
    plt.clp()
    plotter(x_axis, y_axis, "black", "yellow")
    plt.title("Notes Written Per Month")
    plt.xlabel("Date")
    plt.show()
