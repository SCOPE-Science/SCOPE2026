"""Self-contained checks for a split-network grounding theorem.

Run with Python 3.9+; only the standard library is required.
These finite tests supplement, but do not replace, the analytic proof.
"""
from fractions import Fraction as F
from math import sqrt

checks = 0

def check(pred, message):
    global checks
    assert pred, message
    checks += 1

def inverse(M):
    n = len(M)
    A = [list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(M)]
    for j in range(n):
        h=next(i for i in range(j,n) if A[i][j])
        A[j], A[h] = A[h], A[j]
        v=A[j][j]
        A[j]=[x/v for x in A[j]]
        for i in range(n):
            if i != j:
                v=A[i][j]
                A[i]=[x-v*y for x,y in zip(A[i],A[j])]
    return [row[n:] for row in A]

def split_matrix(p,q,a,b):
    n=p+q
    M=[[F(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        M[i][i] += a if i<p else b
    for i in range(n):
        for j in range(i+1,n):
            if i<p or j<p:
                M[i][i] += 1; M[j][j] += 1
                M[i][j] -= 1; M[j][i] -= 1
    return M

def exact_trace(p,q,a,b):
    R=inverse(split_matrix(p,q,a,b))
    return sum(R[i][i] for i in range(p+q))

def reduced(p,q,a,b):
    d=p*a+q*b+a*b
    return F(p-1,p+q+a)+F(q-1,p+b)+(p+q+a+b)/d

def from_budget(p,q,B,a):
    return reduced(p,q,a,(B-p*a)/q)

def derivative_from_matrix(p,q,B,a):
    b=(B-p*a)/q; Q=inverse(split_matrix(p,q,a,b))
    # Directional derivative -sum_i H_ii (Q^2)_ii.
    diag_sq=[sum(Q[i][k]*Q[k][i] for k in range(p+q)) for i in range(p+q)]
    return -sum(diag_sq[:p])+F(p,q)*sum(diag_sq[p:])

def derivative_reduced(p,q,B,a):
    b=(B-p*a)/q; D=p*a+q*b+a*b
    T=p+q+a+b
    dD=b-F(p,q)*a  # derivative with db/da=-p/q
    dT=1-F(p,q)
    return -(p-1)/(p+q+a)**2 + F(p,q)*(q-1)/(p+b)**2+(dT*D-T*dD)/D**2

def alpha_beta(p,q):
    alpha=F(q*(q-1),p)
    beta=1+F(q*q*(p-1),(p+q)**2)
    return alpha,beta

def S(p,q,t):
    alpha,beta=alpha_beta(p,q)
    return alpha/(1+t)**2-beta-2/t

def gamma(beta):
    t0=2/(1+sqrt(1+4*float(beta)))
    return (1+t0)**3/t0**2

def phase(p,q):
    a,b=alpha_beta(p,q)
    v=float(a)-gamma(b)
    return (v>1e-9)-(v< -1e-9)

# Full exact inversion on small graphs, including boundary class omissions.
for p in range(2,7):
    for q in range(2,8):
        for a,b in ((F(0),F(1,2)), (F(2,3),F(0)),
                    (F(1,2),F(3,4)), (F(3,1),F(2,5))):
            check(exact_trace(p,q,a,b)==reduced(p,q,a,b),
                  ('spectral formula',p,q,a,b))

# Exact matrix-based gradients in the feasible tangent direction.
for p in range(2,5):
    for q in range(2,6):
        for B in (F(1,2),F(3),F(37,2)):
            for a in (F(0),B/(3*p),B/p):
                check(derivative_reduced(p,q,B,a)==derivative_from_matrix(p,q,B,a),
                      ('gradient',p,q,B,a))
                if a==0:
                    t=B/F(p*q)
                    check(F(q*q)*derivative_from_matrix(p,q,B,a)==S(p,q,t),
                          ('boundary sign',p,q,B))
                if a==B/p:
                    check(derivative_from_matrix(p,q,B,a)>0,
                          ('peripheral gains cannot vanish',p,q,B))

# Complete small-case phase discrimination using exact rational S sign.
for p,q,B,expect in ((2,6,F(1),False),(2,6,F(6),True),
                      (2,6,F(20),False),(2,5,F(5),False),
                      (3,7,F(10),True),(3,6,F(10),False),
                      (4,9,F(15),True),(4,8,F(15),False)):
    sign=S(p,q,B/F(p*q))
    check((sign>=0)==expect,('boundary phase',p,q,B,sign))

# The alpha-vs-gamma criterion must coincide with a positive S interval.
for p in range(2,15):
    for q in range(2,30):
        c=phase(p,q)
        t0=2/(1+sqrt(1+4*float(alpha_beta(p,q)[1])))
        check((float(S(p,q,F(str(t0))))>0)==(c>0),('phase criterion',p,q))

# The boundary classification agrees with exhaustive rational grids on test budgets.
for p,q in ((2,5),(2,6),(3,6),(3,7),(4,8),(4,9)):
    for B in (F(1),F(3),F(6),F(12),F(30)):
        at_zero=S(p,q,B/F(p*q)) >= 0
        values=[from_budget(p,q,B,B*F(k,20*p)) for k in range(21)]
        if at_zero:
            check(values[0] == min(values), ('global boundary grid',p,q,B))
        else:
            check(from_budget(p,q,B,B*F(1,10**8*p)) < values[0], ('interior beats boundary',p,q,B))

# A concrete eight-vertex witness has two positive transition points.
# S_{2,6}(t)=-[25t^3+82t^2-151t+32]/[16t(1+t)^2].
for t,sgn in ((F(1,10),-1),(F(1,2),1),(F(2),-1)):
    check((S(2,6,t)>0)==(sgn>0),('cubic witness',t))
    check(S(2,6,t)==-F(25*t**3+82*t**2-151*t+32,16*t*(1+t)**2),
          ('cubic identity',t))

# Sharp 3/4-power size crossover, outside its finite-size boundary layer.
for p in (10**8,10**10):
    for c,expected in ((1.25,-1),(1.60,1)):
        q=int(c*p**.75)
        check(phase(p,q)==expected,('size crossover',p,q))

print('PASS:',checks,'checks; exact Laplacian inversions, derivatives, phases and scaling witnesses')
