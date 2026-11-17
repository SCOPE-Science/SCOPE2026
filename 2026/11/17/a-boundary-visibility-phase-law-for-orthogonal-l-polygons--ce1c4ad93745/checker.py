"""Numerical diagnostics for boundary-to-boundary visibility on orthogonal L regions.

Run: python3 checker.py (Python 3 standard library only).
Finite sampling complements but does not replace the exact integration proof.
"""
import math
import random


def blocked_formula(A, B, C, D):
    assert min(A, B, C, D) > 0
    r = A * D / (B * C)
    if r >= 1:
        integral = (4*A*D + 2*A*C + 2*B*D - B*C*C/(2*D)
                    - B*B*C/(2*A) - B*C*math.log(r))
    else:
        integral = (4*A*D + A*C + B*D + D*A*A/(2*B)
                    + A*D*D/(2*C) + A*D*math.log(1/r))
    return 2*integral / (2*(A+B+C+D))**2


def sample_boundary(A, B, C, D, gen):
    # Six oriented boundary edges, constructed without reference to the formula.
    vertices = [(0.0, 0.0), (A+C, 0.0), (A+C, B),
                (C, B), (C, B+D), (0.0, B+D), (0.0, 0.0)]
    total = 2*(A+B+C+D)
    draw = gen.random()*total
    for i in range(6):
        x0,y0 = vertices[i]; x1,y1 = vertices[i+1]
        length = abs(x1-x0)+abs(y1-y0)
        if draw <= length:
            z = draw/length
            return (x0+z*(x1-x0),y0+z*(y1-y0))
        draw -= length
    raise ArithmeticError('arclength sampler exceeded boundary')


def line_blocked(p, q, B, C):
    # A segment exits the polygon only by passing through the open northeast
    # quadrant of the reflex corner. Test the two exact crossing parameters.
    x,y=p; xx,yy=q
    west = ((x>C and y<=B) and (xx<=C and yy>B))
    east = ((xx>C and yy<=B) and (x<=C and y>B))
    if not (west or east):
        return False
    if east:
        x,y,xx,yy=xx,yy,x,y
    cross_h = (B-y)/(yy-y)
    cross_v = (x-C)/(x-xx)
    return cross_h < cross_v


def simulate(A, B, C, D, samples, gen):
    blocked=0
    for _ in range(samples):
        p=sample_boundary(A,B,C,D,gen)
        q=sample_boundary(A,B,C,D,gen)
        blocked += line_blocked(p,q,B,C)
    return blocked/samples


def square_analytic_extensions(t):
    L=(4*(1-t)-t**3/(1-t)-2*t*t*math.log((1-t)/t))
    R=(2*(1-t)*(2-t)+(1-t)**3/t+2*(1-t)**2*math.log(t/(1-t)))
    return L,R


def main():
    rng=random.Random(20261110)
    configs=[(1.0,1.0,1.0,1.0),(.1,.9,.3,.2),
             (1.,2.,3.,4.),(4.,2.,3.,.1),(.7,.4,.8,.3),(.9,1.1,1.2,1.3)]
    n=130000
    for dims in configs:
        val=blocked_formula(*dims)
        empirical=simulate(*dims,n,rng)
        sd=math.sqrt(val*(1-val)/n)
        print('sample',dims,'theory',round(val,7),'observed',round(empirical,7),
              'standardized_error',round((empirical-val)/sd,3))
        assert abs(empirical-val) < 5*sd + 0.0005
        assert 0 < val < 0.5
    t=.5
    L,R=square_analytic_extensions(t)
    assert abs(L-1.75)<1e-12 and abs(R-1.75)<1e-12
    for h in (.04,.025,.015,.01):
        x,y=square_analytic_extensions(t+h)
        quotient=(y-x)/h**4
        print('cusp scaling',h,quotient,'limit',128/3)
        assert abs(quotient-128/3)<230*h*h + 0.002
    for t in (.01,.1,.25,.49,.5,.51,.75,.9,.99):
        v=1-(square_analytic_extensions(t)[0 if t<=.5 else 1])/8
        assert .5<v<1
    print('BOUNDARY_L_VISIBILITY_CUSP_CHECK_OK')

if __name__=='__main__':
    main()
