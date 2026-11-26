"""Finite checks for retractions of a rank-one unipotent Alexander quandle.

Uses only Python's standard library. The small-alphabet operations are additive
vector spaces; no extension-field multiplication enters the theorem.
"""
from collections import Counter, defaultdict
from itertools import product
from math import prod


def vectors(p, f):
    return list(product(range(p), repeat=f))


def add(x, y, p):
    return tuple((a+b) % p for a,b in zip(x,y))


def neg(x, p):
    return tuple((-a) % p for a in x)


def sub(x, y, p):
    return add(x, neg(y,p),p)


def span(basis,p,f):
    zero=(0,)*f
    return set(tuple(sum(c*vec[i] for c,vec in zip(coefs,basis)) % p for i in range(f))
               for coefs in product(range(p),repeat=len(basis))) if basis else {zero}


def rank(cols,p,f):
    b=[]
    for c in cols:
        if len(span(b+[c],p,f))>len(span(b,p,f)):
            b.append(c)
    return len(b)


def gaussian(n,r,q):
    if r<0 or r>n: return 0
    num=prod(q**(n-i)-1 for i in range(r))
    den=prod(q**(r-i)-1 for i in range(r))
    return num//den


def predicted(p,f):
    q=p**f
    return {p**(2*r): gaussian(f,r,p)*p**(r*(f-r) +f-r +(f-r)*p**r +r*(q-p**r))
            for r in range(f+1)}


def image_prediction(p,f):
    return {p**(2*r): gaussian(f,r,p)*p**(f-r+(f-r)*p**r) for r in range(f+1)}


def enumerate_parameterized(p,f):
    vec=vectors(p,f)
    zero=vec[0]
    zids={v:i for i,v in enumerate(vec)}
    q=len(vec)
    pair=[(a,b) for a in vec for b in vec]
    pairids={x:i for i,x in enumerate(pair)}
    # Independent evaluation of all additive maps by independent images of basis.
    basis=[tuple(int(j==i) for j in range(f)) for i in range(f)]
    classes=Counter(); images_by_rank=defaultdict(set)
    checked_endos=0
    for colimgs in product(vec,repeat=f):
        linear={x:tuple(sum(x[j]*colimgs[j][i] for j in range(f)) % p for i in range(f)) for x in vec}
        for v in vec:
            for hv in product(vec, repeat=q):
                h=dict(zip(vec,hv))
                ff={ (a,b):(add(linear[a],h[b],p), add(linear[b],v,p)) for a,b in pair }
                # Independent operation-table test, not inferred from normal form.
                assert all(ff[(add(a,sub(b,d,p),p),b)] ==
                           (add(ff[(a,b)][0],sub(ff[(a,b)][1],ff[(c,d)][1],p),p),ff[(a,b)][1])
                           for a,b in pair for c,d in pair)
                checked_endos += 1
                if all(ff[ff[x]]==ff[x] for x in pair):
                    image=frozenset(ff.values())
                    classes[len(image)]+=1
                    images_by_rank[len(image)].add(image)
    assert classes == Counter(predicted(p,f)),(p,f,classes,predicted(p,f))
    assert {r:len(s) for r,s in images_by_rank.items()}==image_prediction(p,f),(
            p,f,{r:len(s) for r,s in images_by_rank.items()},image_prediction(p,f))
    for r,sets in images_by_rank.items():
        multiplicity=classes[r]//len(sets)
        i=next(i for i in range(f+1) if p**(2*i)==r)
        assert multiplicity == p**(i*(f-i)+i*(q-p**i))
    return checked_endos,dict(classes),{r:len(s) for r,s in images_by_rank.items()}


def exhaustive_small():
    p,f=2,1
    vec=vectors(p,f)
    pair=[(a,b) for a in vec for b in vec]
    classes=Counter()
    for targets in product(pair,repeat=len(pair)):
        F=dict(zip(pair,targets))
        if not all(F[(add(a,sub(b,d,p),p),b)]==
                   (add(F[(a,b)][0],sub(F[(a,b)][1],F[(c,d)][1],p),p),F[(a,b)][1])
                   for a,b in pair for c,d in pair): continue
        if all(F[F[x]]==F[x] for x in pair):
            classes[len(set(targets))]+=1
    assert classes==Counter(predicted(p,f))
    return dict(classes)

if __name__=='__main__':
    print('FULL_FOUR_POINT',exhaustive_small())
    for p,f in ((2,1),(3,1),(2,2)):
        print('PARAMETERIZED',p,f,*enumerate_parameterized(p,f))
    print('UNIPOTENT_RETRACTION_CENSUS_VERIFIED')
