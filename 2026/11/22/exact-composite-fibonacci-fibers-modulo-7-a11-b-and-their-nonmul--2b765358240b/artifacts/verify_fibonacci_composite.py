from collections import Counter
from math import gcd
REG7_E={0:2,1:2,6:2}
REG7_O={1:2,2:2,5:2,6:2}
REG11_E={0:1,1:1,3:1,8:1,10:1}
REG11_O={1:2,2:2}

def roots_for_multiple_p(z,p,k):
    # # roots s mod p^k such that s divisible by p and s*s == z
    m=p**k
    z%=m
    if z==0:
        return p**(k//2)
    v=0
    while z%p==0:
        v+=1; z//=p
    if v<2 or v%2:
        return 0
    if pow(z%p,(p-1)//2,p)!=1:
        return 0
    return 2*p**(v//2)

def parity_fibers(p,k,y):
    r=y%p
    if p==7:
        if r in (3,4): return roots_for_multiple_p(5*y*y+4,7,k),0
        return REG7_E.get(r,0),REG7_O.get(r,0)
    if p==11:
        if r==5:return 0,roots_for_multiple_p(5*y*y-4,11,k)
        return REG11_E.get(r,0),REG11_O.get(r,0)
    raise ValueError

def observed(p,k):
    m=p**k
    period=(16 if p==7 else 10)*p**(k-1)
    a,b=0,1
    c=Counter()
    for n in range(period):
        c[(a,n%2)]+=1
        a,b=b,(a+b)%m
    assert (a,b)==(0,1)
    for y in range(m):
        assert (c[(y,0)],c[(y,1)])==parity_fibers(p,k,y),(p,k,y,c[(y,0)],c[(y,1)],parity_fibers(p,k,y))
    return c

def square_count(p,j):
    if j<=0:return 1
    return 1+sum(((p-1)//2)*p**(j-2*h-1) for h in range((j-1)//2+1))

def support_count(a,b):
    A=7**(a-1);B=11**(b-1)
    return 21*A*B+10*B*square_count(7,a-2)+4*A*square_count(11,b-2)

for p in (7,11):
    for k in range(1,6):
        c=observed(p,k)
        print('LOCAL_OK',p,k,'period',sum(c.values()),'support',len(set(y for y,s in c if c[(y,s)])))

for a,b in [(1,1),(2,1),(1,2),(2,2),(3,2),(2,3),(3,3)]:
    m=7**a*11**b
    P7=16*7**(a-1);P11=10*11**(b-1)
    assert gcd(P7,P11)==2
    period=P7*P11//2
    c=Counter()
    x,y=0,1
    for n in range(period):
        c[x]+=1
        x,y=y,(x+y)%m
    assert (x,y)==(0,1)
    supp=0
    for z in range(m):
        e7,o7=parity_fibers(7,a,z%(7**a))
        e11,o11=parity_fibers(11,b,z%(11**b))
        pred=e7*e11+o7*o11
        actual=c.get(z,0)
        assert actual==pred,(a,b,z,actual,pred)
        if pred:supp+=1
    assert supp==support_count(a,b),(a,b,supp,support_count(a,b))
    print('COMPOSITE_OK',a,b,'modulus',m,'period',period,'support',supp)
print('VERIFY_OK all local and composite parity fibers and exact support')
