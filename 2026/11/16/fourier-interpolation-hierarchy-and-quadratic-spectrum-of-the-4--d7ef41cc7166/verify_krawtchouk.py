"""Exact Fourier-sampling certificate for the 4-by-4 binary margin-(2,2,2,2) fiber.
Run: python verify_krawtchouk.py   (requires SymPy)
"""
from itertools import combinations, product
from math import comb
from sympy import Matrix, Symbol, prod, factor

n=4
row_patterns = [sum(1<<j for j in J) for J in combinations(range(n), 2)]
tables = sorted(sum(r<<(n*i) for i,r in enumerate(R))
                for R in product(row_patterns,repeat=n)
                if all(sum((r>>j)&1 for r in R)==2 for j in range(n)))
assert len(tables)==90 and len(set(tables))==90
assert all(a.bit_count()==8 for a in tables)
# There are 18 disjoint pairs of 4-cycles, the other 72 tables are 8-cycles.
def components_count(a):
    graph=[[] for _ in range(8)]
    for i in range(4):
        for j in range(4):
            if a & (1<<(4*i+j)):
                graph[i].append(4+j)
                graph[4+j].append(i)
    seen=set();count=0
    for v in range(8):
        if v not in seen:
            count+=1;stack=[v];seen.add(v)
            while stack:
                for w in graph[stack.pop()]:
                    if w not in seen:seen.add(w);stack.append(w)
    return count
assert sum(components_count(a)==1 for a in tables)==72
assert sum(components_count(a)==2 for a in tables)==18

def kraw(j,d):
    return sum((-1)**i*comb(d,i)*comb(16-d,j-i)
               for i in range(max(0,j-(16-d)),min(j,d)+1))
D=[[ (a^b).bit_count() for b in tables] for a in tables]
x=Symbol('x')
expected=[
    {0:89,90:1},
    {0:80,90:1,160:9},
    {0:51,160:9,256:9,320:4,384:12,512:4,650:1},
]
# Factor form for the two nontrivial quadratic sectors.
expected_polynomials=[
    prod((x-v)**m for v,m in expected[0].items()),
    prod((x-v)**m for v,m in expected[1].items()),
    prod((x-v)**m for v,m in expected[2].items()),
    x**15*(x-1280)**18*(x-768)**9*(x-650)*(x-512)**4*(x-384)**12*(x-320)**4*(x-256)**9*(x*x-2432*x+1409024)**9,
    (x-4096)**6*(x-3840)**9*(x-3712)**12*(x-1280)**18*(x-768)**9*(x*x-8192*x+16646144)**4*(x*x-7778*x+14956544)*(x*x-7616*x+14483456)**4*(x*x-2432*x+1409024)**9
]
for r in range(5):
    B=Matrix(90,90,lambda i,j:sum(kraw(t,D[i][j]) for t in range(r+1)))
    got=B.charpoly(x).as_expr()
    assert got.expand()==expected_polynomials[r].expand(), ('characteristic mismatch',r)
    rank=90 if r==4 else [1,10,39,75][r]
    print('degree',r,'rank',rank,'columns',sum(comb(16,j) for j in range(r+1)))
    if r==2:
        assert B==Matrix(90,90,lambda i,j:137-34*D[i][j]+2*D[i][j]**2)
        assert B.trace()==90*137
        print('quadratic nonzero eigenvalues',[(160,9),(256,9),(320,4),(384,12),(512,4),(650,1)])
print('EXACT_KRAWTCHOUK_CERTIFICATE_PASS')
