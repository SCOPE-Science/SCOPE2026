"""Finite-model checks of two extremal commutative nilpotent semigroup families.
Pure Python 3, no external packages. These checks support but do not replace the proof.
"""

def hook(c):
    # a^(i) for 1<=i<c; a^i b for 0<=i<c; plus zero.
    elems = [('A',i,0) for i in range(1,c)] + [('A',i,1) for i in range(c)] + [None]
    def mul(x,y):
        if x is None or y is None: return None
        j=x[2]+y[2]; i=x[1]+y[1]
        if j>=2 or i>=c: return None
        target=('A',i,j)
        return target if target in elems else None
    return elems,mul,('A',1,0),('A',0,1)

def parity(c):
    assert c>=4 and c%2==0
    elems=[('B',k,e) for k in range(1,c) for e in (0,1)]+[('B',c,1),None]
    def mul(x,y):
        if x is None or y is None:return None
        k=x[1]+y[1]; e=(x[2]+y[2])%2
        target=('B',k,e)
        return target if target in elems else None
    return elems,mul,('B',1,0),('B',1,1)

def check(c,make):
    S,mul,a,b=make(c); expected=2*c
    assert len(S)==len(set(S))==expected
    assert a!=b and a in S and b in S
    checks=0
    for x in S:
        assert mul(None,x) is None and mul(x,None) is None
        for y in S:
            assert mul(x,y)==mul(y,x)
            for z in S:
                assert mul(mul(x,y),z)==mul(x,mul(y,z))
                checks+=1
    power_sets=[None,set(S)]
    for k in range(2,c+2):
        power_sets.append({mul(x,y) for x in power_sets[-1] for y in S})
    assert power_sets[c]!={None}
    assert power_sets[c+1]=={None}
    layers=[power_sets[k]-power_sets[k+1] for k in range(1,c+1)]
    assert list(map(len,layers))==[2]*(c-1)+[1]
    for x in S:
        acc=x
        for i in range(2,c+1): acc=mul(acc,x)
        assert acc is None
    # Full-length mixed product is nonzero, and all one-element c-th powers vanish.
    w=a
    for i in range(c-2): w=mul(w,a)
    w=mul(w,b)
    assert w is not None
    indecomp=power_sets[1]-power_sets[2]
    assert indecomp=={a,b}
    sq_zero=sum(mul(x,x) is None for x in indecomp)
    if make==hook:
        assert sq_zero==1 if c>=3 else sq_zero==2
    else:
        assert sq_zero==0
        assert mul(a,a)==mul(b,b)!=None
    return len(S),list(map(len,layers)),sq_zero,checks

if __name__=='__main__':
    count=0
    for c in range(2,13):
        size,layers,z,tests=check(c,hook); count+=tests
        print(f'd={c+1} hook size={size} layers={layers} squarezero_generators={z}')
        if c>=4 and c%2==0:
            size2,layers2,z2,t2=check(c,parity); count+=t2
            assert size2==size and layers2==layers and z2!=z
            print(f'd={c+1} parity size={size2} layers={layers2} squarezero_generators={z2} nonisomorphic=yes')
    print(f'VERIFY_OK degree_range=3..13 models=16 associativity_triples={count}')
