"""Finite corroboration of marker-skeleton shift identities. Run: python verify_marker.py"""
from itertools import product

def legal_bits(t):
    n=len(t)
    pos=[i for i,v in enumerate(t) if v]
    if len(pos)<2:return True
    k=pos[1]-pos[0]
    return k>=2 and pos[0]<k and n-1-pos[-1]<k and all(pos[j]-pos[j-1]==k for j in range(1,len(pos)))

def minimal_bits(t):
    return not legal_bits(t) and legal_bits(t[1:]) and legal_bits(t[:-1])

def allowed_periodic(x,q):
    n=len(x)
    markers=[i for i,v in enumerate(x) if v>=q]
    if not markers:return True
    return any(k>=2 and n%k==0 and all((i%k == markers[0]%k)==(x[i]>=q) for i in range(n)) for k in range(2,n+1) if n%k==0)

def sigma1(n):return sum(k for k in range(1,n+1) if n%k==0)

for n in range(1,17):
    patterns=list(product((0,1),repeat=n))
    ok=sum(legal_bits(t) for t in patterns)
    expect=n+n*n//4 if n>=2 else 2
    assert ok==expect,(n,ok,expect)
    forbidden=[t for t in patterns if minimal_bits(t)]
    expected=1 if n==2 else 2 if n>=5 and n%2 else 0
    assert len(forbidden)==expected,(n,forbidden)
    if n>=5 and n%2:
        k=(n-1)//2
        expected_bits=[(0,)*k+(1,)+(0,)*(k-1)+(1,), (1,)+(0,)*(k-1)+(1,)+(0,)*k]
        assert set(forbidden)==set(expected_bits),(n,forbidden)
for q in (2,3):
    for n in range(1,7):
        fixed=sum(allowed_periodic(w,q) for w in product(range(2*q),repeat=n))
        expected=q**n*sigma1(n)
        assert fixed==expected,(q,n,fixed,expected)
        print('fixed',q,n,fixed)
print('VERIFY_OK indicator_languages=16 indicator_minimal_layers=16 fixed_period_censuses=12')
