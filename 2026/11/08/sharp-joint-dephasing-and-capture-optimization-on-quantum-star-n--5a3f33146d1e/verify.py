"""Reproducible checks for dephased star-network capture-time identities.

Run: python verify.py
Dependencies: numpy, sympy. The finite checks supplement the analytic proof.
"""
import math
import numpy as np
import sympy as sp

checks = 0

def check(cond, message):
    global checks
    assert bool(cond), message
    checks += 1


def exact_formula(n, J, gamma, kappa):
    return (n/kappa + (n-1)*kappa/(4*J**2)
            + n*gamma/(2*J**2) + (n-3)/gamma
            + (n-2)*(n-3)/(2*gamma+kappa))


def full_liouvillian_time(n, J, gamma, kappa):
    """Unreduced N^2-complex-variable generator; initial site is leaf 2."""
    H = np.zeros((n,n), complex)
    for j in range(1,n):
        H[0,j] = H[j,0] = J
    trap = np.zeros((n,n), complex)
    trap[1,1] = 1
    L = np.empty((n*n,n*n), complex)
    for column in range(n*n):
        E = np.zeros((n,n), complex)
        E.flat[column] = 1
        d = (-1j*(H@E-E@H)
             -gamma*(E-np.diag(np.diag(E)))
             -0.5*kappa*(trap@E+E@trap))
        L[:,column] = d.reshape(-1)
    rho0 = np.zeros((n,n), complex)
    rho0[2,2] = 1
    X = np.linalg.solve(-L,rho0.reshape(-1)).reshape((n,n))
    check(abs(X.trace().imag)<1e-9, 'Mean must be real')
    check(abs(kappa*X[1,1]-1)<1e-9, 'Total capture probability')
    return X.trace().real


def verify_symbolic():
    n,m,J,g,k=sp.symbols('n m J g k', positive=True)
    A = 1/(2*J)
    B = -1/(2*J*m)
    Q = 1/k
    D = -1/(m*g)
    C = (m-1)/(m*(2*g+k))
    P = Q+m*C+(g+k/2)*A/J
    O = P-C-(m-1)*D-g*B/J
    check(sp.simplify(-2*J*(A+m*B))==0,'hub equation')
    check(sp.simplify(2*J*A-k*Q)==0,'trap equation')
    check(sp.simplify(2*J*B+1/m)==0,'other-leaf initial condition')
    check(sp.simplify(J*(P-Q-m*C)-(g+k/2)*A)==0,'hub-trap coherence')
    check(sp.simplify(J*(P-C-O-(m-1)*D)-g*B)==0,'hub-other coherence')
    check(sp.simplify(J*(A+B)-(g+k/2)*C)==0,'trap-other coherence')
    check(sp.simplify(2*J*B-g*D)==0,'other-other coherence')
    expression = sp.simplify(P+Q+m*O)
    target = exact_formula(m+2,J,g,k)
    check(sp.simplify(expression-target)==0,'closed capture-time formula')
    derivative = (m+2)/(2*J**2)-(m-1)/g**2-2*m*(m-1)/(2*g+k)**2
    second = 2*(m-1)/g**3+8*m*(m-1)/(2*g+k)**3
    check(sp.simplify(sp.diff(target,g)-derivative)==0,'first derivative')
    check(sp.simplify(sp.diff(target,g,2)-second)==0,'second derivative')
    check(sp.simplify(sp.diff(derivative,k)-4*m*(m-1)/(2*g+k)**3)==0,'sink monotonicity')
    check(sp.simplify(((m+2)/(2*J**2) - (m-1)/g**2
                   -2*m*(m-1)/(2*g)**2).subs(g,J*sp.sqrt(m-1)))==0,'weak sink boundary')
    a=sp.symbols('a', positive=True)
    b=2*(1-a)
    f=1/b-b/4+1/a-sp.Rational(5,2)
    root=(1-sp.sqrt(3)+sp.sqrt(2*sp.sqrt(3)))/2
    check(sp.simplify(sp.diff(f,a).subs(a,root))==0,'asymptotic rate ratio')
    check(sp.simplify(sp.diff(f,a,2) - (1/(1-a)**3+2/a**3))==0,'strict convexity on the limit manifold')
    check(sp.simplify(sp.Symbol('s')/4+1/sp.Symbol('s')-1
        -(sp.Symbol('s')-2)**2/(4*sp.Symbol('s')))==0,'sharp leading minimum')
    return root


def verify_numeric(root):
    for n in [3,4,5,6,7]:
        for J,g,k in [(1.0,0.3,2.0),(0.8,1.4,0.7),(1.6,2.5,3.1),
                      (1.2,0.06,0.9)]:
            actual=full_liouvillian_time(n,J,g,k)
            expected=exact_formula(n,J,g,k)
            check(abs(actual-expected)<1e-7*max(1,abs(expected)),
                  'full Liouvillian mismatch for n=%s J=%s g=%s k=%s'%(n,J,g,k))
    a0=float(root.evalf(30))
    b0=2*(1-a0)
    check(0<a0<1 and 0<b0<2,'asymptotic interior constants')
    for n in [4,5,6,10,50,100,1000,10000]:
        # Strictly convex two-variable objective; solve both stationary conditions.
        def d_k(g,k):
            return -n/k**2+(n-1)/4-(n-2)*(n-3)/(2*g+k)**2
        def d_g(g,k):
            return n/2-(n-3)/g**2-2*(n-2)*(n-3)/(2*g+k)**2
        # Bisection nested on unique g optimum at each k, then k optimum.
        def g_best(k):
            lo=1e-12;hi=max(2*math.sqrt(n),4.0)
            for _ in range(110):
                mid=(lo+hi)/2
                if d_g(mid,k)>0:hi=mid
                else:lo=mid
            return (lo+hi)/2
        lo=1e-8;hi=8*math.sqrt(n)
        for _ in range(110):
            mid=(lo+hi)/2
            g=g_best(mid)
            # Envelope derivative in k.
            if d_k(g,mid)>0: hi=mid
            else: lo=mid
        k=(lo+hi)/2;g=g_best(k)
        check(abs(d_g(g,k))<1e-8,'gamma optimality residual')
        check(abs(d_k(g,k))<1e-8,'sink optimality residual')
        check(0<g and 0<k,'positive joint optimum')
        if n==10000:
            check(abs(g/math.sqrt(n)-a0)<2e-4,'large-N gamma constant')
            check(abs(k/math.sqrt(n)-b0)<2e-4,'large-N sink constant')
            check(abs(exact_formula(n,1,g,k)/n**1.5-1)<5e-4,'large-N minimal-time scaling')
    return True

if __name__=='__main__':
    r=verify_symbolic()
    verify_numeric(r)
    print('PASS:',checks,'symbolic and independently evaluated Liouvillian/optimization assertions')
    print('Large-size dimensionless constants:',float(r.evalf(15)),2*(1-float(r.evalf(15))))
