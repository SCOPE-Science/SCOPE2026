#!/usr/bin/env python3
"""Check binary Frobenius-code cohomology correspondence in all degree <= 6 irreducible defining polynomials."""
import itertools, math
from collections import Counter

def pmul(a,b):
    o=0
    while b:
        if b&1:o^=a
        a<<=1;b>>=1
    return o

def prem(a,b):
    db=b.bit_length()-1
    while a and a.bit_length()-1>=db:a^=b << (a.bit_length()-1-db)
    return a

def irreducible(f,d):
    for t in range(1,d//2+1):
        for lower in range(1<<t):
            g=(1<<t)|lower
            if g&1 and prem(f,g)==0:return False
    return True

def field_mul(a,b,f,d):return prem(pmul(a,b),f)
def field_pow(a,e,f,d):
    o=1
    while e:
        if e&1:o=field_mul(o,a,f,d)
        a=field_mul(a,a,f,d);e>>=1
    return o

def rank_binary(cols):
    pivots={}
    for v in cols:
        while v:
            p=v.bit_length()-1
            if p not in pivots:pivots[p]=v;break
            v^=pivots[p]
    return len(pivots)

def direct_betti(f,d):
    # The columns of multiplication by x in the monomial basis.
    M=[field_mul(2,1<<j,f,d) for j in range(d)]
    # T^* on covectors: output j-th coefficient is M_{i,j}.
    dual=[sum(((M[j]>>i)&1)<<j for j in range(d)) for i in range(d)]
    ranks=[]
    for r in range(d+1):
        basis=list(itertools.combinations(range(d),r));idx={b:i for i,b in enumerate(basis)}
        cols=[]
        for b in basis:
            out=0
            for old in b:
                for new in range(d):
                    if (dual[old]>>new)&1 and (new==old or new not in b):
                        cc=tuple(sorted((set(b)-{old})|{new}));out ^= (1<<idx[cc])
            cols.append(out)
        ranks.append(rank_binary(cols))
    return [(math.comb(d,r)-ranks[r] if r<=d else 0)+(math.comb(d,r-1)-ranks[r-1] if r else 0) for r in range(d+2)]

def codewords(f,d,a=2):
    conj=[field_pow(a,2**i,f,d) for i in range(d)]
    return frozenset(mask for mask in range(1<<d) if (lambda z: z==0)(sum_xor([conj[i] for i in range(d) if mask>>i&1])))

def sum_xor(items):
    z=0
    for x in items:z^=x
    return z

def code_betti(f,d):
    conjugates=[field_pow(2,2**i,f,d) for i in range(d)]
    w=Counter()
    for mask in range(1<<d):
        v=0
        for i in range(d):
            if mask>>i&1:v^=conjugates[i]
        if not v:w[mask.bit_count()]+=1
    return [w[r]+w[r-1] for r in range(d+2)],w

def main():
    trials=0; nonnormal=0
    examples=[]
    for d in range(2,7):
        for f in range((1<<d)+1,(1<<(d+1)),2):
            if not irreducible(f,d):continue
            trials+=1
            bd=direct_betti(f,d);bc,w=code_betti(f,d)
            assert bd==bc,(d,f,bd,bc)
            assert bd[0]==bd[1]==1 and bd[2]==0,(d,f,bd)
            if sum(w.values())>1:nonnormal+=1
            if d==3:examples.append((hex(f),bd,dict(w)))
    assert examples==[('0xb',[1,1,0,1,1],{0:1,3:1}),('0xd',[1,1,0,0,0],{0:1})],examples
    # Realizability: all binary cyclic ideals with minimum distance >=3, including zero,
    # are exactly annihilator codes of degree-d field elements.
    realizations=0
    for d in range(2,7):
        f=next(h for h in range((1<<d)+1,1<<(d+1),2) if irreducible(h,d))
        realized=set()
        for a in range(1,1<<d):
            conj=[field_pow(a,2**i,f,d) for i in range(d)]
            if len(set(conj))!=d:continue
            realized.add(codewords(f,d,a))
        want=set()
        F=(1<<d)|1
        for deg in range(d+1):
            for low in range(1<<deg):
                g=(1<<deg)|low
                if prem(F,g):continue
                code=frozenset(pmul(g,h) for h in range(1<<(d-deg)))
                if all(w==0 or w.bit_count()>=3 for w in code):want.add(code)
        assert realized==want,(d,len(realized),len(want),realized^want)
        realizations+=len(want)
    print('BINARY_FROBENIUS_CODE_COHOMOLOGY_VERIFIED')
    print('all_cyclic_code_realizations_checked=',realizations)
    print('irreducible_polynomials_checked=',trials,'nonnormal_examples=',nonnormal)
    print('degree_three_examples=',examples)

if __name__=='__main__':main()
