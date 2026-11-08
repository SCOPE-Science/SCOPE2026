#!/usr/bin/env python3
"""Exact rational checks for periodic mean-zero point-mass Sobolev constants.
The independent piecewise-quadratic variational energy is evaluated directly.
Requires Python >=3.9; no third-party packages.
"""
from fractions import Fraction as F
from random import Random

def r(t):
    t = t % 1
    return t*(1-t)

def value(x, atoms):
    n = len(atoms)
    return sum((r(x-a) for a in atoms), F(0))/n

def slope(x, atoms):
    n=len(atoms)
    assert all((x-a)%1 != 0 for a in atoms)
    return sum((1-2*((x-a)%1) for a in atoms), F(0))/n

def periods(atoms):
    n=len(atoms)
    assert atoms[0] == 0 and all(atoms[i]<atoms[i+1] for i in range(n-1))
    return [(atoms[i], atoms[i+1] if i+1<n else F(1)) for i in range(n)]

def optimum(atoms):
    peaks=[]
    for l,u in periods(atoms):
        m=(l+u)/2
        q=slope(m,atoms)
        z=max(l,min(u,m+q/2))
        peaks.extend((value(z,atoms),value(l,atoms),value(u,atoms)))
    return max(peaks)

def direct_energy(x,atoms,S):
    # Solve -g'' = delta_x - (dt + (S/n)sum delta_atom)/(1+S)
    # exactly; the constant of integration is fixed by periodicity.
    n=len(atoms)
    M=1+S
    w=S/n
    breaks=sorted(set([F(0),F(1),x]+atoms))
    parts=[]
    whole=F(0)
    for a,b in zip(breaks[:-1],breaks[1:]):
        m=(a+b)/2
        c=(w*sum(z<m for z in atoms))/M - int(x<m)
        parts.append((a,b,c))
        whole += (b*b-a*a)/(2*M)+c*(b-a)
    shift=-whole
    energy=F(0)
    for a,b,c in parts:
        b0=c+shift
        energy += (b**3-a**3)/(3*M*M) + b0*(b*b-a*a)/M + b0*b0*(b-a)
    return energy

def check(atoms,S):
    n=len(atoms)
    M=1+S
    gaps=[u-l for l,u in periods(atoms)]
    mids=[(l+u)/2 for l,u in periods(atoms)]
    B=optimum(atoms)
    Q=sum((g**3 for g in gaps),F(0))
    W=sum((r(a-b) for a in atoms for b in atoms),F(0))/(n*n)
    original=F(1,12*M*M)+S*B/M-S*S*W/(2*M*M)
    defect=sum((g*(B-value(m,atoms)) for g,m in zip(gaps,mids)),F(0))
    grad=sum((g*slope(m,atoms)**2 for g,m in zip(gaps,mids)),F(0))
    expanded=F(1,12)+S*(1+2*S)*Q/(12*M*M)+S*defect/M+S*S*grad/(4*M*M)
    assert expanded==original,(atoms,S,expanded,original)
    equal=F(1,12)+S*(1+2*S)/(12*M*M*n*n)
    assert original>=equal
    if Q==F(1,n*n):
        assert original==equal
        assert all(v==B for v in [value(m,atoms) for m in mids])
    else:
        assert original>equal
    for x in list(atoms)+mids:
        direct=direct_energy(x,atoms,S)
        via_r=F(1,12*M*M)+S*value(x,atoms)/M-S*S*W/(2*M*M)
        assert direct==via_r,(atoms,S,x,direct,via_r)
    return len(atoms)+len(mids)

def main():
    rng=Random(18491)
    tests=0
    cells=0
    for n in range(2,9):
        for S in (F(1,3),F(2),F(11,5)):
            atoms=[F(j,n) for j in range(n)]
            cells+=check(atoms,S);tests+=1
            for _ in range(20):
                bits=[rng.randint(1,24) for _ in range(n)]
                tot=sum(bits)
                atoms=[F(0)]
                for b in bits[:-1]:
                    atoms.append(atoms[-1]+F(b,tot))
                cells+=check(atoms,S);tests+=1
    print('INDEPENDENT_PERIODIC_VARIATIONAL_RATIONAL_CASES_PASSED',tests)
    print('EXACT_POINT_EVALUATION_ENERGY_IDENTITIES_PASSED',cells)
    print('CUBIC_GAP_DEFICIT_AND_UNIQUE_EQUAL_SPACING_PASSED')

if __name__=='__main__':
    main()
