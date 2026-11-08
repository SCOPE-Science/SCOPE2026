"""Finite non-counting k-variable color refinement on matching-deleted bicliques.

This checks small graph instances only; the accompanying mathematical proof
establishes the all-size and unrestricted-depth statement.
Requires Python 3 and NumPy.
"""
from itertools import product
from collections import defaultdict
import numpy as np

def graph(a, b, t):
    assert 3 <= a <= b and 0 <= t <= a
    n = a+b
    E = np.zeros((n,n), dtype=np.uint8)
    for i in range(a):
        for j in range(b):
            if not (i < t and i == j):
                E[i,a+j] = E[a+j,i] = 1
    return E

def initial_signature(E, x):
    k = len(x)
    return (tuple(x[i]==x[j] for i in range(k) for j in range(i+1,k)),
            tuple(int(E[x[i],x[j]]) for i in range(k) for j in range(i+1,k)))

def classes(instances, k):
    all_types = set(); datasets=[]
    for name,E in instances.items():
        n=len(E)
        types=[initial_signature(E,x) for x in product(range(n),repeat=k)]
        all_types.update(types)
        datasets.append((name,n,types))
    palette={s:i for i,s in enumerate(sorted(all_types))}
    states=[(name,n,np.array([palette[v] for v in types],dtype='int32').reshape((n,)*k))
            for name,n,types in datasets]
    rounds = 0
    while True:
        all_keys=[]; sequences=[]
        for name,n,colors in states:
            successors=[]
            for axis in range(k):
                moved=np.moveaxis(colors,axis,-1)
                arr=np.empty(moved.shape[:-1],dtype=object)
                for pos in np.ndindex(arr.shape):
                    arr[pos]=tuple(sorted(set(int(z) for z in moved[pos])))
                successors.append(arr)
            keys=[]
            for x in np.ndindex(colors.shape):
                key=(int(colors[x]),)+tuple(successors[axis][x[:axis]+x[axis+1:]]
                                            for axis in range(k))
                keys.append(key)
            all_keys.extend(keys)
            sequences.append((name,n,keys))
        new_palette={s:i for i,s in enumerate(sorted(set(all_keys)))}
        states=[(name,n,np.array([new_palette[s] for s in keys],dtype='int32').reshape((n,)*k))
                for name,n,keys in sequences]
        rounds+=1
        if len(new_palette)==len(palette):
            break
        palette=new_palette
        assert rounds < 30
    # The set of stable k-tuple colors determines all k-variable sentences:
    # an existing color is testable by existentially binding its k coordinates.
    by_type=defaultdict(list)
    for name,n,colors in states:
        by_type[frozenset(int(z) for z in colors.flat)].append(name)
    actual={name:frozenset(group) for group in by_type.values() for name in group}
    return actual,len(by_type),rounds

def profile(name,k):
    a,b,t=name
    if k<=2:
        return ("all",)
    if t==0:
        return (0,tuple(sorted((min(a,k),min(b,k)))))
    return (1,min(t,k),tuple(sorted((min(a-t,k),min(b-t,k)))))

def run(k,highest):
    graphs={(a,b,t):graph(a,b,t)
            for a in range(3,highest+1)
            for b in range(a,highest+1)
            for t in range(a+1)}
    actual, count, rounds=classes(graphs,k)
    expected={x:frozenset(y for y in graphs if profile(x,k)==profile(y,k)) for x in graphs}
    bad=[x for x in graphs if expected[x]!=actual[x]]
    print('k=%d max_side=%d graphs=%d fixed_point_rounds=%d theories=%d disagreements=%d' %
          (k,highest,len(graphs),rounds,count,len(bad)))
    assert not bad, bad[:5]
    return count

if __name__=='__main__':
    assert run(2,6)==1
    assert run(3,6)==20
    assert run(4,4)==13 # small sample; not the full width-four spectrum
    print('FINITE PEBBLE CHECKS PASSED')
