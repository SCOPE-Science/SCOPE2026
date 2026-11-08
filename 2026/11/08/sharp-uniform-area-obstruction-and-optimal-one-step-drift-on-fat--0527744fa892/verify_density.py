#!/usr/bin/env python3
"""Finite corroboration of the explicit triangular inverse-branch table.
No finite test substitutes for the geometric proof in RESULT.md.
"""
from decimal import Decimal, getcontext
from fractions import Fraction
getcontext().prec = 60
Q = Decimal
qvec = ((0, 0), (1, 0), (0, 1))

def admissible(x, y, i, L):
    # At the preimage (z+q_i)/beta, digit j is legal iff z+q_i-q_j is in Delta.
    valid = []
    for j in range(3):
        xx = x + qvec[i][0] - qvec[j][0]
        yy = y + qvec[i][1] - qvec[j][1]
        if xx >= 0 and yy >= 0 and xx + yy <= L:
            valid.append(j)
    return tuple(valid)

def direct(x, y, L, p, s, t):
    u = Q(1)-s-t
    total = Q(0)
    for i in range(3):
        v = admissible(x,y,i,L)
        if len(v)==1: total += 1
        elif len(v)==2: total += p if i==v[0] else (Q(1)-p)
        elif len(v)==3: total += (s,t,u)[i]
        else: raise AssertionError((x,y,i,v))
    return total

def regional(x, y, L, p, s, t):
    z=x+y; U=L-Q(1)
    if x<Q(1) and y<Q(1):
        return Q(3)-Q(2)*p if z<U else Q(3)
    if x>Q(1) and y<Q(1):
        return Q(2)-s-t if z<U else Q(2)
    if x<Q(1) and y>Q(1):
        return Q(1)+t if z<U else Q(1)+Q(2)*p
    if x>Q(1) and y>Q(1):
        return Q(1) if z<U else Q(1)+s
    raise AssertionError('boundary sample')

def verify():
    rt2=Q(2).sqrt(); checks=0
    for beta in [Q('1.1'), Q('1.23'), Q('1.32'), Q('1.4'), rt2, Q('1.47'),Q('1.5')]:
        L=Q(1)/(beta-Q(1))
        for p,s,t in [(Q('0.5'),Q('0.23'),Q('0.27')),(Q('0.3'),Q('0.11'),Q('0.35')),(Q('0.73'),Q('0.31'),Q('0.12'))]:
            for a in range(1,86):
                for b in range(1,86):
                    x=Q(a)/Q(40);y=Q(b)/Q(40)
                    if x+y>=L or abs(x-Q(1))<Q('0.0001') or abs(y-Q(1))<Q('0.0001') or abs(x+y-(L-Q(1)))<Q('0.0001'):
                        continue
                    assert direct(x,y,L,p,s,t)==regional(x,y,L,p,s,t), (beta,p,s,t,x,y)
                    if beta==rt2 and p==Q('0.5'):
                        z=direct(x,y,L,p,s,t)
                        unique=(x<Q(1) and y<Q(1) and x+y>rt2)
                        assert (z>Q(2))==unique
                    checks+=1
    # Exact algebra by integer identity: (3-2sqrt(2))*(3+2sqrt(2))=1.
    assert 3*3-2*2*2 == 1
    delta=(Q(3)-Q(2)*rt2)**2
    expected=Q(17)-Q(12)*rt2
    assert abs(delta-expected)<Q('1e-52')
    areaG=(Q(2)-rt2)**2/Q(2)
    areaD=(Q(1)+rt2)**2/Q(2)
    assert abs(areaG/(Q(2)*areaD)-expected)<Q('1e-52')
    print('PASS: %d finite exact-decimal branch comparisons, sharp constant %.12f' %(checks, delta))

if __name__=='__main__':verify()
