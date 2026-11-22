#!/usr/bin/env python3
"""Integer-polynomial coefficient checker for maximal double Roman labels on K_2 square K_n."""
from math import comb

def add(*polys):
    r=[0]*max(map(len,polys))
    for p in polys:
        for i,x in enumerate(p): r[i]+=x
    return r

def neg(p): return [-x for x in p]

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): c[i+j]+=x*y
    return c

def scale(p,k): return [k*x for x in p]

def power(p,n):
    v=[1]
    for _ in range(n): v=mul(v,p)
    return v

def mono(k): return [0]*k+[1]

def polynomial(n):
    A=[0,1,1,1]
    E=add(power(A,n),neg(mono(n)))
    safe=add(power([1,1,1,1],n),neg(power(A,n)),
             neg(power([1,1],n)),mono(n),
             neg(scale(mul(mono(2),power([1,1],n-1)),n)),
             scale(mono(n+1),n))
    allpositive=add(mul(E,E),scale(mul(mono(n),power([0,0,1,1],n)),2))
    one2=scale(mul(mul(mono(2),A),
          add(power([0,0,2,2,1],n-1),
              neg(power([0,0,1,1,1],n-1)))),n)
    nohigh=add(power([0,0,0,2,1],n),
               neg(power([0,0,0,1,1],n)),neg(mono(3*n)))
    return add(allpositive,scale(add(mul(E,safe),one2,nohigh),2))

expected={
  3:(7,36,2108),
  4:(8,32,30032),
  5:(9,50,402068),
  6:(10,72,5175000),
}
for n in range(3,15):
    p=polynomial(n)
    terms=[(i,v) for i,v in enumerate(p) if v]
    assert all(v>0 for _,v in terms)
    assert terms[-1]==(6*n,1)
    if n>=4:
        assert [i for i,_ in terms]==list(range(n+4,6*n+1))
        assert p[n+4]==2*n*n
    if n in expected:
        assert (terms[0][0],terms[0][1],sum(p)) == expected[n]
    total=(9**n-1+2*(3**n-1)*(4**n-3**n-2**n+1-n*2**(n-1)+n)
           +6*n*(5**(n-1)-3**(n-1)))
    assert sum(p)==total
    if n<=8:
        print(f'n={n} min={terms[0][0]} min_count={terms[0][1]} total={sum(p)}')
print('FORMULA_CHECK_OK')
