#I.G : @deeplearningindia
import re
txt = "Hello from deeplearningindia. How are You."

"""Find all lower case characters alphabetically between 
"h" and "p" """
x = re.findall("[h-p]", txt)

print(x)

