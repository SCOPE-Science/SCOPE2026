"""Independent finite diagnostics for two-degree Hardy-annulus cross-commutators.

Only finite identities and quadratures are checked; the infinite theorem is analytic.
"""
from fractions import Fraction as F
from math import exp, log, sqrt, isclose

checks = 0

def check(ok, detail=''):
    global checks
    assert ok, detail
    checks += 1

def qpow(q, j):
    return q ** j

def cross_coeff_rational(q, m, n, j):
    x, am, bn = qpow(q,j), qpow(q,m), qpow(q,n)
    root_num = (1+x)*(1+bn*x/am)
    first = (1+bn*x)
    second = (1+x)*(1+bn*x/am)/(1+x/am)
    algebraic_a = (first-second)
    algebraic_b = x*(1-am)*(1-bn)/(am+x)
    return algebraic_a, algebraic_b, root_num

def V(a,b,t):
    alpha, beta, x = exp(-a), exp(-b), exp(-t)
    return (1-alpha)*(1-beta)*x/((alpha+x)*sqrt((1+x)*(1+beta*x/alpha)))

def midpoint_integral(f,left,right,N=20000):
    step=(right-left)/N
    return step * sum(f(left+(j+0.5)*step) for j in range(N))

def H2_formula(a,b):
    alpha,beta=exp(-a),exp(-b)
    if abs(a-b)<1e-12:
        return a*(1-alpha*alpha)-2*(1-alpha)**2
    I=(-1/((1-alpha)*(1-beta))
       -alpha*log(alpha)/((1-alpha)**2*(alpha-beta))
       +beta*log(beta)/((alpha-beta)*(1-beta)**2))
    return (1-alpha)**2*(1-beta)**2*I

for q in [F(1,2),F(2,3),F(4,5)]:
    for m in range(1,8):
        for n in range(1,8):
            for j in range(-8,10):
                A,B,D=cross_coeff_rational(q,m,n,j)
                check(A==B, f'cross coefficient failed {q} {m} {n} {j}')
                check(A>0 and D>0)

for a,b in [(.31,.62),(.83,1.34),(1.5,.3),(.7,.7),(2.4,1.7)]:
    # Wide enough for exponential tails for these positive scaling limits.
    numeric=midpoint_integral(lambda t: V(a,b,t)**2, -36.,36.)
    closed=H2_formula(a,b)
    check(isclose(numeric,closed,rel_tol=2e-8,abs_tol=2e-9),(a,b,numeric,closed))
    for t in [-4,-1.1,0,1.2,4]:
        check(isclose(V(a,b,t),V(b,a,t+b-a),rel_tol=1e-13,abs_tol=1e-13))

for h,m,n in [(.31,2,3),(.1,4,8),(.025,16,27),(.008,125,198)]:
    a,b=m*h,n*h
    for u in [.01,.05,.1,.2,.3,.4]:
        # Dense grid gives a numerical peak and two crossings.
        step=.001
        xx=[-25+i*step for i in range(50001)]
        vv=[V(a,b,t) for t in xx]
        chosen=[t for t,v in zip(xx,vv) if v>u]
        if not chosen: continue
        # endpoints bracketed by adjacent grid points
        left,right=chosen[0],chosen[-1]+step
        N=sum(V(a,b,j*h)>u for j in range(-int(25/h),int(25/h)+1))
        check(abs(h*N-(right-left))<=h+3*step,(h,m,n,u,N,left,right))

print('HARDY_CROSS_COMMUTATOR_DIAGNOSTICS_OK',checks)
