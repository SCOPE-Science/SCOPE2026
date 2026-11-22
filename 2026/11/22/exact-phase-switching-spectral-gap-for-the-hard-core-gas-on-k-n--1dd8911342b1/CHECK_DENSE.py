"""Independent full-state reversible-spectrum checks for the hard-core biclique.

Requirements: Python 3, numpy, scipy. This finite test is not an infinite proof.
"""
import math
import numpy as np
from scipy.optimize import brentq


def dense_gap(n, lam):
    # Integer labels: zero is empty; 2*subset+side for nonempty configurations.
    states = [0]+[2*s+side for s in range(1,2**n) for side in (0,1)]
    index={s:i for i,s in enumerate(states)}
    Q=np.zeros((len(states),len(states)),dtype=float)
    for i,s in enumerate(states):
        if s==0:
            for side in (0,1):
                for v in range(n):
                    Q[i,index[2*(1<<v)+side]]+=lam
        else:
            subset,side=s//2,s%2
            for v in range(n):
                if subset&(1<<v):
                    newset,rate=subset^(1<<v),1.0
                else:
                    newset,rate=subset|(1<<v),lam
                newlabel=0 if newset==0 else 2*newset+side
                Q[i,index[newlabel]]+=rate
        Q[i,i]=-sum(Q[i,:])
    weights=np.array([1 if s==0 else lam**((s//2).bit_count()) for s in states])
    sym=np.sqrt(weights)[:,None]*Q/np.sqrt(weights)[None,:]
    assert np.max(np.abs(sym-sym.T))<1e-10
    eigs=np.linalg.eigvalsh(-sym)
    assert abs(eigs[0])<1e-9
    return float(eigs[1])


def scalar_gap(n,lam):
    b=1+lam
    def f(a):
        return 1/a-sum(math.comb(n,j)*lam**j/(j*b-a) for j in range(1,n+1))
    return brentq(f,1e-14,b*(1-1e-13),xtol=1e-14)


def main():
    cases=0
    for lam in (0.25,1.0,3.0):
        previous=math.inf
        for n in range(1,8):
            got=dense_gap(n,lam)
            expected=scalar_gap(n,lam)
            assert abs(got-expected)<1e-8,(n,lam,got,expected)
            assert got<previous-1e-10,(n,lam,got,previous)
            previous=got
            cases+=1
    assert abs(scalar_gap(1,2.0)-1)<1e-12
    assert abs(scalar_gap(2,1.0)-(2-2**0.5))<1e-12
    print('FULL_STATE_GAP_AND_SIZE_DESCENT_PASSED',cases)

if __name__=='__main__':
    main()
