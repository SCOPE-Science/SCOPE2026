"""Finite diagnostics for the two-cell tanh map; not a substitute for the degree proof."""
from fractions import Fraction as Q
from math import tanh, cosh, isfinite
from random import Random

A = 17 / 10
B = (-3 / 10, 3 / 10)

def image(z, step, gain):
    x, y = z
    u, v = tanh(gain*x), tanh(gain*y)
    return ((1-step)*x + step*(A*u-v+B[0]),
            (1-step)*y + step*(u+A*v+B[1]))

def jacobian(z, step, gain):
    x, y = z
    d1 = gain/cosh(gain*x)**2
    d2 = gain/cosh(gain*y)**2
    return ((1-step+step*A*d1, -step*d2),
            (step*d1, 1-step+step*A*d2))

def determinant(z, step, gain):
    (a,b),(c,d) = jacobian(z,step,gain)
    return a*d-b*c

def det_formula(z, step, gain):
    x,y=z
    d1=gain/cosh(gain*x)**2
    d2=gain/cosh(gain*y)**2
    q=1-step
    return (q+step*A*d1)*(q+step*A*d2)+step*step*d1*d2

def newton(z, target, step, gain):
    for _ in range(45):
        f=image(z,step,gain)
        r=f[0]-target[0],f[1]-target[1]
        if max(map(abs,r))<1e-13:
            return z
        (a,b),(c,d)=jacobian(z,step,gain)
        det=a*d-b*c
        if abs(det)<1e-12:
            raise AssertionError('singular diagnostic iterate')
        dx=(d*r[0]-b*r[1])/det
        dy=(-c*r[0]+a*r[1])/det
        z=(z[0]-dx,z[1]-dy)
    raise AssertionError('numerical diagnostic did not converge')

def main():
    checks=0
    r=Random(20230927)
    for step,gain in [(0.1,0.5),(0.9,3),(1,1.8),(2.3,0.5),(20/3,0.5),(7.0,0.5),(20,0.2)]:
        for _ in range(91):
            z=(r.uniform(-10,10),r.uniform(-10,10))
            assert abs(determinant(z,step,gain)-det_formula(z,step,gain))<1e-12
            checks+=1
            if step<1 or (step>1 and (step-1)>=step*A*gain):
                assert determinant(z,step,gain)>0
                checks+=1
    # An entirely rational sign certificate at z=(0,6), T=23/10, alpha=1/2.
    # cosh(3) > sum_{k=0}^4 3^(2k)/(2k)! > 10, so d2 < 1/200.
    from math import factorial
    lower=sum(Q(3)**(2*k)/factorial(2*k) for k in range(5))
    assert lower==Q(9005,896) and lower>10
    det_upper=-Q(1703,2000)+Q(104121,20000)/200
    assert det_upper==-Q(3301879,4000000)<0
    assert determinant((0,6),2.3,0.5)<float(det_upper)
    checks+=3
    # This triple-preimage example is illustrative only; the all-parameter
    # existence theorem follows from proper mapping degree, not from sampling.
    step,gain=2.3,0.5
    target=image((0.,6.),step,gain)
    seeds=[(0.,6.),(-2.5,4.5),(2.6,7.5)]
    roots=[newton(seed,target,step,gain) for seed in seeds]
    for k,z in enumerate(roots):
        assert max(abs(u-v) for u,v in zip(image(z,step,gain),target))<1e-11
        assert all(sum((z[i]-roots[j][i])**2 for i in range(2))>1 for j in range(k))
        assert determinant(z,step,gain)*(1 if k else -1)>0
        checks+=3
    # The borderline map has no finite critical point, but its determinant
    # approaches zero along one unsaturated / one saturated coordinate.
    step,gain=20/3,0.5
    values=[determinant((0.,z),step,gain) for z in [4.,6.,8.,10.]]
    assert all(v>0 for v in values) and values[-1]<values[0]/100
    checks+=1
    print('PASS',checks,'finite diagnostics; triple roots',roots)

if __name__=='__main__':
    main()
