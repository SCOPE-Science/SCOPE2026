"""Independent enumeration of the quartic and incidence with 48 pairing lines.

This program enumerates all standard projective charts, not merely a sample.
"""
from collections import Counter


def field_tables(p, d=None):
    if d is not None:
        assert pow(d, (p - 1) // 2, p) == p - 1
    q = p if d is None else p * p
    add = [[0]*q for _ in range(q)]
    mul = [[0]*q for _ in range(q)]
    for a in range(q):
        for b in range(q):
            if d is None:
                add[a][b] = (a + b) % p
                mul[a][b] = (a * b) % p
            else:
                x, y, z, w = a % p, a // p, b % p, b // p
                add[a][b] = (x + z) % p + p*((y + w) % p)
                mul[a][b] = (x*z + d*y*w) % p + p*((x*w+y*z) % p)
    power4 = [mul[mul[x][x]][mul[x][x]] for x in range(q)]
    roots = [x for x in range(q) if power4[x] == p-1]
    assert len(roots) == 4
    return q, add, mul, power4, roots


def projective_points(q):
    for a in range(q):
        for b in range(q):
            for c in range(q):
                yield (a,b,c,1)
    for a in range(q):
        for b in range(q):
            yield (a,b,1,0)
    for a in range(q):
        yield (a,1,0,0)
    yield (1,0,0,0)


def check(p,d=None):
    q,add,mul,pow4,roots = field_tables(p,d)
    pairings = [((0,1),(2,3)),((0,2),(1,3)),((0,3),(1,2))]
    lines = [((i,j),(k,l),r,s)
             for ((i,j),(k,l)) in pairings
             for r in roots for s in roots]
    assert len(lines) == 48
    histogram = Counter()
    witness = None
    for pt in projective_points(q):
        if add[add[pow4[pt[0]]][pow4[pt[1]]]][
                add[pow4[pt[2]]][pow4[pt[3]]]] != 0:
            continue
        n = sum(pt[i] == mul[r][pt[j]] and pt[k] == mul[s][pt[l]]
                for ((i,j),(k,l),r,s) in lines)
        histogram[n] += 1
        if n == 0 and witness is None:
            witness = pt
    expected = {17: (600,0), 25:(1112,128),
                41:(2520,768), 49:(3480,1344)}[q]
    assert sum(histogram.values()) == expected[0], (q,histogram)
    assert histogram[0] == expected[1]
    assert histogram[1] == 48*(q-9), histogram
    assert histogram[2] == 192, histogram
    assert histogram[4] == 24, histogram
    assert set(histogram) <= {0,1,2,4}, histogram
    print(f"F_{q}: spectrum={dict(sorted(histogram.items()))}; "
          f"first_off_line_point={witness}")


def main():
    for p,d in [(17,None),(5,2),(41,None),(7,3)]:
        check(p,d)
    print('VERIFY_INCIDENCE_OK')


if __name__ == '__main__':
    main()
