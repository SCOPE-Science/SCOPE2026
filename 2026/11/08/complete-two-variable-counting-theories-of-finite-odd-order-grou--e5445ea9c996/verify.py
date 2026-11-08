"""Finite reproducibility checks for the odd-order group C^2 classification.

Run using Python 3.10 or later: python verify.py.
These finite checks corroborate, but do not replace, the general proof.
"""
from collections import Counter, defaultdict
from itertools import product


def cyclic(n):
    return (tuple(range(n)), lambda a,b:(a+b)%n, 0)


def abelian(mods):
    elements=tuple(product(*(range(m) for m in mods)))
    return (elements, lambda a,b:tuple((x+y)%m for x,y,m in zip(a,b,mods)), tuple(0 for _ in mods))


def heisenberg3():
    elements=tuple(product(range(3), repeat=3))
    def mult(a,b):
        return ((a[0]+b[0])%3,(a[1]+b[1])%3,(a[2]+b[2]+a[0]*b[1])%3)
    return elements,mult,(0,0,0)


def frobenius21():
    elements=tuple(product(range(7),range(3)))
    def mult(a,b):
        return ((a[0]+pow(2,a[1],7)*b[0])%7,(a[1]+b[1])%3)
    return elements,mult,(0,0)


def make(g):
    elements, mult, identity=g
    n=len(elements); idx={x:i for i,x in enumerate(elements)}
    assert len(idx)==n and identity in idx and n%2==1
    T=tuple(tuple(idx[mult(a,b)] for b in elements) for a in elements)
    e=idx[identity]
    for x in range(n):
        assert T[e][x]==x and T[x][e]==x
        assert sum(T[x][y]==e for y in range(n))==1
        for y in range(n):
            for z in range(n):
                assert T[T[x][y]][z]==T[x][T[y][z]]
    torsion3={x for x in range(n) if x!=e and T[T[x][x]][x]==e}
    return T,e,torsion3


def pair_type(T,e,x,y):
    # All atomic R-constraints obtained from the two variable names and e.
    choices=(x,y,e)
    return (x==y,x==e,y==e)+tuple(
        T[choices[a]][choices[b]]==choices[c]
        for a,b,c in product(range(3),repeat=3))


def refine(groups):
    # Disjoint tagged structures are compared with shared global type identifiers.
    tables=[g[0] for g in groups]
    es=[g[1] for g in groups]
    ptrs=[[[pair_type(T,e,x,y) for y in range(len(T))]
            for x in range(len(T))] for T,e,_ in groups]
    def compress(sigs):
        keys=sorted({v for sig in sigs for v in sig})
        d={v:i for i,v in enumerate(keys)}
        return [[d[x] for x in s] for s in sigs]
    colors=compress([[ptrs[i][x][x] for x in range(len(T))]
                     for i,T in enumerate(tables)])
    for it in range(max(map(len,tables))+2):
        new=[]
        for i,T in enumerate(tables):
            s=[]
            for x in range(len(T)):
                counts=Counter((ptrs[i][x][y], colors[i][y]) for y in range(len(T)))
                s.append((colors[i][x],tuple(sorted(counts.items()))))
            new.append(s)
        c2=compress(new)
        # Compare partitions rather than numerical labels between rounds.
        old_flat=[v for group_colors in colors for v in group_colors]
        new_flat=[v for group_colors in c2 for v in group_colors]
        if all((old_flat[i]==old_flat[j]) == (new_flat[i]==new_flat[j])
               for i in range(len(old_flat)) for j in range(len(old_flat))):
            colors=c2; break
        colors=c2
    else:raise AssertionError('Refinement did not stabilize')
    return tuple(tuple(sorted(Counter(col).values())) for col in colors), colors, it


def exact_profile(g):
    T,e,t3=g;n=len(T)
    def cls(v): return 'I' if v==e else 'T' if v in t3 else 'N'
    result={}
    for x in range(n):
        c=cls(x)
        profile=Counter((cls(y),pair_type(T,e,x,y)) for y in range(n))
        if c in result:
            assert result[c]==profile, (c,x)
        else:result[c]=profile
    return result


def main():
    models={
       'C3':cyclic(3),'C5':cyclic(5),'C7':cyclic(7),
       'C9':cyclic(9),'C3xC3':abelian((3,3)),
       'C25':cyclic(25),'C5xC5':abelian((5,5)),
       'C27':cyclic(27),'C9xC3':abelian((9,3)),
       'C3xC3xC3':abelian((3,3,3)),'Heis3':heisenberg3(),
       'C7xC3':abelian((7,3)),'C7semidirectC3':frobenius21(),
    }
    data={name:make(g) for name,g in models.items()}
    for name,g in data.items():
        n=len(g[0]);t=len(g[2]);
        print('GROUP',name,'order',n,'nonidentity_3_torsion',t)
    for name,compare in [('C25','C5xC5'),('C3xC3xC3','Heis3'),
                         ('C9','C3xC3'),('C27','C9xC3'),
                         ('C7xC3','C7semidirectC3')]:
        g,h=data[name],data[compare]
        # The colors are compared in one coherent palette, preserving multiplicities.
        _,co,it=refine([g,h])
        counta=Counter(co[0]);countb=Counter(co[1]);
        expected=(len(g[0])==len(h[0]) and len(g[2])==len(h[2]))
        assert (counta==countb)==expected, (name,compare)
        print('PAIR',name,compare,'equivalent',expected,'rounds',it)
    profs={k:exact_profile(g) for k,g in data.items()}
    for k,g in data.items():
        for j,h in data.items():
            if len(g[0])==len(h[0]) and len(g[2])==len(h[2]):
                assert profs[k]==profs[j],(k,j)
    # Symbolic formula, derived by counting without group enumeration:
    # for a nonidentity order-3 vertex, exactly one other order-3 element
    # is simultaneously its inverse, square, and square root;
    # for all other nonidentity vertices, those three points are distinct.
    for g in data.values():
        T,e,t3=g
        for x in range(len(T)):
            if x==e: continue
            inverse=next(y for y in range(len(T)) if T[x][y]==e)
            sqrt=next(y for y in range(len(T)) if T[y][y]==x)
            sq=T[x][x]
            if x in t3:assert inverse==sqrt==sq and inverse!=x
            else:assert len({inverse,sqrt,sq,x})==4
    print('VERIFY_OK',len(data),'finite_groups')

if __name__=='__main__':main()
