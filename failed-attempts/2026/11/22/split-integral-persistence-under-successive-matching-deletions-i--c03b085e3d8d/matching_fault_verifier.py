#!/usr/bin/env python3
"""Independent finite tests for the integral matching-fault filtration theorem.

Only elementary modular linear algebra is used. Exact integral arguments are
provided separately in the written proof; finite-field checks are not a proof
for arbitrarily large parameters.
"""
from itertools import combinations


def rank_mod(columns, p):
    pivots = {}
    for col in columns:
        v = {i: int(x) % p for i, x in enumerate(col) if x % p}
        while v:
            i = min(v)
            if i not in pivots:
                c = pow(v[i], -1, p)
                pivots[i] = {j: (c*x) % p for j, x in v.items() if c*x % p}
                break
            f = v[i]
            for j,x in pivots[i].items():
                nv = (v.get(j, 0)-f*x) % p
                if nv: v[j] = nv
                else: v.pop(j, None)
    return len(pivots)


def nullspace_columns(columns, nrows, p):
    # Inputs are column vectors of length nrows; find coefficient kernel.
    pivot = {}  # row -> (normalized image, coefficient vector)
    n = len(columns)
    result = []
    for colidx, column in enumerate(columns):
        v = {i: column[i] % p for i in range(nrows) if column[i] % p}
        w = {colidx: 1}
        while v:
            i = min(v)
            if i not in pivot:
                f = pow(v[i], -1, p)
                pivot[i] = ({j: x*f % p for j,x in v.items() if x*f % p},
                            {j: x*f % p for j,x in w.items() if x*f % p})
                break
            b, c = pivot[i]; f = v[i]
            for j,x in b.items():
                y = (v.get(j,0)-f*x) % p
                if y: v[j] = y
                else: v.pop(j,None)
            for j,x in c.items():
                y = (w.get(j,0)-f*x) % p
                if y: w[j] = y
                else: w.pop(j,None)
        else:
            result.append(tuple(w.get(j,0) for j in range(n)))
    return result


def stage(a,b,t):
    eidx = {(i,j): i*b+j for i in range(a) for j in range(b)}
    # Each triangle is oriented so its relative boundary has exactly one +1
    # at a mixed edge, and one -1 at the diagonal mixed edge.
    triangles=[]; lookup={}; boundary2=[]
    for s in range(t):
        for i in range(a):
            if i == s: continue
            lookup['L',s,i] = len(triangles)
            triangles.append(('L',s,i))
            v=[0]*(a*b);v[eidx[i,s]]=1;v[eidx[s,s]]=-1
            boundary2.append(v)
        for j in range(b):
            if j == s: continue
            lookup['R',s,j] = len(triangles)
            triangles.append(('R',s,j))
            v=[0]*(a*b);v[eidx[s,j]]=1;v[eidx[s,s]]=-1
            boundary2.append(v)
    boundary3=[]
    for i,j in combinations(range(t),2):
        v=[0]*len(triangles)
        for k,sgn in [(('L',i,j),1),(('R',j,i),-1),(('L',j,i),1),(('R',i,j),-1)]:
            v[lookup[k]] += sgn
        boundary3.append(v)
    return boundary2,boundary3


def brute_faces(a,b,t):
    # Compare the complete classification of mixed faces (at most 4 vertices)
    # with independent graph-induced maximum degree <=1 tests.
    vertices=[('A',i) for i in range(a)]+[('B',j) for j in range(b)]
    accepted=set()
    for count in range(2,min(a+b,6)+1):
        for face in combinations(vertices,count):
            if len({side for side,_ in face}) != 2: continue
            deg={v:0 for v in face}
            for u,v in combinations(face,2):
                if u[0]==v[0]: continue
                if u[1]==v[1] and u[1]<t: continue
                deg[u]+=1;deg[v]+=1
            if max(deg.values())<=1: accepted.add(frozenset(face))
    predicted=set()
    for i in range(a):
        for j in range(b): predicted.add(frozenset([('A',i),('B',j)]))
    for s in range(t):
        for i in range(a):
            if i!=s: predicted.add(frozenset([('A',s),('A',i),('B',s)]))
        for j in range(b):
            if j!=s: predicted.add(frozenset([('A',s),('B',s),('B',j)]))
    for i,j in combinations(range(t),2):
        predicted.add(frozenset([('A',i),('A',j),('B',i),('B',j)]))
    assert accepted==predicted, (a,b,t,len(accepted),len(predicted),accepted^predicted)


def run():
    ncases=0;nchecks=0
    for a in range(3,6):
        for b in range(a,7):
            prev=None
            for t in range(a+1):
                brute_faces(a,b,t)
                d2,d3=stage(a,b,t)
                for p in (2,3,5):
                    assert all(all(z==0 for z in [sum(d2[c][v]*col[c] for c in range(len(d2))) for v in range(a*b)]) for col in d3)
                    r2=rank_mod(d2,p);r3=rank_mod(d3,p)
                    b1=(a*b-1)-r2
                    b2=len(d2)-r2-r3
                    want1=a*b-1 if t==0 else (a-t)*(b-t)
                    want2=0 if t==0 else (t-1)*(t-2)//2
                    assert (b1,b2)==(want1,want2), (a,b,t,p,b1,b2)
                    if prev is not None:
                        old2,old3=prev
                        old_null=nullspace_columns(old2,a*b,p)
                        padded=[tuple(v)+(0,)*(len(d2)-len(v)) for v in old_null]
                        new_image_rank=rank_mod(d3+padded,p)-r3
                        assert new_image_rank == (0 if t==1 else (t-2)*(t-3)//2), (a,b,t,p,new_image_rank)
                        # H1 maps are quotient projections from a common
                        # degree-one augmented chain lattice, hence surjective.
                    nchecks+=1
                prev=d2,d3;ncases+=1
    print('PASS: %d stages; %d modular checks over primes 2, 3, 5' %(ncases,nchecks))
    print('PASS: all mixed faces independently enumerated; every tetrahedron boundary squared to zero')
    print('PASS: all integral rank predictions modulo three primes; H2 inclusion-image ranks')
    print('LIMIT: finite modular tests only; integral split and infinite family proven in RESULT.md')

if __name__=='__main__': run()
