"""Independent GL(4,2) enumeration and F4 point-count verification."""
from itertools import product

REP = [(1,2,4,8),(1,2,4,9),(1,2,4,11),(1,2,4,15),
       (1,2,5,10),(1,2,5,11),(1,2,7,11),(1,2,8,7),
       (1,2,9,6),(2,1,8,4)]
EXPECTED = [(420,7,45),(3360,7,21),(5040,7,29),(1120,3,21),
            (1120,9,33),(4032,5,25),(420,3,29),(1260,11,29),
            (3360,9,17),(28,15,45)]

def rank(A):
    rows = list(A)
    count = 0
    for j in range(4):
        pivot = next((k for k in range(count,4) if rows[k] & (1<<j)), None)
        if pivot is None: continue
        rows[pivot], rows[count] = rows[count], rows[pivot]
        for k in range(count+1,4):
            if rows[k] & (1<<j): rows[k] ^= rows[count]
        count += 1
    return count

def dot(x, y):
    return (x & y).bit_count() & 1

def value(A, u, v):
    return sum(dot(A[i],v) for i in range(4) if (u>>i)&1)&1

def count_F4(A):
    # Independent multiplication in F4 = F2[t]/(t^2+t+1).
    mult = [[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]]
    n = 0
    for x in product(range(4), repeat=4):
        if not any(x): continue
        t = 0
        for i in range(4):
            x2 = mult[x[i]][x[i]]
            for j in range(4):
                if A[i]>>j & 1: t ^= mult[x2][x[j]]
        n += t == 0
    assert n % 3 == 0
    return n//3

GL = []
for a in product(range(16),repeat=4):
    if rank(a)==4:
        cols = [sum(((a[i]>>j)&1)<<i for i in range(4)) for j in range(4)]
        GL.append(tuple(cols))
assert len(GL)==20160
for i,A in enumerate(REP):
    stab = 0
    for col in GL:
        transformed = tuple(sum(value(A,col[r],col[s]) << s for s in range(4)) for r in range(4))
        stab += transformed == A
    orbit = 20160//stab
    n1 = sum(value(A,x,x)==0 for x in range(1,16))
    n2 = count_F4(A)
    assert (orbit,n1,n2)==EXPECTED[i], (i,orbit,n1,n2)
    print(i, 'orbit', orbit, 'stabilizer', stab, 'N1', n1, 'N2', n2)
assert sum(x[0] for x in EXPECTED)==20160
assert len({(n1,n2) for _,n1,n2 in EXPECTED})==10
print('PASS: independent direct stabilizers, F4-field arithmetic and arithmetic signatures')
