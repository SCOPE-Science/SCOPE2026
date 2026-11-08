"""Independent ternary-state model and constructive reachability checks.
Run with Python 3: python verify_structural.py
"""
from itertools import combinations
from collections import Counter, deque
from math import comb
import random


def generate(n):
    for z in range(n):
        rem=[i for i in range(n) if i!=z]
        for r in range(2,n-2):
            for reds in combinations(rem,r):
                x=[2]*n;x[z]=0
                for i in reds:x[i]=1
                yield tuple(x)


def neighbors(s):
    z=s.index(0); a=s.count(1); b=s.count(2)
    for j,c in enumerate(s):
        if c==1 and a>2 or c==2 and b>2:
            t=list(s);t[j]=0;t[z]=3-c
            yield tuple(t)


def components(G):
    unseen=set(G); result=[]
    while unseen:
        root=unseen.pop(); component=[root]
        for u in component:
            for v in G[u]:
                if v in unseen:unseen.remove(v);component.append(v)
        result.append(component)
    return result


def move(s,j):
    assert s[j] in (1,2)
    y=list(s); h=y.index(0); y[h]=3-y[j];y[j]=0; y=tuple(y)
    assert y in set(neighbors(s)), (s,j,y)
    return y


def recolor(s,j):
    """3 actual slides recolor one nonempty index, restore same hole; n>=7."""
    h=s.index(0);color=s[j];p=s.count(1);q=s.count(2)
    if color==2:
        assert q>=3
        if p>=3:
            a=next(i for i,x in enumerate(s) if x==1)
            y=move(s,a);y=move(y,j);y=move(y,h)
        else:
            assert q>=4
            b=next(i for i,x in enumerate(s) if x==2 and i!=j)
            y=move(s,j);y=move(y,b);y=move(y,h)
    else:
        assert p>=3
        if q>=3:
            b=next(i for i,x in enumerate(s) if x==2)
            y=move(s,b);y=move(y,j);y=move(y,h)
        else:
            assert p>=4
            a=next(i for i,x in enumerate(s) if x==1 and i!=j)
            y=move(s,j);y=move(y,a);y=move(y,h)
    expected=list(s);expected[j]=3-color
    assert y==tuple(expected), (s,j,y)
    return y


def relocate_hole(s,j):
    h=s.index(0)
    if h==j:return s
    if s[j]==2:
        catalyst=next(i for i,c in enumerate(s) if c==1)
        assert s.count(1)>=3
    else:
        catalyst=next(i for i,c in enumerate(s) if c==2)
        assert s.count(2)>=3
    y=move(s,catalyst);y=move(y,j)
    expected=list(s);expected[h]=expected[j];expected[j]=0
    assert y==tuple(expected)
    return y


def path_to(s,t):
    """Explicit reachability using only 3-slide flips and 2-slide hole transfers."""
    assert len(s)==len(t) and len(s)>=7
    n=len(s)
    # Create at least three tokens on each side with original hole.
    while s.count(1)<3:
        j=next(i for i,v in enumerate(s) if v==2);s=recolor(s,j)
    while s.count(2)<3:
        j=next(i for i,v in enumerate(s) if v==1);s=recolor(s,j)
    s=relocate_hole(s,t.index(0))
    # Adjust the red population, always using a wrong-colored index.
    while s.count(1)<t.count(1):
        j=next(i for i in range(n) if s[i]==2 and t[i]==1)
        s=recolor(s,j)
    while s.count(1)>t.count(1):
        j=next(i for i in range(n) if s[i]==1 and t[i]==2)
        s=recolor(s,j)
    # Equal total red counts. Recolor a red-to-blue and blue-to-red pair
    # in the order that stays inside [2,n-3].
    while s!=t:
        i=next(i for i in range(n) if s[i]==1 and t[i]==2)
        j=next(i for i in range(n) if s[i]==2 and t[i]==1)
        if s.count(1)==2:
            s=recolor(s,j);s=recolor(s,i)
        else:
            s=recolor(s,i);s=recolor(s,j)
    return s

for n in range(5,13):
    states=list(generate(n)); S=set(states)
    G={s:list(neighbors(s)) for s in states}
    assert all(set(G[s]).issubset(S) for s in states)
    assert all(s in G[t] for s in states for t in G[s])
    assert len(S)==n*(2**(n-1)-2*n)
    assert sum(map(len,G.values()))//2 == n*(n-1)//2 * (2**(n-1)-4*n+4)
    sizes=Counter(len(c) for c in components(G))
    if n==5:assert sizes==Counter({1:30})
    elif n==6:
        assert sizes==Counter({6:20})
        for c in components(G):
            assert all(len(G[x])==3 for x in c)
            assert all(y in G[x] for x in c for y in c if x.count(1)!=y.count(1))
    else:assert sizes==Counter({len(states):1})
    if n>=7:
        rng=random.Random(20261106+n)
        for _ in range(150):
            a=rng.choice(states);b=rng.choice(states)
            assert path_to(a,b)==b
    print(f'n={n} states={len(states)} components={dict(sizes)} PASS')
print('ALL_STRUCTURAL_CHECKS_PASS')
