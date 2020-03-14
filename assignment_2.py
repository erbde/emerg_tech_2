#%%

from string import punctuation
import pandas as pd

# %%
f = open("shakes.txt", "r+", encoding="UTF-8")
shakes = f.read()
f.close()
# %%
def tokenizer(document: str, punct_to_remove: str):
    new_doc = document.replace("\n"," ", -1)
    punct_to_remove = list(punct_to_remove)
    for i in punct_to_remove:
        new_doc = new_doc.replace(i, "", -1)
    new_doc = new_doc.lower()
    new_doc = new_doc.split()
    return new_doc

# %%
new_shakes = tokenizer(document = shakes, punct_to_remove = punctuation)


# %%
x = lambda a : a + 10
print(x(5))
#%%
def myfunc(n):
    return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))

# %%
scifi_authors = ["Isaac Asimov", "Ray Bradbury", "Robert Heinlein", "Arthur C. Clark", "Frank Herbert", "Orson Scott Card", "Douglas Adams", "H. G. Wells", "Leigh Brackett"]
scifi_authors.sort(key=lambda name: name.split(" ")[-1].lower())

# %%
