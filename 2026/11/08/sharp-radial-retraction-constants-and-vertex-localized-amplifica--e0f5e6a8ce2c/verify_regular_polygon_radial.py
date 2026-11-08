"""Independent finite-geometry checks for the regular-polygon radial theorem.

Uses polygon support functions directly, not the displayed closed-form conclusion.
The universal assertion is proved analytically in RESULT.md.
"""
from math import cos, sin, pi, hypot, isclose


def vertices(n):
    return [(cos(2*pi*j/n), sin(2*pi*j/n)) for j in range(n)]


def norm(n, x):
    alpha=pi/n
    return max((x[0]*cos((2*j+1)*alpha)+x[1]*sin((2*j+1)*alpha))/cos(alpha) for j in range(n))


def det(a,b):
    return a[0]*b[1]-a[1]*b[0]


def local_operator_norm(n,t):
    v=vertices(n)
    u=((1-t)*v[0][0]+t*v[1][0],(1-t)*v[0][1]+t*v[1][1])
    edge=(v[1][0]-v[0][0],v[1][1]-v[0][1])
    denom=abs(det(v[0],edge))
    # The induced rank-one norm is attained on a vertex of the unit polygon.
    return norm(n,edge)*max(abs(det(u,h)) for h in v)/denom

checks=0
for n in range(4,122,2):
    vals=[local_operator_norm(n,t) for t in (0,0.13,0.33,0.5,0.67,0.87,1)]
    predicted=1/(cos(pi/n)**2) if n%4==0 else 1
    assert isclose(max(vals),predicted,rel_tol=1e-11,abs_tol=1e-11),(n,vals,predicted)
    assert isclose(vals[0],predicted,rel_tol=1e-11,abs_tol=1e-11)
    assert isclose(vals[-1],predicted,rel_tol=1e-11,abs_tol=1e-11)
    if n%4==0:
        assert max(vals[1:-1]) < predicted-1e-9,(n,vals)
    checks+=7
print('DIRECT_SIGNED_FACET_OPERATOR_VERTEX_CHECKS_PASSED',checks)

# Independent difference quotients: approach a vertex from the exterior of
# a facet, with the input direction where the operator norm is maximal.
for n in range(4,62,4):
    v=vertices(n)
    delta=pi/n
    vertex=v[0]
    # u is on first facet, at distance epsilon from its endpoint.
    eps=1e-6
    u=((1-eps)*v[0][0]+eps*v[1][0],(1-eps)*v[0][1]+eps*v[1][1])
    x=(1+eps)*u[0],(1+eps)*u[1]
    h=(0,1)
    hstep=eps**2
    y=(x[0]+hstep*h[0],x[1]+hstep*h[1])
    def retract(z):
        r=max(1,norm(n,z))
        return (z[0]/r,z[1]/r)
    ax=retract(x); ay=retract(y)
    quotient=norm(n,(ay[0]-ax[0],ay[1]-ax[1]))/norm(n,(y[0]-x[0],y[1]-x[1]))
    target=1/(cos(pi/n)**2)
    assert abs(quotient-target)<3e-4,(n,quotient,target)
print('SHARP_EXTERIOR_DIFFERENCE_QUOTIENTS_PASSED',len(range(4,62,4)))
print('SQUARE_HEXAGON_OCTAGON_DODECAGON_VALUES',[(n,round(local_operator_norm(n,0),12)) for n in (4,6,8,10,12)])
print('ALL_REGULAR_POLYGON_RADIAL_DIAGNOSTICS_PASSED')
