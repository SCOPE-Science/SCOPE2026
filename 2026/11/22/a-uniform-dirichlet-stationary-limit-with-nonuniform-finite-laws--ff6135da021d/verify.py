"""Exact finite-state checks for multipartite zealot voter dynamics."""
from fractions import Fraction as F
from itertools import product
from collections import defaultdict
import json
from pathlib import Path


def states(r,n):
    return product(range(r), repeat=r*(n-1))


def free_index(j,t,n):
    return j*(n-1)+t


def transitions(s,r,n):
    """Generator off-diagonal rates, including multiplicities of donor vertices."""
    rate = F(1,(r-1)*n)
    out = defaultdict(F)
    for j in range(r):
        for t in range(n-1):
            at=free_index(j,t,n)
            for k in range(r):
                if k==j: continue
                donor_colours = [k]+[s[free_index(k,u,n)] for u in range(n-1)]
                for c in donor_colours:
                    if c==s[at]:continue
                    q=list(s);q[at]=c
                    out[tuple(q)]+=rate
    return out


def local(s,r,n):
    x=[[F(int(j==a)+sum(s[free_index(j,t,n)]==a for t in range(n-1)),n)
       for a in range(r)] for j in range(r)]
    p=[sum(x[j][a] for j in range(r))/r for a in range(r)]
    return x,p


def check_local(r,n):
    count=0
    for s in states(r,n):
        s=tuple(s)
        x,p=local(s,r,n)
        T=transitions(s,r,n)
        # Check both the shore moment identity and the exact global drift.
        for a in range(r):
            lhs=sum(rate*(local(t,r,n)[1][a]-p[a]) for t,rate in T.items())
            assert lhs==(1-r*p[a])/F(r*n)
            for j in range(r):
                lhs2=sum(rate*(local(t,r,n)[0][j][a]-x[j][a]) for t,rate in T.items())
                away=sum(x[k][a] for k in range(r) if k!=j)/(r-1)
                assert lhs2==F(n-1,n)*away-x[j][a]+F(int(j==a),n)
        count+=1
    return count


def check_certificate():
    p=Path(__file__).resolve().with_name('FINITE_CERTIFICATE.json')
    c=json.loads(p.read_text(encoding='utf-8'))
    r,n=3,2
    S=list(states(r,n));idx={s:i for i,s in enumerate(S)}
    w=c['integer_stationary_weights']
    assert len(w)==len(S)==27 and sum(w)==c['normalizing_sum']==8100
    assert all(isinstance(x,int) and x>=0 for x in w)
    balance=[F(0) for _ in S]
    for i,s in enumerate(S):
        T=transitions(s,r,n)
        balance[i]-=w[i]*sum(T.values())
        for t,rate in T.items():balance[idx[t]]+=w[i]*rate
    assert all(z==0 for z in balance)
    masses=defaultdict(F)
    for s,weight in zip(S,w):
        key=tuple(s.count(c) for c in range(3))
        masses[key]+=F(weight,8100)
    corners=[key for key in masses if 3 in key]
    boundary=[key for key in masses if 2 in key]
    assert len(corners)==3 and len(boundary)==6
    assert all(masses[key]==F(46,405) for key in corners)
    assert all(masses[key]==F(13,135) for key in boundary)
    assert masses[(1,1,1)]==F(11,135)
    assert sum(masses.values())==1
    for a in range(3):
        for j in range(3):
            mean=sum(F(w[i],8100)*local(s,r,n)[0][j][a] for i,s in enumerate(S))
            expected=F(n+r-2,r*n-1) if j==a else F(n-1,r*n-1)
            assert mean==expected
    return len(S)


if __name__=='__main__':
    assert check_local(3,2)==27
    assert check_local(3,3)==729
    assert check_local(4,2)==256
    assert check_certificate()==27
    print('MULTIPARTITE_VOTER_EXACT_CHECKS_PASSED 1012 local configurations and 27 state stationarity balances')
