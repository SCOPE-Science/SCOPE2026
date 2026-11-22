"""Exact rational verification for seven-vertex weighted-tree probing witness.
Standard-library only: python verify_exact.py
"""
from fractions import Fraction as F
from itertools import product

N=7
EDGES=((0,1,2),(0,2,2),(0,6,1),(1,3,1),(1,4,1),(1,5,1))
B=(1,-1,-1,1,1,1,-1)
MU=F(1,3)
assertions=0

def test(cond):
    global assertions
    assertions+=1
    assert cond

def inverse(a):
    n=len(a)
    t=[list(a[i])+[F(i==j) for j in range(n)] for i in range(n)]
    for k in range(n):
        r=next(r for r in range(k,n) if t[r][k])
        t[k],t[r]=t[r],t[k]
        pivot=t[k][k]
        t[k]=[v/pivot for v in t[k]]
        for i in range(n):
            if i!=k:
                z=t[i][k]
                t[i]=[t[i][j]-z*t[k][j] for j in range(2*n)]
    return [x[n:] for x in t]

def precision(mu=MU):
    a=[[mu if i==j else F(0) for j in range(N)] for i in range(N)]
    for u,v,c in EDGES:
        a[u][u]+=c; a[v][v]+=c; a[u][v]-=c; a[v][u]-=c
    return a

Q=precision()
G=inverse(Q)
for i in range(N):
    for j in range(N):
        test(sum(Q[i][k]*G[k][j] for k in range(N)) == (i==j))
        test(G[i][j]>0)

def variance(s):
    return 4*sum(G[i][j]**2 for i in range(N) for j in range(i+1,N) if s[i]==s[j])

def energy(s):
    return sum(s[i]*s[j]*G[i][j]**2 for i in range(N) for j in range(N))

def flip(s,subset):
    return tuple(-s[i] if i in subset else s[i] for i in range(N))

V0=variance(B); E0=energy(B)
test(V0==F(384984171,95452900))
for s in product((-1,1), repeat=N-1):
    z=(1,)+s
    test(variance(z)-V0==energy(z)-E0)

root_subtrees=((1,3,4,5),(2,),(6,),(3,),(4,),(5,))
expected_edge=(F(3321648,23863225),F(20631024,23863225),F(12053124,23863225),F(730863,47726450),F(730863,47726450),F(730863,47726450))
for subset,expected in zip(root_subtrees,expected_edge):
    test(variance(flip(B,subset))-V0==expected)
    test(expected>0)
expected_vertex=(F(38945124,23863225),F(51623244,23863225),F(20631024,23863225),F(730863,47726450),F(730863,47726450),F(730863,47726450),F(12053124,23863225))
for j,expected in enumerate(expected_vertex):
    test(variance(flip(B,(j,)))-V0==expected)
    test(expected>0)

out=[(variance((1,)+s),(1,)+s) for s in product((-1,1),repeat=6)]
lo=min(z for z,_ in out)
test(lo==F(377990793,95452900))
winners=[s for v,s in out if v==lo]
test(len(winners)==3)
for s in winners:
    test((s[0],s[1],s[2],s[6])==(1,1,-1,-1))
    test(sum(s[i]==1 for i in (3,4,5))==1)
test(V0-lo==F(3496689,47726450))

# The eight-row, four-column reduced exact exhaustive table.
expected_table={
(-1,-1,-1):(530849700,189197856,16910208,13986756),
(-1,-1,1):(380371140,121020480,31034016,110411748),
(-1,1,-1):(373411620,139255200,74462976,179034948),
(-1,1,1):(478421316,326566080,344075040,530948196),
(1,-1,-1):(40559940,0,128804256,426972708),
(1,-1,1):(36394596,78135840,289241280,669710916),
(1,1,-1):(74224836,141160320,377460000,783123876),
(1,1,1):(325547748,474784416,793385280,1281350340),
}
for (a,b,c),row in expected_table.items():
    for t,expected in enumerate(row):
        s=(1,a,b)+(1,)*t+(-1,)*(3-t)+(c,)
        test((variance(s)-lo)*190905800==expected)

test(B[3]*sum(B[i]*G[3][i]**2 for i in range(N))==F(223184259,190905800))
print(f'PASS: {assertions} exact rational assertions; all 64 colorings and seven singleton flips checked')
