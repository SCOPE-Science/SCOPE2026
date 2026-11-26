#!/usr/bin/env python3
"""Exact rational certificate for the unitary reciprocal-cube range."""
from fractions import Fraction as F
from itertools import product

def primes_upto(n):
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[0:2] = b'\x00\x00'
    for p in range(2, int(n**0.5) + 1):
        if sieve[p]:
            sieve[p*p:n+1:p] = b'\x00' * ((n-p*p)//p+1)
    return [j for j in range(2, n+1) if sieve[j]]

prime_list = primes_upto(50000)
assert len(prime_list)>3101
for j in range(10,3100):
    p,q=prime_list[j-1:j+1]
    assert q**3<2*p**3, (j,p,q)

for p, followers in [
    (11,[13,17,19]),(13,[17,19,23,29]),(17,[19,23]),
    (19,[23,29,31]),(23,[29,31,37])]:
    y=F(1)
    for q in followers:y*=1+F(1,q**3)
    assert y>1+F(1,p**3),(p,followers)

Q=1000
T_low=F(1)
for p in prime_list:
    if p>Q:break
    if p>=11:T_low*=1+F(1,p**3)
T_high=T_low/(1-F(1,2*Q**2))
assert T_low < T_high
head_primes=(2,3,5,7)
max_exponents=(4,2,2,2)
for p,A in zip(head_primes,max_exponents):
    assert 1+F(1,p**(3*A))<=T_low

xs=[]
for ix in product(*[range(A+1) for A in max_exponents]):
    x=F(1)
    for p,a in zip(head_primes,ix):
        if a:x*=1+F(1,p**(3*a))
    xs.append((x,ix))
xs.sort()
assert len(xs)==135 and len(set(x for x,_ in xs))==135

def clusters(T):
    c=[]
    for j,(x,ix) in enumerate(xs):
        if c and x<=c[-1][1]:
            lo,hi,inds=c[-1]
            c[-1]=(lo,max(hi,x*T),inds+[j])
        else:c.append((x,x*T,[j]))
    return c

low=clusters(T_low)
high=clusters(T_high)
assert len(low)==len(high)==14, (len(low),len(high))
assert [x[2] for x in low]==[x[2] for x in high]
for lc,hc in zip(low,high):
    assert lc[0]==hc[0]
    assert lc[1]<hc[1]

# Component index tuples and rational factors; all comparisons above are exact.
print('VERIFY_OK',
      'prime_ratio_indices',3090,
      'small_prime_tail_cases',5,
      'head_products',len(xs),
      'connected_components',len(low),
      'prime_product_cutoff',Q)
print('T_decimal_bounds %.15f %.15f'%(float(T_low),float(T_high)))
for i,(l,r,inds) in enumerate(low,1):
    mx=max((xs[j] for j in inds),key=lambda z:z[0])
    print('COMPONENT',i,'lower_pattern',xs[inds[0]][1],
        'upper_pattern',mx[1], 'interval_count',len(inds),
        'endpoint_lower',f'{float(l):.12f}',
        'endpoint_upper',f'{float(mx[0]*T_high):.12f}')
