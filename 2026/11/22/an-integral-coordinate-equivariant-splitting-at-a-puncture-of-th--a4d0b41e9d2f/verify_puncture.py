#!/usr/bin/env python3
"""Standard-library finite checks of a cubical Rips relative integral splitting.
Run: python3 verify_puncture.py
The general proof is in RESULT.md; finite enumeration is not its substitute.
"""
from itertools import combinations, product
from collections import defaultdict, Counter
from math import comb

def faces(n, link=False, omit_zero=False):
    if link:
        vs=sorted([1<<i for i in range(n)]+[(1<<i)|(1<<j) for i,j in combinations(range(n),2)])
    else:
        vs=list(range(1 if omit_zero else 0,2**n))
    good=[(x,) for x in vs]
    for f in good:
        for y in vs:
            if y>f[-1] and all((y^x).bit_count()<=2 for x in f):
                good.append(f+(y,))
    return good

def chi(F):
    return sum((-1)**(len(f)-1) for f in F)

def c_n(n):
    return sum((j+1)*(2**(n-2)-2**(i-1)) for i in range(1,n) for j in range(i))

def fundamental(I):
    ii=list(I)
    pairs=[(0,sum(1<<k for k in ii))]+[(1<<k,sum(1<<j for j in ii if j!=k)) for k in ii]
    ans={}
    for bits in product((0,1),repeat=4):
        q=tuple(pairs[a][bits[a]] for a in range(4))
        inv=sum(q[a]>q[b] for a in range(4) for b in range(a+1,4))
        ans[tuple(sorted(q))]=(-1)**(sum(bits)+inv)
    return ans

def boundary(ch):
    out=defaultdict(int)
    for f,c in ch.items():
        for i in range(len(f)):
            out[f[:i]+f[i+1:]]+=((-1)**i)*c
    return {f:c for f,c in out.items() if c}

def relative(ch):
    out=defaultdict(int)
    for f,c in ch.items():
        if 0 in f:
            i=f.index(0)
            out[tuple(x for x in f if x)]+=(-1)**i*c
    return {f:c for f,c in out.items() if c}

def sig(v,perm):
    return sum(((v>>j)&1)<<perm[j] for j in range(len(perm)))

def push(ch,perm):
    out=defaultdict(int)
    for f,c in ch.items():
        t=tuple(sig(x,perm) for x in f)
        inv=sum(t[a]>t[b] for a in range(len(t)) for b in range(a+1,len(t)))
        out[tuple(sorted(t))]+=(-1)**inv*c
    return dict(out)

def sign_on_triple(I,p):
    t=[p[x] for x in I]
    return (-1)**sum(t[a]>t[b] for a in range(3) for b in range(a+1,3))

def main():
    for n in range(3,7):
        F=faces(n)
        D=faces(n,omit_zero=True)
        L=faces(n,link=True)
        cn=c_n(n); k=comb(n,3)
        assert chi(F)==1-cn
        assert chi(D)==1-(cn-k)
        assert chi(L)==1+k
        for I in combinations(range(n),3):
            z=fundamental(I)
            assert len(z)==16 and not boundary(z)
            b=relative(z)
            assert len(b)==8 and not boundary(b)
            U=tuple(sorted((1<<i)|(1<<j) for i,j in combinations(I,2)))
            assert abs(b[U])==1
            for J in combinations(range(n),3):
                if J!=I:
                    assert U not in relative(fundamental(J))
            for j in range(n-1):
                p=list(range(n));p[j],p[j+1]=p[j+1],p[j]
                J=tuple(sorted(p[i] for i in I))
                s=sign_on_triple(I,p)
                assert push(z,p)=={f:s*v for f,v in fundamental(J).items()}
                assert push(b,p)=={f:s*v for f,v in relative(fundamental(J)).items()}
        print(f'n={n} |K|faces={len(F)} |D|faces={len(D)} |link|faces={len(L)} '+
              f'chiK={chi(F)} chiD={chi(D)} chiL={chi(L)} '+
              f'rank_H3_K={cn} rank_H3_D={cn-k} split_rank={k} '+
              f'cube_cycles_and_Sn_transpositions=PASS')
    print('PASS: exact face Euler checks, integer 3-cycle boundaries, primitive link signatures, and equivariance')
if __name__=='__main__':main()
