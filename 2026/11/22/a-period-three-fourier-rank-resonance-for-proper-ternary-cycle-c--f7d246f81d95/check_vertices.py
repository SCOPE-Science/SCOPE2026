#!/usr/bin/env python3
"""Direct exact Fourier sums on proper vertex colorings (no difference variables)."""
from itertools import product
from math import factorial

def coeff_direct(n, beta):
    # Reconstruct balanced vertex frequencies from beta_i = sum_{j=i}^{n-1} xi_j.
    m=n-1
    xi=[0]*n
    xi[0]=(-beta[0])%3
    for i in range(1,m):xi[i]=(beta[i-1]-beta[i])%3
    xi[m]=beta[m-1]
    assert sum(xi)%3==0
    residues=[0]*3
    for x in product(range(3),repeat=n):
        if any(x[i]==x[(i+1)%n] for i in range(n)): continue
        residues[sum(a*b for a,b in zip(x,xi))%3]+=1
    assert residues[1]==residues[2]
    return residues[0]-residues[1]

def prediction(beta):
    a=beta.count(0);b=beta.count(1);c=beta.count(2)
    return (-1)**len(beta)*(2*(-2)**a-(-2)**b-(-2)**c)

if __name__=='__main__':
    for n in range(3,9):
        zeros=0
        for beta in product(range(3), repeat=n-1):
            observed=coeff_direct(n,beta)
            assert observed==prediction(beta),(n,beta,observed,prediction(beta))
            zeros+=(observed==0)
        print(n,zeros,'balanced modes checked',3**(n-1))
    print('PASS direct vertex-character enumeration')
