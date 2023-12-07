from collections import defaultdict

I = open('input.txt').read().strip()

# I = ('Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\n'
#      'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\n'
#      'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\n'
#      'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\n'
#      'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\n'
#      'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11')

p1 = 0
p2 = 0
vals = defaultdict(int)
cp_reg = []
for line in I.split("\n"):
    cards = line.split(":").pop(1).split("|")
    id = int(line.split()[1][:-1])
    v = 0
    win_cnt = 0
    cp_cnt = cp_reg.count(id)
    for win_c in [int(card_n) for card_n in cards[0].split()]:
        if any(filter(lambda card_n: card_n == win_c, [int(card_n) for card_n in cards[1].split()])):
            win_cnt += 1
            if v == 0:
                v += 1
            else:
                v *= 2
    p1 += v
    vals[id] = v
    for n in range(cp_cnt + 1):
        for cp in range(id + 1, id + win_cnt + 1):
            cp_reg.append(cp)
    p2 += cp_cnt + 1
print(p1)
print(p2)
