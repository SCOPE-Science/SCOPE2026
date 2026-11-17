"""Numerical verification by independent Hamiltonian eigenspace SVD."""
import math
import numpy as np
from itertools import combinations
from check_modular import dim_formula,survival_formula

def explicit_projector(n,traps,phi):
    H=np.zeros((n,n),complex)
    for j in range(n):
        k=(j+1)%n
        H[k,j]+=np.exp(1j*phi/n)
        H[j,k]+=np.exp(-1j*phi/n)
    en,ev=np.linalg.eigh(H)
    P=np.zeros((n,n),complex)
    lo=0
    while lo<n:
        hi=lo+1
        while hi<n and abs(en[hi]-en[lo])<1e-8:hi+=1
        v=ev[:,lo:hi]
        A=v[list(traps),:]
        u,s,vh=np.linalg.svd(A,full_matrices=True)
        rank=sum(x>1e-8 for x in s)
        dark=v @ vh.conj().T[:,rank:]
        P+=dark@dark.conj().T
        lo=hi
    return P

cases=0
for n in range(3,13):
    trap_sets={(0,), tuple(range(0,n,2)), tuple(range(0,n,3)), (0,n//2),tuple(range(n)),(0,1)}
    for a in range(n):
        trap_sets.add((0,a)) if a else None
    for traps in trap_sets:
        traps=tuple(sorted(set(traps)))
        for half_flux,phi in ((False,0.),(True,math.pi),(None,0.313987)):
            P=explicit_projector(n,traps,phi)
            expect=0 if half_flux is None else dim_formula(n,traps,half_flux)
            assert abs(np.trace(P).real-expect)<1e-7,(n,traps,phi,np.trace(P),expect)
            assert np.linalg.norm(P@P-P)<1e-7
            for r in range(n):
                pe=0. if half_flux is None else survival_formula(n,traps,half_flux,r)
                assert abs(P[r,r].real-pe)<1e-7,(n,traps,phi,r,P[r,r],pe)
            cases+=1
print(f'PASS: {cases} full-Hamiltonian eigenspace projections, three flux regimes')
