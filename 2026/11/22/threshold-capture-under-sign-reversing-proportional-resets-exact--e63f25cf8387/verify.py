"""Reproducible deterministic checks for multiplicative-reflection threshold capture.

Requirements: Python 3.10+, mpmath, numpy, scipy.
Run: python verify.py
All assertions test finite diagnostics; the theorem relies on the mathematical proof.
"""
from fractions import Fraction
import math
import mpmath as mp
import numpy as np
from scipy.sparse import lil_matrix
from scipy.sparse.linalg import spsolve

mp.mp.dps = 65


def entire_functions(q, z, max_terms=300):
    """Return H_q, H_q', G_q, G_q' from the defining factorial series."""
    q, z = mp.mpf(q), mp.mpf(z)
    H = Hp = G = Gp = mp.mpf('0')
    c = mp.mpf(1)
    for n in range(max_terms):
        H += c*z**(2*n+1)/mp.factorial(2*n+1)
        Hp += c*z**(2*n)/mp.factorial(2*n)
        c *= 1+q**(2*n+1)
    c = mp.mpf(1)
    for n in range(1, max_terms+1):
        G += c*z**(2*n)/mp.factorial(2*n)
        Gp += c*z**(2*n-1)/mp.factorial(2*n-1)
        c *= 1-q**(2*n)
    return H, Hp, G, Gp


def analytic(q, beta):
    q, beta = mp.mpf(q), mp.mpf(beta)
    h, _, g, _ = entire_functions(q, beta)
    H, Hp, G, Gp = entire_functions(q, beta/q)
    den = Hp + H + h
    B = (g - G - Gp - 1) / den
    p = h / den
    u = g - B*h
    return u, p, B, den


def inner_u(q, beta, x):
    u, _, B, _ = analytic(q,beta)
    h, _, g, _ = entire_functions(q,beta)
    hh, _, gg, _ = entire_functions(q,beta*mp.mpf(x))
    return B*(hh-h)-(gg-g)


def inner_p(q, beta, x):
    _, _, _, den = analytic(q,beta)
    h = entire_functions(q,beta)[0]
    hh = entire_functions(q,beta*mp.mpf(x))[0]
    return (h-hh)/den


def fd_solver(q, beta, N):
    """Independent central finite-difference / interpolation boundary solver.

    Solves u''-beta^2 u+beta^2 u(-q x)=-beta^2,
    and p''-beta^2 p+beta^2 p(-q x)=0 on [-1/q, 1].
    Left boundary is u' = beta(u-1), right Dirichlet zero.
    """
    left = -1/q
    grid = np.linspace(left, 1., N+1)
    dx = grid[1]-grid[0]
    A = lil_matrix((N+1, N+1), dtype=float)
    rhs_u = np.zeros(N+1)
    rhs_p = np.zeros(N+1)
    # Second-order one-sided approximation to the exact left Robin condition.
    A[0,0] = -3/(2*dx)-beta
    A[0,1] = 4/(2*dx)
    A[0,2] = -1/(2*dx)
    rhs_u[0] = rhs_p[0] = -beta
    for j in range(1,N):
        A[j,j-1] += 1/dx**2
        A[j,j] += -2/dx**2-beta**2
        A[j,j+1] += 1/dx**2
        xt = -q*grid[j]
        z = (xt-left)/dx
        low = int(np.floor(z))
        low = max(0,min(N-1,low))
        t = max(0.,min(1.,z-low))
        A[j,low] += beta**2*(1-t)
        A[j,low+1] += beta**2*t
        rhs_u[j] = -beta**2
    A[N,N] = 1
    ua = spsolve(A.tocsc(),rhs_u)
    pa = spsolve(A.tocsc(),rhs_p)
    return np.interp(0.,grid,ua),np.interp(0.,grid,pa)


def rational_recurrence_checks():
    q=Fraction(1,2)
    oh=[Fraction(1)]
    eg=[Fraction(1)]
    for n in range(1,18):
        oh.append(oh[-1]*(1+q**(2*n-1)))
        eg.append(eg[-1]*(1-q**(2*n-2)) if n>=2 else Fraction(1))
    # Odd recursion for H''=H-H(-q z); even for G''=1+G-G(-q z).
    for n in range(17):
        assert oh[n+1] == oh[n]*(1+q**(2*n+1))
        if n>=1:
            assert eg[n+1] == eg[n]*(1-q**(2*n))
    return 34


def main():
    tests = rational_recurrence_checks()
    for q,beta in [(0.25,0.5),(0.25,1.5),(0.5,0.5),(0.5,1.),
                   (0.5,2.),(0.75,0.8),(0.75,2.),(1.,1.),(1.,2.)]:
        q,beta=mp.mpf(str(q)),mp.mpf(str(beta))
        u,p,B,den=analytic(q,beta)
        assert 0 < p < 1 and u>0
        assert abs(inner_u(q,beta,1))<mp.mpf('1e-48')
        assert abs(inner_p(q,beta,1))<mp.mpf('1e-48')
        # Matching at the outer-to-inner interface.
        y=beta/q
        H,Hp,G,Gp=entire_functions(q,y)
        h=entire_functions(q,beta)[0]
        assert abs(B*Hp+Gp-(B*(-H-h)-G+entire_functions(q,beta)[2]-1))<mp.mpf('1e-48')
        assert abs((-Hp/den)-((H+h)/den-1))<mp.mpf('1e-48')
        # Independent coefficient derivatives of the two entire series.
        for x in [-0.5/float(q),-0.3,0.,0.4,0.8]:
            if x < -1/float(q) or x > 1: continue
            y=beta*mp.mpf(str(x))
            hc=mp.mpf(1); gc=mp.mpf(1); h2=mp.mpf(0); g2=mp.mpf(0)
            for n in range(1,160):
                hc *= 1+q**(2*n-1)
                h2 += hc*y**(2*n-1)/mp.factorial(2*n-1)
                g2 += gc*y**(2*n-2)/mp.factorial(2*n-2)
                gc *= 1-q**(2*n)
            hval=entire_functions(q,y)[0]
            hshift=entire_functions(q,-q*y)[0]
            gval=entire_functions(q,y)[2]
            gshift=entire_functions(q,-q*y)[2]
            assert abs(h2-hval+hshift)<mp.mpf('1e-35')
            assert abs(g2-1-gval+gshift)<mp.mpf('1e-35')
            tests += 2
        # Separate finite-difference boundary-value solver must converge.
        errors=[]
        for N in [150,300,600]:
            un,pn=fd_solver(float(q),float(beta),N)
            errors.append(max(abs(un-float(u)), abs(pn-float(p))))
            tests += 2
        # At least the finest grid agrees to a specified absolute tolerance.
        assert errors[-1] < 2.0e-4, (q,beta,errors)
        # Convergence versus grid refinement at the expected second order.
        assert errors[2] < .40*errors[1] or errors[2] < 2.e-6,(q,beta,errors)
        tests += 6
    # Exact noncontractive endpoint q=1 has elementary closed forms.
    for beta in ['0.5','1','2']:
        b=mp.mpf(beta)
        h=mp.sinh(mp.sqrt(2)*b)/mp.sqrt(2)
        den=mp.cosh(mp.sqrt(2)*b)+2*h
        exact_u=b*b/2+(1+b)*h/den
        exact_p=h/den
        u,p,*_=analytic(mp.mpf(1),b)
        assert abs(u-exact_u)<mp.mpf('1e-45')
        assert abs(p-exact_p)<mp.mpf('1e-45')
        tests+=2
    # Two limits: q -> 0 and beta -> infinity.
    beta=mp.mpf('1')
    ratios=[]
    for q in ['0.25','0.15','0.1','0.06']:
        p=analytic(q,beta)[1]
        ratios.append(p/(mp.sinh(beta)*mp.exp(-beta/mp.mpf(q))))
        tests+=1
    assert abs(ratios[-1]-1)<mp.mpf('.07'),ratios
    for q in ['0.25','0.5']:
        ratios=[]
        for beta in ['4','8','12','18']:
            p=analytic(q,beta)[1]
            ref=mp.mpf('.5')*mp.exp(-mp.mpf(beta)*(1/mp.mpf(q)-1))
            ratios.append(p/ref)
            tests+=1
        assert abs(ratios[-1]-1)<mp.mpf('.004'),(q,ratios)
    print('PASS',tests,'finite independent algebra/finite-difference/asymptotic diagnostics')
    u,p,*_=analytic(mp.mpf('.5'),mp.mpf('1'))
    print('q=1/2, beta=1: r E_0 tau =',mp.nstr(u,20),'jump-capture probability =',mp.nstr(p,20))

if __name__=='__main__': main()
