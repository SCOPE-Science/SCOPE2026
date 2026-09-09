"""Committed explicit multiplication tables. Every table is brute-force checked
for associativity/identity/inverses inside cd_compute.py before use."""

def cyclic_table(n):
    return [[(a+b) % n for b in range(n)] for a in range(n)]

def vec_table(p, k):
    n = p**k
    def dec(x):
        v = []
        for _ in range(k):
            v.append(x % p); x //= p
        return v
    def enc(v):
        x = 0
        for d in reversed(v):
            x = x*p + d
        return x
    mult = [[0]*n for _ in range(n)]
    for a in range(n):
        va = dec(a)
        for b in range(n):
            vb = dec(b)
            mult[a][b] = enc([(va[i]+vb[i]) % p for i in range(k)])
    return mult

def dihedral_table(N):
    n = 2*N
    mult = [[0]*n for _ in range(n)]
    def M(a, b):
        ta, xa = (0, a) if a < N else (1, a-N)
        tb, xb = (0, b) if b < N else (1, b-N)
        if ta == 0 and tb == 0: return (xa+xb) % N
        if ta == 0 and tb == 1: return N + ((xa+xb) % N)
        if ta == 1 and tb == 0: return N + ((xa-xb) % N)
        return (xa-xb) % N
    for a in range(n):
        for b in range(n):
            mult[a][b] = M(a, b)
    return mult

def genquat_table():
    N = 32
    n = 64
    mult = [[0]*n for _ in range(n)]
    def M(a, b):
        ta, xa = (0, a) if a < N else (1, a-N)
        tb, xb = (0, b) if b < N else (1, b-N)
        if ta == 0 and tb == 0: return (xa+xb) % N
        if ta == 0 and tb == 1: return N + ((xa+xb) % N)
        if ta == 1 and tb == 0: return N + ((xa-xb) % N)
        return (xa-xb+16) % N
    for a in range(n):
        for b in range(n):
            mult[a][b] = M(a, b)
    return mult

def semidihedral_table():
    N = 32
    n = 64
    mult = [[0]*n for _ in range(n)]
    def M(a, b):
        ta, xa = (0, a) if a < N else (1, a-N)
        tb, xb = (0, b) if b < N else (1, b-N)
        if ta == 0 and tb == 0: return (xa+xb) % N
        if ta == 0 and tb == 1: return N + ((xa+xb) % N)
        if ta == 1 and tb == 0: return N + ((xa+15*xb) % N)
        return (xa+15*xb) % N
    for a in range(n):
        for b in range(n):
            mult[a][b] = M(a, b)
    return mult

def q8_table():
    sgn = [1,-1,1,-1,1,-1,1,-1]
    bas = [0,0,1,1,2,2,3,3]
    prod = {(0,0):(0,1),(0,1):(1,1),(0,2):(2,1),(0,3):(3,1),
            (1,0):(1,1),(1,1):(0,-1),(1,2):(3,1),(1,3):(2,-1),
            (2,0):(2,1),(2,1):(3,-1),(2,2):(0,-1),(2,3):(1,1),
            (3,0):(3,1),(3,1):(2,1),(3,2):(1,-1),(3,3):(0,-1)}
    mult = [[0]*8 for _ in range(8)]
    for a in range(8):
        for b in range(8):
            (c, s) = prod[(bas[a], bas[b])]
            t = s*sgn[a]*sgn[b]
            mult[a][b] = c*2 + (0 if t == 1 else 1)
    return mult

def s3_table():
    import itertools
    perms = list(itertools.permutations([0,1,2]))
    idx = {p: i for i, p in enumerate(perms)}
    mult = [[0]*6 for _ in range(6)]
    for a, pa in enumerate(perms):
        for b, pb in enumerate(perms):
            mult[a][b] = idx[tuple(pa[pb[i]] for i in range(3))]
    e = idx[(0,1,2)]
    perm = list(range(6)); perm[0], perm[e] = perm[e], perm[0]
    invp = [0]*6
    for i, p in enumerate(perm):
        invp[p] = i
    return [[invp[mult[perm[a]][perm[b]]] for b in range(6)] for a in range(6)]

def a4_table():
    import itertools
    perms = [p for p in itertools.permutations([0,1,2,3])
             if sum(1 for i in range(4) for j in range(i+1, 4) if p[i] > p[j]) % 2 == 0]
    assert len(perms) == 12
    idx = {p: i for i, p in enumerate(perms)}
    mult = [[0]*12 for _ in range(12)]
    for a, pa in enumerate(perms):
        for b, pb in enumerate(perms):
            mult[a][b] = idx[tuple(pa[pb[i]] for i in range(4))]
    e = idx[(0,1,2,3)]
    perm = list(range(12)); perm[0], perm[e] = perm[e], perm[0]
    invp = [0]*12
    for i, p in enumerate(perm):
        invp[p] = i
    return [[invp[mult[perm[a]][perm[b]]] for b in range(12)] for a in range(12)]

def s4_table():
    import itertools
    perms = list(itertools.permutations([0,1,2,3]))
    idx = {p: i for i, p in enumerate(perms)}
    mult = [[0]*24 for _ in range(24)]
    for a, pa in enumerate(perms):
        for b, pb in enumerate(perms):
            mult[a][b] = idx[tuple(pa[pb[i]] for i in range(4))]
    e = idx[(0,1,2,3)]
    perm = list(range(24)); perm[0], perm[e] = perm[e], perm[0]
    invp = [0]*24
    for i, p in enumerate(perm):
        invp[p] = i
    return [[invp[mult[perm[a]][perm[b]]] for b in range(24)] for a in range(24)]

def semidirect_cq(q, p, act):
    n = q*p
    pw = [[u % q]*p for u in range(q)]
    for u in range(q):
        for v in range(1, p):
            pw[u][v] = (act*pw[u][v-1]) % q
    assert (pw[1][p-1]*act) % q == 1, "act^p != id mod q"
    mult = [[0]*n for _ in range(n)]
    for a in range(n):
        ua, va = a//p, a % p
        for b in range(n):
            ub, vb = b//p, b % p
            mult[a][b] = ((ua+pw[ub][va]) % q)*p + ((va+vb) % p)
    return mult

def product_table(A, B):
    na, nb = len(A), len(B)
    n = na*nb
    mult = [[0]*n for _ in range(n)]
    for a in range(n):
        aa, ab = a//nb, a % nb
        for b in range(n):
            ba, bb = b//nb, b % nb
            mult[a][b] = A[aa][ba]*nb + B[ab][bb]
    return mult

# name -> (family, builder, abelian_flag)
BUILDERS = {
    "S3": ("calib", s3_table, False),
    "D8": ("calib", lambda: dihedral_table(4), False),
    "Q8": ("calib", q8_table, False),
    "A4": ("calib", a4_table, False),  # A4: V4 normal; S4/A4 used for CD-minimal calibration only
    "S4": ("witness", s4_table, False),  # CD-minimal witness (outside 64/81 window): CD={1,S4}
    "C64": ("ord64", lambda: cyclic_table(64), True),
    "C8xC8": ("ord64", lambda: product_table(cyclic_table(8), cyclic_table(8)), True),
    "C2x6": ("ord64", lambda: vec_table(2, 6), True),
    "D64": ("ord64", lambda: dihedral_table(32), False),
    "Q64": ("ord64", genquat_table, False),
    "SD64": ("ord64", semidihedral_table, False),
    "D8xC8": ("ord64", lambda: product_table(dihedral_table(4), cyclic_table(8)), False),
    "C81": ("ord81", lambda: cyclic_table(81), True),
    "C9xC9": ("ord81", lambda: product_table(cyclic_table(9), cyclic_table(9)), True),
    "C3x4": ("ord81", lambda: vec_table(3, 4), True),
    "C9sem3": ("ord81", lambda: semidirect_cq(9, 3, 4), False),
    "C27sem3": ("ord81", lambda: semidirect_cq(27, 3, 10), False),
}
