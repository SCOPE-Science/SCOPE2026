"""Finite orbit diagnostics for cyclic and dihedral actions on even-gonal facet indices.
The infinite classification is proved in the accompanying article, not by these tests.
"""
from itertools import product

def orbit_partition(n, step, s=None):
    unseen = set(range(n))
    out = []
    while unseen:
        a = min(unseen)
        todo = {a}
        orb = set()
        while todo:
            x = todo.pop()
            if x in orb:
                continue
            orb.add(x)
            todo.add((x + step) % n)
            if s is not None:
                todo.add((s - x) % n)
        out.append(orb)
        unseen.difference_update(orb)
    return out

def covers(n, step, s=None):
    classes = orbit_partition(n, step, s)
    return all(all((v in O or (v-1)%n in O) for O in classes) for v in range(n))

if __name__ == '__main__':
    checks=0
    for n in range(4, 162, 2):
        for step in range(1,n+1):
            if n%step: continue
            assert covers(n,step) == (step<=2)
            checks+=1
            for s in range(step):
                assert covers(n,step,s) == (step<=2)
                checks+=1
    print(f'{checks} finite subgroup-orbit diagnostics passed')
