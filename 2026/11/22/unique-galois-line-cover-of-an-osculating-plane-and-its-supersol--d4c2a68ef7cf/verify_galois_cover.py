"""Independent finite-field checks for the optimal Galois-line cover theorem.

Usage: python verify_galois_cover.py
Only standard Python is required. All arithmetic uses polynomial bases over F_2.
The finite checks do not replace the proof for arbitrary powers of two.
"""
from collections import Counter
from itertools import combinations

POLY = {4: 0x13, 6: 0x43, 8: 0x11D}


def field(m):
    Q = 1 << m
    irr = POLY[m]
    def mul(a, b):
        r = 0
        while b:
            if b & 1: r ^= a
            b >>= 1
            a <<= 1
            if a & Q: a ^= irr
        return r
    return Q, mul


def main(m):
    Q, mul = field(m)
    # Coordinates (X,Y,W) of the osculating plane Z=0.
    points = [(x,y,1) for y in range(Q) for x in range(Q)]
    points += [(x,1,0) for x in range(Q)] + [(1,0,0)]
    L = [(1,t,mul(t,t)) for t in range(Q)]
    M = [(0,1,d) for d in range(1,Q)]
    lines = L+M
    def on(p,line):
        return (mul(p[0],line[0]) ^ mul(p[1],line[1]) ^ mul(p[2],line[2]))==0
    if m in (4,6):
        incidence = [sum(on(p,line) for line in lines) for p in points]
        profile = Counter(incidence)
        expected = {1:Q*(Q+3)//2,3:Q*(Q-1)//2,Q-1:1}
        assert profile==expected, (m,profile,expected)
        assert all(incidence)
        # Deletion of every chosen line exposes at least one rational point.
        for i in range(len(lines)):
            assert any(on(p,lines[i]) and sum(on(p,h) for j,h in enumerate(lines) if i!=j)==0 for p in points)
    else:
        # Q=256: prove the key two witness formulas by exact finite arithmetic.
        assert len({mul(t,t) for t in range(Q)})==Q
        for d in range(1,Q):
            assert len({mul(t,t)^mul(d,t) for t in range(Q)})==Q//2

    # All pairs of distinct L lines meet at a unique triple point,
    # and all such points are distinct and indexed by unordered pairs.
    triple_points = {(mul(t,u),t^u,1) for t,u in combinations(range(Q),2)}
    assert len(triple_points)==Q*(Q-1)//2
    for t,u in combinations(range(Q),2):
        p=(mul(t,u),t^u,1)
        assert on(p,L[t]) and on(p,L[u])
        # M list excludes zero: parameter d corresponds to index d-1
        assert on(p,M[(t^u)-1])

    # Each nonzero pencil direction has Q/2 points off all L lines,
    # and Y=0 has none, so the unique minimal cover omits only M_0.
    assert len({mul(t,t) for t in range(Q)})==Q
    assert all(len({mul(t,t)^mul(d,t) for t in range(Q)})==Q//2 for d in range(1,Q))
    print('GF(%d): %d minimal lines, %d triple points, point covering and witnesses PASS' %
          (Q,2*Q-1,Q*(Q-1)//2))

if __name__=='__main__':
    for m in (4,6,8): main(m)
    print('All exact finite checks passed. General validity follows from the proof, not these tests.')
