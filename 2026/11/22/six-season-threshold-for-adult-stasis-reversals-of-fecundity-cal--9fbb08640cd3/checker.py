"""Exact-arithmetic diagnostic checks for the seasonal two-stage projection theorem.

Python 3 standard library only. The symbolic combinatorial argument in RESULT.md
proves the arbitrary-period result; these finite checks test implementation and examples.
"""
from fractions import Fraction as F
from itertools import permutations, combinations

checks = 0

def check(condition, explanation):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(explanation)

def product(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in (0, 1))
                       for j in (0, 1)) for i in (0, 1))

def monodromy(calendar, s, t):
    p = ((F(1), F(0)), (F(0), F(1)))
    for x in calendar:
        p = product(((F(0), F(x)), (F(s), F(t))), p)
    return p

def trace(M):
    return M[0][0] + M[1][1]

def det(M):
    return M[0][0] * M[1][1] - M[0][1] * M[1][0]

def trace_cycles(calendar, s, t):
    n = len(calendar)
    assert n >= 2
    result = F(0)
    for k in range(n // 2 + 1):
        for C in combinations(range(n), k):
            S = set(C)
            if any(((i + 1) % n) in S for i in S):
                continue
            term = s ** k * t ** (n - 2*k)
            for i in S:
                term *= calendar[i]
            result += term
    return result

rates = [(F(1, 4), F(1, 2)), (F(1, 4), F(9, 10)),
         (F(3, 5), F(1, 4)), (F(7, 10), F(8, 9))]
for n in range(2, 7):
    for cal in permutations(range(1, n+1)):
        for s,t in rates:
            M = monodromy(cal,s,t)
            check(trace(M) == trace_cycles(cal,s,t),
                  f'cycle trace n={n}, cal={cal}, s={s}, t={t}')
            check(det(M) == (-s)**n * __import__('math').prod(cal),
                  f'order-free determinant n={n}, cal={cal}')

# The n<=5 comparison sign is independent of s,t when all are positive.
for n in range(2, 6):
    choices = list(permutations(range(1, n+1)))
    reference = [trace(monodromy(c, F(1,4), F(1,3))) for c in choices]
    alternative = [trace(monodromy(c, F(3,4), F(9,10))) for c in choices]
    for i,j in combinations(range(len(choices)),2):
        a = reference[i] - reference[j]
        b = alternative[i] - alternative[j]
        check((a>0)-(a<0)==(b>0)-(b<0), f'n={n}, pair={i,j}')

C1=(1,2,3,4,5,6)
C2=(1,2,4,3,5,6)
s=F(1,4)
for t, expected in [(F(1,2),F(1,16)),(F(9,10),-F(17,400))]:
    d=trace(monodromy(C1,s,t))-trace(monodromy(C2,s,t))
    check(d==expected, f'witness exact trace difference t={t}')
    check(d==s*s*(7*s-3*t*t),f'witness identity t={t}')

# Independent test of the adjacent swap factor using random-looking exact samples.
for a,b,c,d,e,f in [(1,2,3,4,5,6),(7,3,9,1,4,8),(5,11,2,6,10,4)]:
    for s,t in rates:
        lhs=trace(monodromy((a,b,c,d,e,f),s,t))-trace(monodromy((a,b,d,c,e,f),s,t))
        rhs=s*s*(c-d)*(s*(a*e-b*f)-t*t*(b-e))
        check(lhs==rhs, 'adjacent swap formula')

# Cross-unit persistence diagnostic: compare exact det(I-P) for shared fertility scalings.
for t,z,expected_signs in [(F(1,2),F(609,1000),(-1,1)),
                            (F(9,10),F(579,5000),(1,-1))]:
    for cal,sign in zip((C1,C2),expected_signs):
        M=monodromy(tuple(F(x)*z for x in cal),F(1,4),t)
        D=det(M)
        gap=F(1)-trace(M)+D
        check(F(0)<D<F(1), 'monodromy determinant below 1 in persistence witness')
        check(((gap>0)-(gap<0))==sign, 'cross-unit threshold witness')

print(f'PASS: {checks} exact-arithmetic diagnostic assertions.')
print('The unrestricted ordering and sharpness theorem is proved in RESULT.md;')
print('finite checks are not asserted to certify an arbitrary input domain.')
