from math import gcd

def prime_factors(n):
    out=[]
    d=2
    while d*d<=n:
        if n%d==0:
            out.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:out.append(n)
    return out

def predicted(m):
    if m%4==0:return 0
    if any(p%4!=1 for p in prime_factors(m) if p!=2):return 0
    return 2**len(prime_factors(m))

def direct(m):
    s=0
    for x in range(m):
        f=x*x
        h=(x+1)*(x+1)
        for y in range(m):
            if (f+y*y)%m==0 and (h+(y+1)*(y+1))%m==0:
                s+=1
    return s

for m in range(1,130):
    got=direct(m)
    want=predicted(m)
    assert got==want, (m,got,want)
print('CRT congruence counts: all 129 moduli passed')

from collections import Counter
for N in (100,300,600):
    hist=Counter(gcd(x*x+y*y,(x+1)**2+(y+1)**2) for x in range(1,N+1) for y in range(1,N+1))
    assert all(d%4 and all(p%4==1 for p in prime_factors(d) if p!=2) for d in hist)
    print('Box',N,'counts',len(hist),'P(gcd=1)',round(hist[1]/N**2,8),'P(gcd=2)',round(hist[2]/N**2,8))
print('All tests passed')
