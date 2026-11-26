"""Finite-dimensional diagnostics for quantum-shift return laws.
The all-chain statements are proved analytically, not by these tests.
"""
from math import sqrt
import numpy as np

def forbidden_dim(psi, n):
    if n == 1:
        return 2
    bra = np.conjugate(np.array(psi, dtype=complex).reshape(1,4))
    blocks = []
    for j in range(n-1):
        left = np.eye(2**j)
        right = np.eye(2**(n-j-2))
        blocks.append(np.kron(np.kron(left, bra),right))
    arr = np.concatenate(blocks,axis=0)
    return int(2**n-np.linalg.matrix_rank(arr,tol=1e-9))

def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

if __name__ == '__main__':
    psi_list = {
        'same-product': ([1,0,0,0],True),
        'separate-product': ([0,1,0,0],False),
        'singlet': ([0,1/sqrt(2),-1/sqrt(2),0],False),
        'bell': ([1/sqrt(2),0,0,1/sqrt(2)],False),
        'near-same-entangled': ([1/sqrt(1+1e-4),0,0,0.01/sqrt(1+1e-4)],False),
    }
    checks=0
    for name,(psi,exception) in psi_list.items():
        for n in range(1,8):
            observed=forbidden_dim(psi,n)
            predicted=fib(n+2) if exception else n+1
            assert observed==predicted,(name,n,observed,predicted)
            checks+=1
        for m in range(0,6):
            g1=forbidden_dim(psi,m+1)
            g2=forbidden_dim(psi,m+2)
            num=2*g1-g2
            predicted=fib(m+1) if exception else m+1
            assert num==predicted,(name,m,num,predicted)
            checks+=1
    # The return laws sum to one and have the stated first two moments.
    for exception in (False,True):
        weights=[]
        for k in range(1,350):
            if exception:
                a=(fib(k) if k>=1 else 0)/2**(k-1)
                b=fib(k+1)/2**k
            else:
                a=k/2**(k-1)
                b=(k+1)/2**k
            weights.append(a-b)
        assert abs(sum(weights)-1)<1e-11
        mean=sum((k+1)*p for k,p in enumerate(weights))
        variance=sum(((k+1)-mean)**2*p for k,p in enumerate(weights))
        assert abs(mean-4)<1e-10
        assert abs(variance-(20 if exception else 4))<1e-8,(exception,variance)
        checks+=3
    print(f'QUANTUM_KAC_FINITARY_CHECK_OK {checks}')
