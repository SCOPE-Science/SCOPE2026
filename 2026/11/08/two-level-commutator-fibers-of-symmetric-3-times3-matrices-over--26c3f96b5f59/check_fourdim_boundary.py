"""Independent centralizer-dimension check for the 4x4 nonuniformity witness."""
from itertools import combinations_with_replacement

def rankmod(rows, p):
    a = [[x % p for x in row] for row in rows]
    n = len(a)
    m = len(a[0]) if a else 0
    r = 0
    for j in range(m):
        piv = next((i for i in range(r, n) if a[i][j]), None)
        if piv is None:
            continue
        a[r], a[piv] = a[piv], a[r]
        inv = pow(a[r][j], -1, p)
        a[r] = [(v*inv) % p for v in a[r]]
        for i in range(n):
            if i != r and a[i][j]:
                c = a[i][j]
                a[i] = [(v-c*w) % p for v, w in zip(a[i], a[r])]
        r += 1
    return r

def product(a, b, p):
    return [[sum(a[i][k]*b[k][j] for k in range(4)) % p for j in range(4)] for i in range(4)]

def centerdim(z, p):
    bases = []
    for i in range(4):
        for j in range(i, 4):
            e = [[0]*4 for _ in range(4)]
            e[i][j] = e[j][i] = 1
            ze, ez = product(z, e, p), product(e, z, p)
            bases.append([(ze[i][j]-ez[i][j]) % p for i in range(4) for j in range(4)])
    rows = [list(col) for col in zip(*bases)]
    return 10 - rankmod(rows,p)

p = 5
z1 = [[0,1,0,0],[-1,0,0,0],[0,0,0,0],[0,0,0,0]]
z2 = [[0,1,0,0],[-1,0,0,0],[0,0,0,2],[0,0,-2,0]]
a, b = centerdim(z1, p), centerdim(z2, p)
assert (a, b) == (4,2), (a,b)
print(f"q={p} skew_witness_1_symmetric_centralizer={a} skew_witness_2_symmetric_centralizer={b} PASS")
print("FOURDIMENSIONAL_NONUNIFORMITY_WITNESS_PASS")
