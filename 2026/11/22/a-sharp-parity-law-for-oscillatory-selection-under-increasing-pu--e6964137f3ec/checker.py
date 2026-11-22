"""Exact-rational independent checks for monotone-return selection oscillations.
Python 3 stdlib only; no external datasets or third-party modules.
"""
from fractions import Fraction as Q
from math import comb


def choose(a, b):
    if b < 0 or b > a or a < 0:
        return 0
    return comb(a,b)


def schedule(n):
    eps = Q(1,4)
    d = [None] + [-eps]
    for k in range(2,n):
        d.append(eps * (1 if k % 2 == 0 else -1) / (2**k))
    d.append(-sum(d[1:]))
    r = [Q(0)]
    for k in range(1,n+1):
        r.append(n*n * (1 + sum(d[1:k+1])/k))
    return d,r


def avg_payoff_difference(N, n, i, r):
    """Independent original focal-person hypergeometric payoff calculation."""
    denom=choose(N-1,n-1)
    PC=Q(-1)
    PD=Q(0)
    for j in range(n):
        cp=Q(choose(i-1,j)*choose(N-i,n-1-j),denom)
        dp=Q(choose(i,j)*choose(N-i-1,n-1-j),denom)
        PC+=cp*Q((j+1)*r[j+1],n)
        PD+=dp*Q(j*r[j],n)
    return PC-PD


def coupling_difference(N,n,i,r):
    alpha=Q(N-n,N-1)
    denom=choose(N-2,n-1)
    total=Q(-1)
    for j in range(n):
        prob=Q(choose(i-1,j)*choose(N-i-1,n-1-j),denom)
        increment=Q((j+1)*r[j+1]-j*r[j],n)
        total+=alpha*prob*increment
    return total


def test():
    models=0; evaluated=0; degree_checks=0
    for n in range(2,21):
        d,r=schedule(n)
        N=n+1
        assert all(r[k]>0 for k in range(1,n+1))
        assert all(r[k+1]>r[k] for k in range(1,n))
        assert r[n]==n*n and sum(d[1:])==0
        assert all(Q(k*r[k],n)>Q((k-1)*r[k-1],n) for k in range(1,n+1))
        seq=[]
        for i in range(1,N):
            a=avg_payoff_difference(N,n,i,r)
            b=coupling_difference(N,n,i,r)
            assert a==b==d[i],(N,n,i,a,b,d[i])
            seq.append(a)
            evaluated+=1
        count=sum(x*y<0 for x,y in zip(seq,seq[1:]))
        assert count==(n-1 if n%2==0 else n-2),(n,count)
        assert seq[0]<0 and seq[-1]>0
        models+=1
    # Polynomial finite-difference check with an unrelated, strictly increasing schedule.
    for n in range(2,9):
        N=2*n+5
        r=[Q(0)]+[Q(3+k*k,2) for k in range(1,n+1)]
        seq=[avg_payoff_difference(N,n,i,r) for i in range(1,N)]
        for i in range(1,N):
            assert seq[i-1]==coupling_difference(N,n,i,r)
            evaluated+=1
        vals=seq
        for order in range(1,n+1):
            vals=[b-a for a,b in zip(vals,vals[1:])]
            if order==n:
                assert all(v==0 for v in vals), (n, vals)
                degree_checks+=len(vals)
    print('PASS',models,'exact monotone constructive models;',evaluated,
          'independent payoff/coupling equalities;',degree_checks,
          'zero nth differences; all parity maxima and terminal neutrality checks')

if __name__=='__main__':
    test()
