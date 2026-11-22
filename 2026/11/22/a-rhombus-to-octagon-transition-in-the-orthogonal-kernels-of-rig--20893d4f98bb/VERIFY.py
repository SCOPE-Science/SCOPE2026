"""Exact checks for all-face orthogonal kernels of right rectangular pyramids.

Requires only Python 3 standard library. Finite tests complement, not prove,
the all-parameter geometric and algebraic arguments.
"""
from fractions import Fraction as Q
from itertools import product
from random import Random


def dot(u, v):
    return sum(x*y for x,y in zip(u,v))


def sub(u,v):
    return tuple(x-y for x,y in zip(u,v))


def feet_all_faces(a,b,h, B):
    """Direct Euclidean projections on all nontrivial face affine hulls."""
    x,y,z = B
    if not (0 < z < h and abs(x) < a*(1-z/h) and abs(y) < b*(1-z/h)):
        return False
    # Base facet and four base edges.
    if not(abs(x)<a and abs(y)<b):
        return False
    # The four apex-to-corner edges: compute orthogonal segment parameters.
    apex=(Q(0), Q(0), h)
    for vx,vy in product((-a,a),(-b,b)):
        v=(vx,vy,Q(0)); direction=sub(apex,v)
        q=dot(sub(B,v),direction)/dot(direction,direction)
        if not(0 < q < 1):
            return False
    # Every lateral triangular facet: directly project onto its plane and
    # test the actual projected coordinates against triangle inequalities.
    for sign in (-1,1):
        n=(sign*h,Q(0),a); c=a*h
        correction=(dot(n,B)-c)/dot(n,n)
        px,py,pz=tuple(B[i]-correction*n[i] for i in range(3))
        if not(0 < pz < h and abs(py) < b*(1-pz/h)):
            return False
        n=(Q(0),sign*h,b);c=b*h
        correction=(dot(n,B)-c)/dot(n,n)
        px,py,pz=tuple(B[i]-correction*n[i] for i in range(3))
        if not(0 < pz < h and abs(px) < a*(1-pz/h)):
            return False
    return True


def predicted_kernel(a,b,h,B):
    x,y,z=B
    if not (0 < z < h):
        return False
    s=h*h; u=abs(x)/a; v=abs(y)/b; rhs=s*(1-z/h)
    return ((s+b*b)*u+b*b*v < rhs and
            a*a*u+(s+a*a)*v < rhs)


def formula_fraction(a,b,h):
    s=h*h; L=max(a*a,b*b); M=min(a*a,b*b)
    return s*s/(2*L*(s+L)) - s*max(Q(0),s-(L-M))**2/(2*L*(s+M)*(s+L+M))


def clip(poly,c1,c2,rhs):
    out=[]
    def val(p): return c1*p[0]+c2*p[1]-rhs
    for p,q in zip(poly,poly[1:]+poly[:1]):
        vp=val(p); vq=val(q)
        if vp<=0:
            out.append(p)
        if (vp<0<vq or vq<0<vp):
            t=vp/(vp-vq)
            out.append((p[0]+t*(q[0]-p[0]),p[1]+t*(q[1]-p[1])))
        elif vp==0 and vq<0:
            pass
    return out


def polygon_area(poly):
    return abs(sum(x*v-y*u for (x,y),(u,v) in zip(poly,poly[1:]+poly[:1])))/2


def independent_area_fraction(a,b,h):
    s=h*h
    poly=[(Q(0),Q(0)),(Q(1),Q(0)),(Q(1),Q(1)),(Q(0),Q(1))]
    poly=clip(poly,s+b*b,b*b,s)
    poly=clip(poly,a*a,s+a*a,s)
    return polygon_area(poly)


def run():
    cases=[(1,1,1),(1,1,3),(1,1,Q(1,2)),
           (1,2,Q(1,5)),(1,2,2),(1,2,3),
           (2,1,Q(1,5)),(3,1,3),(1,3,1),
           (Q(7,10),Q(14,10),Q(1,5)),
           (Q(3,5),Q(8,5),Q(3,2)),(Q(4,3),Q(5,7),Q(5,3))]
    rng=Random(8675309); comparisons=0
    for a,b,h in cases:
        a,b,h=Q(a),Q(b),Q(h)
        assert formula_fraction(a,b,h)==independent_area_fraction(a,b,h),(a,b,h)
        for _ in range(320):
            B=(a*Q(rng.randrange(-120,121),100),
               b*Q(rng.randrange(-120,121),100),
               h*Q(rng.randrange(-25,126),100))
            actual=feet_all_faces(a,b,h,B)
            predicted=predicted_kernel(a,b,h,B)
            assert actual==predicted,(a,b,h,B,actual,predicted)
            comparisons+=1
    # Exact square-max checks for sample equal-base-product deformations.
    for h in (Q(1,4),Q(1),Q(2),Q(5)):
        center=formula_fraction(Q(1),Q(1),h)
        for t in (Q(2),Q(3),Q(4),Q(5)):
            assert formula_fraction(t,Q(1)/t,h)<center
    print(f'PASS: {len(cases)} exact clipped-area identities; '
          f'{comparisons} exact face-projection checks; 16 square-optimality instances')


if __name__=='__main__':run()
