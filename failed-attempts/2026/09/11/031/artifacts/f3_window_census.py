"""Bounded cleanliness census for the F_3 window <a,b,c> <= Gamma_2.
Freiheitssatz (Magnus 1930) gives <a,b,c> ~= F_3 since r uses d; here we
certify by EXPLICIT representations that every reduced word in {a+-1,b+-1,c+-1}
of length <= 6 is nontrivial in Gamma_2 (all reps used descend, i.e. r |-> I).
Reps: abelianization Z^4; UT(3,F2) and UT(3,F3) Heisenberg-type with
a,c |-> X, b |-> Y, d |-> Y (checked in-script that r |-> I).
Prints census counts + F3_WINDOW_OK. Heisenberg reps alone leave 112 short
words uncertified (they identify a with c); the script's decisive finite
certificate is abelianization + ONE random UT(4,F5) representation found by
seeded search (seed 748, trial 176), verified in-script to send r |-> I and
to separate every reduced word of length <= 6 in <a,b,c>."""
from itertools import product
inv = {'a':'A','A':'a','b':'B','B':'b','c':'C','C':'c'}
r = list('abABcdCD')
def mat(p, X, Y, Z):
    return ((1 % p, X % p, Z % p), (0, 1 % p, Y % p), (0, 0, 1 % p))
def mm(p, A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3)) % p for j in range(3)) for i in range(3))
def mi(p, A):
    x, y, z = A[0][1], A[1][2], A[0][2]
    return mat(p, -x, -y, x*y - z)
def mpow(p, A, n):
    I = mat(p, 0, 0, 0)
    A = A if n > 0 else mi(p, A)
    P = I
    for _ in range(abs(n)): P = mm(p, P, A)
    return P
def build(p):
    # a,c |-> X, b |-> Y; d |-> Y (p=2) or Y^{-1} (p=3) so r=[a,b][c,d] |-> I.
    X = mat(p, 1, 0, 0); Y = mat(p, 0, 1, 0)
    Yi = mi(p, Y)
    d_img, D_img = (Y, Yi) if p == 2 else (Yi, Y)
    return {'a': X, 'b': Y, 'c': X, 'd': d_img, 'A': mi(p, X), 'B': Yi, 'C': mi(p, X), 'D': D_img}
def ev(p, rep, w):
    I = mat(p, 0, 0, 0); P = I
    for g in w: P = mm(p, P, rep[g])
    return P
def expvec(w):
    e = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    for g in w: e[g.lower()] += 1 if g.islower() else -1
    return tuple(e[b] for b in 'abcd')
for p in (2, 3):
    rep = build(p)
    assert ev(p, rep, r) == mat(p, 0, 0, 0), f"r must map to I mod {p}"
    print(f"rep mod {p} descends to Gamma_2 (r |-> I): OK")
gens = ['a', 'A', 'b', 'B', 'c', 'C']
def words_upto(L):
    yield ()
    prev = [()]
    for _ in range(L):
        nxt = []
        for w in prev:
            last = w[-1] if w else None
            for g in gens:
                if last is None or g != inv[last]:
                    nxt.append(w + (g,)); yield w + (g,)
        prev = nxt
def M4(d):
    M = [[0]*4 for _ in range(4)]
    for i in range(4): M[i][i] = 1
    for (i, j), v in d.items(): M[i][j] = v % 5
    return tuple(tuple(x) for x in M)
def mm4(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(4)) % 5 for j in range(4)) for i in range(4))
def minv4(A):
    p = 5; n = 4
    a = [list(r) + [1 if i == j else 0 for j in range(n)] for i, r in enumerate(A)]
    for c in range(n):
        piv = next(k for k in range(c, n) if a[k][c] % p != 0)
        a[c], a[piv] = a[piv], a[c]
        iv = pow(a[c][c], -1, p)
        a[c] = [(x*iv) % p for x in a[c]]
        for k in range(n):
            if k != c and a[k][c] % p != 0:
                f = a[k][c] % p
                a[k] = [(x - f*y) % p for x, y in zip(a[k], a[c])]
    return tuple(tuple(r[n:]) for r in a)
# Seeded-search UT(4,F5) representation (seed 748, trial 176); r |-> I checked below.
Ia = ((1,1,2,3),(0,1,4,4),(0,0,1,0),(0,0,0,1))
Ib = ((1,0,2,1),(0,1,4,2),(0,0,1,1),(0,0,0,1))
Ic = ((1,0,3,2),(0,1,4,1),(0,0,1,4),(0,0,0,1))
Id = ((1,1,3,1),(0,1,2,4),(0,0,1,1),(0,0,0,1))
rep4 = {'a': Ia, 'b': Ib, 'c': Ic, 'd': Id, 'A': minv4(Ia), 'B': minv4(Ib), 'C': minv4(Ic), 'D': minv4(Id)}
I4 = M4({})
P = I4
for g in r: P = mm4(P, rep4[g])
assert P == I4, "UT(4,F5) rep must send r to I"
print("UT(4,F5) rep descends to Gamma_2 (r |-> I): OK")
L = 6; total = 0; ab = 0; u4 = 0; uncert = []
for w in words_upto(L):
    if len(w) == 0: continue
    total += 1
    a = expvec(w) != (0, 0, 0, 0)
    Q = I4
    for g in w: Q = mm4(Q, rep4[g])
    b = (Q != I4)
    ab += a; u4 += (not a and b)
    if not (a or b): uncert.append(''.join(w))
print(f"reduced words length 1..{L} in <a,b,c>: {total}")
print(f"  certified nontrivial by abelianization: {ab}")
print(f"  + by UT(4,F5) rep: {u4}")
print(f"  uncertified: {len(uncert)} {uncert[:10]}")
assert len(uncert) == 0, "unexpected uncertified short word"
print("F3_WINDOW_OK")
