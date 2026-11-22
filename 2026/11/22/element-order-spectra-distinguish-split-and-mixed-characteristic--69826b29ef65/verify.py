"""Direct multiplication-based verification of affine-group order spectra."""
from collections import Counter
from itertools import product

def ring(p,d,mixed):
    if mixed:
        assert d==2
        R=list(product(range(p*p),range(p)))
        add=lambda a,b: ((a[0]+b[0])%(p*p),(a[1]+b[1])%p)
        mul=lambda a,b: (a[0]*b[0]%(p*p),((a[0]%p)*b[1]+(b[0]%p)*a[1])%p)
        z=(0,0);o=(1,0)
    else:
        R=list(product(range(p),repeat=d+1))
        add=lambda a,b:tuple((x+y)%p for x,y in zip(a,b))
        mul=lambda a,b:(a[0]*b[0]%p,)+tuple((a[0]*b[i]+b[0]*a[i])%p for i in range(1,d+1))
        z=(0,)*(d+1);o=(1,)+(0,)*d
    U=[a for a in R if a[0]%p]
    return R,U,z,o,add,mul

def prediction(p,d,mixed):
    from math import gcd
    q=p
    c=Counter({1:1})
    c[p]+=q**(2*d+1)-1 if not mixed else q**(2*d)-1
    if mixed:c[p*p]+=(q-1)*q**(2*d)
    for t in range(2,q):
        k=1;a=t%q
        while a!=1:
            a=a*t%q;k+=1
        c[k]+=q**(d+1)
        c[k*p]+=q**(d+1)*(q**d-1)
    return +c

def check(p,d,mixed=False):
    R,U,z,o,add,mul=ring(p,d,mixed)
    e=(z,o)
    def prod(g,h):return add(g[0],mul(g[1],h[0])),mul(g[1],h[1])
    out=Counter()
    for x in product(R,U):
        y=e
        for k in range(1,10000):
            y=prod(y,x)
            if y==e:
                out[k]+=1;break
        else:raise AssertionError('unexpectedly long group order')
    expected=prediction(p,d,mixed)
    assert +out==expected,(p,d,mixed,out,expected)
    assert sum(out.values())==len(R)*len(U)
    print('PASS',p,d,'mixed' if mixed else 'split','order',len(R)*len(U),'spectrum',dict(sorted(out.items())))

if __name__=='__main__':
    for p,d,mixed in [(3,1,False),(3,2,False),(3,2,True),(5,1,False),(5,2,False),(5,2,True)]:check(p,d,mixed)
    print('VERIFY_OK')
