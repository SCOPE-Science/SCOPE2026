"""Finite independent check of affine direction transversals in orders two and three."""
from itertools import product
from collections import Counter

def compute(q):
    coords=[(x,y) for x in range(q) for y in range(q)]
    classes=[]
    for slope in range(q):
        classes.append([frozenset((x,y) for x,y in coords if (y-slope*x)%q==b) for b in range(q)])
    classes.append([frozenset((x,y) for x,y in coords if x==b) for b in range(q)])
    counts=Counter()
    for choices in product(range(q),repeat=q+1):
        lines=[classes[i][b] for i,b in enumerate(choices)]
        union=set().union(*lines)
        counts[len(union)]+=1
    return dict(sorted(counts.items()))

if __name__=='__main__':
    assert compute(2)=={3:4,4:4}
    assert compute(3)=={7:72,9:9}
    print('direction tuples q=2:',compute(2))
    print('direction tuples q=3:',compute(3))
    print('PASS')
