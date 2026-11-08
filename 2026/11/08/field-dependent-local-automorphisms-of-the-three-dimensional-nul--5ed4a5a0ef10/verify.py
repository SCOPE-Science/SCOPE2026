"""Brute-force finite-field validation of local automorphisms on a three-dimensional nilpotent associative algebra.
No external dependencies. Run python3 verify.py.
"""
from itertools import product
from math import gcd

def field(q):
    if q==4:
        # elements a+b*z; z^2=z+1
        add=lambda x,y:x^y
        def mul(x,y):
            a,b=x&1,x>>1
            c,d=y&1,y>>1
            return (a*c ^ b*d) | ((a*d ^ b*c ^ b*d)<<1)
        return add,mul
    assert q in (2,3,5)
    return lambda a,b:(a+b)%q, lambda a,b:(a*b)%q

def run(q):
    add,mul=field(q)
    elems=list(range(q)); nz=elems[1:]
    zeros=(0,0,0)
    # Collect the image of every element under every true algebra automorphism.
    orbits={x:set() for x in product(elems, repeat=3)}
    for u,v,w in product(nz,elems,elems):
        u2=mul(u,u);u3=mul(u2,u);two_uv=add(mul(u,v),mul(u,v))
        for x in orbits:
            x0,x1,x2=x
            y=(mul(u,x0),add(mul(v,x0),mul(u2,x1)),
               add(add(mul(w,x0),mul(two_uv,x1)),mul(u3,x2)))
            orbits[x].add(y)
    # All triangular matrices with arbitrary entries, no structure used in selecting them.
    total=0; patterns={};local=set()
    for a,b,c,d,e,f in product(elems,repeat=6):
        if a==0 or c==0 or f==0: continue
        good=True
        for x in orbits:
            x0,x1,x2=x
            y=(mul(a,x0),add(mul(b,x0),mul(c,x1)),
               add(add(mul(d,x0),mul(e,x1)),mul(f,x2)))
            if y not in orbits[x]:good=False;break
        if good:
            local.add((a,b,c,d,e,f))
            patterns[(c,e,f)]=patterns.get((c,e,f),0)+1
    if q%2:
        expected=q**3*(q-1)**3//(2*gcd(3,q-1))
    else:
        expected=q**2*(q-1)**2
    assert len(local)==expected, (q,len(local),expected)
    aut=set()
    for a,b,d in product(nz,elems,elems):
        a2=mul(a,a);a3=mul(a2,a)
        aut.add((a,b,a2,d,add(mul(a,b),mul(a,b)),a3))
    assert aut<=local
    assert len(aut)==(q-1)*q**2
    if q==2:assert aut==local
    if q!=2:assert aut!=local
    print('q',q,'local',len(local),'auto',len(aut),'nonauto',len(local)-len(aut))

for q in [2,3,4,5]:run(q)
print('VERIFY_OK')
