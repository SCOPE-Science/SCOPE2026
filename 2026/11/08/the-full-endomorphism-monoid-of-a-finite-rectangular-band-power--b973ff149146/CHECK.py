#!/usr/bin/env python3
"""Independent finite tests for endomorphisms of power semigroups of rectangular bands."""
from itertools import product
from math import comb
from random import Random


def t_formula(r,c):
    return sum((-1)**(i+j)*comb(r,i)*comb(c,j)*2**((r-i)*(c-j))
               for i in range(r+1) for j in range(c+1))


def construct(m,n):
    vertices=list(product(range(m),range(n)))
    subs=[]
    for mask in range(1,1<<len(vertices)):
        s=frozenset(vertices[i] for i in range(len(vertices)) if mask>>i&1)
        subs.append(s)
    ss=set(subs)
    def row(s): return frozenset(i for i,j in s)
    def col(s): return frozenset(j for i,j in s)
    def rect(r,c):return frozenset(product(r,c))
    def mul(a,b):return rect(row(a),col(b))
    fibers={}
    for s in subs:
        fibers.setdefault((row(s),col(s)),[]).append(s)
    return subs,ss,row,col,rect,mul,fibers


def make_random_end(m,n, rng):
    subs,ss,row,col,rect,mul,fibers=construct(m,n)
    rows=list({row(x) for x in subs})
    cols=list({col(x) for x in subs})
    sigma={r:rng.choice(rows) for r in rows}
    tau={c:rng.choice(cols) for c in cols}
    F={}
    for (r,c), xs in fibers.items():
        target=fibers[(sigma[r],tau[c])]
        for x in xs:
            F[x]=rect(sigma[r],tau[c]) if x==rect(r,c) else rng.choice(target)
    return F, (subs,mul)


def run():
    for m,n in [(1,1),(1,3),(2,2),(2,3),(3,2)]:
        subs,ss,row,col,rect,mul,fibers=construct(m,n)
        assert len(subs)==2**(m*n)-1
        assert len(fibers)==(2**m-1)*(2**n-1)
        for (r,c), xs in fibers.items():
            assert len(xs)==t_formula(len(r),len(c))
            assert rect(r,c) in xs
        for x in subs:
            assert mul(x,x)==rect(row(x),col(x))
            for y in subs:
                assert mul(x,y) in ss
                assert mul(x,y)==rect(row(x),col(y))
        rng=Random(9011+100*m+n)
        samples=100 if m*n<=4 else 30
        for _ in range(samples):
            F,(elts,prodmap)=make_random_end(m,n,rng)
            for x in elts:
                for y in elts:
                    assert F[prodmap(x,y)]==prodmap(F[x],F[y])
        print(f"m={m}, n={n}, elements={len(subs)}, idempotents={len(fibers)}, random_endomorphisms_verified={samples}")
    subs,ss,row,col,rect,mul,fibers=construct(2,2)
    assert t_formula(2,2)==7
    # Direct enumeration of 3^3 by 3^3 restriction maps to the 3-by-3 rectangle band.
    supports=list({row(s) for s in subs})
    cols=list({col(s) for s in subs})
    all_sigmas=product(supports,repeat=3)
    total=0
    hist={}
    for out in all_sigmas:
        sig=dict(zip(supports,out))
        for other in product(cols,repeat=3):
            tau=dict(zip(cols,other))
            num=1
            for (r,c),ls in fibers.items():
                num*=len(fibers[(sig[r],tau[c])])**(len(ls)-1)
            total+=num
            hist[num]=hist.get(num,0)+1
    assert hist=={1:648,7**6:81},hist
    assert total==648+81*7**6==9530217
    print(f"m=n=2: {sum(hist.values())} base maps, fiber-weight classes={sorted(hist.items())}; exact endomorphisms={total}")
    assert 3**3==27
    print('VERIFY_OK')

if __name__=='__main__':run()
