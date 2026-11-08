"""Independent characteristic-two extension-field check for unequal-block square-zero centralizers."""
from itertools import product
from collections import Counter

def add(a,b):return a^b

def mul(a,b):
    r=0
    for i in range(2):
        if (a>>i)&1:
            for j in range(2):
                if (b>>j)&1:r^=1<<(i+j)
    if r&8:r^=0b1100
    if r&4:r^=0b111
    return r

def mm(A,B):
    N=len(A)
    return [[reduce_xor(mul(A[i][s],B[s][j]) for s in range(N)) for j in range(N)]for i in range(N)]

def reduce_xor(vals):
    r=0
    for v in vals:r^=v
    return r

def inv(a):
    assert a
    return next(b for b in (1,2,3) if mul(a,b)==1)

def rk(a):
    a=[r[:] for r in a]
    n=len(a);p=0
    for j in range(n):
        i=next((t for t in range(p,n) if a[t][j]),None)
        if i is None:continue
        a[i],a[p]=a[p],a[i]
        b=inv(a[p][j]);a[p]=[mul(v,b) for v in a[p]]
        for z in range(n):
            if z!=p and a[z][j]:
                b=a[z][j];a[z]=[v^mul(b,w) for v,w in zip(a[z],a[p])]
        p+=1
    return p

def test(n):
    q=4;N=n+1;B=[[0]*N for _ in range(N)]
    for i in range(n-1):B[i+1][i]=1
    counts=Counter()
    for params in product(range(q),repeat=n+3):
        a=params[:n];b,c,d=params[n:]; X=[[0]*N for _ in range(N)]
        for j in range(n):
            for k in range(n-j):X[j+k][j]=a[k]
        X[n-1][n]=b;X[n][0]=c;X[n][n]=d
        assert mm(X,B)==mm(B,X)
        if all(x==0 for row in mm(X,X) for x in row):counts[rk(X)]+=1
    h=n//2
    expect=Counter({0:1,1:(q-1)*(2*q+1)})
    for r in range(2,h+1):expect[r]=(q-1)*(2*q-1)*q**(r-1)
    if n%2:expect[h+1]=q**h*(q-1)**2
    assert counts==expect,(counts,expect)
    print(f'GF(4), n={n}: {dict(sorted(counts.items()))} total={sum(counts.values())} PASS')
for n in (2,3,4,5):test(n)
print('ALL_EXTENSION_FIELD_CENTRALIZER_CHECKS_PASS')
