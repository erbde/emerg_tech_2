#%%

from string import punctuation
import pandas as pd
import re

# %%
f = open("shakes.txt", "r+", encoding="UTF-8")
# %%
shakes = f.read()
f.close()
shakes_words = shakes.split()
#%%
punct_list = list(punctuation)

# %%
#table = print(shakes.maketrans(x = "", y = "", z = punctuation))
print(shakes.maketrans(shakes,shakes,punctuation))

# %%
new_shakes = shakes
new_shakes = new_shakes.replace("\n", " ", -1)
for i in punct_list:
    new_shakes = new_shakes.replace(i, "", -1)
# %%
new_shakes = new_shakes.lower()
print(new_shakes)
# %%
