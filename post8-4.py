#I.G : @deeplearningindia
import re

txt = "I hope you all are having a great day"

#Check if the string ends with 'day':

x = re.findall("day$", txt)
if x:
  print("Yes, the string -->",txt," <--  ends with 'day'")
else:
  print("Better luck next time")
