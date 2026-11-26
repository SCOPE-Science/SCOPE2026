#!/usr/bin/env python3
"""Finite ring enumeration for rank-two Borel group formulas."""
from itertools import product
from collections import Counter

def ring(p,d,kind):
    if kind=='split':
        els=list(product(range(p),repeat=d+1))
        one=(1,)+(0,)*d
        mul=lambda x,y:(x[0]*y[0]%p,)+tuple((x[0]*y[i]+y[0]*x[i])%p for i in range(1,d+1))
        add=lambda x,y:tuple((a+b)%p for a,b in zip(x,y))
        neg=lambda x:tuple(-a%p for a in x)
        unit=lambda x:x[0]!=0
        chars=list(product(range(p),repeat=d+1));D=p
        val=lambda c,x:sum(a*b for a,b in zip(c,x))%p
    elif kind=='residue':
        mod=p*p;els=list(range(mod));one=1
        mul=lambda x,y:x*y%mod
        add=lambda x,y:(x+y)%mod
        neg=lambda x:-x%mod
        unit=lambda x:x%p!=0
        chars=list(range(mod));D=mod
        val=lambda c,x:c*x%mod
    elif kind=='mixed2':
        assert p==2 and d==2
        els=list(product(range(4),range(2)));one=(1,0)
        mul=lambda x,y:(x[0]*y[0]%4,((x[0]%2)*y[1]+(y[0]%2)*x[1])%2)
        add=lambda x,y:((x[0]+y[0])%4,(x[1]+y[1])%2)
        neg=lambda x:((-x[0])%4,x[1])
        unit=lambda x:x[0]%2!=0
        chars=list(product(range(4),range(2)));D=4
        val=lambda c,x:(c[0]*x[0]+2*c[1]*x[1])%4
    else:raise ValueError(kind)
    return els,one,mul,add,neg,unit,chars,D,val

def test(p,d,kind):
    els,one,mul,add,neg,isunit,chars,D,val=ring(p,d,kind)
    units=[x for x in els if isunit(x)];U=len(units);T=len(els)
    assert U==(p-1)*p**d and T==p**(d+1)
    imul={u:next(v for v in units if mul(u,v)==one) for u in units}
    G=list(product(units,els,units))
    def matmul(g,h):
        a,b,c=g;x,y,z=h
        return (mul(a,x),add(mul(a,y),mul(b,z)),mul(c,z))
    def inv(g):
        a,b,c=g;return (imul[a],neg(mul(mul(imul[a],b),imul[c])),imul[c])
    seen=set();classes=Counter()
    for x in G:
        if x in seen:continue
        conj={matmul(matmul(g,x),inv(g)) for g in G}
        assert not (conj&seen)
        seen.update(conj);classes[len(conj)]+=1
    assert len(seen)==len(G)
    L=lambda n:(p**n-1)//(p-1)
    expected=Counter()
    A=U*(U-p**d);B=U*(p**d-1);C=U
    for size,num in [(T,A),(U,B+C),(p*(p-1),B*L(d-1)),(p,B),(p-1,C*L(d)),(1,C)]:
        expected[size]+=num
    expected={size:n for size,n in expected.items() if n}
    assert classes==expected,(p,d,kind,classes,expected)
    assert sum(size*count for size,count in classes.items())==len(G)
    # Enumerate the complete additive-character group and its unit-action orbit sizes.
    signature={tuple(val(c,x) for x in els):c for c in chars}
    assert len(signature)==len(els)
    unseen=set(chars);degrees=Counter()
    while unseen:
        c=next(iter(unseen))
        orbit={signature[tuple(val(c,mul(u,x)) for x in els)] for u in units}
        assert orbit<=unseen
        unseen-=orbit
        deg=len(orbit);degrees[deg]+=U//deg
        assert U%deg==0
    # construct merged prediction without overlap issues
    prediction=Counter()
    for degree,count in [(1,U),(p-1,p**d),(p*(p-1),p**(d-1)*L(d))]: prediction[degree]+=count
    assert degrees==prediction,(p,d,kind,degrees,prediction)
    assert sum(dg*dg*count for dg,count in degrees.items())==U*T
    assert sum(degrees.values())*U==sum(classes.values())
    assert sum(classes.values())==p**(2*d-1)*((p-1)*p*p+p**d-1)
    print('PASS',p,d,kind,'group_order',len(G),'classes',sum(classes.values()),'class_sizes',sorted(classes.items()),'affine_degrees',sorted(degrees.items()))

for configuration in [(2,1,'split'),(3,1,'split'),(2,2,'split'),(2,1,'residue'),(3,1,'residue'),(2,2,'mixed2')]:
    test(*configuration)
print('VERIFY_OK')
