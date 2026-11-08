#!/usr/bin/env python3
"""Exact certificates for the 27 hyperosculating conics of a Fermat cubic.

Requirements: Python 3, SymPy. No numeric point searches are used.
"""
import itertools
from collections import Counter
from sympy import symbols, Poly, groebner, expand, real_root, sqrt

x,y,z = symbols('x y z')
V = (x,y,z)
MON = ((2,0,0),(0,2,0),(0,0,2),(1,1,0),(1,0,1),(0,1,1))
TRIPLES = list(itertools.combinations(range(27),3))
LABELS = [(h,i,j) for h in range(3) for i in range(3) for j in range(3)]

def form(h,i,j,alpha,omega):
    cyclic = (h,(h+1)%3,(h+2)%3)
    u = omega**i * V[cyclic[0]]
    v = omega**j * V[cyclic[1]]
    t = V[cyclic[2]]
    return expand((u-v)**2 - t*(alpha**2*(u+v)+2*alpha*t))

def calc(p,alpha,omega):
    assert pow(alpha,3,p)==2 and pow(omega,3,p)==1 and omega!=1
    assert (omega*omega+omega+1)%p==0
    def norm(c):
        cc=tuple(int(t)%p for t in c)
        b=next(t for t in cc if t)
        return tuple(t*pow(b,-1,p)%p for t in cc)
    def coefficients(f):
        pol=Poly(f,x,y,z,modulus=p)
        return norm(pol.coeff_monomial(x**a*y**b*z**c) for a,b,c in MON)
    forms=[coefficients(form(*key,alpha,omega)) for key in LABELS]
    assert len(set(forms))==27
    index={c:i for i,c in enumerate(forms)}
    def transform(c,perm,scales):
        f=sum(int(t)*x**a*y**b*z**d for t,(a,b,d) in zip(c,MON))
        f=f.subs({x:scales[0]*V[perm[0]], y:scales[1]*V[perm[1]],
                  z:scales[2]*V[perm[2]]}, simultaneous=True)
        return coefficients(f)
    generators=[((0,1,2),(omega,1,1)),((0,1,2),(1,omega,1)),
                ((1,2,0),(1,1,1)),((1,0,2),(1,1,1))]
    actions=[tuple(index[transform(f,*g)] for f in forms) for g in generators]
    # These four permutations generate the Fermat cubic's 54-element group.
    images={(tuple(range(27)))}
    pending=list(images)
    while pending:
        a=pending.pop()
        for g in actions:
            b=tuple(g[a[i]] for i in range(27))
            if b not in images:
                images.add(b);pending.append(b)
    assert len(images)==54
    remaining=set(TRIPLES)
    orbits=[]
    while remaining:
        seed=min(remaining);orbit={seed};todo=[seed]
        while todo:
            current=todo.pop()
            for g in actions:
                follow=tuple(sorted(g[i] for i in current))
                if follow not in orbit:
                    orbit.add(follow);todo.append(follow)
        remaining.difference_update(orbit)
        orbits.append((seed,orbit))
    assert len(orbits)==65 and sum(len(orbit) for _,orbit in orbits)==2925
    def nonempty_common_chart(triple, fixed):
        pol=[sum(int(c)*x**a*y**b*z**d for c,(a,b,d) in zip(forms[i],MON))
             for i in triple]
        other=[v for v in V if v!=fixed]
        G=groebner([f.subs(fixed,1) for f in pol],*other,modulus=p)
        return not any(v.as_expr()==1 for v in G.polys)
    present=set()
    for seed,orbit in orbits:
        if any(nonempty_common_chart(seed,fixed) for fixed in (x,y,z)):
            present.add(seed)
    return orbits,present

orbits1,yes1=calc(109,57,45)
orbits2,yes2=calc(127,32,19)
assert [seed for seed,_ in orbits1]==[seed for seed,_ in orbits2]
assert [len(orb) for _,orb in orbits1]==[len(orb) for _,orb in orbits2]
assert all(orbit1==orbit2 for (_,orbit1),(_,orbit2) in zip(orbits1,orbits2))
common=yes1 & yes2
assert common == {(0,1,2),(0,4,8)}
assert len(yes1)==5 and len(yes2)==4
assert Counter((seed in yes1, seed in yes2) for seed,_ in orbits1) == {
    (False,False):58,(True,False):3,(False,True):2,(True,True):2}
assert sum(len(orbit) for seed,orbit in orbits1 if seed in common)==27

# The complete 27 genuinely concurrent triples: 9 tangential and 18 transverse.
p_triples={tuple(sorted(LABELS.index((h,i,(i+k)%3)) for i in range(3)))
           for h in range(3) for k in range(3)}
t_triples={tuple(sorted(LABELS.index((h,i,j)) for j in range(3)))
           for h in range(3) for i in range(3)} | {
           tuple(sorted(LABELS.index((h,i,j)) for i in range(3)))
           for h in range(3) for j in range(3)}
assert len(p_triples)==9 and len(t_triples)==18 and not p_triples&t_triples
confirmed=set().union(*(orbit for seed,orbit in orbits1 if seed in common))
assert confirmed==p_triples|t_triples
pairs=Counter(pair for triple in confirmed for pair in itertools.combinations(triple,2))
assert max(pairs.values())==1  # In particular, four conics cannot meet.
assert len(pairs)==81

# Exact characteristic-zero charts of representatives for the two positive orbits.
a=real_root(2,3); w=(-1+sqrt(-3))/2
q=[form(*key,a,w) for key in LABELS]
def chart_basis(triple,fixed):
    other=[v for v in V if v!=fixed]
    return groebner([q[i].subs(fixed,1) for i in triple],*other,extension=[a,w])
for label,fixed,roots in (((0,1,2),z,2),((0,4,8),y,1)):
    gb=chart_basis(label,fixed)
    assert not any(v.as_expr()==1 for v in gb.polys)
    if label==(0,1,2):
        assert gb.contains(y) and gb.contains(x*x-a*a*x-2*a)
        assert a**4+8*a!=0  # Two distinct points on Y=0.
        gx=chart_basis(label,x)
        gy=chart_basis(label,y)
        assert gx.contains(y) and gx.contains(z*z+a*z/2-a*a/4)
        assert any(v.as_expr()==1 for v in gy.polys)
    else:
        assert gb.contains(z) and gb.contains((x-1)**2)
        gx=chart_basis(label,x)
        gz=chart_basis(label,z)
        assert gx.contains(z) and gx.contains((y-1)**2)
        assert any(v.as_expr()==1 for v in gz.polys)
    print('EXACT_REPRESENTATIVE',label,'chart',str(fixed),'degree',roots)
print('FERMAT_27_CONICS_COMPLETE_PASS',len(TRIPLES),len(orbits1),len(yes1),
      len(yes2),len(common),len(p_triples),len(t_triples),
      2*len(t_triples),54+324*4-3*(2*len(t_triples)))
