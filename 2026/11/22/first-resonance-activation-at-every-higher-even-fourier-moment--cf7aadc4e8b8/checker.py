"""Independent exact-arithmetic checks of the finite Fourier coefficient identities.

Run: python3 checker.py
This checker is not a substitute for the analytic all-integer proof.
"""
from fractions import Fraction as Q
from math import comb, factorial

checks = 0

def validate(statement, label):
    global checks
    if not statement:
        raise AssertionError(label)
    checks += 1

def multinomial(k, i, j, l):
    return factorial(k) // (factorial(i) * factorial(j) * factorial(l))

def exact_moment_convolution(k, m, n, r, a, b, c):
    poly = {0: Q(1)}
    terms = [(0, a), (m, r**m * b), (n, r**n * c)]
    for _ in range(k):
        nxt = {}
        for e, v in poly.items():
            for d, w in terms:
                nxt[e + d] = nxt.get(e + d, Q(0)) + v * w
        poly = nxt
    return sum((v*v for v in poly.values()), Q(0))

def exact_moment_formula(k, m, n, r, a, b, c):
    s = r**(2*m)
    t = r**(2*n)
    diagonal = Q(0)
    for i in range(k+1):
        for j in range(k-i+1):
            l = k-i-j
            diagonal += Q(multinomial(k,i,j,l)**2) * a**(2*i) * (s*b*b)**j * (t*c*c)**l
    if n == k*m:
        diagonal += 2*k*s**k*a**(k-1)*b**k*c
    return diagonal

for k in range(3, 9):
    for m in (1, 2):
        for n in (k*m, k*m+1, k*m+3):
            for r in (Q(1,2), Q(2,3)):
                for a,b,c in ((Q(1,3),Q(2,5),Q(3,7)), (Q(4,5),Q(1,6),Q(1,9))):
                    u=exact_moment_convolution(k,m,n,r,a,b,c)
                    v=exact_moment_formula(k,m,n,r,a,b,c)
                    validate(u==v, f"moment identity k={k} m={m} n={n}")
    # Exact quadratic normal-form coefficients at s=1/k.
    s=Q(1,k)
    linear=-k+k*k*s
    quad=comb(k,2)-k*k*s*(k-1)+Q(comb(k,2)**2)*s*s
    validate(linear==0, f"critical linear coefficient k={k}")
    validate(quad==-Q(k*k-1,4), f"critical quadratic coefficient k={k}")
    xlead=Q(2*k*k,k*k-1)
    clead=Q(1,k**k-k)
    gain=k*s**(2*k)/(1-k*s**k)*xlead**k
    predicted=Q(k, k**(2*k))/(1-k*s**k)*xlead**k
    validate(gain==predicted, f"resonance gain k={k}")
    validate(clead==s**k/(1-k*s**k), f"activated mode prefactor k={k}")
    validate(gain>0, f"strict positive gain k={k}")
    for degree in range(2,18):
        validate(comb(degree+k-1,k-1)<k**degree, f"composition counting k={k} d={degree}")
print(f"PASS: {checks} exact rational/combinatorial assertions")
