"""Exact-rational boundary and linearization checks for two-cohort recruitment.
Run with Python 3: python check.py. No third-party dependencies.
The mathematical proof of the all-parameter result is in RESULT.md.
"""
from fractions import Fraction as Q
from cmath import sqrt

N = 0

def check(v, description):
    global N
    assert v, description
    N += 1

def poly_conditions(a, g):
    # Polynomial: lambda^2 - a*g*lambda - a*(1-g)
    return (1-a, 1+a*(2*g-1), 1+a*(1-g))

def exact_sink(a, g):
    return all(v > 0 for v in poly_conditions(a, g))

def spectral_radius(a, g):
    roots = ((a*g+sqrt((a*g)**2+4*a*(1-g)))/2,
             (a*g-sqrt((a*g)**2+4*a*(1-g)))/2)
    return max(abs(z) for z in roots)

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in (0,1)) for j in (0,1)] for i in (0,1)]

def matpow(A,n):
    P=[[Q(1),Q(0)],[Q(0),Q(1)]]
    for _ in range(n): P=matmul(P,A)
    return P

for q in [Q(i,10) for i in range(1,61)]:
    a=-q
    for j in range(21):
        g=Q(j,20)
        expected = (q < 1 or (q == 1 and 0 < g < 1) or
                    (1 < q < 3 and (1-Q(1)/q < g < (1+Q(1)/q)/2)))
        check(exact_sink(a,g)==expected, f'q={q}, g={g}')
        # This numerical eigenvalue check is subsidiary, not a proof.
        if all(abs(float(x)) > 1e-7 for x in poly_conditions(a,g)):
            radius=spectral_radius(float(a),float(g))
            check((radius<1)==expected, f'eigen q={q},g={g},rho={radius}')

for r in [Q(1,2),Q(1),Q(3,2),Q(2),Q(5,2),Q(3),Q(7,2),Q(4),Q(5)]:
    for j in range(101):
        g=Q(j,100)
        a=1-r
        if r<2: expected=True
        elif r==2: expected=Q(0)<g<Q(1)
        elif r<4: expected=1-Q(1)/(r-1)<g<(1+Q(1)/(r-1))/2
        else: expected=False
        check(exact_sink(a,g)==expected, f'Ricker r={r},g={g}')

J=[[Q(-2),Q(-1)],[Q(1),Q(0)]]
I=[[Q(1),Q(0)],[Q(0),Q(1)]]
Nmat=[[J[i][j]+I[i][j] for j in (0,1)] for i in (0,1)]
check(matmul(Nmat,Nmat)==[[0,0],[0,0]],'nilpotency')
for n in range(61):
    target=[[(-1)**n*(I[i][j]-n*Nmat[i][j]) for j in (0,1)] for i in (0,1)]
    check(matpow(J,n)==target, f'power n={n}')

# Stability window and the unique 4 ceiling.
for q in [Q(11,10),Q(6,5),Q(3,2),Q(2),Q(5,2),Q(29,10)]:
    L=1-Q(1)/q; U=(1+Q(1)/q)/2
    check(U-L==(3-q)/(2*q),'window')
    check(L<Q(2,3)<U,'contains optimum')
for g in [Q(j,60) for j in range(61) if j!=40]:
    if g < Q(2,3):
        rlim=1+Q(1)/(1-g)
    else:
        rlim=1+Q(1)/(2*g-1)
    check(rlim<4,'unique maximizer')
print(f'PASS: {N} assertions')
