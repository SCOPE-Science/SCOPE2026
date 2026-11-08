"""Reproduce exact sparse-output reachability for periodic elementary Rule 22.

No external packages or input files. Run: python3 verify_rule22.py
"""
from itertools import product, combinations
from math import comb

# Boolean relation on states 00,01,10,11, packed as a 16-bit row matrix.
IDENTITY = sum(1 << (5 * i) for i in range(4))

def compose(left, right):
    result = 0
    for i in range(4):
        row = 0
        for j in range(4):
            if (left >> (4*i + j)) & 1:
                row |= (right >> (4*j)) & 15
        result |= row << (4*i)
    return result

def edge_matrix(letter):
    m = 0
    for a,b,c in product((0,1), repeat=3):
        if (a+b+c == 1) == bool(letter):
            i, j = 2*a+b, 2*b+c
            m |= 1 << (4*i+j)
    return m

ZERO, ONE = edge_matrix(0), edge_matrix(1)
assert (ZERO, ONE) == (0xc281, 0x0142)
ZERO_POW = [IDENTITY]
for k in range(5):
    ZERO_POW.append(compose(ZERO_POW[-1], ZERO))
assert ZERO_POW[4] == ZERO_POW[5] == 0xeee1

def reachable_gaps(gaps):
    r = IDENTITY
    for d in gaps:
        assert d >= 1
        r = compose(compose(r, ONE), ZERO_POW[min(d-1,4)])
    return bool(r & IDENTITY)

def canonical(gaps):
    return min(tuple(gaps[(j+k)%len(gaps)] for j in range(len(gaps))) for k in range(len(gaps)))

assert [d for d in range(1,6) if not reachable_gaps((d,))] == [1,3,4]
assert sorted(g for g in product(range(1,6),repeat=2) if not reachable_gaps(g)) == [(1,1),(1,2),(2,1)]

# Complete finite certificate: the forbidden third coordinates for each
# pair of first coordinates, each in the capped alphabet {1,...,5}.
EXPECTED_TABLE = [
    [(), (2,3), (2,3), (), ()],
    [(2,3), (1,3,4), (1,2,3,4,5), (2,3), (3,)],
    [(2,3), (1,2,3,4,5), (1,2,3,4,5), (2,3), (2,3)],
    [(), (2,3), (2,3), (), ()],
    [(), (3,), (2,3), (), ()],
]
for a,b in product(range(1,6), repeat=2):
    forbidden = tuple(c for c in range(1,6) if not reachable_gaps((a,b,c)))
    assert forbidden == EXPECTED_TABLE[a-1][b-1], (a,b,forbidden)

FORBIDDEN_CANONICAL = {
    (1,2,2), (1,2,3), (1,3,2), (1,3,3), (2,2,3),
    (2,2,4), (2,3,3), (2,3,4), (2,3,5), (2,4,3),
    (2,5,3), (3,3,3), (3,3,4), (3,3,5)
}
assert {canonical(g) for g in product(range(1,6),repeat=3)
        if not reachable_gaps(g)} == FORBIDDEN_CANONICAL

# The complete gap characterization for all ring lengths >= 10.
def expected_forbidden(gaps):
    a,b,c = gaps
    n = sum(gaps)
    return n >= 10 and canonical(gaps) in {
        canonical((2,3,n-5)), canonical((2,n-5,3)),
        canonical((3,3,n-6))
    }

def gen_gaps(n, k):
    if k == 1:
        yield (n,)
    elif k == 2:
        for a in range(1,n):yield (a,n-a)
    elif k == 3:
        for a in range(1,n-1):
            for b in range(1,n-a):yield (a,b,n-a-b)
    else:
        raise ValueError(k)

count_gap_tests = 0
for n in range(5,61):
    assert reachable_gaps((n,))
    assert all(reachable_gaps(g) for g in gen_gaps(n,2))
    if n >= 10:
        for g in gen_gaps(n,3):
            count_gap_tests += 1
            assert (not reachable_gaps(g)) == expected_forbidden(g), (n,g)
        # Each cyclic word of weight three has exactly 3 distinguished one-starts.
        missing = sum(not reachable_gaps(g) for g in gen_gaps(n,3)) * n // 3
        # Each rotation of a gap triple counted three times in the above sum;
        # number of words = n/3 * count_of_compositions.
        assert missing == 3*n, (n,missing)

EXPECTED_SMALL = {5:5,6:12,7:14,8:16,9:21}
for n,value in EXPECTED_SMALL.items():
    count = sum(not reachable_gaps(g) for g in gen_gaps(n,3))*n//3
    assert count == value,(n,count,value)

# Independent direct source-word evolution; no Boolean matrix paths involved.
def evolve(word, n):
    out = 0
    for i in range(n):
        s = ((word >> ((i-1)%n)) & 1) + ((word >> i) & 1) + ((word >> ((i+1)%n)) & 1)
        if s == 1: out |= 1<<i
    return out

word_checks = 0
for n in range(3,18):
    image = bytearray(1<<n)
    for word in range(1<<n):
        image[evolve(word,n)] = 1
        word_checks += 1
    for target in range(1<<n):
        if target.bit_count() > 3:continue
        pos = [i for i in range(n) if (target>>i)&1]
        if not pos:
            pred = True
        else:
            gaps = [pos[i+1]-pos[i] for i in range(len(pos)-1)] + [n+pos[0]-pos[-1]]
            pred = reachable_gaps(gaps)
        assert pred == bool(image[target]), (n,target,pred)
    if n>=10:
        bad = sum(not image[target] for target in range(1<<n) if target.bit_count()==3)
        assert bad == 3*n
print(f'VERIFY_OK capped_cases=125 ring_lengths=5..60 gap_cases={count_gap_tests} direct_inputs={word_checks}')
