#!/usr/bin/env python3
"""Exact-integer checks for paired level-14 Apéry-like residues modulo five.

Uses only the Python standard library. Finite computations illustrate and
cross-check the stated infinite proof; they do not replace Lucas' theorem or
Fourier orthogonality.
"""
from collections import Counter
from math import factorial

DIGITS = ((1, 1), (0, 1), (3, 4), (4, 4), (0, 0))
G = {((pow(3, j, 5) * pow(4, h, 5)) % 5,
      (pow(4, j, 5) * pow(4, h, 5)) % 5)
     for j in range(4) for h in range(2)}
assert len(G) == 8


def recurrence(epsilon, count):
    a = [1]
    for n in range(count - 1):
        an = a[n]
        am = a[n-1] if n else 0
        amm = a[n-2] if n >= 2 else 0
        rhs = (2*n+1)*((2*epsilon-7)*(n*n+n)+epsilon-4)*an
        rhs -= n*((6*epsilon*epsilon-42*epsilon+13)*n*n
                  +epsilon*epsilon-8*epsilon+11)*am
        rhs += n*(2*n-1)*(n-1)*(2*epsilon**3
                  -21*epsilon*epsilon+13*epsilon+224)*amm
        assert rhs % (n+1)**3 == 0, (epsilon, n)
        a.append(rhs // (n+1)**3)
    return a


def coefficient_series(sign, size=16):
    def mul(a,b):
        c=[0]*size
        for i,x in enumerate(a):
            if x:
                for j,y in enumerate(b[:size-i]):
                    c[i+j]+=x*y
        return c
    def inv(a):
        assert a[0] == 1 or a[0] == -1
        b=[0]*size
        b[0]=a[0]
        for n in range(1,size):
            b[n]=-b[0]*sum(a[i]*b[n-i] for i in range(1,n+1))
        return b
    def power(a,k):
        if k<0:
            return power(inv(a),-k)
        out=[1]+[0]*(size-1)
        while k:
            if k&1:out=mul(out,a)
            a=mul(a,a)
            k//=2
        return out
    def eprod(step):
        f=[1]+[0]*(size-1)
        for m in range(step,size,step):
            t=[1]+[0]*(size-1)
            t[m]=-1
            f=mul(f,t)
        return f
    f1,f2,f7,f14=[eprod(h) for h in (1,2,7,14)]
    w=mul(mul(power(f1,4),power(f14,4)),
          mul(power(f2,-4),power(f7,-4)))
    w=[0]+w[:-1]
    v=[1+sign*w[0]]+[sign*x for x in w[1:]]
    t=mul(w,power(v,-2))
    a=t[1:]+[0]
    z=mul(mul(mul(f1,f2),mul(f7,f14)),inv(a))
    q=[0]*size
    ai=inv(a)
    for k in range(1,size):
        coef=power(ai,k)[k-1]
        assert coef%k==0
        q[k]=coef//k
    out=[0]*size
    qpow=[1]+[0]*(size-1)
    for coefficient in z:
        for k in range(size):
            out[k]+=coefficient*qpow[k]
        qpow=mul(qpow,q)
    return out


def digit_product(n):
    p=(1,1)
    while n:
        d=n%5
        p=((p[0]*DIGITS[d][0])%5,(p[1]*DIGITS[d][1])%5)
        n//=5
    return p


def formula(L):
    out=Counter()
    out[(0,0)]=5**L-4**L
    if L:
        out[(0,1)]=(4**L-3**L+(-1)**(L+1))//2
        out[(0,4)]=(4**L-3**L-(-1)**(L+1))//2
    for j in range(4):
        for h in range(2):
            value=0
            for r in range(L+1):
                if r%4!=j: continue
                for s in range(L-r+1):
                    if s%2!=h: continue
                    value+=factorial(L)//(factorial(r)*factorial(s)*factorial(L-r-s))
            g=((pow(3,j,5)*pow(4,h,5))%5,
               (pow(4,j,5)*pow(4,h,5))%5)
            out[g]=value
    return +out


def main():
    a,b=recurrence(9,400),recurrence(5,400)
    assert a[:11] == [1,5,33,269,2545,26565,295785,
                       3441765,41336145,508419125,6370849633]
    assert b[:11] == [1,1,9,49,385,2961,24801,
                       212409,1878129,16924945,155204329]
    assert a[:13]==coefficient_series(+1)[:13]
    assert b[:13]==coefficient_series(-1)[:13]
    assert tuple((a[d]%5,b[d]%5) for d in range(5)) == DIGITS
    for n in range(400):
        assert (a[n]%5,b[n]%5) == digit_product(n)
    for L in range(0,8):
        f=formula(L)
        direct=Counter(digit_product(n) for n in range(5**L))
        assert direct == f, (L,direct,f)
        assert sum(f.values())==5**L
        assert {g for g in f if f[g]} <= G|{(0,0),(0,1),(0,4)}
        if L>=4: assert {g for g in f if f[g]} == G|{(0,0),(0,1),(0,4)}
    for L in range(0,24):
        f=formula(L)
        assert sum((8*f[g]-3**L)**2 for g in G) == 8*(2*5**L+5)
    assert formula(4)==Counter({(0,0):369,(0,1):87,(0,4):88,
        (1,1):9,(1,4):12,(2,1):16,(2,4):4,
        (3,1):4,(3,4):16,(4,1):12,(4,4):8})
    print('PASS: 400 recurrence terms, 13 independent formal-q coefficients per sequence,')
    print('400 independent digit-product checks, 97,656 indices in complete 5-adic blocks')
    print('through 5^7, and 24 exact group-Fourier Parseval identities.')

if __name__=='__main__':main()
