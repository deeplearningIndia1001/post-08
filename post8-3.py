#I.G : @deeplearningindia
import re

txt = "Hello from deeplearningindia. How are You Heppo."

"""Search for a sequence that starts with "he", followed by
any two characters, and an "o" in last """

x = re.findall("He..o", txt)
print(x)
