"""Independent finite-field checks for exact VC/Littlestone ranks of double parallel lines.
Run: python3 verify.py   (Python standard library only).
Finite checks do not replace the incidence-axiom proof for arbitrary affine planes.
"""
from itertools import combinations, product
from functools import lru_cache


def field(q):
    if q in (2, 3, 5, 7, 11):
        return (lambda x, y: (x + y) % q), (lambda x, y: (x * y) % q)
    if q in (4, 8):
        modulus = {4: 0b111, 8: 0b1011}[q]
        def mult(a, b):
            z = 0
            while b:
                if b & 1: z ^= a
                b >>= 1
                a <<= 1
                if a & q: a ^= modulus
            return z
        return (lambda x, y: x ^ y), mult
    if q == 9:
        # F_3[u] / (u^2 + 1).  Encode a+b*u as a+3*b.
        def add(a, b):
            return ((a % 3 + b % 3) % 3 + 3 * ((a // 3 + b // 3) % 3))
        def mul(a, b):
            a0, a1 = a % 3, a // 3
            b0, b1 = b % 3, b // 3
            return ((a0*b0-a1*b1) % 3 + 3 * ((a0*b1+a1*b0) % 3))
        return add, mul
    raise ValueError('unsupported demonstration field')


def build(q):
    add, mul = field(q)
    points = list(product(range(q), repeat=2))
    lines = []
    directions = []
    for direction in range(q + 1):
        parallel_class = []
        for b in range(q):
            if direction == q:
                line = frozenset(j for j, (x,y) in enumerate(points) if x == b)
            else:
                line = frozenset(j for j, (x,y) in enumerate(points)
                                 if add(y, mul(direction, x)) == b)
            parallel_class.append(line)
            lines.append(line)
        directions.append(parallel_class)
    assert len(set(lines)) == q * (q + 1)
    assert all(len(L)==q for L in lines)
    assert all(len(A&B)==0 for parallel in directions
               for A,B in combinations(parallel,2))
    concepts = sorted({frozenset(A|B) for parallel in directions
                       for A,B in combinations(parallel,2)}, key=lambda z: tuple(sorted(z)))
    assert len(concepts) == (1 if q == 2 else (q+1)*q*(q-1)//2)
    return points, concepts


def exact_ldim(points, concepts):
    n = len(concepts)
    query_masks = [sum(1 << h for h,C in enumerate(concepts) if i in C)
                   for i in range(len(points))]
    full = (1 << n)-1
    @lru_cache(None)
    def shattered(mask, depth):
        if depth == 0: return bool(mask)
        if mask.bit_count() < (1 << depth): return False
        for query in query_masks:
            pos = mask & query
            neg = mask ^ pos
            if pos and neg and shattered(pos,depth-1) and shattered(neg,depth-1):
                return True
        return False
    out = 0
    for d in range(1, 6):
        if shattered(full,d): out = d
        else: break
    return out, shattered.cache_info().currsize


def lower_support(q, points, concepts):
    if q < 4:return None
    # Four points on a vertical affine line, plus one transverse point.
    S = [points.index((0,i)) for i in range(4)] + [points.index((1,0))]
    T = S[:3] + S[4:]
    traces = {tuple(int(p in C) for p in T) for C in concepts}
    assert len(traces) == 16
    return len(traces)


def main():
    expected = {2:0, 3:2, 4:4, 5:4, 7:4, 8:4, 9:4, 11:4}
    for q,rank in expected.items():
        points, concepts = build(q)
        actual, states = exact_ldim(points, concepts)
        assert actual == rank, (q,actual,rank)
        trace_count = lower_support(q, points, concepts)
        print(f'q={q} points={len(points)} concepts={len(concepts)} '
              f'Ldim={actual} states={states} shattered_four_traces={trace_count}')
    print('DOUBLE_PARALLEL_LINE_RANKS_PASS')

if __name__ == '__main__':main()
