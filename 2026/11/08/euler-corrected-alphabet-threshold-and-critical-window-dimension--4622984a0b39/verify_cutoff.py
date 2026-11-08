"""Reproduce finite-alphabet Zipf pressure and threshold diagnostics.
Requires mpmath >= 1.3; finite tests supplement the analytical proof.
"""
import mpmath as mp

mp.mp.dps = 95

def parameters(lam, eps):
    q = 1 + eps
    c = lam / mp.zeta(q)
    a = c ** (1 / q)
    return q, c, a

def partial_zeta(p, n):
    if p == 1:
        return mp.digamma(n+1) + mp.euler
    return mp.zeta(p) - mp.zeta(p, n+1)

def pressure(e, a, n):
    return a ** (1+e) * partial_zeta(1+e, n)

def solve_e(a, n, guess):
    return mp.findroot(lambda e: pressure(e, a, n)-1, (guess-mp.mpf('0.00001'),guess+mp.mpf('0.00001')), solver='secant', tol=mp.mpf('1e-75'), verify=True)

def main():
    tests = 0
    for lamstr in ('0.4','0.6'):
        lam = mp.mpf(lamstr)
        for estr in ('0.07', '0.03', '0.015'):
            eps=mp.mpf(estr)
            q,c,a = parameters(lam,eps)
            L=1/a-mp.euler
            for t in (-1,1):
                n=int(mp.floor(mp.exp(L+t)))
                e=solve_e(a,n,2*a*a*t)
                assert e*t>0
                ratio=e/(2*a*a*t)
                assert mp.mpf('0.60') < ratio < mp.mpf('1.1'), (lamstr,estr,t,ratio)
                assert abs(pressure(e,a,n)-1)<mp.mpf('1e-65')
                tests+=1
            n0=int(mp.floor(mp.exp(1/(lam*eps))))
            ec=solve_e(a,n0,2*lam*eps**2*mp.log(1/eps))
            assert ec>0
            tests+=1
            # For the index at the exact strict-crossing boundary, the harmonic criterion decides the sign.
            for n,t in [(int(mp.floor(mp.exp(L-2))),-2),(int(mp.floor(mp.exp(L+2))),2)]:
                sign=mp.sign(a*partial_zeta(1,n)-1)
                assert sign==mp.sign(t)
                tests+=1
    print('VERIFY_OK finite_pressure_roots=18 threshold_signs=12 high_precision=95')
    print('Analytic asymptotic and historical priority are not certified by these tests.')

if __name__=='__main__':
    main()
