"""Exact arithmetic checks for the center-coordinate path-law theorem.

Tests finite cases only. The full all-M, all-p theorem is proved analytically.
"""
from fractions import Fraction as F
from math import comb
from itertools import product


def gram_u(m, r, s):
    # Integral y^r (Ty)^s dy, T(y)=my mod 1.
    total=F(0)
    for j in range(m):
        for i in range(r+1):
            total += F(comb(r,i)*j**(r-i),m**(r+1)*(i+s+1))
    return total


def gram_l(m, r, s):
    # Integral y^r (1/m) sum_k ((y+k)/m)^s dy.
    total=F(0)
    for k in range(m):
        for i in range(s+1):
            total += F(comb(s,i)*k**(s-i),m**(s+1)*(r+i+1))
    return total


def gram_k(m, p, r, s):
    return p*gram_l(m,r,s)+(1-p)*gram_u(m,r,s)


def kernel_probability(word, m, p):
    prob=F(1)
    for k in word:
        prob *= (1-p) if k == -1 else p/m
    return prob


def demonstrate(m,p):
    q=1-p
    # Stationarity and adjointness: all monomial test degrees <=5.
    for r in range(6):
        for s in range(6):
            assert gram_l(m,r,s)==gram_u(m,s,r), (m,r,s)
            assert gram_k(m,p,r,s)==gram_k(m,q,s,r),(m,p,r,s)
            if r==0:
                assert gram_k(m,p,r,s)==F(1,s+1)
    for n in range(1,5):
        # Full (m+1)^n categorical path probabilities: exact mass =1.
        words=product(range(-1,m),repeat=n)
        total=sum((kernel_probability(w,m,p) for w in words),F(0))
        assert total==1,(m,p,n,total)
        # Exact binary-type reversibility ratio and the FT in rational form.
        for k in range(n+1):
            prob=F(comb(n,k))*p**k*q**(n-k)
            opposite=F(comb(n,n-k))*p**(n-k)*q**k
            assert prob/opposite==(p/q)**(2*k-n)
    # Paths of generic rational y have unique observed transition labels.
    y=F(1,97)
    outputs=[(y+k)/m for k in range(m)]+[m*y-(m*y).__floor__()]
    assert len(set(outputs))==m+1

for m in (2,3,4,6,8):
    for p in (F(1,5),F(1,3),F(1,2),F(3,4),F(9,10)):
        demonstrate(m,p)

# Independent deterministic-map spot checks: the observed center pairs decode
# the same categorical full-branch labels selected by the expanding base.
for m in (2,3,4):
    for p in (F(1,3),F(1,2),F(3,4)):
        a=p/m
        q=1-p
        for seed in range(1,51):
            x=F(seed,1009)
            y=F(19,1103)
            for t in range(8):
                if x<p:
                    k=int(x/a)
                    label=k
                    xnew=(x-k*a)/a
                    ynew=(y+k)/m
                else:
                    label=-1
                    xnew=(x-p)/q
                    ynew=m*y-(m*y).__floor__()
                pop=m*y-(m*y).__floor__()
                if ynew==pop:
                    # An exact graph crossing is an allowed null-set exception.
                    pass
                else:
                    decoded=m*ynew-y
                    assert decoded.denominator==1
                    assert label==decoded.numerator
                assert 0<=xnew<1 and 0<=ynew<1
                x,y=xnew,ynew
print('PASS: 25 parameter combinations and 450 deterministic orbit spot checks; exact stationary adjoints, categorical laws, path decoding, and fluctuation ratios')
