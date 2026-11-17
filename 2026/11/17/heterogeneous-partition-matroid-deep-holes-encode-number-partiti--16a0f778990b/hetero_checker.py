#!/usr/bin/env python3
"""Exact checks for heterogeneous partition-matroid deep-hole theorem.

Standard library only; enumerates 0/1 vertices and independently certifies
least-squares projections by blockwise support inequalities.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import comb


def phi(q,c,j):
    if 0<=j<=c: return F((c-j)**2,q-j)
    if c<j<=q: return F((j-c)**2,j)
    raise ValueError((q,c,j))


def compressed_candidates(qs,cs):
    R=sum(cs); m=len(qs)
    vals=[]
    for flags in product([0,1],repeat=m):
        # All vertices at 0/q_i or at most one genuinely partial coordinate
        for t in range(m):
            if flags[t]: continue
            js=[qs[i]*flags[i] for i in range(m)]
            rem=R-sum(js)
            if 0<=rem<=qs[t]:
                js[t]=rem
                vals.append(tuple(js))
    # some full/zero profiles can have multiple representations, deduplicate
    return sorted(set(vals))


def dist_formula(qs,cs,js):
    return sum((phi(q,c,j) for q,c,j in zip(qs,cs,js)), F(0))


def projection_and_residual(qs,cs,S):
    n=sum(qs); S=set(S); y=[F(0)]*n
    offset=0; js=[]
    for q,c in zip(qs,cs):
        ones=[i for i in range(offset,offset+q) if i in S]
        j=len(ones); js.append(j)
        if j<=c:
            for i in range(offset,offset+q):
                y[i]= F(1) if i in S else F(c-j,q-j)
        else:
            for i in ones: y[i]=F(c,j)
        assert sum(y[offset:offset+q])==c
        offset+=q
    r=[F(int(i in S))-y[i] for i in range(n)]
    d=sum(z*z for z in r)
    # Exact projection certificate: r dot y equals max of r dot any base.
    offset=0; support=F(0)
    for q,c in zip(qs,cs):
        support+=sum(sorted(r[offset:offset+q],reverse=True)[:c])
        offset+=q
    assert support==sum(a*b for a,b in zip(r,y))
    assert d==dist_formula(qs,cs,js)
    return d,tuple(js)


def exhaustive():
    specs=[]
    # every heterogeneous two- and three-block profile with sizes 2/3;
    # a few four-block and size-four profiles stress strict convexity.
    for m in [2,3,4]:
        for qs in product([2,3],repeat=m):
            for cs in product(*[range(1,q) for q in qs]):
                specs.append((qs,cs))
    specs += [((2,4,3),(1,2,1)),((3,4,4),(2,1,3)),
              ((4,4,4),(2,2,2)),((2,4,6),(1,2,3)),
              ((2,4,4,2),(1,2,2,1))]
    total=0; cases=0; nmax=0
    for qs,cs in specs:
        R=sum(cs); n=sum(qs)
        if comb(n,R)>50000:continue
        cases+=1
        candidate=compressed_candidates(qs,cs)
        opt=max(dist_formula(qs,cs,js) for js in candidate)
        actualmax=F(-1); maxjs=set(); ns=0
        for S in combinations(range(n),R):
            d,js=projection_and_residual(qs,cs,S)
            if d>actualmax:actualmax=d;maxjs={js};ns=1
            elif d==actualmax: maxjs.add(js);ns+=1
            total+=1
        assert actualmax==opt,(qs,cs,actualmax,opt)
        assert all(sum(0<j<q for q,j in zip(qs,js))<=1 for js in maxjs)
        nmax+=ns
    print(f'HETEROGENEOUS_COMPRESSION_PASS configurations={cases} exact_vertices={total} maximal_vertices={nmax}')


def partition_tests():
    tested=0; yes=0
    for m in range(2,6):
        for aa in product(range(1,5),repeat=m):
            total=sum(aa)
            # A counterfactual independent enumeration of subset sums.
            partitions=any(sum(aa[i] for i in range(m) if mask>>i&1)*2==total for mask in range(1<<m))
            qs=tuple(2*a for a in aa); cs=aa
            mx=max(dist_formula(qs,cs,js) for js in compressed_candidates(qs,cs))
            assert (mx==F(total,2))==partitions,(aa,mx,partitions)
            if partitions: yes+=1
            tested+=1
    print(f'PARTITION_THRESHOLD_PASS instances={tested} yes_instances={yes}')


if __name__=='__main__':
    exhaustive()
    partition_tests()
