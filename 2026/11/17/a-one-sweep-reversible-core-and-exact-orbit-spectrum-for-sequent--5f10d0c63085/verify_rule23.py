"""Direct finite-state checks for the sequential complement-of-majority automaton."""
from math import gcd

def sweep(x,n):
    b=[(x>>i)&1 for i in range(n)]
    for i in range(n):
        a,c,d=b[(i-1)%n],b[i],b[(i+1)%n]
        b[i]=1-(int(a+c+d>=2))
    return sum(z<<i for i,z in enumerate(b))

def predicted_image(y,n):
    if (y&1)!=((y>>(n-1))&1):return True
    return bool(n%2) and all(((y>>i)&1)==(((y&1)^ (i%2))) for i in range(n))

def formula(n,t):
    L=n-1; g=gcd(L,t)
    core=(1<<g) if ((L-1)*t//g)%2==0 else 0
    return core+(2 if n%2 and t%2==0 else 0)

for n in range(3,15):
    N=1<<n
    nxt=[sweep(x,n) for x in range(N)]
    image=set(nxt)
    expected={y for y in range(N) if predicted_image(y,n)}
    assert image==expected,(n,'image',len(image),len(expected))
    assert all(nxt[nxt[x]] in image for x in range(N))
    assert set(nxt[y] for y in image)==image
    current=list(range(N))
    counts=[]
    for t in range(1,2*n+1):
        current=[nxt[x] for x in current]
        observed=sum(x==current[x] for x in range(N))
        assert observed==formula(n,t),(n,t,observed,formula(n,t))
        if t in (1,2,n-1,2*(n-1)):counts.append((t,observed))
    print(f'n={n:2d} image={len(image):5d} checks={counts}')
print('all direct checks passed')
