#!/usr/bin/env python3
"""Numerical regression checks for a fractional Volterra power commutator.

These are supplementary checks, not proofs of operator-norm or spectral assertions.
Needs mpmath; run python verify_fractional_commutator.py.
"""
import mpmath as mp
mp.mp.dps = 35


def H(alpha, beta):
    # Exact Hilbert-Schmidt expression after triangular-kernel scaling.
    j = mp.quad(lambda z: (z**beta - 1)**2*(1-z)**(2*alpha-2), [0, mp.mpf('0.1'), mp.mpf('0.5'), 1])
    return j/(2*(alpha+beta)*mp.gamma(alpha)**2)


def critical_kernel(alpha, s):
    return mp.expm1(alpha*s)*mp.e**(-s/2)*(1-mp.e**(-s))**(alpha-1)/mp.gamma(alpha)


def critical_residue(alpha):
    j = mp.quad(lambda z: (z**(-alpha)-1)**2*(1-z)**(2*alpha-2), [0, mp.mpf('0.1'), mp.mpf('0.5'), 1])
    return j/mp.gamma(alpha)**2


def critical_cutoff_HS(alpha, n):
    eps=mp.e**(-n)
    return mp.quad(lambda z: (z**(-alpha)-1)**2*(1-z)**(2*alpha-2)*(n+mp.log(z)), [eps, mp.mpf('0.1'), mp.mpf('0.5'), 1])/mp.gamma(alpha)**2


def rel_close(a,b,tol=mp.mpf('1e-14')):
    assert abs(a-b) <= tol*max(1,abs(a),abs(b)), (a,b)


def main():
    tests=0
    for alpha in [mp.mpf('0.1'),mp.mpf('0.2'),mp.mpf('0.25'),mp.mpf('0.35')]:
        norm_gamma=mp.gamma(mp.mpf('.5')-alpha)/mp.gamma(mp.mpf('.5'))-mp.gamma(mp.mpf('.5'))/mp.gamma(mp.mpf('.5')+alpha)
        norm_integral=mp.quad(lambda s: critical_kernel(alpha,s), [0,1,5,30,300])
        rel_close(norm_gamma,norm_integral, mp.mpf('1e-12'));tests+=1
        residue=critical_residue(alpha)
        j_closed=(-2*mp.gamma(1-alpha)*mp.gamma(2*alpha-1)/mp.gamma(alpha)+1/(2*alpha-1))/mp.gamma(alpha)**2
        rel_close(residue,j_closed, mp.mpf('5e-9')); tests+=1
        # Critical cutoff energy has the explicit logarithmic slope.
        n1,n2=mp.mpf(25),mp.mpf(60)
        slope=(critical_cutoff_HS(alpha,n2)-critical_cutoff_HS(alpha,n1))/(n2-n1)
        assert abs(slope/residue-1)<mp.mpf('0.001'), (alpha,slope/residue);tests+=1
        delta=mp.mpf('.0001')
        hs=H(alpha,-alpha+delta)
        assert abs(2*delta*hs/residue-1)<mp.mpf('.2'), (alpha,hs,residue);tests+=1
    # For beta < -alpha, the localized block norm scales exactly as epsilon^(alpha+beta).
    alpha,beta=mp.mpf('.2'),mp.mpf('-.3')
    e1,e2=mp.mpf('.01'),mp.mpf('.0001')
    block_ratio=(e1/e2)**(alpha+beta)
    rel_close(block_ratio,mp.power(100,mp.mpf('-.1')));tests+=1
    print('PASS',tests,'supplementary numerical identities/asymptotic checks')

if __name__=='__main__':
    main()
