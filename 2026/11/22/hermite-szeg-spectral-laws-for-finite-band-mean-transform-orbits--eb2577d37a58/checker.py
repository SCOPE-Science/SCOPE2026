"""Finite checks for a Gaussian spectral law in mean-transform orbits.
These calculations illustrate, but do not prove, the asymptotic theorem.
Requires Python 3, NumPy and SciPy.
"""
import math
import numpy as np
from scipy.special import gammaln
from scipy.linalg import eigh_tridiagonal


def binomial_probs(k, q=0.5):
    j = np.arange(k + 1, dtype=float)
    return np.exp(gammaln(k+1)-gammaln(j+1)-gammaln(k-j+1)
                  +j*np.log(q)+(k-j)*np.log1p(-q))


def example_spectrum(k, epsilon=0.2):
    # A has (0,1) entry +eps and (1,2) entry -eps, with adjoints.
    # After k mean transforms, the offdiagonal coefficients are
    # eps*(p_k(-n)-p_k(1-n)), for -k-1 <= n <= 0.
    p = np.pad(binomial_probs(k), (1, 1))
    edge = epsilon*(p[1:-1]-p[2:])
    # Include both end zeros; adding zero eigenvalues does not change norms.
    vals = eigh_tridiagonal(np.zeros(len(edge)+1), edge,
                            eigvals_only=True, check_finite=True)
    return vals


def verify():
    eps=0.2
    assert eps*math.sqrt(2)<1
    op_limit = 2*eps/math.sqrt(2*math.pi*math.e)
    hs_sq_limit = eps*eps/(2*math.sqrt(math.pi))
    trace_limit = (4*eps/math.pi)*math.sqrt(2/math.pi)
    records=[]
    for k in (40, 80, 160, 320, 640):
        vals=example_spectrum(k,eps)
        sigma=math.sqrt(k)/2
        op=sigma**2*np.max(np.abs(vals))
        hs2=sigma**3*np.sum(vals**2)
        l1=sigma*np.sum(np.abs(vals))
        exact_hs2=4*eps*eps/(k+1)*math.exp(gammaln(2*k+1)-2*gammaln(k+1)-2*k*math.log(2))
        assert abs(np.sum(vals**2)-exact_hs2)<2e-12
        records.append((k,op,hs2,l1))
    assert abs(records[-1][1]/op_limit-1)<0.08, (records,op_limit)
    assert abs(records[-1][2]/hs_sq_limit-1)<0.01, (records,hs_sq_limit)
    assert abs(records[-1][3]/trace_limit-1)<0.08, (records,trace_limit)
    # Zero sum, nonzero first moment on each offdiagonal.
    a_plus={0:eps,1:-eps}
    assert abs(sum(a_plus.values()))<1e-14
    assert abs(sum(j*v for j,v in a_plus.items())+eps)<1e-14
    print('PASS: exact Hilbert-Schmidt binomial identity and asymptotic example')
    print('k, scaled_op_norm, scaled_HS_sq, scaled_trace_norm')
    for r in records: print(*[f'{x:.10g}' for x in r])
    print('predicted limits',op_limit,hs_sq_limit,trace_limit)

if __name__=='__main__': verify()
