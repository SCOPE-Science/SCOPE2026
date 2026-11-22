"""Exact finite checks for automorphism orbits of ideals in k[x,y]/(x^2,xy,y^N).
Only prime fields are needed for small checks; the proof covers every field.
"""
from itertools import combinations, product
from collections import deque, Counter


def rref(rows, q, n):
    rows = [list(x) for x in rows if any(x)]
    pivots=[]; h=0
    for c in range(n):
        t=next((i for i in range(h,len(rows)) if rows[i][c]%q),None)
        if t is None: continue
        rows[h],rows[t]=rows[t],rows[h]
        inv=pow(rows[h][c],-1,q)
        rows[h]=[(v*inv)%q for v in rows[h]]
        for i in range(len(rows)):
            if i!=h and rows[i][c]:
                z=rows[i][c]
                rows[i]=[(a-z*b)%q for a,b in zip(rows[i],rows[h])]
        pivots.append(c);h+=1
        if h==len(rows):break
    return tuple(tuple(x) for x in rows[:h])


def all_subspaces(n,q):
    for dim in range(n+1):
        for piv in combinations(range(n),dim):
            nonp=[j for j in range(n) if j not in piv]
            frees=[(i,j) for i,p in enumerate(piv) for j in nonp if j>p]
            for values in product(range(q),repeat=len(frees)):
                mat=[[1 if j==p else 0 for j in range(n)] for p in piv]
                for (i,j),val in zip(frees,values): mat[i][j]=val
                yield tuple(tuple(row) for row in mat)


def stable(vectors,q,n):
    images=[]
    for row in vectors:
        images.append(tuple([0,0]+list(row[1:n-1])))
    return len(rref(list(vectors)+images,q,n))==len(vectors)


def aut_generators(n,q):
    # image basis vectors for y->y+x, x->x+y^(n-1), x->2x, y->2y
    gens=[]
    mat=[list(int(i==j) for j in range(n)) for i in range(n)]
    mat[1][0]=1; gens.append(mat)
    mat=[list(int(i==j) for j in range(n)) for i in range(n)]
    mat[0][n-1]=1;gens.append(mat)
    if q>2:
        mat=[list(int(i==j) for j in range(n)) for i in range(n)];mat[0][0]=2;gens.append(mat)
        mat=[[0]*n for _ in range(n)];mat[0][0]=1
        for j in range(1,n):mat[j][j]=pow(2,j,q)
        gens.append(mat)
    return gens


def act(basis,g,q,n):
    return rref([[sum(row[i]*g[i][j] for i in range(n))%q for j in range(n)] for row in basis],q,n)


def run(n,q):
    ideals=set(b for b in all_subspaces(n,q) if stable(b,q,n))
    expected=(n-1)*q+n+1  # proper ideals, all contained in the radical
    assert len(ideals)==expected,(n,q,len(ideals),expected)
    generators=aut_generators(n,q)
    for g in generators:
        assert all(act(B,g,q,n) in ideals for B in ideals)
    remaining=set(ideals);lengths=[]
    while remaining:
        start=next(iter(remaining));remaining.remove(start); queue=deque([start]); sz=0
        while queue:
            B=queue.popleft();sz+=1
            for g in generators:
                C=act(B,g,q,n)
                if C in remaining:
                    remaining.remove(C);queue.append(C)
        lengths.append(sz)
    expected_orbits=3*n-3  # add one orbit for the full ring
    assert len(lengths)==expected_orbits,(n,q,len(lengths),expected_orbits,Counter(lengths))
    print(f'CHECK n={n} q={q}: ideals={len(ideals)} orbits={len(lengths)}, orbit_sizes={dict(sorted(Counter(lengths).items()))}')


if __name__=='__main__':
    for n in range(3,7): run(n,2)
    for n in range(3,6): run(n,3)
    print('ARTIN_IDEAL_ORBIT_TESTS_PASSED')
