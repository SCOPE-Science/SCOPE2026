from collections import Counter
from math import gcd
def raise_aff(b,u,e,N):
    # Direct binary powering in the affine semidirect product; no geometric-sum shortcut.
    a,t=0,1
    while e:
        if e&1: a,t=(a+t*b)%N,t*u%N
        b,u=(b+u*b)%N,u*u%N
        e//=2
    return a,t

def power_fiber(p,m,e,y):
    N=p**m;t,v=y
    s=0;c=e
    while c%p==0:s+=1;c//=p
    h=gcd(c,p-1);d=min(s,m-1);a=min(s,m);L=(p-1)//h
    if pow(v,L,p)!=1 or pow(v,p-1,p**min(m,s+1))!=1:return 0
    if v%p!=1:return h*p**d
    ell=next((i for i in range(m) if (v-1)%(p**(i+1))!=0),m)
    return (p**(d+a) if t%p**a==0 else 0) + ((h-1)*p**(d+ell) if t%p**ell==0 else 0)

def check(p,m,e):
    N=p**m;U=[u for u in range(N) if gcd(u,p)==1]
    fib=Counter(raise_aff(b,u,e,N) for u in U for b in range(N))
    for v in U:
        for t in range(N):
            f=power_fiber(p,m,e,(t,v))
            assert fib[(t,v)]==f,(p,m,e,(t,v),fib[(t,v)],f)
    s=0;c=e
    while c%p==0:s+=1;c//=p
    h=gcd(c,p-1);d=min(s,m-1);a=min(s,m);L=(p-1)//h
    im=(L-1)*p**(2*m-1-d)+p**(2*m-1-d-a)
    assert len(fib)==im,(p,m,e,len(fib),im)
    return (p,m,e,len(fib),str(sorted(Counter(fib.values()).items())))

if __name__=='__main__':
    for p,mmax in [(3,4),(5,3),(7,2),(11,2)]:
        for m in range(1,mmax+1):
            for e in list(range(1,2*p+4))+[(p-1)*p**s for s in range(m+2)]+[p**s for s in range(m+2)]+[(p-1)//2*p**s for s in range(m+1)]:
                print('PASS',check(p,m,e))
