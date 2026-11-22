"""Independent complete priority-order enumeration; only Python standard library.
For each pair position among ten clocks, enumerate every ordering of the eight
ordinary vertices, then sum exact probabilities of the ranked exponential clocks.
"""
from fractions import Fraction
from itertools import combinations, permutations

V = list(combinations(range(5), 2))
closed = []
for i, a in enumerate(V):
    closed.append(sum(1 << j for j, b in enumerate(V)
                      if i == j or set(a).isdisjoint(b)))

def rank_table(second):
    ordinary = [i for i in range(10) if i not in (0, second)]
    counts = [[0]*10 for _ in range(10)]
    total = 0
    for perm in permutations(ordinary):
        for first_pos in range(10):
            for second_pos in range(10):
                if first_pos == second_pos:
                    continue
                pos = 0
                blocked = 0
                selected = 0
                for t in range(10):
                    if t == first_pos:
                        vertex = 0
                    elif t == second_pos:
                        vertex = second
                    else:
                        vertex = perm[pos]
                        pos += 1
                    if not (blocked & (1 << vertex)):
                        blocked |= closed[vertex]
                        selected += 1
                assert selected in (3, 4)
                counts[first_pos][second_pos] += (selected == 4)
                total += 1
    assert total == 3628800
    return counts

def exact_probability_four(counts, x, y):
    x, y = Fraction(x), Fraction(y)
    answer = Fraction(0)
    for first_pos in range(10):
        for second_pos in range(10):
            if first_pos == second_pos:
                continue
            weights = [Fraction(1)]*10
            weights[first_pos] = x
            weights[second_pos] = y
            remaining = x + y + 8
            priority_probability = Fraction(1)
            for w in weights:
                priority_probability *= w / remaining
                remaining -= w
            answer += counts[first_pos][second_pos]*priority_probability
    return answer

cases = [(Fraction(1),Fraction(1)),(Fraction(2),Fraction(3)),
         (Fraction(1,2),Fraction(4,3)),(Fraction(7,5),Fraction(11,3)),
         (Fraction(5),Fraction(2)),(Fraction(1,7),Fraction(2,11))]
for second, coefficient in [(7,4),(1,-2)]:
    counts=rank_table(second)
    assert sum(sum(row) for row in counts)==2419200
    for x,y in cases:
        calculated=exact_probability_four(counts,x,y)
        expected=(Fraction(2,3) + coefficient*(x-1)*(y-1) /
                 (3*(x+2)*(y+2)*(x+y+1)*(x+y+8)))
        assert calculated==expected,(second,x,y,calculated,expected)
    print(('adjacent' if coefficient==4 else 'nonadjacent'),
          '8! x 90 orders, 6 rational pairs: PASS')
print('INDEPENDENT PRIORITY CERTIFICATE PASS')
