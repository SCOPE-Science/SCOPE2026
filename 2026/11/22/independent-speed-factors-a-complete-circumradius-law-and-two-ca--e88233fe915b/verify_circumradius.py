"""Reproducible numerical diagnostics for ellipse-inscribed triangle circumradii.

Usage: python3 verify_circumradius.py (Python 3.10+, standard library only).
The analytical proof, not finite tests, establishes the exact laws.
"""
import cmath
import math
import random

PI = math.pi


def q(t, a, b):
    return math.hypot(a * math.sin(t), b * math.cos(t))


def radius_from_vertices(t1, t2, t3, a, b):
    v = [(a * math.cos(t), b * math.sin(t)) for t in (t1, t2, t3)]
    def length(i,j):
        return math.hypot(v[j][0]-v[i][0],v[j][1]-v[i][1])
    cross = abs((v[1][0]-v[0][0])*(v[2][1]-v[0][1])
                -(v[1][1]-v[0][1])*(v[2][0]-v[0][0]))
    return length(0,1)*length(1,2)*length(2,0)/(2*cross)


def product_radius(ts,a,b):
    t1,t2,t3=ts
    return q((t1+t2)/2,a,b)*q((t2+t3)/2,a,b)*q((t3+t1)/2,a,b)/(a*b)


def simpson(fun,lo,hi,n=16384):
    assert n%2==0
    h=(hi-lo)/n
    tot=fun(lo)+fun(hi)
    for i in range(1,n):
        tot+=(4 if i%2 else 2)*fun(lo+i*h)
    return tot*h/3


def dilog_unit(z):
    assert 0<=z<1
    total=0.
    power=z
    for j in range(1,10000):
        term=power/(j*j)
        total+=term
        if abs(term)<1e-16:
            break
        power*=z
    return total


def expected_moments(a,b):
    eq=simpson(lambda t:q(t,a,b),0,PI)/PI
    return eq**3/(a*b),((a*a+b*b)/2)**3/(a*a*b*b)


def test():
    rand=random.Random(202611210531)
    tests=0
    for a,b in [(2.,1.),(4.,0.85),(1.4,1.3),(5.,4.)]:
        d=a*a-b*b
        assert d>0
        for _ in range(450):
            ts=[rand.uniform(0,2*PI) for _ in range(3)]
            if min(abs(math.sin((ts[i]-ts[j])/2)) for i,j in [(0,1),(1,2),(2,0)])<0.003:
                continue
            r0=radius_from_vertices(*ts,a,b)
            r1=product_radius(ts,a,b)
            assert math.isclose(r0,r1,rel_tol=3e-10,abs_tol=1e-10)
            assert b*b/a<r0<a*a/b
            tests+=1
        e1,e2=expected_moments(a,b)
        l_mean=3*math.log((a+b)/2)-math.log(a*b)
        logq_mean=simpson(lambda t:math.log(q(t,a,b)),0,PI)/PI
        assert abs(3*logq_mean-math.log(a*b)-l_mean)<2e-11
        logq_var=simpson(lambda t:(math.log(q(t,a,b))-logq_mean)**2,0,PI)/PI
        rho=(a-b)/(a+b)
        exact_var=1.5*dilog_unit(rho*rho)
        assert abs(3*logq_var-exact_var)<2e-11
        # Two exact moment identities from independent speed factors.
        assert abs(simpson(lambda t:q(t,a,b)**2,0,PI)/PI-(a*a+b*b)/2)<1e-11
        # Invert the first two population log-moments.
        low=0.; high=1.-1e-12
        for _ in range(80):
            mid=(low+high)/2
            if 1.5*dilog_unit(mid**2)<exact_var:low=mid
            else:high=mid
        recovered=(low+high)/2
        mm=math.exp(l_mean)*(1-recovered**2)
        assert abs(mm*(1+recovered)-a)<2e-7
        assert abs(mm*(1-recovered)-b)<2e-7
        # The stationary critical values and their quadratic coefficients.
        Rmin=b*b/a; Rmax=a*a/b
        def rc(z):return q(z[0],a,b)*q(z[1],a,b)*q(z[2],a,b)/(a*b)
        dt=1e-4
        crits=[([0.,0.,0.],Rmin,[d/(2*a)]*3),
               ([PI/2,0.,0.],b,[-b*d/(2*a*a),d/(2*b),d/(2*b)]),
               ([PI/2,PI/2,0.],a,[-d/(2*a),-d/(2*a),a*d/(2*b*b)]),
               ([PI/2]*3,Rmax,[-d/(2*b)]*3)]
        for x,level,weights in crits:
            assert abs(rc(x)-level)<1e-12
            for j,w in enumerate(weights):
                xx=x[:];xx[j]+=dt
                yy=x[:];yy[j]-=dt
                coef=(rc(xx)+rc(yy)-2*level)/(2*dt*dt)
                assert math.isclose(coef,w,rel_tol=3e-6,abs_tol=1e-7),(a,b,x,j,coef,w)
                tests+=1
        # Numerical Monte Carlo cross-check of first and second moments.
        vals=[]
        for _ in range(26000):
            ts=[rand.random()*2*PI for _ in range(3)]
            vals.append(product_radius(ts,a,b))
        em=sum(vals)/len(vals)
        em2=sum(v*v for v in vals)/len(vals)
        assert abs(em-e1)<0.018*e1,(a,b,em,e1)
        assert abs(em2-e2)<0.035*e2,(a,b,em2,e2)
        tests+=2
    print('ALL_CHECKS_PASSED',tests)

if __name__=='__main__':
    test()
