#!/usr/bin/env python3
"""Independent exhaustive checks of permuted-product multiplicities.
No external dependencies; counts Gram values independently of derived formulas.
"""
from itertools import product, permutations
from collections import Counter
from math import comb


def expected(p,m):
    d = 2*m
    t=(p**d-1)*p**(2*d-3)
    z=p**(2*d)+t
    ns={1:1,2:4*(p-1),3:9*(p-1),4:6*(p-1)*(p-3),
        5:3*(p-1)*(p-3),6:(p-1)*(p-3)*(p-5)}
    return {k:(z if k==1 else n*t) for k,n in ns.items() if k==1 or n}


def symp(x,y,p):
    return sum(x[2*i]*y[2*i+1]-x[2*i+1]*y[2*i] for i in range(len(x)//2)) % p


def gram_hist(p,m):
    vs=list(product(range(p),repeat=2*m))
    h=Counter(); gr=Counter()
    for a in vs:
        for b in vs:
            u=symp(a,b,p)
            for c in vs:
                v=symp(a,c,p); w=symp(b,c,p)
                offsets=(0,u,w,u+v,v+w,u+v+w)
                h[len({z%p for z in offsets})]+=1
                gr[(u,v,w)]+=1
    return h,gr


def explicit_group_hist(p):
    # Full group elements (x,y,t) and central-cocycle multiplication.
    gs=list(product(range(p),repeat=3)); perms=list(permutations(range(3)))
    inv2=pow(2,-1,p)
    def mul(a,b):
        return ((a[0]+b[0])%p,(a[1]+b[1])%p,
                (a[2]+b[2]+inv2*(a[0]*b[1]-a[1]*b[0]))%p)
    h=Counter()
    for a in gs:
        for b in gs:
            for c in gs:
                w=(a,b,c)
                products=set()
                for perm in perms:
                    products.add(mul(mul(w[perm[0]],w[perm[1]]),w[perm[2]]))
                h[len(products)]+=1
    return h


def exponent_p_squared_hist(p):
    # Standard extraspecial group of order p^3 and exponent p^2:
    # (i,j)(k,l)=(i+(1+p)^j k mod p^2, j+l mod p).
    gs=list(product(range(p*p),range(p)))
    perms=list(permutations(range(3)))
    def mul(a,b):
        return ((a[0]+pow(1+p,a[1],p*p)*b[0])%(p*p),(a[1]+b[1])%p)
    h=Counter()
    for a in gs:
        for b in gs:
            for c in gs:
                w=(a,b,c)
                products={mul(mul(w[t[0]],w[t[1]]),w[t[2]]) for t in perms}
                h[len(products)]+=1
    return h


def main():
    total=0
    for p,m in ((3,1),(5,1),(7,1),(3,2)):
        h,gr=gram_hist(p,m)
        e=expected(p,m)
        assert dict(h)==e, (p,m,h,e)
        assert sum(gr.values())==p**(6*m)
        T=(p**(2*m)-1)*p**(4*m-3)
        Z=p**(4*m)+T
        assert gr[(0,0,0)]==Z
        assert {v for k,v in gr.items() if k!=(0,0,0)}=={T}
        print('GRAM_OK',p,m,'hist',dict(sorted(h.items())),'zero',Z,'nonzero_per_triple',T)
        total+=p**(6*m)
    gh=explicit_group_hist(3)
    e={k:v*3**3 for k,v in expected(3,1).items()}
    assert dict(gh)==e,(gh,e)
    print('GROUP_OK p=3 complete',dict(sorted(gh.items())))
    eh=exponent_p_squared_hist(3)
    assert dict(eh)==e,(eh,e)
    print('GROUP_EXPONENT_P2_OK p=3 complete',dict(sorted(eh.items())))
    print('VERIFY_OK vector_triples=',total,'group_triples=',2*27**3)
if __name__=='__main__':
    main()
