import sys

file = ""

if len(sys.argv) < 2:
	file = input("File to interpret? ")
else:
	file = sys.argv[1]

file = open(file, "r")

script = file.read()

file.close()

script = script.replace("\n", "")
script = script.split(" ")

fishnum = 0

for char in script:
  if char == "<><":
    fishnum += 1
  elif char == "><>":
    print(chr(fishnum), end = "")
    fishnum = 0
  elif char == "~":
    fishnum *= 2
