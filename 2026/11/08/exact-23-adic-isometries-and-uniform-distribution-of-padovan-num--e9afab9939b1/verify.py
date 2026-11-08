"""Standalone integer/matrix verification of Padovan 23-adic branch certificates."""
from collections import Counter
from random import Random

p = 23
M = ((0,1,0),(0,0,1),(1,1,0))
I = ((1,0,0),(0,1,0),(0,0,1))
w = (1,1,1)
N = ((16,13,22),(22,15,13),(13,12,15))

def mul(A,B,q):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3))%q for j in range(3)) for i in range(3))

def power(A,n,q):
    result=I
    while n:
        if n&1: result=mul(result,A,q)
        A=mul(A,A,q); n>>=1
    return result

def mv(A,v,q):
    return tuple(sum(A[i][j]*v[j] for j in range(3))%q for i in range(3))

def pad(n,q):
    return mv(power(M,n,q),w,q)[0]

def vp(n):
    i=0
    while n%p==0:
        i+=1;n//=p
    return i

assert power(M,22,p)==tuple(tuple((I[i][j]+N[i][j])%p for j in range(3)) for i in range(3))
assert mul(N,N,p)==((0,0,0),)*3
assert power(M,506,p)==I
assert power(M,506,p*p)==tuple(tuple((I[i][j]+p*N[i][j])%(p*p) for j in range(3)) for i in range(3))
assert mv(N,w,p)==(5,4,17)
assert mv(M,mv(N,w,p),p)==tuple(10*x%p for x in mv(N,w,p))
assert pow(10,11,p)==p-1 and pow(10,2,p)!=1
assert sorted([5*pow(10,r,p)%p for r in range(22)])==list(range(1,23))
for r in range(22):
    assert (pad(r+22,p)-pad(r,p))%p==5*pow(10,r,p)%p
    for t in range(23):
        assert pad(r+22*t,p)==(pad(r,p)+t*5*pow(10,r,p))%p

for k in (1,2,3):
    mod=p**k
    length=22*mod
    value=Counter()
    state=[1,1,1]
    for n in range(length):
        value[state[0]]+=1
        state[0],state[1],state[2]=state[1],state[2],(state[0]+state[1])%mod
    assert len(value)==mod and set(value.values())=={22}
    assert state==[1,1,1]
    assert power(M,length//p,mod)!=I

rng=Random(942106)
for i in range(2000):
    r=rng.randrange(22)
    s=rng.randrange(200000)
    t=rng.randrange(200000)
    if s==t: t+=1
    e=vp(abs(t-s))
    q=p**(e+2)
    diff=(pad(r+22*t,q)-pad(r+22*s,q))%q
    assert diff%(p**e)==0 and diff%(p**(e+1))!=0

print('VERIFY_OK matrix22=PASS matrix506=PASS slopes=22/22 branches=506 periods_k=1..3 images=23^k multiplicity=22 random_exact_isometries=2000')
