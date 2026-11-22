"""Independent numerical diagnostics for the rotated Lamé-region overlap theorem.

The proof in RESULT.md is analytic; numerical tests do not certify the
continuous assertions. Requires only Python's standard library.
"""
import math

PI = math.pi


def radial_squared(p, t):
    return (abs(math.cos(t))**p + abs(math.sin(t))**p)**(-2.0/p)


def interval_midpoint(p, a, b, count=16384):
    if b == a:
        return 0.0
    step = (b-a) / count
    return step * sum(radial_squared(p, a+(j + .5)*step)
                      for j in range(count))

def primitive_midpoint(p, x, count=16384):
    return interval_midpoint(p, 0.0, x, count)


def area_closed(p):
    return 4*math.gamma(1+1/p)**2/math.gamma(1+2/p)


def overlap_formula(p, delta):
    d = abs((delta+PI/4) % (PI/2) - PI/4)
    return (area_closed(p) - 4*(primitive_midpoint(p, d/2)
        - interval_midpoint(p, PI/4-d/2, PI/4)))


def overlap_direct(p, delta, count=65536):
    step=2*PI/count
    return step*0.5*sum(min(radial_squared(p,(j+.5)*step),
                            radial_squared(p,(j+.5)*step-delta))
                         for j in range(count))


def astroid_F(t):
    u = math.tan(t)**(1/3)
    return 3/8*(math.atan(u) + (u**3-u)/(1+u*u)**2)


def astroid_formula(delta):
    d = abs((delta+PI/4) % (PI/2)-PI/4)
    return 3*PI/4-4*(astroid_F(d/2)+astroid_F(PI/4-d/2))


def small_angle(p, delta):
    slope=2*(1-2**(1-2/p))
    correction=2**(2-p)/(p*(p+1))
    return area_closed(p)-slope*delta+correction*delta**(p+1)


def main():
    checks=0
    for p in (.5, 2/3, 1.0, 1.3, 1.8):
        for d in (0., .002, .07, .15, .32, .55, PI/4):
            predicted=overlap_formula(p,d)
            direct=overlap_direct(p,d)
            assert abs(predicted-direct)<0.00007,(p,d,predicted,direct)
            checks+=1
            assert abs(overlap_formula(p,d+PI/2)-predicted)<1e-11
            checks+=1
            assert abs(overlap_formula(p,-d)-predicted)<1e-11
            checks+=1
        ds=[j*PI/80 for j in range(21)]
        vals=[overlap_formula(p,d) for d in ds]
        assert all(vals[j]>vals[j+1] for j in range(len(ds)-1))
        checks+=1
        assert abs(vals[0]-area_closed(p))<1e-10
        checks+=1
        for d in ((.0001, .0003) if p <= 1.5 else ()):
            slope=2*(1-2**(1-2/p))
            coef=2**(2-p)/(p*(p+1))
            residual=(overlap_formula(p,d)-area_closed(p)+slope*d)/(coef*d**(p+1))
            assert abs(residual-1)<.065, (p,d,residual)
            checks+=1
    for k in range(1,20):
        d=k*PI/80
        assert abs(astroid_F(d)-primitive_midpoint(2/3,d))<2e-8
        checks+=1
        assert abs(astroid_formula(d)-overlap_formula(2/3,d))<2e-8
        checks+=1
    minimal=astroid_formula(PI/4)
    assert abs(minimal-0.8450642364070553)<1e-12
    checks+=1
    assert abs(astroid_formula(0)-3*PI/8)<1e-14
    checks+=1
    print('PASS',checks,'diagnostics')
    print('astroid right-angle-period overlap minimum',format(minimal,'.15f'))
    print('astroid small-angle correction',format(36/(5*2**(5/3)),'.15f'))


if __name__=='__main__':
    main()
