"""Exact-moment and direct integration checks for Dirichlet diversity covariance.

Run: python check_covariance.py
Requires Python standard library; optional mpmath for the direct beta integrations.
"""
from fractions import Fraction
from itertools import product


def harmonic(n):
    return sum((Fraction(1, j) for j in range(1, n + 1)), Fraction(0))


def raw_moment_covariance(alpha):
    """Evaluate E[SH]-E[S]E[H] from differentiated Dirichlet moments."""
    a = tuple(alpha)
    A = sum(a)
    B = sum(x * x for x in a)
    M = A + B
    den = A * (A + 1) * (A + 2)
    e_s = Fraction(M, A * (A + 1))
    e_h = sum((Fraction(x, A) * (harmonic(A) - harmonic(x)) for x in a), Fraction(0))
    e_sh = sum((Fraction(-x * (M + 2*x + 2), den) * (harmonic(x) - harmonic(A + 2))
                 - Fraction(x * (2*x + 3), den) for x in a), Fraction(0))
    return e_sh - e_s * e_h


def pairwise_covariance(alpha):
    a = tuple(alpha)
    A = sum(a)
    total = Fraction(0)
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            diff = (a[i]-a[j]) * (harmonic(a[i]) - harmonic(a[j]))
            bracket = 1 + Fraction(A+1,A)*diff
            assert bracket >= 1
            total += a[i]*a[j]*bracket
    return -Fraction(2, A*(A+1)**2*(A+2))*total


def weighted_decomposition(alpha):
    a = tuple(alpha)
    A = sum(a)
    B = sum(x*x for x in a)
    mu_a = Fraction(B,A)
    mu_psi = sum((Fraction(x,A)*harmonic(x) for x in a), Fraction(0))
    cw = sum((Fraction(x,A)*(x-mu_a)*(harmonic(x)-mu_psi) for x in a), Fraction(0))
    return -Fraction(A*A-B, A*(A+1)**2*(A+2)) - Fraction(2, (A+1)*(A+2))*cw


def test_exact():
    n = 0
    for m in range(2, 6):
        for alpha in product(range(1, 5), repeat=m):
            moment = raw_moment_covariance(alpha)
            assert moment == pairwise_covariance(alpha), alpha
            assert moment == weighted_decomposition(alpha), alpha
            assert moment < 0, alpha
            if len(set(alpha)) == 1:
                a=alpha[0]
                assert moment == -Fraction(a*(m-1), (m*a+1)**2*(m*a+2))
            n += 1
    return n


def test_integrals():
    import mpmath as mp
    mp.mp.dps = 55
    out = []
    for a_text,b_text in [('0.4','1.9'),('1','2'),('4.5','0.8'),('3.2','3.2')]:
        a,b=mp.mpf(a_text),mp.mpf(b_text)
        A=a+b
        B=a*a+b*b
        S=A+B
        norm=mp.beta(a,b)
        def h(x):
            if x == 0 or x == 1: return mp.mpf('0')
            return -x*mp.log(x)-(1-x)*mp.log(1-x)
        def mass(x):
            if x == 0 or x == 1: return mp.mpf('0')
            return x**(a-1)*(1-x)**(b-1)/norm
        def integ(func):
            def smooth(u):
                if u == 0 or u == 1:
                    return mp.mpf('0')
                x8 = u**8
                y8 = (1-u)**8
                x = x8/(x8+y8)
                jac = 8*u**7*(1-u)**7/(x8+y8)**2
                return mass(x)*func(x)*jac
            return mp.quad(smooth,[0,mp.mpf('.25'),mp.mpf('.5'),mp.mpf('.75'),1])
        eg=integ(lambda x:x*x+(1-x)*(1-x))
        eh=integ(h)
        egh=integ(lambda x:(x*x+(1-x)*(1-x))*h(x))
        observed=egh-eg*eh
        w=[a/A,b/A]
        alpha=[a,b]
        psi=[mp.digamma(a+1),mp.digamma(b+1)]
        mu_a=sum(w[i]*alpha[i] for i in range(2))
        mu_psi=sum(w[i]*psi[i] for i in range(2))
        cw=sum(w[i]*(alpha[i]-mu_a)*(psi[i]-mu_psi) for i in range(2))
        predicted=-(A*A-B)/(A*(A+1)**2*(A+2))-2*cw/((A+1)*(A+2))
        err=abs(observed-predicted)
        assert err < mp.mpf('1e-45'), (a_text,b_text,err)
        out.append((a_text,b_text,mp.nstr(observed,16),mp.nstr(err,5)))
    return out

if __name__=='__main__':
    count = test_exact()
    print('Exact integer-vector cases:',count,'(three formula checks and strict sign each)')
    for row in test_integrals():
        print('Numerical beta integration:',*row)
    print('All checks passed.')
