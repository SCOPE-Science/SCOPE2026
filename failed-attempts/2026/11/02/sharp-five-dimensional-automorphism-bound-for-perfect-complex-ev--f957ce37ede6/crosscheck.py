"""Independent spot checks of the exact integer graph-lattice computation.

Requires sympy; the primary exhaustive checker is standalone C++17.
Usage: python crosscheck.py ./verify
"""
import itertools
import math
import random
import subprocess
import sys
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form

N = 5
PERMS = list(itertools.permutations(range(N)))

def graph_order(mask):
    edges = {(i, j) for i in range(N) for j in range(N)
             if (mask >> (N*i+j)) & 1}
    aut = sum(all((p[i], p[j]) in edges for i, j in edges)
              for p in PERMS)
    # If no cycle cover, the structure matrix cannot be invertible.
    if not any(all((i,p[i]) in edges for i in range(N)) for p in PERMS):
        return None, aut
    relations = Matrix([[int(j == k) - 2*int(i == k)
                         for k in range(N)] for i,j in sorted(edges)])
    D = abs(int(hermite_normal_form(relations.T).det()))
    return D, aut

def burnside():
    fixed = 0
    points = [(i,j) for i in range(N) for j in range(N)]
    for p in PERMS:
        visited = set()
        n_orbits = 0
        for x in points:
            if x in visited:
                continue
            n_orbits += 1
            a=x
            while a not in visited:
                visited.add(a)
                a=(p[a[0]],p[a[1]])
        fixed += 1 << n_orbits
    assert fixed % len(PERMS) == 0
    return fixed // len(PERMS)

def main():
    program = sys.argv[1] if len(sys.argv)>1 else './verify'
    assert burnside() == 291968
    cases={0, (1<<25)-1, 1122820, 1122448,
           sum(1<<(6*i) for i in range(N))}
    rng = random.Random(172026)
    for _ in range(300):
        cases.add(rng.randrange(1<<25))
    tested=0
    for mask in sorted(cases):
        D,aut=graph_order(mask)
        s=subprocess.check_output([program,str(mask)],text=True).strip()
        vals=dict(z.split('=') for z in s.split() if '=' in z)
        assert int(vals['mask'])==mask
        assert int(vals['aut'])==aut
        if D is None:
            assert 'no_cycle_cover' in s
        else:
            assert int(vals['diagonal'])==D, (mask,D,s)
            assert int(vals['bound'])==D*aut
        tested+=1
    print('Burnside unlabeled digraphs:',burnside())
    print('Integer-lattice/automorphism crosschecked graphs:',tested)
    print('C5:',graph_order(1122820),'C2+C3:',graph_order(1122448))
    print('CROSSCHECK_OK')
if __name__=='__main__':main()
