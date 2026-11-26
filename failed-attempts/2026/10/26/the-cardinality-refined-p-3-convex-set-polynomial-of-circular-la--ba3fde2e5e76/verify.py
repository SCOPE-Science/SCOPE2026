"""Separately implemented finite checks for the P3-convex-subset polynomial on cycle prisms.
Run: python verify.py (requires Python 3 and SymPy)."""
from collections import Counter, defaultdict
from itertools import product
import sympy as sp

t, z = sp.symbols('t z')


def local_valid(left, center, right):
    """Bits 0,1 represent membership in the upper/lower vertex pair."""
    for row in (0, 1):
        if not (center >> row) & 1:
            number_of_selected_neighbors = ((left >> row) & 1) + ((right >> row) & 1) + ((center >> (1-row)) & 1)
            if number_of_selected_neighbors >= 2:
                return False
    return True


states = [(a, b) for a in range(4) for b in range(4)]
index = {state: j for j, state in enumerate(states)}
transitions = []
T = sp.zeros(16)
for a, b, c in product(range(4), repeat=3):
    if local_valid(a, b, c):
        i, j = index[(a, b)], index[(b, c)]
        w = b.bit_count()
        transitions.append((i, j, w))
        T[i, j] += z**w
assert len(transitions) == 33

Q2 = 1-z*t+z*t*t
Q5 = 1-(1+z+z*z)*t + (z*z+z**3)*t*t - (z+z*z)*t**3 + 2*z**3*t**4 + z**3*t**5
Q = sp.expand(Q2*Q5)
actual_det = sp.expand((sp.eye(16)-t*T).det(method='domain-ge'))
assert sp.expand(actual_det-Q) == 0
core = [(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(2,0),(2,2),(3,0),(3,3)]
core_ids = [index[k] for k in core]
M = T.extract(core_ids,core_ids)
core_det = sp.expand((sp.eye(10)-t*M).det(method='domain-ge'))
assert sp.expand(core_det-Q)==0
for outside in set(range(16))-set(core_ids):
    assert not T[outside,outside]  # no forbidden pair can have a self-loop
print('DETERMINANT_OK degree_t=7 transitions=33 recurrent_states=10')

q = [sp.expand(Q).coeff(t, j) for j in range(8)]
S = {0:sp.Integer(7)}
for n in range(1, 33):
    if n<=7:
        S[n] = sp.expand(-sum(q[j]*S[n-j] for j in range(1,n))-n*q[n])
    else:
        S[n] = sp.expand(-sum(q[j]*S[n-j] for j in range(1,8)))


def polynomial_from_transfer(n):
    profile = Counter()
    # For each named starting pair, sum weights of cyclic walks.
    for start in range(16):
        dp = {(start,0):1}
        for _ in range(n):
            nxt = defaultdict(int)
            for (u,w), multiplicity in dp.items():
                for i,j,k in transitions:
                    if i == u:
                        nxt[(j,w+k)] += multiplicity
            dp = nxt
        for (u,w),multiplicity in dp.items():
            if u==start:
                profile[w]+=multiplicity
    return sp.Poly.from_dict({(k,):v for k,v in profile.items()}, z).as_expr()


def brute(n):
    """Directly enumerate subsets and graph neighborhoods, with no local-state test."""
    nb=[]
    for col in range(n):
        for row in (0,1):
            nb.append(((2*((col-1)%n)+row), (2*((col+1)%n)+row), (2*col+(1-row))))
    profile=Counter()
    for mask in range(1<<(2*n)):
        if all(((mask>>v)&1) or sum((mask>>u)&1 for u in nb[v])<=1 for v in range(2*n)):
            profile[mask.bit_count()]+=1
    return sp.Poly.from_dict({(k,):v for k,v in profile.items()},z).as_expr()

for n in range(3,21):
    calc = polynomial_from_transfer(n)
    assert sp.expand(calc-S[n])==0, ('Newton transfer disagreement', n)
    if n<=9:
        independently = brute(n)
        assert sp.expand(calc-independently)==0, ('brute disagreement',n)
    if n==3:
        assert calc.coeff(z,3)==2
    if n==4:
        assert calc.coeff(z,4)==6
    if n>=5:
        assert calc.coeff(z,2*n-4)==n
        assert all(calc.coeff(z,j)==0 for j in range(2*n-3,2*n))
        assert calc.coeff(z,2*n)==1
    print(f'n={n} total={int(calc.subs(z,1))} top_proper_degree={sp.degree(calc-z**(2*n),z)}')

assert S[1]==1+2*z+z**2
assert sp.expand(S[2]-(1+2*z**2+z**4))==0
assert sp.expand(S[3]-(1+6*z+3*z**2+2*z**3+z**6))==0
assert sp.expand(S[4]-(1+8*z+16*z**2+6*z**4+z**8))==0
print('VERIFY_OK')
