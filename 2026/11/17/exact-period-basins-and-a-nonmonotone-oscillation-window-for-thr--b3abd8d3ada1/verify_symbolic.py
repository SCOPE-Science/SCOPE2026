"""Finite complete certificate for threshold-two three-colour cyclic automata.
Run with Python >= 3.9; only the Python standard library is required.

The six entries denote truncated colour class sizes (0,1,2 meaning 2 or more).
The six origin tags follow the exact colours of the initially monochromatic
vertex groups, including when several groups merge. Zero groups are ignored.
"""
from itertools import product
from collections import Counter


def advance(s, tags):
    s_next = [0] * 6
    tags_next = [0] * 6
    for side in (0, 1):
        targets = tuple((c + int(s[3 * (1 - side) + (c + 1) % 3] == 2)) % 3
                        for c in range(3))
        for c in range(3):
            idx = 3 * side + targets[c]
            s_next[idx] = min(2, s_next[idx] + s[3 * side + c])
        for c in range(3):
            origin = 3 * side + c
            assert tags[origin] // 3 == side
            tags_next[origin] = 3 * side + targets[tags[origin] % 3]
    return tuple(s_next), tuple(tags_next)


def normalized(snapshot, origin):
    s, tags = snapshot
    return s, tuple(tags[i] if origin[i] else -1 for i in range(6))


def classify(origin):
    seq = [(origin, tuple(range(6)))]
    for _ in range(15):
        seq.append(advance(*seq[-1]))
    seq = [normalized(x, origin) for x in seq]
    assert seq[3] == seq[15], ('unbounded orbit', origin)
    p = next((p for p in (1, 2, 3, 4)
              if all(seq[t] == seq[t + p] for t in range(3, 16 - p))), None)
    assert p in (1, 3, 4), ('unexpected period', origin, p)
    return p, seq


def main():
    periods = Counter()
    table = Counter()
    e3 = 0
    period_three = set()
    for origin in product(range(3), repeat=6):
        p, seq = classify(origin)
        periods[p] += 1
        if p == 3:
            period_three.add(origin)
        if p == 4:
            typ = lambda side: ''.join(map(str, sorted(origin[side:side + 3])))
            table[(typ(0), typ(3))] += 1
        if seq[2] != seq[2 + p]:
            e3 += 1
    expected = {1: 666, 3: 15, 4: 48}
    assert dict(periods) == expected, periods
    expected_three = {(2,2,2,2,2,2)} | {(2,2,2,*epsilon) for epsilon in product((0,1), repeat=3) if any(epsilon)} | {(*epsilon,2,2,2) for epsilon in product((0,1), repeat=3) if any(epsilon)}
    assert period_three == expected_three, (period_three, expected_three)
    assert table == Counter({
        ('022','022'):6, ('022','122'):6, ('122','022'):6,
        ('122','122'):6,
        ('022','112'):3, ('112','022'):3,
        ('122','112'):3, ('112','122'):3,
        ('022','222'):3, ('222','022'):3,
        ('122','222'):3, ('222','122'):3,
    }), table
    print('all 729 truncated signatures: PASS')
    print('F^15 = F^3 for all labelled configurations: PASS')
    print('period signatures: fixed=666 period3=15 period4=48')
    print('15 period-three signatures match the full high-high/one-side-low classification: PASS')
    print('period-four type-pair multiplicities:', sorted(table.items()))
    print('symbolic signatures that require the third update:', e3)

if __name__ == '__main__':
    main()
