"""Independent arithmetic and deterministic quadrature checks for a shear-ordering theorem.

The continuum theorem follows from a sign-symmetry/Jensen proof in RESULT.md;
finite checks here are illustrative and test the exact moments, not a proof.
"""
from fractions import Fraction as F
from itertools import product
from math import sqrt


def uniform_integral_poly(poly):
    """Integrate polynomial in two independent Uniform[-1,1] variables."""
    return sum(coef / F((i+1)*(j+1)) for (i,j),coef in poly.items() if i % 2 == 0 and j % 2 == 0)


def multiply(p,q):
    out = {}
    for (i,j),v in p.items():
        for (k,l),w in q.items():
            key=(i+k,j+l)
            out[key]=out.get(key,F(0))+v*w
    return out


def direct_moments(a,b,c,kind):
    """Directly integrate every ordered edge/face pair, no sampling or fitted formulas."""
    # X = (x(t),y(t)) in generator coordinates; X' = (x'(s),y'(s)).
    # 2D polynomials are indexed by powers of t and s.
    const=lambda x:{(0,0):F(x)}
    tt={(1,0):F(1)}; ss={(0,1):F(1)}
    def sub(p,q):
        r=p.copy()
        for k,v in q.items():r[k]=r.get(k,F(0))-v
        return r
    def add(*xs):
        r={}
        for x in xs:
            for k,v in x.items():r[k]=r.get(k,F(0))+v
        return r
    def scale(p,k):return {z:v*k for z,v in p.items()}
    def rpoly(x,y,X,Y):
        u=sub(x,X);v=sub(y,Y)
        return add(scale(multiply(u,u),a*a),scale(multiply(v,v),b*b),scale(multiply(u,v),2*a*b*c))
    sides=[]
    if kind=='boundary':
        for sig in (-1,1):
            sides.append((tt,const(sig),a/F(2*(a+b))))
            sides.append((const(sig),tt,b/F(2*(a+b))))
    else:
        # Truly independent four-variable expansion for two area-uniform points.
        # Variables t1,t2,s1,s2 are iid Uniform[-1,1].
        def mul4(p,q):
            out={}
            for e,v in p.items():
                for f,w in q.items():
                    k=tuple(x+y for x,y in zip(e,f))
                    out[k]=out.get(k,F(0))+v*w
            return out
        def add4(*ps):
            out={}
            for p in ps:
                for k,v in p.items():out[k]=out.get(k,F(0))+v
            return out
        def int4(p):
            return sum(v/F((e[0]+1)*(e[1]+1)*(e[2]+1)*(e[3]+1)) for e,v in p.items() if all(t%2==0 for t in e))
        v1={(1,0,0,0):F(1),(0,0,1,0):F(-1)}
        v2={(0,1,0,0):F(1),(0,0,0,1):F(-1)}
        zz=add4({e:a*a*v for e,v in mul4(v1,v1).items()},
                {e:b*b*v for e,v in mul4(v2,v2).items()},
                {e:2*a*b*c*v for e,v in mul4(v1,v2).items()})
        return int4(zz),int4(mul4(zz,zz))
    E2=E4=F(0)
    for x,y,wx in sides:
        for xp,yp,wy in sides:
            # X' variables use s rather than t
            xp={(0,j):v for (i,j),v in xp.items() if j==0 for j in [i]}
            yp={(0,j):v for (i,j),v in yp.items() if j==0 for j in [i]}
            z=rpoly(x,y,xp,yp)
            weight=wx*wy
            E2+=weight*uniform_integral_poly(z)
            E4+=weight*uniform_integral_poly(multiply(z,z))
    return E2,E4


def predicted(a,b,c,kind):
    s=a+b
    if kind=='boundary':
        m20=(a/F(3)+b)/s
        m02=(a+b/F(3))/s
        m22=F(1,3)
        e2=F(2,3)*s*s
        # B = 2ab U V, U=X_1-X'_1, V=X_2-X'_2.
        cross=4*a*a*b*b*(2*m22+2*m20*m02)
        # fourth moment when generators are perpendicular
        alpha=m20; beta=m02
        m4=a/s*(b**4+F(2,3)*a*a*b*b+a**4/F(5))+b/s*(a**4+F(2,3)*a*a*b*b+b**4/F(5))
        e4=2*m4+2*(s*s/F(3))**2+4*(alpha*alpha*a**4+beta*beta*b**4)
    else:
        e2=F(2,3)*(a*a+b*b)
        cross=F(16,9)*a*a*b*b
        e4=F(2,5)*(a**4+b**4)+F(4,9)*a*a*b*b+F(2,9)*(a*a+b*b)**2+F(4,9)*(a**4+b**4)
    return e2,e4+c*c*cross,cross


def boundary_quadrature(a,b,c,n=55):
    # Midpoint integration; p noninteger checks are approximate only.
    from math import hypot
    v=(b*c,b*sqrt(1-c*c))
    rows=[]
    for i in range(n):
        t=(2*i+1)/n-1
        for sig in (-1,1):
            rows.append((t*a+sig*v[0],sig*v[1],a/(2*n*(a+b))))
            rows.append((sig*a+t*v[0],t*v[1],b/(2*n*(a+b))))
    res={1.0:0.,2.0:0.,4.0:0.}
    for x,y,w in rows:
        for X,Y,W in rows:
            d=hypot(x-X,y-Y)
            for p in res:res[p]+=w*W*d**p
    return res

if __name__=='__main__':
    n=0
    for a,b,c in [(F(1,2),F(1,2),F(0)),(F(1,2),F(1,2),F(3,5)),(F(1,4),F(3,4),F(5,13)),(F(2,3),F(1,6),F(3,5)),(F(7,11),F(5,13),F(0)),(F(7,11),F(5,13),F(12,13))]:
        for kind in ['boundary','interior']:
            direct=direct_moments(a,b,c,kind)
            e2,e4,k=predicted(a,b,c,kind)
            assert direct==(e2,e4),(a,b,c,kind,direct,(e2,e4))
            assert k>0
            n+=1
    # Numerical independent pair integration confirms strict exponent switch.
    a,b=.75,.25
    vals=[]
    for c in (0.,.5,.9):
        v=boundary_quadrature(a,b,c,45)
        vals.append(v)
        # midpoint quadrature exact on degree <=1; exact p2 except O(n^-2)
        e2=float(predicted(F(3,4),F(1,4),F(str(c)),'boundary')[0])
        assert abs(v[2.0]-e2)<.0004,(v,e2)
    assert vals[0][1.0]>vals[1][1.0]>vals[2][1.0]
    assert vals[0][4.0]<vals[1][4.0]<vals[2][4.0]
    print('SHEAR_CONVEX_ORDER_CHECK_OK exact_pair_moments='+str(n)+' sample_power_tests=3 strong_curvature_coefficients=exact')
