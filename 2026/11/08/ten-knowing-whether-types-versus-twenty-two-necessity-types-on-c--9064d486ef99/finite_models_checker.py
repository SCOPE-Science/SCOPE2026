"""Finite direct-model checks for unary non-contingency on K_{a,b}.

Run: python3 checker.py
Uses only Python's standard library.
"""
from itertools import product

def models(a,b):
    n=a+b
    nei=[tuple(range(a,n)) if w<a else tuple(range(a)) for w in range(n)]
    instances=[(val,w) for val in range(1<<n) for w in range(n)]
    return nei,instances

def modal(f,nei,instances):
    pos={(v,w):i for i,(v,w) in enumerate(instances)}
    return tuple(int(len({f[pos[(v,u)]] for u in nei[w]})==1) for v,w in instances)

def refine(a,b,cap=8):
    nei,I=models(a,b); n=a+b
    p=tuple((v>>w)&1 for v,w in I)
    part=[p]
    counts=[]
    classes=[tuple(t) for t in zip(*part)]
    for d in range(cap):
        uniq=sorted(set(classes)); k=len(uniq)
        counts.append(2**k)
        assert k<=8,('unexpected size',a,b,d,k)
        probes=[]
        for bm in range(1<<k):
            vals=tuple((bm>>uniq.index(cls))&1 for cls in classes)
            probes.append(modal(vals,nei,I))
        keys=[(classes[i],)+tuple(x[i] for x in probes) for i in range(len(I))]
        nxt=[tuple(x) if isinstance(x,tuple) else (x,) for x in keys]
        if len(set(nxt))==len(set(classes)):
            return counts
        classes=nxt
    raise AssertionError('no stabilization')

def direct_generators(a,b):
    nei,I=models(a,b)
    p=tuple((v>>w)&1 for v,w in I)
    D=modal(p,nei,I)
    J=modal(tuple(x&y for x,y in zip(p,D)),nei,I)
    return len(set(zip(p,D,J))), len(set(p)), len(set(zip(p,D)))

for a,b,expected in [(1,1,[4]),(1,2,[4,16]),(1,3,[4,16]),(2,2,[4,16,64]),(2,3,[4,16,64]),(3,3,[4,16,64])]:
    found=refine(a,b)
    six,zero,one=direct_generators(a,b)
    assert found==expected,(a,b,found,expected)
    assert [2**zero,2**one,2**six][-1]==expected[-1]
    print(f'K_{{{a},{b}}}: exact Boolean-algebra depth profile {found}; generator types {six}')
print('PASS: finite direct-model exhaustive Boolean closure checks')
