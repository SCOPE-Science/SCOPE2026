"""Independently enumerate order-reversing involutions of height-two crowns.
The crown has minima A_i and maxima B_j, with A_i<B_i and A_i<B_{i-1}.
"""
from itertools import permutations
from collections import Counter

def dualities(n):
    E={(i,i) for i in range(n)}|{(i,(i-1)%n) for i in range(n)}
    ans=[]
    for pi in permutations(range(n)):
        inv=[pi.index(i) for i in range(n)]
        if all(((i,j) in E)==((inv[j],pi[i]) in E) for i in range(n) for j in range(n)):
            ans.append((pi,sum((i,pi[i]) in E for i in range(n))))
    return ans

def rotations_reflections(n):
    # On the A-side and B-side separately: (alpha,beta), both permutations.
    for t in range(n):
        yield tuple((i+t)%n for i in range(n)),tuple((j+t)%n for j in range(n))
        yield tuple((t-i)%n for i in range(n)),tuple((t-j-1)%n for j in range(n))

for n,expected in [(3,{0:1,2:3}),(4,{2:4}),(5,{0:1,2:5})]:
    Ds=dict(dualities(n));assert dict(Counter(Ds.values()))==expected
    orbits=set()
    for pi in Ds:
        imgs=set()
        for alpha,beta in rotations_reflections(n):
            inv=[alpha.index(i) for i in range(n)]
            pi2=tuple(beta[pi[inv[i]]] for i in range(n))
            assert pi2 in Ds
            imgs.add(pi2)
        orbits.add(frozenset(imgs))
    assert len(orbits) in (1,2)
    print(f'Crown C_{2*n}: involutions={len(Ds)}, fixed-edge distribution={expected}, equivalence-orbit sizes={sorted(map(len,orbits))}')
print('VERIFY_OK')
