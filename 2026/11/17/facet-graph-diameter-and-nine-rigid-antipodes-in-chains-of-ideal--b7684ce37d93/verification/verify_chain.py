"""Exact finite base checks for the facet-adjacency metric of chains of ideal 24-cells.

Standard library only. The infinite-parameter step is the min-plus identity
proved in RESULT.md; finite tests here certify its bounded kernels/tables.
"""
from itertools import combinations, product
from collections import Counter, deque


def roots():
    return sorted(tuple(signs[pair.index(i)] if i in pair else 0 for i in range(4))
                  for pair in combinations(range(4), 2)
                  for signs in product((-1, 1), repeat=2))

R = roots()
r = (1, 1, 0, 0)
neg = lambda x: tuple(-a for a in x)
dot = lambda x, y: sum(a*b for a,b in zip(x,y))
sigma = lambda x: tuple(r[i]-x[i] for i in range(4))
assert len(R) == len(set(R)) == 24
edges = [(x,y) for x,y in combinations(R, 2) if dot(x,y) == 1]
assert len(edges) == 96


def graph(vertices):
    V = set(vertices)
    g = {x: set() for x in V}
    for x,y in edges:
        if x in V and y in V:
            g[x].add(y)
            g[y].add(x)
    return g


def bfs(g,start):
    d = {start: 0}
    q = deque((start,))
    while q:
        v = q.popleft()
        for z in g[v]:
            if z not in d:
                d[z] = d[v]+1
                q.append(z)
    assert len(d) == len(g)
    return d

G=graph(R)
assert all(len(G[x])==8 for x in R)
A=sorted(x for x in R if dot(r,x)==1)
B=sorted(neg(x) for x in A)
assert len(A)==len(B)==8 and set(A).isdisjoint(B)
H = {'L':graph(x for x in R if x!=r),
     'I':graph(x for x in R if x not in (r,neg(r))),
     'R':graph(x for x in R if x!=neg(r))}
d = {k:{x:bfs(v,x) for x in v} for k,v in H.items()}
checks=0
for key, g in H.items():
    assert max(z for v in d[key].values() for z in v.values())==3
    checks+=1
    for seam in ([A] if key=='L' else [B] if key=='R' else [A,B]):
        cube=graph(seam)
        assert all(len(cube[x])==3 for x in seam)
        cd={x:bfs(cube,x) for x in seam}
        for x in seam:
            for y in seam:
                assert d[key][x][y]==cd[x][y]
                checks+=1


def phi(a,b):
    return 0 if a==b else 2 if a==sigma(b) else 1

for a in A:
    assert sigma(sigma(a))==a and sigma(a) in A
    for b in A:
        assert phi(a,b)==phi(b,a)
        assert phi(sigma(a),sigma(b))==phi(a,b)
        assert d['I'][neg(a)][b] == 1 + phi(a,sigma(b))
        checks+=3
        for c in A:
            assert phi(a,c)<=phi(a,b)+phi(b,c)
            checks+=1

# Distances across an intermediate cell = T=1+phi(a,sigma(b)).
# Since phi is a metric, min-plus phi*phi=phi; sigma is an isometry;
# hence T^{*p}(a,b)=p+phi(a,sigma^p(b)) for p>=1.
T=[[d['I'][neg(a)][b] for b in A] for a in A]
for p in (1,2,3,4):
    X=[[0 if i==j else 10**8 for j in range(8)] for i in range(8)]
    for _ in range(p):
        X=[[min(X[i][k]+T[k][j] for k in range(8)) for j in range(8)] for i in range(8)]
    for i,a in enumerate(A):
        for j,b in enumerate(A):
            assert X[i][j]==p+phi(a, sigma(b) if p%2 else b)
            checks+=1

# Finite endpoint table: removing the universal p contribution,
# max of cross-cell endpoint corrections is 4 with multiplicity 9
# for L/R and 8 for all other end/interior combinations.
for left,right in (('L','R'),('L','I'),('I','R'),('I','I')):
    for parity in (0,1,2):
        top=[]
        for x in H[left]:
            U=[d[left][x][a] for a in A]
            for y in H[right]:
                V=[d[right][neg(b)][y] for b in A]
                if parity==0: # p=0: exact identity kernel
                    c=min(U[i]+V[i] for i in range(8))
                else: # p odd/even positive
                    c=min(U[i]+phi(a,sigma(b) if parity==1 else b)+V[j]
                          for i,a in enumerate(A) for j,b in enumerate(A))
                assert c<=4
                if c==4:top.append((x,y))
                checks+=1
        assert len(top)==(9 if (left,right)==('L','R') else 8)
        if (left,right)==('L','R'):
            target={(neg(r),r)}
            target.update((x,neg(x) if parity==1 else tuple(x[i]+r[i] for i in range(4)))
                          for x in R if dot(r,x)==-1)
            assert set(top)==target
            checks+=1

# Independently construct the full quotient graph for a finite chain;
# this is only a corroborative check of the proved general theorem.
def chain(m):
    all_nodes={(i,x) for i in range(m) for x in R}
    parent={q:q for q in all_nodes}
    def find(a):
        while parent[a]!=a:
            parent[a]=parent[parent[a]]
            a=parent[a]
        return a
    for i in range(m-1):
        for x in A:
            u,v=find((i,x)),find((i+1,neg(x)))
            parent[u]=v
    removed={(i,r) for i in range(m-1)}|{(i,neg(r)) for i in range(1,m)}
    g={find(q):set() for q in all_nodes if q not in removed}
    for i in range(m):
        for x,y in edges:
            if (i,x) in removed or (i,y) in removed:continue
            a,b=find((i,x)),find((i,y))
            assert a!=b
            g[a].add(b);g[b].add(a)
    return g

for m in range(2,9):
    C=chain(m)
    assert len(C)==14*m+10
    dd={x:bfs(C,x) for x in C}
    hist=Counter(dd[x][y] for x,y in combinations(C.keys(),2))
    assert max(hist)==m+2 and hist[m+2]==9
    assert hist[1]==68*m+28
    if m==2:assert hist=={1:164,2:374,3:156,4:9}
    checks+=len(C)*(len(C)-1)//2

print('PASS: finite kernels, endpoint multiplicities, and chain BFS checks.')
print('Exact assertions performed:',checks)
print('At m=2: 38 facets; 164 facet-adjacency edges; distance counts (164,374,156,9).')
print('All m>=2 theorem: diameter m+2; exactly nine diametral facet pairs.')
