"""Reproducible checks for the four-occasion count-identification theorem.

Only Python standard library is required. Exact fractions prove finite
identities for rational samples; numerical inversion tests are supplementary
and are not substitutes for the analytic global proof.
"""
from fractions import Fraction as F
from math import comb, log, isclose
from random import Random


def counts(n, occupancy, use, detect, memory):
    assert n >= 1
    assert 0 < occupancy < 1 and 0 < use < 1
    assert 0 < detect < 1 and 0 < memory < 1
    q01 = use * (1-memory)
    q11 = use + (1-use)*memory
    states = {(0, 0): (1-use), (1, 0): use}
    for j in range(n):
        nextstates = {}
        for (w, k), mass in states.items():
            if j:
                arrivals = [(0, 1 - (q11 if w else q01)),
                            (1, (q11 if w else q01))]
            else:
                arrivals = [(w, 1)]
            for neww, prob in arrivals:
                likelihood = (detect if neww else 0)
                for y, py in [(0, 1-likelihood), (1, likelihood)]:
                    key = (neww, k+y)
                    nextstates[key] = nextstates.get(key, 0) + mass*prob*py
        states = nextstates
    out = [F(0) if isinstance(use,F) else 0.0 for _ in range(n+1)]
    for (w, k), mass in states.items():
        out[k] += occupancy * mass
    out[0] += 1-occupancy
    return out


def moments(q):
    return [sum(comb(j,k)*q[j] for j in range(k,len(q))) for k in range(1,len(q))]


def polynomial_moments(n, occupancy, use, detect, memory):
    t = memory*(1-use)/use
    z = detect*use
    if n == 3:
        fs = [3, 3+t*(2+memory), (1+t)**2]
    elif n == 4:
        fs = [4,
              6+t*(3+2*memory+memory**2),
              2*(1+t)*(2+t*(1+memory)),
              (1+t)**3]
    else:
        raise ValueError('n must be three or four')
    return [occupancy*z**(i+1)*f for i,f in enumerate(fs)]


def invariants(t, r):
    f2 = 6+t*(3+2*r+r*r)
    f3 = 2*(1+t)*(2+t*(1+r))
    f4 = (1+t)**3
    return 4*f3/f2**2, f2*f4/f3**2


def identify(q):
    assert len(q) == 5
    e1,e2,e3,e4 = moments(q)
    R = e1*e3/e2**2
    U = e2*e4/e3**2
    if not 4/9 < R < 8/9:
        raise ValueError('moment ratio outside positive-memory interior')
    def Rupper(r):
        return 8*(1+r)/(3+2*r+r*r)**2
    a,b=0.0,1.0
    for _ in range(90):
        mid = (a+b)/2
        if Rupper(mid) > R: a=mid
        else: b=mid
    rmax=(a+b)/2
    def t_of_r(r):
        low,high=0.0,1.0
        while invariants(high,r)[0] < R:
            high*=2
        for _ in range(90):
            mid=(low+high)/2
            if invariants(mid,r)[0] < R: low=mid
            else: high=mid
        return (low+high)/2
    # U decreases along the R contour. Use interior roots only.
    low,high=0.0,rmax
    for _ in range(85):
        r=(low+high)/2
        u_here=invariants(t_of_r(r),r)[1]
        if u_here > U: low=r
        else: high=r
    r=(low+high)/2
    t=t_of_r(r)
    f2=6+t*(3+2*r+r*r)
    z=4*e2/(e1*f2)
    use=r/(r+t)
    detect=z/use
    occupancy=e1/(4*z)
    if not (0 < occupancy < 1 and 0 < use < 1 and 0 < detect < 1 and 0 < r < 1):
        raise ValueError('shape has no admissible parameters')
    return occupancy,use,detect,r


def run():
    checks=0
    for n in (3,4):
        for oi in (F(1,5),F(1,2),F(4,5)):
            for ui in (F(1,6),F(2,5),F(5,6)):
                for pi in (F(1,4),F(3,5),F(7,8)):
                    for ri in (F(1,8),F(1,2),F(7,8)):
                        q=counts(n,oi,ui,pi,ri)
                        a=moments(q)
                        b=polynomial_moments(n,oi,ui,pi,ri)
                        assert a==b,(n,oi,ui,pi,ri,a,b)
                        assert sum(q)==1
                        checks+=len(a)+1
    # Exact same three-count law from two different parameter quadruples.
    first=(F(3,5),F(2,5),F(3,4),F(1,2))
    other=(F(48,65),F(13,38),F(57,80),F(3,5))
    assert first != other
    assert counts(3,*first) == counts(3,*other)
    assert counts(4,*first) != counts(4,*other)
    checks+=3
    gen=Random(20240601)
    for j in range(1000):
        params=(gen.uniform(.08,.90),gen.uniform(.12,.88),
                gen.uniform(.15,.9),gen.uniform(.08,.85))
        q=counts(4,*params)
        got=identify(q)
        assert max(abs(x-y) for x,y in zip(params,got)) < 4e-7,(params,got)
        checks+=4
    # Exact rational determinant identity at a grid of interior shape points.
    # Here derivative quotients are rational, so this is a finite exact check.
    for t in (F(1,10),F(1,2),F(1,1),F(5,2)):
        for r in (F(1,10),F(1,3),F(3,4)):
            d=6+t*(3+2*r+r*r)
            g=2+t*(1+r)
            den=(1+t)*g*d
            l1t=(1-r)*(r*r*t+6*r*t+4*r+3*t+6)/den
            l1r=-t*(3*r*r*t+6*r*t+8*r+t+2)/(g*d)
            l2t=(1-r)*(r*r*t-2*r+3*t+6)/den
            l2r=4*t*(r-t-2)/(g*d)
            lhs=l1t*l2r-l1r*l2t
            rhs=-3*t*(1-r)**2/den
            assert lhs==rhs,(t,r,lhs,rhs)
            assert l1t>0 and rhs<0
            checks+=3
    print('PASS:',checks,'exact and numerical supplementary assertions')
    print('Three-occasion ambiguity:',tuple(map(str,first)),'vs',tuple(map(str,other)))
    print('Four-occasion original:',tuple(map(str,first)))
    print('Four-occasion recovered:',identify(counts(4,*first)))

if __name__=='__main__':
    run()
