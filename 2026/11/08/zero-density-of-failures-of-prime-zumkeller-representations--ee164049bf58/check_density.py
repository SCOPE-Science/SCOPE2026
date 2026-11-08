"""Finite checks of the prime-block density envelope, not an infinite proof."""
from fractions import Fraction
from math import pi,prod,isqrt,gcd

def primes_below(n):
    a=bytearray(b'\x01')*(n+1);a[0:2]=b'\x00\x00'
    for d in range(2,isqrt(n)+1):
        if a[d]:a[d*d::d]=b'\x00'*((n-d*d)//d+1)
    return [i for i in range(2,n+1) if a[i]]

p=primes_below(20000)
checks=0
for k in [2,3,4,5,6,8,10,12,15,18,20]:
    S=Fraction(1); PHI=Fraction(1);last=None
    for q in p[k-1:]:
        S*=Fraction(q+1,q); PHI*=Fraction(q-1,q);last=q
        if S>=2:break
    else:raise AssertionError('increase sieve')
    assert S<2*Fraction(last+1,last)
    assert PHI>Fraction(3,10)
    assert 0<PHI<1
    checks+=1
    if k in [2,4,10,20]:
        print('BLOCK',k,'start',p[k-1],'end',last,'phi_ratio',round(float(PHI),7),'sigma_ratio',round(float(S),7))
assert Fraction(3,10)<3/pi**2
# Direct partition for the classic small odd Zumkeller seed.
def divs(n):return [d for d in range(1,n+1) if n%d==0]
def ztest(n):
    D=divs(n);s=sum(D)
    if s%2:return False
    bits=1;mask=(1<<(s//2+1))-1
    for d in D:bits=(bits|(bits<<d))&mask
    return bool(bits>>(s//2)&1)
assert ztest(945)
for t in range(21): assert ztest(945*(1+945*t)),t
print('RATIONAL_PRIME_BLOCK_CHECKS_OK',checks,'ODD_SEED_MULTIPLIERS_OK',21)
print('Infinity rests on the cited established prime-block Zumkeller lemma, CRT, and fixed-modulus prime distribution.')
