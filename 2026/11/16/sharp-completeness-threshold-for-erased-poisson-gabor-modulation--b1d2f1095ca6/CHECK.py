"""Numerical consistency checks of the Poisson-window Gabor completeness formulas."""
import cmath
import math

checks = 0

def test(condition, label):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(label)

for lam in (0.5, 1.0, 2.4):
    r = math.exp(-lam)
    for x in (0.07, 0.19, 0.31, 0.43):
        A0 = math.exp(-lam*x)-r*r*math.exp(lam*x)
        B0 = r*(math.exp(lam*x)-math.exp(-lam*x))
        A1 = math.exp(lam*(x-0.5))-r*r*math.exp(-lam*(x-0.5))
        B1 = r*(math.exp(-lam*(x-0.5))-math.exp(lam*(x-0.5)))
        test(min(A0,B0,A1,B1)>0, 'strict positivity')
        test(abs(A0*A1-B0*B1-math.sqrt(r)*(1-r)**2*(1+r)) < 1e-12, 'determinant')
        for angle in (0.11,0.6,1.4,2.3,4.8):
            z=cmath.exp(1j*angle)
            D=(1-r*z)*(1-r/z)
            v0=sum(math.exp(-lam*abs(x+k))*z**k for k in range(-90,91))
            v1=sum(math.exp(-lam*abs(x+k-0.5))*z**k for k in range(-90,91))
            test(abs(v0-(A0+B0/z)/D)<3e-11,'even Zak')
            test(abs(v1-(A1+B1*z)/D)<3e-11,'odd Zak')
            test(abs(v0.conjugate()-(A0+B0*z)/D)<3e-11,'conjugate even Zak')
            test(abs(v1.conjugate()-(A1+B1/z)/D)<3e-11,'conjugate odd Zak')
    coeff={-1:-r,0:1+r*r,1:-r}
    def out(x,m):
        return sum(c*math.exp(-lam*abs(x+k-m/2)) for k,c in coeff.items())
    for x in (0.05,0.15,0.3,0.46):
        for m in range(-18,19):
            if m not in (-1,0,1,2):
                test(abs(out(x,m))<2e-12,'four row null vector')
        test(abs(out(x,2)-2*r*math.sinh(lam*x))<1e-12,'three row surviving leakage')
        test(abs(sum(c*c for c in coeff.values())-(1+4*r*r+r**4))<1e-12,'fiber norm')
    for x in (1e-3,2e-3,3e-3):
        test(abs(out(x,2))<0.03,'near-zero amplitude')
# Exhaustive small Laurent-polynomial support stress test for coprime generic filters.
import itertools
for length in (1, 2, 3, 4):
    for entries in itertools.product((-2,-1,0,1,2),repeat=length):
        if entries[0]==0 or entries[-1]==0:
            continue
        rcoef={j:v for j,v in enumerate(entries) if v}
        outputs_even={j:3*v+rcoef.get(j-1,0) for j,v in rcoef.items()}
        outputs_even.update({j:3*rcoef.get(j,0)+rcoef.get(j-1,0) for j in range(0,length+1)})
        outputs_odd={j:5*rcoef.get(j,0)+2*rcoef.get(j+1,0) for j in range(-1,length)}
        occupied=[2*j for j,v in outputs_even.items() if v] + [2*j+1 for j,v in outputs_odd.items() if v]
        test(len(occupied)>=4 if length==1 else len(occupied)>=5,'extreme-support lemma')
        if length==1:
            test(sorted(occupied)==[-1,0,1,2],'four consecutive support')
print('CHECK_OK assertions='+str(checks))
