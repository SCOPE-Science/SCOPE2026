"""Finite checks of first-order or higher band Fourier sampling on a coordinate-punctured product.

Requires Python 3 and NumPy. Full matrix entries are generated independently of
all spectral formulas. The theorem for arbitrary dimensions is proved in RESULT.md.
"""
from itertools import product, combinations
from math import comb
import numpy as np


def frequencies(qs, r):
    out = []
    for a in product(*(range(q) for q in qs)):
        if sum(x != 0 for x in a) <= r:
            out.append(a)
    return out


def predict(qs, r):
    n=len(qs)
    D=len(frequencies(qs,r))
    values=[]
    rank=0
    for s in range(r+1):
        for T in combinations(range(n), s):
            mult=int(np.prod([qs[j]-2 for j in T]))
            if not mult:
                continue
            # Direct Poisson-binomial distribution, independent of the Gram construction.
            probs=np.array([1.0])
            for j in range(n):
                if j not in T:
                    eps=1.0/qs[j]
                    probs=np.convolve(probs, [1-eps,eps])
            beta=sum(probs[:r-s+1])
            values.extend([1-beta]*mult)
            rank+=mult
    values.extend([1.0]*(D-rank))
    return np.array(sorted(values))


def test(qs, r, marks):
    xs=list(product(*(range(q) for q in qs)))
    basis=frequencies(qs,r)
    keep=[x for x in xs if any(x[j]==marks[j] for j in range(len(qs)))]
    phases=np.array([[sum(a[j]*x[j]/qs[j] for j in range(len(qs))) for a in basis]
                     for x in keep], dtype=np.float64)
    F=np.exp(2j*np.pi*phases)/np.sqrt(len(xs))
    eig=np.sort(np.linalg.eigvalsh(F.conj().T@F))
    model=predict(qs,r)
    error=max(abs(eig-model))
    assert error<2e-12, (qs,r,error)
    direct_kappa=np.sqrt(max(eig)/min(eig))
    prob=np.array([1.0])
    for q in qs:
        prob=np.convolve(prob, [1-1/q, 1/q])
    exact_kappa=1/np.sqrt(sum(prob[r+1:]))
    assert abs(direct_kappa/exact_kappa-1)<2e-11, (qs,r,direct_kappa,exact_kappa)
    return (len(xs),len(keep),len(basis),error,exact_kappa)


def main():
    cases=[((2,2),1,(0,1)), ((2,3),1,(0,2)),
           ((3,4),1,(2,1)), ((2,3,4),1,(1,0,3)),
           ((2,3,4),2,(1,0,3)), ((3,4,5),1,(1,3,2)),
           ((3,4,5),2,(1,3,2)), ((2,2,3,3),2,(1,0,2,1)),
           ((2,3,4,5),2,(0,1,2,3)), ((2,3,4,5),3,(0,1,2,3)),
           ((2,2,2,3,3),2,(1,0,1,2,1)),
           ((2,2,2,3,3),3,(1,0,1,2,1))]
    max_error=0.0
    for qs,r,marks in cases:
        N,rows,cols,error,kappa=test(qs,r,marks)
        max_error=max(max_error,error)
        print('case',qs,'degree',r,'ambient',N,'sample_rows',rows,
              'columns',cols,'max_abs_eig_error',f'{error:.3g}',
              'condition',f'{kappa:.10g}')
    print('HETEROGENEOUS_PUNCTURE_SPECTRUM_PASS cases=%d max_error=%.3g'%
          (len(cases),max_error))

if __name__=='__main__':
    main()
