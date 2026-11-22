"""Independent finite diagnostics for the three-pulse Nash/Erlang-3 peak theorem.
The argument for all real spacings is in RESULT.md; numerical checks are not that proof.
Run with Python 3 standard library: python CHECKER.py
"""
import math
from fractions import Fraction


def derivative(x):
    return x * (2.0 - x) * math.exp(-x) if x > 0 else 0.0


def hydrograph_derivative(t, gap, events=3):
    return sum(derivative(t - i * gap) for i in range(events))


def scaled_polynomial_coefficients(gap, count):
    # On t >= (count-1)*gap, exp(t)*H'(t) is a quadratic.
    a = b = c = 0.0
    for j in range(count):
        shift = j * gap
        weight = math.exp(shift)
        a -= weight
        b += weight * (2.0 + 2.0 * shift)
        c -= weight * shift * (shift + 2.0)
    return a, b, c


def polynomial_roots(a,b,c):
    discriminant = b*b-4*a*c
    if discriminant <= 0: return []
    root=math.sqrt(discriminant)
    return sorted(((-b-root)/(2*a),(-b+root)/(2*a)))


def observed_peak_count(gap, count=3):
    # Exact polynomial *form* gives all stationary candidates on each region.
    # Only approximate numerical root locations/signs are used for diagnostics.
    bounds=[0.0]+[i*gap for i in range(1,count)]
    all_roots=[]
    for j in range(1,count+1):
        start=bounds[j-1]
        end=bounds[j] if j<count else float('inf')
        for root in polynomial_roots(*scaled_polynomial_coefficients(gap,j)):
            if start+1e-8<root<end-1e-8: all_roots.append(root)
    all_roots.sort()
    eps=max(1e-6,gap*1e-7)
    return sum(hydrograph_derivative(r-eps,gap,count)>0 and
               hydrograph_derivative(r+eps,gap,count)<0 for r in all_roots)


def critical_gap():
    l,r=1.5,1.6
    for _ in range(75):
        m=(l+r)/2
        f=(2-m)+4*(1-m)*math.exp(-m)
        if f>0:l=m
        else:r=m
    return (l+r)/2


def main():
    assertions=0
    # Exact polynomial coefficient identity: raw h'(t)=t(2-t)e^-t.
    for shift in range(0,12):
        for t in range(shift,shift+8):
            lhs=Fraction(t-shift)*Fraction(2-t+shift)
            rhs=-Fraction(t*t)+Fraction(2+2*shift)*t-Fraction(shift*(shift+2))
            assert lhs==rhs
            assertions+=1
    dstar=critical_gap()
    assert 1.53780548<dstar<1.53780550
    assertions+=1
    # Deterministic values avoid the bifurcation itself, where roots coalesce.
    grid=[i*0.007+0.01 for i in range(700)]
    grid += [dstar + offset for offset in (-0.4,-0.2,-0.02,-0.001,0.001,0.02,0.2,0.4)]
    for d in grid:
        expected=1 if d<dstar else (2 if d<=2 else 3)
        observed=observed_peak_count(d)
        assert observed==expected,(d,expected,observed)
        assertions+=1
        if d<2:
            assert observed_peak_count(d,count=2)==1,(d,'two events')
            assertions+=1
    # Critical sign at the second arrival; formula is exact after cancellation.
    for i in range(1,1000):
        d=0.004*i
        f=2-d+4*(1-d)*math.exp(-d)
        q=hydrograph_derivative(2*d,d,events=2)
        assert (f>0)==(q>0) if abs(f)>1e-10 else True
        assertions+=1
    M=2*(1+math.sqrt(2))*math.exp(-2-math.sqrt(2))
    assert 2*M < math.exp(-1)
    assertions+=1
    for i in range(1,200):
        d=1.0+0.012*i
        assert hydrograph_derivative(2*d+1,d,events=3)>0
        assertions+=1
    print(f'PASS: {assertions} assertions; critical gap = {dstar:.12f}; '
          f'peak counts: 1 at d=1, 2 at d=1.8, 3 at d=2.2')

if __name__=='__main__':main()
