"""Exact independent checks for prime-divisibility block spectra of central trinomial numbers."""
from collections import Counter


def trinomial_values(N):
    a=[1,1]
    for n in range(2,N):
        v=(2*n-1)*a[-1]+3*(n-1)*a[-2]
        assert v%n==0
        a.append(v//n)
    return a[:N]


def theory(p,L):
    t=trinomial_values(p)
    Z=[j for j,x in enumerate(t) if x%p==0]
    N=p**L
    if not Z:
        return Counter(),Counter({N:1})
    z=len(Z);a=p-z
    assert Z[0]>0 and Z[-1]<p-1
    assert all(y>x+1 for x,y in zip(Z,Z[1:]))
    s=Z[0]; r=p-1-Z[-1]
    E=(p-1-2*z)*(a**(L-1)-1)//(a-1)
    zero=Counter({p**j:z*a**(L-j-1) for j in range(L)})
    good=Counter()
    for x,y in zip(Z,Z[1:]): good[y-x-1]+=a**(L-1)
    good[s]+=a**(L-1)-E
    good[r]+=a**(L-1)-E
    good[s+r]+=E
    assert sum(k*v for k,v in zero.items())+sum(k*v for k,v in good.items()) == N
    assert sum(k*v for k,v in good.items())==a**L
    return zero,good


def empirical(p,L):
    vals=trinomial_values(p**L)
    b=[v%p==0 for v in vals]
    zero=Counter();good=Counter()
    j=0
    while j<len(b):
        k=j+1
        while k<len(b) and b[k]==b[j]:k+=1
        (zero if b[j] else good)[k-j]+=1
        j=k
    return zero,good

def is_prime(p):
    if p<2:return False
    for d in range(2,int(p**0.5)+1):
        if p%d==0:return False
    return True

if __name__=='__main__':
    tests=0
    for p in range(5,102):
        if not is_prime(p): continue
        for L in range(1,7):
            if p**L>15000:break
            target=theory(p,L)
            got=empirical(p,L)
            assert target==got,(p,L,target,got)
            tests+=p**L
            print('PASS',p,L,dict(target[0]),dict(target[1]))
    print('ALL PASS: exact recurrence comparisons on',tests,'indices')
