"""Exact-arithmetic verification of four short list-two deletion codes.

Run: python3 verify.py
Only Python's standard library is required.
"""
from collections import Counter
from itertools import product

CODES = {
    4: "000 003 032 111 113 120 122 130 201 222 231 233 302 333".split(),
    5: "000 004 012 022 033 104 111 130 132 211 222 230 240 243 314 333 342 403 421 441 444".split(),
    8: "000 012 041 044 072 075 105 111 112 133 146 167 206 214 222 235 237 247 260 300 315 333 342 364 370 403 421 444 455 463 510 532 536 540 547 555 562 603 625 651 661 666 677 706 713 722 731 745 764 777".split(),
}

def cyclic_six():
    words = []
    for a in range(6):
        words.extend([f"{a}{a}{a}", f"{a}{a}{(a+2)%6}"])
        words.extend(f"{a}{(a+b)%6}{(a+c)%6}"
                     for b, c in [(1, 2), (4, 3), (5, 3)])
    return sorted(words)

CODES[6] = cyclic_six()


def descendants(w):
    # Set: two deletion positions that produce one output count just once.
    return {w[:i] + w[i + 1:] for i in range(3)}


def adjacency_triangle(words, triple):
    assert len(set(triple)) == 3 and set(triple) <= set(words)
    for i in range(3):
        assert descendants(triple[i]) & descendants(triple[(i + 1) % 3])


def test():
    for q in [4, 5, 6, 8]:
        words = CODES[q]
        assert len(set(words)) == len(words)
        assert all(len(w) == 3 and all(0 <= int(d) < q for d in w)
                   for w in words)
        expected = q + (2 * q * q) // 3
        assert len(words) == expected

        loads = Counter(y for w in words for y in descendants(w))
        all_outputs = [''.join(x) for x in product(map(str, range(q)), repeat=2)]
        profile = Counter(loads[y] for y in all_outputs)
        assert all(0 <= loads[y] <= 2 for y in all_outputs)
        assert profile == ({2: q*q} if q == 6 else {1: 2, 2: q*q-2})

        one = sum(len(descendants(w)) == 1 for w in words)
        two = sum(len(descendants(w)) == 2 for w in words)
        three = sum(len(descendants(w)) == 3 for w in words)
        assert (one, two) == (q, q)
        assert one + two + three == len(words)
        assert len([w for w in words if w[0]==w[1]==w[2]]) == q
        assert sum(loads.values()) == one + 2 * two + 3 * three

        if q == 6:
            assert set(words) == {''.join(str((int(d) + 1) % q) for d in w)
                                  for w in words}
        else:
            assert len(words) % q != 0
        if q == 5:
            adjacency_triangle(words, ('230', '240', '243'))
        if q == 8:
            adjacency_triangle(words, ('403', '463', '603'))

        print(f"alphabet={q}; messages={len(words)}; one-shadow={one}; "
              f"two-shadow={two}; three-shadow={three}; "
              f"receiver-list-histogram={dict(sorted(profile.items()))}; "
              f"total-incidences={sum(loads.values())}")

    print('All four codebooks passed complete receiver-by-receiver verification.')
    print('Cyclic invariance at alphabet six and two explicit conflict triangles passed.')
    print('Optimality follows from the separate universal incidence inequality in RESULT.md.')

if __name__ == '__main__':
    test()
