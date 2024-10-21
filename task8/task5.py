import zipfile

with zipfile.ZipFile("voina-i-mir.zip", "r") as zip_ref:
    file_name = [name for name in zip_ref.namelist() if name.endswith('.txt')][0]
    with zip_ref.open(file_name) as file: text = file.read().decode('utf-8')
char_count = {}
for char in text:
    if char.isalpha():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
sorted_chars = sorted(char_count.items(), key=lambda x: (-x[1], x[0]))
with open("result.txt", "w", encoding="utf-8") as file:
    for char, freq in sorted_chars:
        file.write(f"{char}: {freq}\n")