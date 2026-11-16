"""Exact cyclotomic tensor Fourier cross-check across abelian alphabets.
All arithmetic occurs in Z[omega_3] or Z[i] (or Z for Klein four).
"""
from math import prod

def primes(n):
    return [p for p in range(2,n+1) if n%p==0 and all(p%d for d in range(2,int(p**.5)+1))]

def digits(x,q,n):
    z=[]
    for _ in range(n):z.append(x%q);x//=q
    return z

def primitive(x,q,n):
    w=digits(x,q,n)
    return not any(all(w[j]==w[(j+n//p)%n] for j in range(n)) for p in primes(n))

def mulroot(a,t,q):
    # a+b*zeta, zeta^2=-zeta-1 for q=3, zeta^2=-1 for q=4
    if q==3:
        t%=3
        if t==0:return a
        if t==1:return (-a[1],a[0]-a[1])
        return (-a[0]+a[1],-a[0])
    if q==4:
        t%=4
        if t==0:return a
        if t==1:return (-a[1],a[0])
        if t==2:return (-a[0],-a[1])
        return (a[1],-a[0])
    raise ValueError(q)

def transform(q,n,klein=False):
    m=q**n
    a=[(int(primitive(x,q,n)),0) for x in range(m)]
    for i in range(n):
        stride=q**i; size=q*stride
        for block in range(0,m,size):
            for off in range(stride):
                sub=[a[block+off+j*stride] for j in range(q)]
                for k in range(q):
                    re=im=0
                    for j,v in enumerate(sub):
                        if klein:
                            s=(-1)**((k&j).bit_count()%2)
                            r=(s*v[0],s*v[1])
                        else:r=mulroot(v,(k*j)%q,q)
                        re+=r[0];im+=r[1]
                    a[block+off+k*stride]=(re,im)
    return a

def C(freq,q,n,d,klein=False):
    z=digits(freq,q,n)
    for i in range(d):
        t=0
        for j in range(i,n,d):
            if klein:t^=z[j]
            else:t=(t+z[j])%q
        if t:return False
    return True

for q,klein,lengths in [(3,False,range(2,8)),(4,False,range(2,7)),(4,True,range(2,7))]:
    for n in lengths:
        p=primes(n);d=n//prod(p)
        a=transform(q,n,klein)
        assert all(v[1]==0 for v in a)
        expected=q**(n-d)
        rank=sum(v!=(0,0) for v in a)
        assert rank==expected,(q,klein,n,rank,expected)
        assert all((v!=(0,0))==C(k,q,n,d,klein) for k,v in enumerate(a)),(q,klein,n)
        count=sum(primitive(x,q,n) for x in range(q**n))
        assert a[0]==(count,0)
        assert max(abs(v[0]) for v in a)==count
        assert min(abs(v[0]) for v in a if v!=(0,0))==q**d
        print('alphabet',('V4' if klein else 'Z'+str(q)),'n',n,'rank',rank,'count',count,'min',q**d)
print('all exact cyclotomic and Klein-four checks passed')
