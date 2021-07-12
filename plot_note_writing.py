from datetime import datetime
from collections import Counter
import os
import re
import plotext as plt

files = os.listdir('./zettel')
note_format = re.compile(r"\d{12}(?:[a-z])?\.md")
notes = [note.strip('a.md') for note in files if note_format.match(note)]

notes_time_series = [datetime.strptime(note, "%Y%m%d%H%M") for note in sorted(notes)]
count_by_month = Counter([note.strftime('01/%m/%Y') for note in sorted(notes_time_series)])

x_axis = []
y_axis = []
for date, count in count_by_month.items():
    x_axis.append(plt.string_to_time(date))
    y_axis.append(count)

x_labels = "Dec 2020,Jan 2021,Feb 2021,Mar 2021,Apr 2021,May 2021,Jun 2021,Jul 2021".split(',')

print(f'Your Zettelkasten contains {len(notes)} notes.', end='\n\n')

plt.clp()
plt.plot(x_axis, y_axis, marker="dot", color='white')
plt.xticks(x_axis, x_labels)
plt.title("Notes Written Per Month")
plt.xlabel("Date")
plt.ticks_color('white')
plt.plotsize(87, 30)
plt.canvas_color('blue')
plt.axes_color('blue')
plt.show()
