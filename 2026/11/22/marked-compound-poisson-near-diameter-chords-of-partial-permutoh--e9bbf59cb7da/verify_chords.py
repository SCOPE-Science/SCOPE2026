"""Exact finite chord checks for partial permutohedron vertex statistics."""
from fractions import Fraction
from itertools import permutations
from math import comb, exp

def falling(m,k):
    result = 1
    for j in range(k):
        result *= m-j
    return result

def rank_vertices(m,n):
    for k in range(n+1):
        vals = tuple(range(n-k+1, n+1))
        for pos in permutations(range(m),k):
            x=[0]*m
            for i,p in enumerate(pos): x[p]=vals[i]
            yield tuple(x)

def check(m,n):
    assert 2*n <= m
    vs=list(rank_vertices(m,n))
    assert len(vs)==sum(falling(m,k) for k in range(n+1))
    full=[v for v in vs if sum(a>0 for a in v)==n]
    assert len(full)==falling(m,n)
    pairs=len(full)**2
    q=sum(i*i for i in range(1,n+1))
    s=sum(range(1,n+1))
    dot_sum=0
    dot2_sum=0
    zeros=0
    for a in full:
        for b in full:
            dot=sum(t*u for t,u in zip(a,b))
            dot_sum+=dot
            dot2_sum+=dot*dot
            if dot==0: zeros+=1
            assert 2*q-sum((x-y)**2 for x,y in zip(a,b))==2*dot
    exact_m=Fraction(dot_sum,pairs*n*n)
    formula_m=Fraction(s*s,m*n*n)
    assert exact_m==formula_m,(m,n,exact_m,formula_m)
    exact_v=Fraction(dot2_sum,pairs*n**4)-exact_m**2
    formula_v=Fraction((q*m-s*s)**2,(m*m)*(m-1)*n**4)
    assert exact_v==formula_v,(m,n,exact_v,formula_v)
    exact_z=Fraction(zeros,pairs)
    predicted_z=Fraction(comb(m-n,n),comb(m,n))
    assert exact_z==predicted_z,(m,n,exact_z,predicted_z)
    total=len(vs)
    all_zero_full=Fraction(falling(m,n)**2,total*total)*predicted_z
    assert all_zero_full>0
    # For every pair, the diameter equality is equivalent to full rank and disjoint supports.
    all_zeros=0
    for a in vs:
        for b in vs:
            dab=sum((x-y)**2 for x,y in zip(a,b))
            assert dab<=2*q
            if dab==2*q: all_zeros+=1
    assert Fraction(all_zeros,total*total)==all_zero_full
    return (m,n,len(vs),exact_m,exact_v,exact_z)

def factorial_moments(m,n):
    return [Fraction(falling(n,r)**2,falling(m,r)) for r in range(1,n+1)]

if __name__=='__main__':
    tests=[(2,1),(3,1),(4,2),(5,2),(6,2),(6,3),(7,3),(8,3)]
    for m,n in tests:
        print('EXACT',check(m,n))
    for n in (40,100,250):
        m=n*n
        mu=factorial_moments(m,n)
        assert abs(float(mu[0])-1)<1e-12
        assert abs(float(mu[1])-1)<0.06
        assert abs(float(mu[2])-1)<0.20
        p_disjoint=1.0
        for j in range(n):
            p_disjoint *= (m-n-j)/(m-j)
        assert abs(p_disjoint-exp(-1))<0.04
        print('POISSON_FACTORIAL_MOMENTS',n,m,[round(float(x),7) for x in mu[:3]],'diametral_atom',round(p_disjoint,7))
    print('PARTIAL_PERMUTOHEDRON_MARKED_CHORD_PASS')
