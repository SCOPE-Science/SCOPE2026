"""Independent finite face and boundary checks for tolerance-two of three disjoint simplices.
Uses only the Python standard library. These are finite checks, not a proof of the all-size theorem.
"""
from collections import Counter
from itertools import combinations
from math import comb

CASES = ((2,2,2), (2,3,3), (2,3,4), (3,3,3), (3,3,4), (4,4,4))


def predicted(ns):
    x,y,z=(n-1 for n in ns)
    return (x*y+x*z+y*z+2*x*y*z,
            comb(x,2)*comb(y,2)+comb(x,2)*comb(z,2)+comb(y,2)*comb(z,2))


def faces(ns):
    m=sum(ns)
    blocks=[];start=0
    for n in ns:
        blocks.append(((1<<n)-1)<<start)
        start+=n
    by_degree={}
    for s in range(1,1<<m):
        if min((s&~block).bit_count() for block in blocks)<=2:
            by_degree.setdefault(s.bit_count()-1,[]).append(s)
    return by_degree


def columns(by, degree, p):
    low={s:i for i,s in enumerate(by.get(degree-1,[]))}
    if p==2:
        for face in by.get(degree,[]):
            v=0
            for i in range(face.bit_length()):
                if face&(1<<i):v^=1<<low[face^(1<<i)]
            yield v
    else:
        for face in by.get(degree,[]):
            bits=[i for i in range(face.bit_length()) if face&(1<<i)]
            v={}
            for j,i in enumerate(bits):
                index=low[face^(1<<i)]
                v[index]=(1 if j%2==0 else p-1)
            yield v


def rank_mod2(cols):
    piv={}
    for x in cols:
        while x:
            k=x.bit_length()-1
            if k not in piv:
                piv[k]=x;break
            x^=piv[k]
    return len(piv)


def rank_modp(cols,p):
    piv={}
    for v in cols:
        v=dict(v)
        while v:
            k=max(v)
            a=v[k]
            if k not in piv:
                inv=pow(a,-1,p)
                piv[k]={idx:c*inv%p for idx,c in v.items()}
                break
            for idx,c in piv[k].items():
                z=(v.get(idx,0)-a*c)%p
                if z:v[idx]=z
                else:v.pop(idx,None)
    return len(piv)


def homology(by,p):
    dims=sorted(by)
    ranks={0:0, max(dims)+1:0}
    for d in dims[1:]:
        cols=columns(by,d,p)
        ranks[d]=rank_mod2(cols) if p==2 else rank_modp(cols,p)
    # The group H_0 is 1 for each connected complex.
    return tuple(len(by[d])-ranks[d]-ranks[d+1] for d in dims)


def verify():
    for ns in CASES:
        by=faces(ns)
        b3,b4=predicted(ns)
        expected=(1,0,0,b3,b4)
        expected=(expected + (0,)*max(0,max(by)+1-len(expected)))[:max(by)+1]
        primes=(2,3,5) if sum(ns)<=9 else (2,)
        for p in primes:
            observed=homology(by,p)
            assert observed==expected,(ns,p,observed,expected)
        euler=sum((-1)**d*len(xs) for d,xs in by.items())
        assert euler==1-b3+b4,(ns,euler,b3,b4)
        print('PASS',ns,'faces',sum(map(len,by.values())), 'fvector',tuple(len(by.get(d,[])) for d in range(max(by)+1)),
              'betti',expected,'primes',primes,'Euler',euler)
    print('ALL FINITE TESTS PASS; no conclusion about infinite-family correctness follows from tests alone.')

if __name__=='__main__':verify()
