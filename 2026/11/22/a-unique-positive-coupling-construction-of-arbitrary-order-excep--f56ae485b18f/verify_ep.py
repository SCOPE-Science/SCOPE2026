#!/usr/bin/env python3
"""Exact-rational checks for the terminal-loss exceptional-point design."""
from fractions import Fraction
from math import comb

def add(a,b):
    out=[Fraction(0)]*max(len(a),len(b))
    for k,v in enumerate(a): out[k]+=v
    for k,v in enumerate(b): out[k]+=v
    return trim(out)
def trim(a):
    while len(a)>1 and a[-1]==0: a.pop()
    return a
def scale(a,c): return [v*c for v in a]
def shift(a): return [Fraction(0)]+a

def power(z0,m):
    return [Fraction(comb(m,k))*z0**(m-k) for k in range(m+1)]

def verify(m,beta):
    assert m>=2 and beta>0
    qs=[[Fraction(1)],[Fraction(0),Fraction(1)]]
    couplings=[]
    for k in range(1,m):
        c=beta**2*Fraction(k*(2*m-k),(2*(m-k)-1)*(2*(m-k)+1))
        assert c>0
        couplings.append(c)
        qs.append(add(shift(qs[-1]),scale(qs[-2],c)))
    p=add(qs[m],scale(qs[m-1],m*beta))
    assert p==power(beta,m)
    expected_even=[v if (k-m)%2==0 else 0 for k,v in enumerate(p)]
    expected_odd=[v/(m*beta) if (k-m)%2 else Fraction(0) for k,v in enumerate(p)]
    assert qs[m]==trim(expected_even)
    assert qs[m-1]==trim(expected_odd)
    # Descending inverse recovery of every coupling, using the final pair only.
    qhi,qlo=qs[m],qs[m-1]
    recovered=[]
    for k in range(m-1,0,-1):
        diff=add(qhi,scale(shift(qlo),-1))
        a=diff[k-1]
        assert a==couplings[k-1]
        qprev=scale(diff,1/a)
        assert qprev==qs[k-1]
        recovered.append(a)
        qhi,qlo=qlo,qprev
    assert recovered==couplings[::-1]

if __name__=='__main__':
    tested=0
    for m in range(2,46):
        for beta in (Fraction(1),Fraction(2,3),Fraction(5,4)):
            verify(m,beta)
            tested+=1
    print('PASS: '+str(tested)+' exact rational m/beta scenarios, including inverse recovery')
