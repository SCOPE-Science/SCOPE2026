"""Exact checks for cyclic run-avoidance Fourier multipliers (standard Python)."""
from itertools import product

def admissible(x,n,k):
    return all(any((x >> ((i+j)%n)) & 1 for j in range(k)) for i in range(n))

def fwht(a):
    a=list(a); h=1
    while h<len(a):
        for i in range(0,len(a),2*h):
            for j in range(i,i+h):
                x,y=a[j],a[j+h]
                a[j],a[j+h]=x+y,x-y
        h*=2
    return a

def trans(k,t):
    a=[[0]*k for _ in range(k)]
    for s in range(k):
        a[s][0]=t
        if s+1<k:a[s][s+1]=1
    return a

def mm(a,b):
    k=len(a); out=[[0]*k for _ in range(k)]
    for i in range(k):
        for t in range(k):
            if a[i][t]:
                for j in range(k):out[i][j]+=a[i][t]*b[t][j]
    return out

def ident(k):
    return [[int(i==j) for j in range(k)] for i in range(k)]

def trace(a):return sum(a[i][i] for i in range(len(a)))

def mpow(a,n):
    r=ident(len(a))
    while n:
        if n%2:r=mm(r,a)
        a=mm(a,a); n//=2
    return r

def trpattern(k,signs):
    P=ident(k)
    for t in signs:P=mm(P,trans(k,t))
    return trace(P)

# Every frequency for small dimensions, including n < k.
tests=0
for n in range(1,15):
    for k in range(1,11):
        a=[int(admissible(x,n,k)) for x in range(1<<n)]
        W=fwht(a)
        singular=(k%2==0 and n%(k+1)==0)
        assert (0 in W)==singular,(n,k,"singularity")
        positive=min(abs(w) for w in W if w)
        assert positive == (2 if singular else 1),(n,k,"gap",positive)
        assert all(w%2==(0 if singular else 1) for w in W),(n,k,"parity")
        if n%(k+1):
            assert W[(1<<n)-1]==-1,(n,k,"all negative")
        else:
            for j in range(k+1):
                f=((1<<n)-1)^((1<<j)-1)
                assert W[f]==k-2*j,(n,k,j,W[f])
        tests+=1

# Non-enumerative exact matrix identities for larger k and repeated blocks.
for k in range(1,24):
    B=trans(k,-1)
    assert mpow(B,k+1)==ident(k)
    for n in (k+1,2*(k+1),3*(k+1)):
        for j in range(k+1):
            P=mm(mpow(trans(k,1),j),mpow(B,n-j))
            assert trace(P)==k-2*j,(k,n,j,trace(P))
    # Negative uniform signs at off-resonance.
    for n in (k,k+2,2*k+1):
        if n%(k+1):assert trace(mpow(B,n))==-1,(k,n)
print("CYCLIC_WINDOW_FOURIER_EXACT_PASS", f"all-frequency cases={tests}", "k=1..23 resonances")
