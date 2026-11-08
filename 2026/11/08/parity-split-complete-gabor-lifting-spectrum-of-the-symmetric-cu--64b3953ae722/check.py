#!/usr/bin/env python3
"""Standard-library checks of cubic-symmetric Boolean Gabor spectral law."""
from collections import Counter

def e3(mask):
    w=mask.bit_count()
    return (w*(w-1)*(w-2)//6)&1

def fwht(data):
    v=list(data);n=len(v);h=1
    while h<n:
        for off in range(0,n,2*h):
            for j in range(off,off+h):
                a,b=v[j],v[j+h]
                v[j]=a+b;v[j+h]=a-b
        h*=2
    return v

def polar_rank(a,n):
    t=a.bit_count()&1
    rows=[]
    for i in range(n):
        rows.append(sum((((t ^ ((a>>i)&1) ^ ((a>>j)&1))&1) << j) for j in range(n) if j!=i))
    basis={}
    for x in rows:
        while x:
            k=x.bit_length()-1
            if k not in basis:
                basis[k]=x;break
            x ^= basis[k]
    return len(basis)

def predicted_rank(a,n):
    if a.bit_count()%2:
        return n-1 if n%2 else n-2
    if a==0 or (n%2==0 and a==(1<<n)-1):
        return 0
    return 2

def test(n):
    N=1<<n
    A_counts=Counter()
    for a in range(N):
        rank=predicted_rank(a,n)
        assert polar_rank(a,n)==rank,(n,a,rank,polar_rank(a,n))
        transform=fwht([1 if e3(x)==e3(x^a) else -1 for x in range(N)])
        nonzero=sum(t!=0 for t in transform)
        assert nonzero==1<<rank,(n,a,nonzero,rank)
        assert {abs(t) for t in transform if t}=={1<<(n-rank//2)}
        for z in transform:A_counts[abs(z)]+=1
    expected=Counter()
    # two exceptional shifts for even n; one for odd n
    exceptional=2 if n%2==0 else 1
    expected[N]+=exceptional
    even_shifts=N//2-exceptional
    expected[N//2]+=even_shifts*4
    odd_r=n-1 if n%2 else n-2
    expected[1<<(n-odd_r//2)]+=(N//2)*(1<<odd_r)
    expected[0]=N*N-sum(expected.values())
    assert A_counts==expected, (n,A_counts,expected)
    R=N*N-expected[0]
    formula=N*N//4+2*N-3 if n%2 else N*N//8+2*N-6
    assert R==formula
    assert sum(c*z*z for z,c in expected.items())==N**3
    positive=[x for x in expected if x]
    cond=max(positive)//min(positive)
    assert cond==2**((n-1)//2)
    print('n',n,'N',N,'rank',R,'ker',N*N-R,'nonzero ambiguity',sorted((z,c) for z,c in expected.items() if z), 'kappa',cond)
for n in range(3,10):test(n)
print('CUBIC_SYMMETRIC_GABOR_SPECTRUM_PASS')
