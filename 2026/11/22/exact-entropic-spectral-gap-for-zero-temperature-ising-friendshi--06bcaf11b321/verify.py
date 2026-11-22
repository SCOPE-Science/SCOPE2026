"""Exact finite-state checks for the ground-state antiferromagnetic friendship chain.

All equations use integer transition rates; no third-party modules are needed.
The all-size spectral and asymptotic argument is mathematical, not an extrapolation
of the finite checks implemented here.
"""
import itertools
from fractions import Fraction
from math import comb


def states(n):
    edges = [(0, 2*i+1) for i in range(n)]
    edges += [(0, 2*i+2) for i in range(n)]
    edges += [(2*i+1, 2*i+2) for i in range(n)]
    return [s for s in itertools.product((-1, 1), repeat=2*n+1)
            if sum(s[u] == s[v] for u, v in edges) == n]


def reduced_bits(s, n):
    return tuple(int(s[2*i+1] != s[2*i+2]) for i in range(n))


def test_generator(n):
    ss=states(n)
    assert len(ss)==2*3**n
    state_set=set(ss)
    for s in ss:
        q=reduced_bits(s,n)
        sign=s[0]
        by_q={}
        for v in range(2*n+1):
            other=s[:v]+(-s[v],)+s[v+1:]
            if other in state_set:
                oq=reduced_bits(other,n)
                by_q[(other[0],oq)]=by_q.get((other[0],oq),0)+1
        expected={}
        for i in range(n):
            qq=q[:i]+(1-q[i],)+q[i+1:]
            expected[(sign,qq)]=expected.get((sign,qq),0)+1+(0 if q[i] else 1)
        if all(q):
            expected[(-sign,q)]=1
        assert by_q==expected,(n,s,by_q,expected)
        for target in itertools.product((0,1),repeat=n):
            # f(s)=hub_sign * indicator(reduced_bits(s)==target)
            realized=sum(
                (other[0]*int(reduced_bits(other,n)==target)-sign*int(q==target))
                for v in range(2*n+1)
                for other in (s[:v]+(-s[v],)+s[v+1:],)
                if other in state_set)
            predicted=sum((2 if q[i]==0 else 1)*
                          (sign*int((q[:i]+(1-q[i],)+q[i+1:])==target)-
                           sign*int(q==target)) for i in range(n))
            predicted-=2*int(all(q))*sign*int(q==target)
            assert realized==predicted,(n,s,target,realized,predicted)
    return len(ss)


def resolvent_diagonal(n,t):
    # solve (H0+tI) u=e_B by rational Gaussian elimination; row generator H0.
    states=list(itertools.product((0,1),repeat=n))
    indices={s:i for i,s in enumerate(states)}
    sz=len(states)
    M=[[Fraction(0) for _ in range(sz+1)] for _ in range(sz)]
    for i,s in enumerate(states):
        M[i][i]=t
        for j in range(n):
            nxt=s[:j]+(1-s[j],)+s[j+1:]
            rate=2 if s[j]==0 else 1
            M[i][i]+=rate
            M[i][indices[nxt]]-=rate
        M[i][-1]=Fraction(1) if all(s) else Fraction(0)
    for i in range(sz):
        pivot=next(j for j in range(i,sz) if M[j][i])
        M[i],M[pivot]=M[pivot],M[i]
        den=M[i][i]
        for k in range(i,sz+1):M[i][k]/=den
        for j in range(i+1,sz):
            a=M[j][i]
            if a:
                for k in range(i,sz+1): M[j][k]-=a*M[i][k]
    out=[Fraction(0)]*sz
    for i in range(sz-1,-1,-1):
        out[i]=M[i][-1]-sum(M[i][j]*out[j] for j in range(i+1,sz))
    return out[-1]


if __name__=='__main__':
    total=0
    for n in range(2,7): total+=test_generator(n)
    for n in range(2,6):
        for t in [Fraction(1,2),Fraction(2,3)]:
            rhs=sum(Fraction(comb(n,k)*2**(n-k),3**n)/
                    (3*k+t) for k in range(n+1))
            assert resolvent_diagonal(n,t)==rhs,(n,t)
    print('FRIENDSHIP_EXACT_CHECKS_PASSED ground_states=',total,'resolvent_cases=',8)
