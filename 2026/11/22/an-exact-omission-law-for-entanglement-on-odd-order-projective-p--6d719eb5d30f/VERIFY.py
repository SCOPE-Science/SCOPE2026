#!/usr/bin/env python3
"""Exact GF(2) checks for entanglement under selected omitted incidence gates.
Finite-field coordinate construction and exact integer Gaussian elimination.
"""
from itertools import product, combinations
import random


def rank2(rows):
    pivots={}
    for x in rows:
        while x:
            j=x.bit_length()-1
            if j not in pivots:
                pivots[j]=x
                break
            x^=pivots[j]
    return len(pivots)


def norm3(v,p):
    for a in v:
        if a%p:
            z=pow(a%p,-1,p)
            return tuple((z*b)%p for b in v)
    raise ValueError('zero vector')


def plane(p):
    seq=range(p)
    vec=sorted({norm3(v,p) for v in product(seq,repeat=3) if v!=(0,0,0)})
    n=p*p+p+1
    assert len(vec)==n
    inc=[[int(sum(x*y for x,y in zip(a,b))%p==0) for b in vec] for a in vec]
    assert all(sum(r)==p+1 for r in inc)
    return vec, inc


def proof_matrix_rank(inc,flags):
    n=len(inc); k=len(flags)
    # C_(ij) = incidence(point of missing edge j, line of missing edge i)
    # diagonal entries are 1; D = I + C in GF(2).
    matrix=[]
    for i, (pi,li) in enumerate(flags):
        row=sum((inc[pj][li] ^ (i==j))<<j for j,(pj,lj) in enumerate(flags))
        matrix.append(row | (1<<k))
    matrix.append((1<<k)-1)
    return n - (k+1-rank2(matrix))


def direct_rank(inc,flags):
    n=len(inc); rows=[sum(bit<<j for j,bit in enumerate(r)) for r in inc]
    for pi,li in flags: rows[pi]^=1<<li
    return rank2(rows)


def random_matching(inc,rng,limit):
    pool=[(i,j) for i,r in enumerate(inc) for j,v in enumerate(r) if v]
    rng.shuffle(pool)
    r=[]; pts=set(); lines=set()
    for i,j in pool:
        if i not in pts and j not in lines:
            r.append((i,j)); pts.add(i); lines.add(j)
            if len(r)==limit:break
    return r


def conic_tangent(vec,p):
    lookup={a:i for i,a in enumerate(vec)}
    pairs=[]
    for t in range(p):
        point=norm3((t*t,t,1),p)
        line=norm3((1,-2*t,t*t),p)
        pairs.append((lookup[point],lookup[line]))
    pairs.append((lookup[norm3((1,0,0),p)],lookup[norm3((0,0,1),p)]))
    return pairs


def check():
    rng=random.Random(94381)
    summary=[]
    for p,trials in [(3,500),(5,750),(7,750),(11,350)]:
        vec,inc=plane(p)
        n=len(vec)
        assert rank2([sum(b<<j for j,b in enumerate(row)) for row in inc])==n-1
        fs=[(i,j) for i,row in enumerate(inc) for j,b in enumerate(row) if b]
        count=0
        for f in fs:
            assert direct_rank(inc,[f])==n
            count+=1
        for _ in range(trials):
            k=rng.randint(1,min(12,n))
            F=random_matching(inc,rng,k)
            assert 1<=len(F)<=k
            actual=direct_rank(inc,F)
            predicted=proof_matrix_rank(inc,F)
            assert actual==predicted,(p,F,actual,predicted)
            count+=1
        # every pair of flags disjoint for p=3, verify reduced matrix exact
        if p==3:
            for a,b in combinations(fs,2):
                if a[0]==b[0] or a[1]==b[1]:continue
                f=[a,b]
                assert direct_rank(inc,f)==proof_matrix_rank(inc,f)
                count+=1
        F=conic_tangent(vec,p)
        assert len(F)==p+1
        assert all(inc[pi][li]==(i==j) for i,(pi,_) in enumerate(F) for j,(_,li) in enumerate(F))
        assert direct_rank(inc,F)==n-p
        assert proof_matrix_rank(inc,F)==n-p
        count+=1
        summary.append((p,n,count,n-1,n,p+1,n-p))
    for a in summary:
        print('q=%d N=%d checks=%d baseline=%d one_failure=%d tangent_matching=%d tangent_result=%d'%a)
    print('ALL EXACT GF(2) CHECKS PASSED')
if __name__=='__main__':check()
