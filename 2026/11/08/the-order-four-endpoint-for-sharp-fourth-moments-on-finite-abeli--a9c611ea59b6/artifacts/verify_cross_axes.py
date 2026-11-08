"""Finite consistency checks for a sharp Fourier inequality on coordinate crosses.
No finite computation is used to certify the universal theorem.
Run with: python artifacts/verify_cross_axes.py
"""
from itertools import product
import cmath
import random


def tests(moduli, axes, samples=60):
    H = list(product(*(range(d) for d in moduli)))
    q = len(H)
    zero = (0,) * len(moduli)
    modes = [(zero,) * axes]
    modes += [tuple(h if j == i else zero for j in range(axes))
              for i in range(axes) for h in H if h != zero]
    points = list(product(H, repeat=axes))
    table = []
    for x in points:
        table.append([cmath.exp(2j * cmath.pi * sum(a*b/d
                    for j in range(axes) for a,b,d in zip(mode[j],x[j],moduli)))
                    for mode in modes])
    rng = random.Random(q*100+axes+len(moduli))
    checks=0
    for s in range(samples):
        coeff = [complex(rng.uniform(-1,1),rng.uniform(-1,1)) for _ in modes]
        if s % 7 == 0:
            coeff=[0j]*len(modes)
            j=(s//7) % axes
            amplitude=complex(.73,-.21)
            freq=H[(s+1)%q]
            for ix,mode in enumerate(modes):
                if all(mode[t] == zero for t in range(axes) if t != j):
                    h=mode[j]
                    coeff[ix]=amplitude * cmath.exp(2j*cmath.pi *sum(a*b/d for a,b,d in zip(h,freq,moduli)))
        energy=sum(abs(z)**2 for z in coeff)
        fourth=sum(abs(sum(a*b for a,b in zip(coeff,row)))**4
                   for row in table)/len(points)
        assert fourth <= q*energy*energy+1e-7*max(1,energy*energy), (moduli,axes,s,fourth,energy)
        if s % 7 == 0:
            assert abs(fourth-q*energy*energy) < 1e-7*max(1,energy*energy)
        checks+=1
    return checks


def main():
    count=0
    for moduli,axes in [((4,),2),((4,),3),((2,2),2),((2,2),3),((5,),2),((5,),3),((6,),2),((7,),2)]:
        count+=tests(moduli, axes)
    # Exact count of fourth moments via additive quadruple relations,
    # avoiding floating point evaluation of roots of unity.
    def fourth_integer(q):
        support=[(0,0)]+[(x,0) for x in range(1,q)]+[(0,x) for x in range(1,q)]
        counts={}
        for x in support:
            for y in support:
                z=((x[0]+y[0])%q,(x[1]+y[1])%q)
                counts[z]=counts.get(z,0)+1
        return sum(v*v for v in counts.values()),len(support)
    assert fourth_integer(2)==(21,3)
    assert fourth_integer(3)==(77,5)
    print(f'CROSS_AXES_CHECK_PASS randomized_and_axis={count} exact_witnesses=2')

if __name__=='__main__':
    main()
