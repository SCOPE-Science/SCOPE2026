#!/usr/bin/env python3
"""Independent finite-group enumeration for generalized dihedral C3 x C3.
Computes actual subgroups, counts automorphisms by generator-image checks,
and independently tests every endomorphism of the full group."""
from itertools import product
from collections import Counter
mods=(3,3)
A=list(product(*[range(m) for m in mods])); G=[(a,b) for b in (0,1) for a in A]
e=((0,0),0)
def op(x,y):
    a,b=x; c,d=y; sign=(-1 if b else 1)
    return tuple((a[i]+sign*c[i])%mods[i] for i in range(len(mods))),b^d
def inv(x):
    a,b=x;sgn=1 if b else -1
    return tuple((sgn*a[i])%mods[i] for i in range(len(mods))),b
def grp(gens):
    seen={e};q=[e]
    gens=tuple(gens)+tuple(inv(x) for x in gens)
    for x in q:
        for g in gens:
            z=op(x,g)
            if z not in seen:seen.add(z);q.append(z)
    return frozenset(seen)
def order(x):
    z=e
    for i in range(1,100):
        z=op(z,x)
        if z==e:return i
    raise AssertionError

def generators(H):
    out=[];generated=grp([])
    for x in sorted(H):
        if x not in generated:
            out.append(x);generated=grp(out)
    assert generated==H
    return out

def hom_count(H,K,bijective=False):
    gen=generators(H)
    orders=[order(x) for x in gen]
    can=[[y for y in K if order(y)==o] for o in orders] if bijective else [[y for y in K if o%order(y)==0] for o in orders]
    total=0
    for img in product(*can):
        mapping={e:e}; pending=[e];steps=tuple(zip(gen,img))+tuple((inv(g),inv(y)) for g,y in zip(gen,img));valid=True
        for x in pending:
            for g,y in steps:
                z=op(x,g);w=op(mapping[x],y)
                if z in mapping:
                    if mapping[z]!=w:valid=False;break
                else:
                    mapping[z]=w;pending.append(z)
            if not valid:break
        if valid and len(mapping)==len(H) and (not bijective or len(set(mapping.values()))==len(H)):
            total+=1
    return total

subs={grp([])};q=list(subs)
for H in q:
    for g in G:
        if g not in H:
            K=grp(tuple(H)+(g,))
            if K not in subs:subs.add(K);q.append(K)

def signature(H):return (len(H),tuple(sorted(Counter(order(x) for x in H).items())))
types={}
for H in subs:types.setdefault(signature(H),[]).append(H)
PI=0
for sig,HS in sorted(types.items()):
    aut=hom_count(HS[0],HS[0],bijective=True)
    PI+=len(HS)**2*aut
    print('type',sig,'subgroups',len(HS),'aut',aut)
E=hom_count(frozenset(G),frozenset(G),bijective=False)
# A=C3^2 subgroup types: 1, 4 lines of C3, entire group
# Type weights 1, 4^2*2=32, |GL2(F3)|=48. |End(A)|=3^4=81.
pred= (1+9**2)*1 + (1+9**2//3)*(4**2*2) + (1+9**2//9)*48
assert PI==pred and E==9*81+1,(PI,pred,E)
print('GENERALIZED_DIHEDRAL_C3_SQUARED_OK',PI,E,len(subs))
