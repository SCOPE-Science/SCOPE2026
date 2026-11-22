#!/usr/bin/env python3
"""Check full first/second moment generating functions by two unrelated enumerations."""
from itertools import product
from math import comb


def compositions(n,r):
    if r==1:
        yield (n,)
    else:
        for i in range(n+1):
            for tail in compositions(n-i,r-1):
                yield (i,)+tail


def spectrum(g):
    f=[1]
    for c in g:
        q=[0]*(len(f)+c)
        for j,coeff in enumerate(f):
            for t in range(c+1):q[j+t]+=coeff
        f=q
    return f


def pair_series_coeff(m,r):
    """Expand H(x,y,z)^r, H=sum_c x^c F_c(y)F_c(z), to x^m."""
    state={(0,0,0):1}
    for _ in range(r):
        new={}
        for (cost,u,v),w in state.items():
            for c in range(m-cost+1):
                for j in range(c+1):
                    for k in range(c+1):
                        key=(cost+c,u+j,v+k)
                        new[key]=new.get(key,0)+w
        state=new
    return {(j,k):v for (cost,j,k),v in state.items() if cost==m}


def check(m,r):
    cc=list(compositions(m,r))
    assert len(cc)==comb(m+r-1,r-1)
    rows=[spectrum(g) for g in cc]
    expected={(j,k):sum(row[j]*row[k] for row in rows) for j in range(m+1) for k in range(m+1)}
    computed=pair_series_coeff(m,r)
    assert expected==computed,(m,r)
    for k in range(m+1):
        s=sum(row[k] for row in rows)
        assert s==comb(r+k-1,k)*comb(r+m-k-1,m-k)
    total=[sum(row) for row in rows]
    first=sum(total)
    second=sum(x*x for x in total)
    assert first==comb(m+2*r-1,2*r-1)
    second_theory=sum(comb(r,j)*comb(m-j+3*r-1,3*r-1) for j in range(min(r,m)+1))
    assert second==second_theory, (m,r,second,second_theory)
    return len(cc)*(m+1)**2

if __name__=='__main__':
    checks=0
    for m in range(0,8):
        for r in range(1,5):
            checks+=check(m,r)
    print(f'Passed {8*4} (m,r) parameter pairs and {checks} exact second-moment cells; total-ambiguity first/second moments matched independently.')
