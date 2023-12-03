from collections import defaultdict

I = open('input.txt').read().strip()
p1 = 0
p2 = 0
for line in I.split("\n"):
    ok = True
    id_, line = line.split(":")
    D = defaultdict(int)
    for event in line.split(";"):
        for box in event.split(","):
            n, col = box.split()
            if int(n) > D[col] or D[col] == 0:
                D[col] = int(n)
            if int(n) > {"red": 12, "green": 13, "blue": 14}.get(col):
                ok = False
    score = 1
    for V in D.values():
        score *= V
    p2 += score
    if ok:
        p1 += int(id_.split()[-1])
print(p1)
print(p2)
