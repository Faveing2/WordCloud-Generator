from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import ImageColor
import colorsys
from os import path

import pandas

#### Documentation for Worldcloud, https://github.com/amueller/word_cloud/tree/main

FILEPATH = "Perceptions and Portrayals of Scientists and Engineers in Media (Responses) - Word Cloud People.csv"
USE_COLOR = True
SCALING = .5

TRANSPARENT = False
BACKGROUND = "White"
MODE = "RGB"

OUTPUT = "wordcloud.png"






data_people = pandas.read_csv(FILEPATH)

if TRANSPARENT:
    MODE = "RGBA"
    BACKGROUND = None

word_frequencies = {}
word_colors = {}

#data_people.set_index("Name", inplace=True)

def custom_color_func(word, font_size, position, orientation, random_state, font_path):

    index = data_people.index[data_people['Name'] == word]
    color = str(data_people.iloc[index]["COLOR"].iloc[0])
    r, g, b = ImageColor.getrgb(color)
    return 'rgb({}, {}, {})'.format(r,g,b)


for index, person in enumerate(data_people["Name"]):
    word_frequencies[person] = data_people["Number of mentions"][index]
    word_colors[person] = data_people["COLOR"][index]
### Generate the wordcloud


wc = WordCloud(background_color=BACKGROUND,mode=MODE, width=1000, height=1000, max_words=len(word_frequencies), relative_scaling=SCALING)
wc.generate_from_frequencies(word_frequencies)

if USE_COLOR:
    wc.recolor(color_func=custom_color_func)

plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.show()

wc.to_file(OUTPUT)