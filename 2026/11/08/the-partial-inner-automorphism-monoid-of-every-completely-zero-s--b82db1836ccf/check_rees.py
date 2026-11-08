"""Finite exhaustive verification of a classification of inner partial automorphisms.

The definition is the one in Araujo et al., arXiv:2605.00041,
D(g,h)={a: gha=agh=a}, phi(g,h)(a)=hag.
All group and semigroup operations below are explicitly constructed.
"""
from itertools import permutations, product

ZERO = ('ZERO',)
ONE = ('ONE',)


def group(k,kind):
    if kind == 'cyclic':
        elems = tuple(range(k))
        mult = lambda a,b:(a+b)%k
        inv=lambda a:(-a)%k
        unit=0
    else:
        elems=tuple(permutations(range(k)))
        mult=lambda a,b: tuple(a[b[x]] for x in range(k))
        inv=lambda a:tuple(a.index(x) for x in range(k))
        unit=tuple(range(k))
    return elems,mult,inv,unit


def check_case(label, kind, size, zero_pattern, nontrivial_values=False):
    G,mul,inv,one=group(size,kind)
    rows=len(zero_pattern)
    cols=len(zero_pattern[0])
    assert all(len(row)==cols for row in zero_pattern)
    assert all(any(row) for row in zero_pattern)
    assert all(any(zero_pattern[r][c] for r in range(rows)) for c in range(cols))
    # Entry values deliberately vary to test non-normalized sandwich matrices.
    nonid=[x for x in G if x!=one]
    P=[[None if not zero_pattern[r][c] else
        (nonid[(r*cols+c)%len(nonid)] if nontrivial_values and nonid else one)
        for c in range(cols)] for r in range(rows)]
    S=[ZERO]+[(i,x,r) for i in range(cols) for x in G for r in range(rows)]
    Sidx={x:i for i,x in enumerate(S)}
    m=sum(x is not None for row in P for x in row)
    def smul(a,b):
        if a==ZERO or b==ZERO:return ZERO
        if a==ONE:return b
        if b==ONE:return a
        i,x,r=a;j,y,s=b
        p=P[r][j]
        if p is None:return ZERO
        return (i,mul(mul(x,p),y),s)
    extone=ONE if not (rows==cols==1) else (0,inv(P[0][0]),0)
    extras=S+[ONE] if extone==ONE else S
    identity=tuple((k,k) for k in range(len(S)))
    bottom=((0,0),)
    def phi(g,h):
        gh=smul(g,h)
        return tuple((Sidx[a],Sidx[smul(smul(h,a),g)]) for a in S if smul(gh,a)==a==smul(a,gh))
    generators=set(phi(g,h) for g in extras for h in extras)
    # Expected Brandt normal form, built independently in G-coordinates.
    E=[(i,r) for i in range(cols) for r in range(rows) if P[r][i] is not None]
    def sigma(i,r,z):return (i,mul(z,inv(P[r][i])),r)
    inners={tuple(mul(mul(t,z),inv(t)) for z in G) for t in G}
    expected={bottom,identity}
    for (i,r),(j,s), inner in product(E,E,inners):
        mp=[(0,0)]
        for z,w in zip(G,inner):
            mp.append((Sidx[sigma(i,r,z)],Sidx[sigma(j,s,w)]))
        expected.add(tuple(sorted(mp)))
    assert generators==expected,(label,len(generators),len(expected),len(generators^expected))
    def comp(f,g):
        d=dict(g)
        return tuple((a,d[b]) for a,b in f if b in d)
    for f in generators:
        for g in generators:
            assert comp(f,g) in generators, (label,f,g)
    predicted=len(E)*len(E)*len(inners)+(1 if len(E)==1 else 2)
    assert len(generators)==predicted,(label,len(generators),predicted)
    print(f'{label}: PASS |S|={len(S)} idempotent_H_classes={m} Inn(G)={len(inners)} |Inn(S)|={len(generators)} compositions={len(generators)**2}')


def main():
    tests=[
      ('trivial one H', 'cyclic',1,[[1]],False),
      ('cyclic2 one H', 'cyclic',2,[[1]],False),
      ('cyclic3 rectangular', 'cyclic',3,[[1,1]],True),
      ('cyclic2 Brandt', 'cyclic',2,[[1,0],[0,1]],False),
      ('cyclic3 triangular', 'cyclic',3,[[1,1],[0,1]],True),
      ('cyclic2 full', 'cyclic',2,[[1,1],[1,1]],True),
      ('S3 one H', 'symmetric',3,[[1]],True),
      ('S3 rectangular', 'symmetric',3,[[1,1]],True),
      ('S3 Brandt', 'symmetric',3,[[1,0],[0,1]],True),
      ('S3 triangular', 'symmetric',3,[[1,1],[0,1]],True),
      ('S3 full', 'symmetric',3,[[1,1],[1,1]],True),
    ]
    for args in tests:
        check_case(*args)
    print('VERIFY_OK cases='+str(len(tests)))

if __name__=='__main__':main()
