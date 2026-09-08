"""Independent verifier for lane-261 White p=2 diagonal threshold.

Replays from committed vertices only, stdlib-only:
 1. facet inequalities == barycentric membership (k in {1,2,5,6,11,12}, t=0..3)
 2. brute-force box counts == closed form L_k(t) (k=1..12, t=0..4)
 3. interior counts == -L_k(-t) (Ehrhart-Macdonald reciprocity)
 4. N(y) slice lemma
 5. h*=(1,0,q-1,0) Ehrhart-series convolution identity
 6. emptiness (L_k(1)=4) and width-1 witness e3
"""
from fractions import Fraction
from math import gcd
import itertools

V = lambda k: [(0,0,0),(1,0,0),(0,0,1),(2,2*k+1,1)]

def closed(k, t):
    q = 2*k+1
    return Fraction(q*t**3 + 6*t**2 + (12-q)*t + 6, 6)

def facet_in(k, p, t):
    q = 2*k+1
    x, y, z = p
    return y >= 0 and q*z-y >= 0 and q*x-2*y >= 0 and q*(x+z)-2*y <= q*t

def facet_interior(k, p, t):
    q = 2*k+1
    x, y, z = p
    return y > 0 and q*z-y > 0 and q*x-2*y > 0 and q*(x+z)-2*y < q*t

def bary_in(k, p, t):
    A, B, C, D = V(k)
    M = [[B[i]-A[i], C[i]-A[i], D[i]-A[i]] for i in range(3)]
    b = [p[i]-t*A[i] for i in range(3)]
    N = [row[:] + [b[i]] for i, row in enumerate(M)]
    for col in range(3):
        piv = next(i for i in range(col, 3) if N[i][col] != 0)
        N[col], N[piv] = N[piv], N[col]
        for i in range(3):
            if i != col and N[i][col] != 0:
                f = N[i][col]/N[col][col]
                for j in range(col, 4):
                    N[i][j] -= f*N[col][j]
    lam = [N[i][3]/N[i][i] for i in range(3)]
    return all(v >= 0 for v in lam) and sum(lam) <= t

def box_counts(k, t):
    q = 2*k+1
    tot = inter = 0
    for x in range(2*t+1):
        for y in range(q*t+1):
            for z in range(t+1):
                if facet_in(k, (x,y,z), t):
                    tot += 1
                    if facet_interior(k, (x,y,z), t):
                        inter += 1
    return tot, inter

def main():
    n = 0
    for k in [1,2,5,6,11,12]:
        for t in [0,1,2,3]:
            q = 2*k+1
            for x in range(2*t+1):
                for y in range(q*t+1):
                    for z in range(t+1):
                        assert bary_in(k,(x,y,z),t) == facet_in(k,(x,y,z),t), (k,(x,y,z),t)
                        n += 1
    print(f"facet==barycentric OK ({n} points)")
    for k in range(1, 13):
        for t in range(0, 5):
            tot, inter = box_counts(k, t)
            assert tot == closed(k, t), (k, t, tot, closed(k, t))
            if t >= 1:
                assert inter == int(-closed(k, -t)), (k, t, inter, -closed(k, -t))
    print("brute counts == closed form, reciprocity OK (k=1..12, t=0..4)")
    import math
    for k in [1,2,6,12]:
        q = 2*k+1
        for t in [0,1,2,3,4,7]:
            for y in range(q*t+1):
                N = t + math.floor(2*y/q) - math.ceil(2*y/q) - math.ceil(y/q)
                if y == 0:
                    N = t
                a, s = divmod(y, q)
                assert N == (t-a if s == 0 else t-a-2), (k,t,y)
    print("N(y) slice lemma OK")
    for k in range(1, 13):
        h = (1, 0, 2*k, 0)
        c = (1,-4,6,-4,1)
        for t in range(0, 7):
            v = sum(c[j]*closed(k, t-j) for j in range(min(4, t)+1))
            assert v == (h[t] if t < 4 else 0), (k, t, v)
    print("h*=(1,0,q-1,0) series identity OK")
    for k in range(1, 13):
        assert box_counts(k, 1)[0] == 4
        vals = [u for (_,_,u) in [V(k)[i] for i in range(4)]]
        assert max(vals)-min(vals) == 1
    print("empty (L(1)=4) + width-1 via e3 OK")
    print("lin coeffs:", [(k, closed_str(k)) for k in range(1,13)])
    print("ALL VERIFY_OK")

def closed_str(k):
    return str(Fraction(11-2*k, 6))

if __name__ == "__main__":
    main()
