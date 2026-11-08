"""Exact transfer and seam-twist spectral identities for three-state excitation on cubic ladders.
Run with Python 3 and SymPy.
"""
from itertools import product
import sympy as S

rungs = tuple(product(range(3), repeat=2))
indices = tuple(product(range(9), repeat=2))
pos = {key: i for i, key in enumerate(indices)}
transpose_rung = tuple(rungs.index((t, s)) for s, t in rungs)
swap = tuple(pos[transpose_rung[a], transpose_rung[b]] for a,b in indices)
T = S.zeros(81)
for i, (a, b) in enumerate(indices):
    left, mid = rungs[a], rungs[b]
    for c, right in enumerate(rungs):
        if all(((mid[1-j]-mid[j]) % 3 == 1 or
                (left[j]-mid[j]) % 3 == 1 or
                (right[j]-mid[j]) % 3 == 1) for j in (0,1)):
            T[i, 9*b+c] = 1
assert T * S.eye(81) == T
assert all(T[swap[i],swap[j]] == T[i,j] for i in range(81) for j in range(81))
fixed = [i for i in range(81) if swap[i] == i]
pairs = [(i,swap[i]) for i in range(81) if i < swap[i]]
assert len(fixed) == 9 and len(pairs) == 36
plus_vectors = [[(i,1)] for i in fixed] + [[(i,1),(j,1)] for i,j in pairs]
minus_vectors = [[(i,1),(j,-1)] for i,j in pairs]

def restricted_matrix(basis):
    M = S.zeros(len(basis))
    for u, vector in enumerate(basis):
        values = [0]*81
        for i, sign in vector:
            for j in range(81):
                if T[i,j]: values[j] += sign
        for v, vector2 in enumerate(basis):
            index, sign = vector2[0]
            M[u,v] = sign*values[index]
            for j,sign2 in vector2:
                assert values[j] == sign2*M[u,v]
    return M
P = restricted_matrix(plus_vectors)
N = restricted_matrix(minus_vectors)
x = S.symbols('x')
char_plus = x**30*(x-1)**3*(x*x-3*x-2)*(x*x+x+1)**2*(x**3+2*x*x+x-1)**2
char_minus = x**28*(x-1)*(x+1)*(x**3+5*x-3)**2
assert S.expand(P.charpoly(x).as_expr() - char_plus) == 0
assert S.expand(N.charpoly(x).as_expr() - char_minus) == 0
print('exact characteristic polynomials: PASS')
print('even dimension =',P.rows,'odd dimension =',N.rows)
print('char(even) =',S.factor(char_plus))
print('char(odd) =',S.factor(char_minus))
S0, S1, S2 = 3, 0, -10
seq=[S0,S1,S2]
for n in range(3,22):seq.append(-5*seq[n-2]+3*seq[n-3])
powT = S.eye(81)
for n in range(1,16):
    powT = powT*T
    ordinary = sum(powT[i,i] for i in range(81))
    twisted = sum(powT[i,swap[i]] for i in range(81))
    assert ordinary-twisted == 2*(1+(-1)**n)+4*seq[n]
    if n>=3:
        assert ordinary > 0 and twisted > 0
        assert ordinary%3 == 0 and twisted%3 == 0
    print(f'n={n:2d} prism={ordinary} mobius={twisted} delta={ordinary-twisted}')
print('all transfer identities: PASS')
