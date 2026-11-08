"""Direct finite-cutoff tests for unitary-radial Bergman Hankel traces.
Run: python CHECK.py. Uses only the Python standard library.
"""
from fractions import Fraction as F
from math import factorial, comb
from itertools import product

checks = 0

def verify(condition, message):
    global checks
    checks += 1
    assert condition, message

def poch(a,k):
    out=1
    for j in range(k):out*=a+j
    return out

def multi(d,L):
    return [a for a in product(range(L+1),repeat=d) if sum(a)==L]

def afac(a):
    out=1
    for v in a:out*=factorial(v)
    return out

def radial_moment(kind,d,L):
    if kind=="ball_t0":return F(poch(d,L),poch(d+1,L))
    if kind=="ball_t2":return F(poch(d,L),poch(d+3,L))
    if kind=="sphere":return F(1)
    if kind=="sphere_mixture":return F(1,3)*F(1,4)**L+F(2,3)

def monomial_norm(a,d,moment):
    return F(afac(a),poch(d,sum(a)))*moment(sum(a))

def exact_direct(f,d,M,moment):
    ans=F(0)
    for L in range(M+1):
        for a in multi(d,L):
            na=monomial_norm(a,d,moment)
            for beta,coeff in f.items():
                k=sum(beta)
                q=tuple(a[j]+beta[j] for j in range(d))
                first=monomial_norm(q,d,moment)/na
                second= F(0)
                if all(a[j]>=beta[j] for j in range(d)):
                    less=tuple(a[j]-beta[j] for j in range(d))
                    second=na/monomial_norm(less,d,moment)
                ans+=coeff*(first-second)
    return ans

def exact_boundary(f,d,M,moment):
    ans=F(0)
    for beta,coeff in f.items():
        k=sum(beta)
        if not k:continue
        energy=coeff*F(afac(beta),poch(d,k))
        shell=sum((F(comb(L+d-1,d-1))*moment(L+k)/moment(L)
                   for L in range(max(0,M-k+1),M+1)),F(0))
        ans+=energy*shell
    return ans

def check_case(f,d,kind,M):
    moment=lambda L:radial_moment(kind,d,L)
    a=exact_direct(f,d,M,moment)
    b=exact_boundary(f,d,M,moment)
    verify(a==b, f"Mismatch: d={d}, measure={kind}, M={M}, direct={a}, boundary={b}")
    verify(a>=0,"Hankel squared energy negative")

for d in (1,2,3):
    symbols=[{(0,)*d:F(5)}, {(1,)+(0,)*(d-1):F(1)},
             {(2,)+(0,)*(d-1):F(3,4),(3,)+(0,)*(d-1):F(2,3)},
             {(0,)*d:F(7,5),(1,)+(0,)*(d-1):F(2),(2,)+(0,)*(d-1):F(1,3)}]
    if d>=2:
        symbols.append({(1,)+(0,)*(d-1):F(3,7),
                        (0,1)+(0,)*(d-2):F(5,2),
                        (1,1)+(0,)*(d-2):F(2,3),
                        (2,)+(0,)*(d-1):F(7,4)})
    for f in symbols:
        for kind in ("ball_t0","ball_t2","sphere","sphere_mixture"):
            for M in range(7):check_case(f,d,kind,M)

# Exact coordinate trace for the power-weighted ball.
for d in (1,2,3,4,5):
    for t in (0,1,2,5):
        moment=lambda L:F(poch(d,L),poch(d+t+1,L))
        f={(1,)+(0,)*(d-1):F(1)}
        for M in (0,1,2,3,5,10,25):
            actual=exact_boundary(f,d,M,moment)
            expected=F(comb(M+d,d),M+d+t+1)
            verify(actual==expected,"coordinate trace closed formula")

# The entire sequence of coordinate traces for arbitrary boundary-reaching radial measures
# is asymptotic to M^(d-1)/d!; exact convergence is proved analytically.
for d in (2,3):
    for kind in ("ball_t0","sphere","sphere_mixture"):
        moment=lambda L:radial_moment(kind,d,L)
        f={(1,)+(0,)*(d-1):F(1)}
        M=10000
        actual=exact_boundary(f,d,M,moment)
        estimate=float(actual)*factorial(d)/M**(d-1)
        verify(abs(estimate-1)<0.002,"large-degree coordinate asymptotic")

print(f"PASS {checks} exact-fraction/numerical assertions")
