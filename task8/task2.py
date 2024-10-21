philosophical_text = open("zen.txt", "r")
lines = philosophical_text.readlines()
philosophical_text.close()
for line in reversed(lines):
    print(line.strip())