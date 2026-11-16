"""Reproducibility tests for weighted prism dimer Fourier spectra.

Exact rational matching enumeration tests the finite moment formulas;
independent numerical Fourier calculations test the spectrum.
Infinite-size claims follow from the proof, not these finite tests.
"""
from fractions import Fraction
from math import asinh, cos, pi, sinh, cosh, tanh


def matchings(n):
    edges = [(i, (i+1) % n) for i in range(n)]
    edges += [(i+n, ((i+1) % n)+n) for i in range(n)]
    edges += [(i, i+n) for i in range(n)]
    neighbors = [[] for _ in range(2*n)]
    for a,b in edges:
        neighbors[a].append(b)
        neighbors[b].append(a)
    def rec(available, rungs):
        if available == 0:
            yield rungs
            return
        least = (available & -available).bit_length()-1
        rem = available & ~(1 << least)
        for other in neighbors[least]:
            if rem & (1 << other):
                new_rungs = rungs | (1 << least) if other == least + n else rungs
                yield from rec(rem & ~(1 << other), new_rungs)
    return list(rec((1 << (2*n))-1, 0))


def path_polys(n, activity):
    arr=[Fraction(1), activity]
    for k in range(2,n+1):
        arr.append(activity*arr[-1]+arr[-2])
    return arr


def eigen_formula(n, activity, j, p):
    if j == 0:
        a = asinh(float(activity)/2)
        v = tanh(a)
        sech2=1/cosh(a)**2
        if n % 2:
            return v*(sech2*cosh(n*a)/sinh(n*a)-n*v/sinh(n*a)**2)
        return v*(sech2*tanh(n*a/2)+(n/2)*v/cosh(n*a/2)**2)
    t=cos(pi*j/n)**2
    return float(p)*4*t/(float(activity)**2+4*t)


def test():
    checks=0
    for n in range(3,15):
        configurations=matchings(n)
        for lam in [Fraction(1,3),Fraction(1,1),Fraction(5,2)]:
            weights=[lam**mask.bit_count() for mask in configurations]
            Z=sum(weights,Fraction(0))
            L0,L1=Fraction(2),lam
            for _ in range(n-1):
                L0,L1=L1,lam*L1+L0
            assert Z == L1 + (2 if n%2==0 else 0);checks+=1
            P=path_polys(n,lam)
            mean=sum((w for w,msk in zip(weights,configurations) if msk&1),Fraction(0))/Z
            assert mean==lam*P[n-1]/Z;checks+=1
            pair=[mean]
            for d in range(1,n):
                numer=sum((w for w,msk in zip(weights,configurations) if msk&1 and msk&(1<<d)),Fraction(0))
                target=lam**2*P[d-1]*P[n-d-1]
                assert numer==target;checks+=1
                pair.append(numer/Z)
            for j in range(n):
                from math import sin
                eig=sum(float(pair[d]-mean**2)*cos(2*pi*j*d/n) for d in range(n))
                target=eigen_formula(n,lam,j,mean)
                assert abs(eig-target)<3e-10,(n,lam,j,eig,target)
                checks+=1
            if n%2==0:
                assert abs(eigen_formula(n,lam,n//2,mean))<1e-24;checks+=1
    return checks

if __name__=='__main__':
    print('PASS:',test(),'checks')
