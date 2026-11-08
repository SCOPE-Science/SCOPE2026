"""Independent finite-state checks for a boundary-flip exclusion-chain autocorrelation.

Run: python3 verify_meandric_endpoint.py
No third-party packages; exhaustive checks are diagnostics, not asymptotic proofs.
"""
from fractions import Fraction
from itertools import product
from math import cos, sin, pi, exp, isclose

checks = 0

def check(ok, message):
    global checks
    if not ok:
        raise AssertionError(message)
    checks += 1

def finite_state_values(m, b, horizon):
    states = list(product((-1, 1), repeat=m))
    index = {s:i for i,s in enumerate(states)}
    # Independent direct transition kernel, including no-update choices.
    transition = []
    for s in states:
        row = {index[s]: Fraction(2*b-m,2*b)}
        for j in range(m):
            v = list(s)
            if j == m-1:
                v[j] *= -1
            else:
                v[j],v[j+1] = v[j+1],v[j]
            ix = index[tuple(v)]
            row[ix] = row.get(ix,Fraction(0))+Fraction(1,2*b)
        check(sum(row.values()) == 1, f'kernel stochastic m={m}, b={b}')
        transition.append(row)
    y = [sum(s) for s in states]
    f = [Fraction(x) for x in y]
    out = []
    for t in range(horizon+1):
        c = sum(Fraction(y[i])*f[i] for i in range(len(states))) / (m * len(states))
        out.append(c)
        if t < horizon:
            f = [sum(prob*f[j] for j,prob in row.items()) for row in transition]
    return out

def linear_values(m,b,horizon):
    # Independently evolved first moment of each coordinate.
    v = [Fraction(1)]*m
    out=[]
    for t in range(horizon+1):
        out.append(sum(v, Fraction(0))/m)
        if t < horizon:
            nxt=[]
            for j in range(m):
                if m==1:
                    lv = 2*v[0]
                elif j==0:
                    lv = v[j]-v[j+1]
                elif j==m-1:
                    lv = 3*v[j]-v[j-1]
                else:
                    lv = 2*v[j]-v[j-1]-v[j+1]
                nxt.append(v[j]-lv/Fraction(2*b))
            v=nxt
    return out

def spectral(m,b,t):
    return sum(
       (1/(2*m*m*sin(theta/2)**2))*(1-(1-cos(theta))/b)**t
       for theta in [(k+0.5)*pi/m for k in range(m)]
    )

for m in range(1,7):
    for b in (m,m+1):
        exact = finite_state_values(m,b,13)
        linear = linear_values(m,b,13)
        for t,(x,y) in enumerate(zip(exact,linear)):
            check(x==y, f'exact and linear m={m}, b={b}, t={t}')
            check(isclose(float(x),spectral(m,b,t),rel_tol=2e-12,abs_tol=1e-12),
                  f'exact and spectral m={m}, b={b}, t={t}')
        check(exact[0]==1, 'initial normalized variance')
        check(all(exact[i+1]<=exact[i] for i in range(13)), 'decreasing correlation')
        check(isclose(sum(1/(2*m*m*sin((k+.5)*pi/(2*m))**2)
                          for k in range(m)),1,abs_tol=1e-12), 'weight sum')

for m in range(1,101):
    for b in (m,m+1):
        # Exact Green function L^{-1}1, checked site-by-site.
        x=[Fraction(m*m-i*(i-1),2) for i in range(1,m+1)]
        for j in range(m):
            z=2*x[0] if m==1 else (
                x[0]-x[1] if j==0 else
                3*x[j]-x[j-1] if j==m-1 else
                2*x[j]-x[j-1]-x[j+1])
            check(z==1,f'Green function m={m}, index={j}')
        g=Fraction(2*b,m)*sum(x)
        check(g==Fraction(b*(2*m*m+1),3),f'integrated autocorrelation m={m}')
        for t in (0,1,m,2*m*m,m**3):
            check(-1e-10 <= spectral(m,b,t) <= 1+1e-10,'spectral range')

# Direct half-integer mode eigen-relation for representative sizes.
for m in range(2,31):
    for k in range(m):
        theta=(k+.5)*pi/m
        vec=[cos((i+.5)*theta) for i in range(m)]
        lam=2-2*cos(theta)
        for j in range(m):
            left = (vec[0]-vec[1] if j==0 else
                    3*vec[-1]-vec[-2] if j==m-1 else
                    2*vec[j]-vec[j-1]-vec[j+1])
            check(isclose(left,lam*vec[j],abs_tol=3e-12,rel_tol=1e-9),'eigenvector')

print(f'VERIFY_OK checks={checks}')
