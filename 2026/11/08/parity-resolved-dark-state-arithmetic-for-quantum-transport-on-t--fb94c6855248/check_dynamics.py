#!/usr/bin/env python3
"""Independent non-Hermitian propagation checks with unequal terminal rates."""
import itertools
import numpy as np
from scipy.linalg import expm
from verify_theta import analytic,build

def run():
    cases=[(2,2,2),(2,4,3),(2,2,3),(2,3,4),(3,3,3),(3,4,5),(4,4,5),
           (4,5,7),(2,4,6),(2,5,5),(5,5,3),(6,4,3),(4,4,4),(3,6,3)]
    count=0
    for lengths in cases:
        H,v=build(lengths)
        d,P=analytic(lengths)
        for gamma in [(0.9,1.5),(2.0,0.6)]:
            eff=H.astype(complex)-0.5j*np.diag([*gamma]+[0]*(len(H)-2))
            mat=expm(-1j*eff*2200)
            actual=np.sum(abs(mat)**2,axis=0)
            want=np.diag(P)
            err=np.max(abs(actual-want))
            assert err<8e-5,(lengths,gamma,err)
            count+=len(H)
    print('PASS unequal-rate non-Hermitian long-time survival for',len(cases)*2,'Hamiltonians,',count,'localized survival comparisons')
if __name__=='__main__':run()
