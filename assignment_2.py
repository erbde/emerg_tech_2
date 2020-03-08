#%%

from string import punctuation
import pandas as pd
import re

# %%
f = open("shakes.txt", "r+", encoding="UTF-8")
# %%
shakes = f.read() 
# %%
f.close()
# %%
shakes_words = shakes.split()
#%%
punct_list = punctuation.split(sep="", maxsplit=-1)
punct_list = punctuation.split(sep="", maxsplit=-1)
punctuation.
# %%
#table = print(shakes.maketrans(x = "", y = "", z = punctuation))
print(shakes.maketrans(shakes,shakes,punctuation))

# %%
shakes.replace(punctuation,"",)
# %%
help(replace)

# %%
