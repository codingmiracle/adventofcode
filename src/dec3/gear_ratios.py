I = open('input.txt').read().strip()
#I = "467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598.."
p1 = 0
lines = I.split("\n")
for id in range(len(lines)):
    num = ""
    n_start = 0
    n_end = 0
    for n in range(len(lines[id])):
        c = lines[id][n]
        if c.isdigit():
            if num == "":
                n_start = n
            num += c
        elif num != "":
            n_end = n - 1
            if (
                    any(filter(lambda s: not s.isalnum() and s != ".", lines[max(id - 1, 0)][max(n_start - 1, 0):min(n_end + 2, len(lines[max(id - 1, 0)]))])) or
                    any(filter(lambda s: not s.isalnum() and s != ".", lines[id][max(n_start - 1, 0):min(n_end + 2, len(lines[id]))])) or
                    any(filter(lambda s: not s.isalnum() and s != ".", lines[min(id + 1, len(lines)-1)][max(n_start - 1, 0):min(n_end + 2, len(lines[min(id + 1, len(lines)-1)]))]))
            ):
                p1 += int(num)
            num = ""
print(p1)
