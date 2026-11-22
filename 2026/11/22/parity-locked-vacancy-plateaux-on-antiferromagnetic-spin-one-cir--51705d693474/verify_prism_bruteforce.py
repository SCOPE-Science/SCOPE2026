"""Exhaustive exact-energy checks for a spin-one ladder, using only Python stdlib."""
from itertools import product
from fractions import Fraction


def brute(n,r,d):
    best=None
    by_count={}
    spins=(-1,0,1)
    for x in product(spins, repeat=2*n):
        occupancy=sum(v*v for v in x)
        leg=sum(x[i]*x[(i+1)%n]+x[n+i]*x[n+(i+1)%n] for i in range(n))
        rung=sum(x[i]*x[n+i] for i in range(n))
        energy=leg+r*rung+d*occupancy
        if best is None or energy<best:
            best=energy
            by_count={occupancy:1}
        elif energy==best:
            by_count[occupancy]=by_count.get(occupancy,0)+1
    return best,by_count


def theorem(n,r,d):
    branches=[(Fraction(0),{0:1})]
    if n%2:
        branches.extend([(2*n*d-(2+r)*n+4,{2*n:2*n}),((2*n-2)*d-(2+r)*n+4+r,{2*n-2:2*n})])
    else:
        branches.append((2*n*d-(2+r)*n,{2*n:2}))
    energy=min(v for v,_ in branches)
    population={}
    for value,counts in branches:
        if value==energy: population.update(counts)
    return energy,population

if __name__=='__main__':
    cases=0
    for n in (3,4,5,6):
        for r in (Fraction(1,3),Fraction(1),Fraction(5,2)):
            a=r/2 if n%2 else 1+r/2
            b=r/2+Fraction(n-2,n-1) if n%2 else a
            probe=sorted(set([a-Fraction(1,4),a,a+Fraction(1,4),b,b+Fraction(1,4)]))
            for d in probe:
                got=brute(n,r,d)
                want=theorem(n,r,d)
                assert got==want,(n,r,d,got,want)
                cases+=1
    print(f'PASS brute-force all spin assignments for {cases} parameters on n=3,4,5,6')
