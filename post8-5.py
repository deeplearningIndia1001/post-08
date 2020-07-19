#I.G : @deeplearningindia
import re

txt = "Not all those who wander are Lost..."
"""Check if the string contains "a" followed by exactly two
 "l" characters: """
x = re.findall("al{2}", txt)

print(x)
if x:
  print("Yes, there is at least one match!")
else:
  print("Better luck next time")