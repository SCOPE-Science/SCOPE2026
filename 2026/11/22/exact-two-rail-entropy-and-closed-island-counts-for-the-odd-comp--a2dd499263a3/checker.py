"""Independent finite-state and finite-island checks for the two-rail odd-component shift.
Run: python checker.py. Requires Python 3 and SymPy.
"""
from itertools import product
from collections import deque
import sympy as sp

# Zero mask and the three possible nonzero column masks. The parity is
# accumulated only for the unique occupied component meeting the frontier.
STATES = [(0, 0), (1, 0), (1, 1), (2, 0), (2, 1), (3, 0), (3, 1)]

def compatible(old, new):
    left, parity = old
    right, next_parity = new
    if left == 0:
        return right == 0 or next_parity == right.bit_count() % 2
    if right == 0:
        return parity == 1
    if left & right:
        return next_parity == (parity + right.bit_count()) % 2
    return parity == 1 and next_parity == right.bit_count() % 2

M = sp.Matrix([[int(compatible(s, t)) for t in STATES] for s in STATES])
EXPECTED = sp.Matrix([
    [1, 0, 1, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0],
    [1, 0, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 1, 1, 0],
    [1, 1, 0, 1, 0, 0, 1],
])
assert M == EXPECTED
assert min(M**3) > 0  # a primitive cover

B = sp.Matrix([
    [1, 0, 2, 1, 0],
    [0, 0, 1, 1, 0],
    [1, 1, 1, 0, 1],
    [0, 0, 2, 1, 0],
    [1, 2, 0, 0, 1],
])
# The 5-dimensional fixed subspace of row exchange is invariant. Verify the
# induced operator by checking all five symmetric basis vectors.
U = sp.zeros(7,5)
for j, inds in enumerate(((0,), (1,3), (2,4), (5,), (6,))):
    for i in inds: U[i,j] = 1
assert M*U == U*B
x,z=sp.symbols('x z')
poly=x**5-4*x**4+3*x**3-5*x**2+2*x+1
assert sp.expand(B.charpoly(x).as_expr()-poly) == 0
assert sp.factor(M.charpoly(x).as_expr()) == (x*x+x-1)*poly
pnum=1-z+2*z*z-3*z**3-z**4
pden=1-4*z+3*z*z-5*z**3+2*z**4+z**5
assert sp.cancel((B*(sp.eye(5)-z*B).inv())[0,0]-pnum/pden)==0

def all_finite_islands_odd(masks):
    remaining={(i,r) for i,m in enumerate(masks) for r in range(2) if (m>>r)&1}
    while remaining:
        root=remaining.pop()
        stack=[root]
        component_size=1
        while stack:
            i,r=stack.pop()
            for y in ((i-1,r),(i+1,r),(i,1-r)):
                if y in remaining:
                    remaining.remove(y)
                    stack.append(y)
                    component_size += 1
        if component_size%2==0:
            return False
    return True

# These tests count all 4^n placements independently by graph-component BFS.
for n in range(9):
    independently=sum(all_finite_islands_odd(masks) for masks in product(range(4),repeat=n))
    from_transfer=int((M**(n+1))[0,0])
    from_symmetric=int((B**(n+1))[0,0])
    assert independently==from_transfer==from_symmetric, (n,independently,from_transfer)
    print('n',n,'admissible',independently)
print('PASS: exact symbolic transition, spectral polynomial, rational series, primitive cover, and 4^n independent finite-island enumeration to n=8')
