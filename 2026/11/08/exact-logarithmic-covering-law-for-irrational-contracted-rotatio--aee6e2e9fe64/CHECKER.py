#!/usr/bin/env python3
"""Finite high-precision consistency checks, not a proof for all parameters."""
from decimal import Decimal, localcontext

def main():
    with localcontext() as ctx:
        ctx.prec = 105
        one=Decimal(1); zero=Decimal(0); lam=one/2
        theta=(Decimal(5).sqrt()-one)/2
        s=zero
        for k in range(1,450):
            d=int((k+1)*theta)-int(k*theta)
            s+=d*(lam**k)
        delta=(one-lam)*(one+s)
        c=(one-delta)/lam
        branches=((zero,c,delta),(c,one,delta-one))
        atoms=[(zero,one)]
        for n in range(1,19):
            nxt=[]
            for lo,hi in atoms:
                for a,b,offset in branches:
                    lower=max(lo,a); upper=min(hi,b)
                    if lower<upper:
                        nxt.append((lam*lower+offset,lam*upper+offset))
            atoms=sorted(nxt)
            assert len(atoms)==n+1,(n,len(atoms))
            assert all(hi-lo<=lam**n for lo,hi in atoms)
            gaps=[atoms[i+1][0]-atoms[i][1] for i in range(n)]
            assert min(gaps)>= (one-lam)*(lam**(n-1))-Decimal('1e-80'),(n,min(gaps))
        print('CONTRACTED_ROTATION_STURMIAN_ATOMS_OK n=1..18; last_atoms=19')
if __name__=='__main__':
    main()
