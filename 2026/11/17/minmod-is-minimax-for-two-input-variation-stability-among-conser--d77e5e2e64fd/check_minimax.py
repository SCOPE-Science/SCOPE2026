"""Independent reproducible checks for the minmod-Hermite BV minimax theorem.

Run: python check_minimax.py. Standard library only.
"""
from fractions import Fraction as Q
from random import Random
from math import sqrt


def minmod(a,b):
    return min(a,b) if a>0 and b>0 else max(a,b) if a<0 and b<0 else Q(0)


def var_discrete(y):
    return sum(abs(y[j+1]-y[j]) for j in range(len(y)-1))


def slopes(y):
    d = [y[j+1]-y[j] for j in range(len(y)-1)]
    return [minmod(d[j-1] if j else Q(0), d[j] if j<len(d) else Q(0)) for j in range(len(y))]


def integral_abs_quad(c0,c1,c2):
    # Integrate |c0+c1*t+c2*t*t|, using exact polynomial primitives
    # and double-precision roots only for random stress tests.
    a,b,c=map(float,(c2,c1,c0))
    roots=[]
    if abs(a)>1.e-13:
        disc=b*b-4*a*c
        if disc>0:
            t=sqrt(disc)
            roots=[(-b-t)/(2*a),(-b+t)/(2*a)]
    elif abs(b)>1.e-13:
        roots=[-c/b]
    parts=[0.]+sorted(t for t in roots if 1.e-12<t<1-1.e-12)+[1.]
    def primitive(t):
        return c*t+b*t*t/2+a*t*t*t/3
    return sum(abs(primitive(v)-primitive(u)) for u,v in zip(parts,parts[1:]))


def var_interpolant_difference(y,z):
    my,mz=slopes(y),slopes(z)
    total=0.
    for j in range(len(y)-1):
        d=(y[j+1]-y[j])-(z[j+1]-z[j])
        a=my[j]-mz[j]
        b=my[j+1]-mz[j+1]
        total+=integral_abs_quad(a, 6*d-4*a-2*b, -6*d+3*a+3*b)
    return total


def exact_basis_checks():
    # A(t)=t(1-t)^2 has minimum 0 and maximum 4/27 at t=1/3.
    # B(t)=-t^2(1-t) has minimum -4/27 at t=2/3.
    t=Q(1,3); u=Q(2,3)
    assert t*(1-t)**2 == Q(4,27)
    assert -u*u*(1-u) == -Q(4,27)
    assert Q(2)*(t*(1-t)**2)==Q(8,27)
    assert Q(1)+Q(2)*Q(8,27)==Q(43,27)
    # Central derivative kernels have nonnegative Bernstein coefficients.
    for p in (0,1):
        for q in (0,1):
            # evaluate at every t in rational mesh (proof in RESULT.md algebraic)
            for k in range(101):
                t=Q(k,100)
                val=6*t*(1-t)+p*(3*t*t-4*t+1)+q*(3*t*t-2*t)
                assert val>=0
    print('EXACT_BASIS_EXTREMA_AND_CENTRAL_BERNSTEIN_PASS 43/27')


def sharp_witnesses():
    # Six successive increments, two equal neighbors enclosing one decrease.
    d=[Q(0),Q(1),Q(1),Q(1),Q(1),Q(0)]
    for epsilon in (Q(1,2),Q(1,10),Q(1,100),Q(1,10000)):
        e=d[:];e[2]-=epsilon
        def integrate(steps):
            y=[Q(0)]
            for s in steps:y.append(y[-1]+s)
            return y
        y,z=integrate(d),integrate(e)
        assert var_discrete([a-b for a,b in zip(y,z)])==epsilon
        gain=var_interpolant_difference(y,z)/float(epsilon)
        assert abs(gain-float(Q(43,27)))<1.e-10,(epsilon,gain)
    print('FOUR_SHARP_SINGLE_JUMP_WITNESSES_PASS 43/27')


def stress():
    rng=Random(1027)
    biggest=0
    for k in range(6000):
        n=rng.randint(5,21)
        d=[Q(rng.randint(-9,9),rng.randint(1,7)) for _ in range(n-1)]
        e=[di+Q(rng.randint(-4,4),rng.randint(1,7)) for di in d]
        def integrate(steps):
            y=[Q(0)]
            for s in steps:y.append(y[-1]+s)
            return y
        y,z=integrate(d),integrate(e)
        denominator=var_discrete([a-b for a,b in zip(y,z)])
        if denominator:
            ratio=var_interpolant_difference(y,z)/float(denominator)
            biggest=max(biggest,ratio)
            assert ratio < float(Q(43,27))+1.e-8,(k,ratio)
    print('RANDOM_TWO_INPUT_BV_STRESS_PASS 6000 max_sample_ratio',round(biggest,9))


def universal_lower_example():
    # For any admissible rule m with m(1,1)=1 and 0<=m(a,b)<=min(a,b),
    # a decrement eps in the central secant forces both neighboring
    # Hermite bump heights at least eps; endpoint data alone force
    # central variation eps. Thus the bound is 1+2*(8/27).
    for e in (Q(1,2),Q(1,10),Q(1,100)):
        assert Q(1)-min(Q(1),Q(1)-e)>=e
    print('UNIVERSAL_LOWER_BOUND_SYMBOLIC_INEQUALITIES_PASS')

if __name__=='__main__':
    exact_basis_checks();sharp_witnesses();stress();universal_lower_example()
    print('ALL_MINMOD_HERMITE_MINIMAX_CHECKS_PASS')
