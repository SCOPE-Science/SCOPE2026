#!/usr/bin/env python3
"""Exact certificate for graph-heat Padé [0/2] positivity through five vertices.

Only Python standard-library integer arithmetic is used. No graph database is
required: all labeled simple graphs on up to five vertices are generated.
"""
from itertools import combinations, permutations
from fractions import Fraction


def trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return tuple(a)


def add(a, b):
    c = [0] * max(len(a), len(b))
    for i, v in enumerate(a): c[i] += v
    for i, v in enumerate(b): c[i] += v
    return trim(c)


def scale(a, k):
    return trim(k * x for x in a)


def mul(a, b):
    c = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if not x: continue
        for j, y in enumerate(b):
            c[i+j] += x*y
    return trim(c)


def parity(p):
    return (-1) ** sum(p[i] > p[j] for i in range(len(p)) for j in range(i+1, len(p)))


def determinant(A):
    n = len(A)
    ans = (0,)
    for perm in permutations(range(n)):
        prod = (1,)
        for i,j in enumerate(perm): prod = mul(prod, A[i][j])
        ans = add(ans,scale(prod,parity(perm)))
    return ans


def cofactor_adjugate(A, i, j):
    # adj(A)[i,j] = (-1)^(i+j) det A without row j, column i
    minor = [[A[r][c] for c in range(len(A)) if c != i]
             for r in range(len(A)) if r != j]
    return scale(determinant(minor), (-1)**(i+j))


def graph_connected(n, edges):
    if n == 1: return True
    seen = {0}
    todo = [0]
    adj = [set() for _ in range(n)]
    for i,j in edges: adj[i].add(j);adj[j].add(i)
    while todo:
        for v in adj[todo.pop()]:
            if v not in seen: seen.add(v);todo.append(v)
    return len(seen)==n


def canonical(n, edges):
    E = {tuple(sorted(e)) for e in edges}
    pairs = list(combinations(range(n), 2))
    return min(tuple(int(tuple(sorted((p[i],p[j]))) in E) for i,j in pairs)
               for p in permutations(range(n)))


def representatives(n):
    pairs = list(combinations(range(n),2))
    cls = {}
    labeled = 0
    for mask in range(1<<len(pairs)):
        edges = tuple(e for k,e in enumerate(pairs) if (mask>>k)&1)
        if not graph_connected(n,edges): continue
        labeled += 1
        cls.setdefault(canonical(n,edges), edges)
    return cls, labeled


def laplacian(n, edges):
    L = [[0]*n for _ in range(n)]
    for i,j in edges:
        L[i][i]+=1;L[j][j]+=1;L[i][j]-=1;L[j][i]-=1
    return L


def poly_matrix(n, edges):
    L = laplacian(n,edges)
    L2 = [[sum(L[i][k]*L[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    # M = 2I+2sL+s^2 L^2, so the update is 2M^{-1}.
    return [[trim((2*int(i==j),2*L[i][j],L2[i][j])) for j in range(n)] for i in range(n)]


def distances(n, edges):
    out=[]
    for x in range(n):
        d=[-1]*n;d[x]=0;Q=[x]
        for u in Q:
            for a,b in edges:
                v = b if u==a else (a if u==b else -1)
                if v >= 0 and d[v]<0: d[v]=d[u]+1; Q.append(v)
        out.append(d)
    return out


def P(s):
    return 5*s**4+40*s**3+42*s**2-4


def main():
    counts=[1,1,2,6,21]
    labeled_counts=[1,1,4,38,728]
    graphs=0; entries=0; exceptional=0
    for n in range(1,6):
        reps, labeled = representatives(n)
        assert (len(reps),labeled)==(counts[n-1],labeled_counts[n-1]), (n,len(reps),labeled)
        for edges in reps.values():
            graphs+=1
            A = poly_matrix(n,edges)
            det = determinant(A)
            assert det[0] == 2**n
            dists = distances(n,edges)
            diam=max(map(max,dists))
            bad=[]
            for i in range(n):
                for j in range(n):
                    q=cofactor_adjugate(A,i,j)
                    entries+=1
                    if any(x<0 for x in q): bad.append((i,j,q))
            if not bad: continue
            exceptional+=1
            assert n==5 and diam==4 and len(bad)==2, (n,edges,bad)
            a,b=next((i,j) for i in range(n) for j in range(n) if dists[i][j]==4)
            assert {v[:2] for v in bad}=={(a,b),(b,a)}
            D1=(4,12,18,6,1)
            D2=(4,20,50,50,25)
            s4P=(0,0,0,0,-4,0,42,40,5)
            for i,j,_ in bad:
                adj=cofactor_adjugate(A,i,j)
                assert scale(mul(adj,mul(D1,D2)),2)==mul(det,s4P)
    assert graphs==31 and exceptional==1
    lo=Fraction(27387026089,10**11)
    hi=Fraction(27387026090,10**11)
    assert P(lo)<0<P(hi)
    print('PASS connected_isomorphism_classes=',graphs, 'cofactor_checks=',entries,
          'exceptional_graphs=',exceptional)
    print('PASS unique_threshold_interval=(27387026089/100000000000, 27387026090/100000000000)')
    print('PASS every other connected graph on at most five vertices: nonnegative polynomial adjugate coefficients')

if __name__=='__main__': main()
