"""Numerical cross-check of a hyperbolic ideal-polyhedron cusp tube law.

Requires scipy. This is not a substitute for the analytical proof.
"""
from math import sqrt, sin, sinh, log, pi, hypot, exp, tan
from scipy.integrate import quad


def area(poly):
    if len(poly) < 3:
        return 0.0
    return abs(sum(x*y1-x1*y for (x,y),(x1,y1)
                   in zip(poly, poly[1:]+poly[:1])))/2


def erode(poly, t):
    # Independent convex clipping of all supporting halfplanes, moved inward by t.
    result=list(poly)
    for (x0,y0),(x1,y1) in zip(poly,poly[1:]+poly[:1]):
        dx,dy=x1-x0,y1-y0
        length=hypot(dx,dy)
        nx,ny=-dy/length,dx/length
        def f(p):
            return nx*(p[0]-x0)+ny*(p[1]-y0)-t
        old=result
        result=[]
        if not old:
            return []
        for p,q in zip(old[-1:]+old[:-1],old):
            fp,fq=f(p),f(q)
            if (fp>=0)!=(fq>=0):
                u=fp/(fp-fq)
                result.append((p[0]+u*(q[0]-p[0]),p[1]+u*(q[1]-p[1])))
            if fq>=0:
                result.append(q)
    return result


def trial(poly, radius, C, perimeter, label):
    A=area(poly)
    for t in (0.005,0.02,0.05):
        e=area(erode(poly,t))
        expected=A-perimeter*t+C*t*t
        assert abs(e-expected)<1.e-10,(label,t,e,expected)
    for s in (0.05,0.02,0.005,0.001):
        h=sinh(s)
        assert h<radius
        top=log(radius/h)
        def integrand(u):
            z=exp(u)
            return z**(-2)*(A-area(erode(poly,z*h)))
        actual=quad(integrand,0,top,epsabs=8.e-11,epsrel=1.e-10,limit=300)[0]
        actual+=A*h*h/(2*radius*radius)
        expected=perimeter*h*(1-h/radius)-C*h*h*log(radius/h)+A*h*h/(2*radius*radius)
        assert abs(actual-expected)<3.e-9,(label,s,actual,expected)
    print(label, 'cusp_erosion_and_volume_OK')


def lobachevsky(x):
    return -x*log(2*x)+x-quad(lambda y:log(sin(y)/y) if y else 0.0,0,x,epsabs=2.e-12)[0]


def tetra_extremal():
    regularB=12*sqrt(3)
    regularV=3*lobachevsky(pi/3)
    for i in range(1,16):
        for j in range(1,16):
            alpha=pi*i/17
            beta=(pi-alpha)*j/17
            gamma=pi-alpha-beta
            B=4*sum(1/tan(x/2) for x in (alpha,beta,gamma))
            V=sum(lobachevsky(x) for x in (alpha,beta,gamma))
            assert B>=regularB-1e-10
            assert V<=regularV+1e-10
            assert B/V>=regularB/regularV-1e-10
    print('tetrahedron_dihedral_extremal_checks_OK',round(regularV,12),round(regularB/regularV,12))

if __name__=='__main__':
    tri=[(0.0,0.0),(1.0,0.0),(0.5,sqrt(3)/2)]
    square=[(-1.0,-1.0),(1.0,-1.0),(1.0,1.0),(-1.0,1.0)]
    trial(tri,sqrt(3)/6,3*sqrt(3),3.0,'triangular_vertex_figure')
    trial(square,1.0,4.0,8.0,'square_vertex_figure')
    tetra_extremal()
    print('IDEAL_HYPERBOLIC_POLYHEDRON_LOG_TUBE_OK')
