"""Reproducible numerical cross-checks for random endpoint-chord separation geometry.
This script uses only Python's standard library. It does not replace analytic proofs.
"""
from math import pi, sin, cos, sqrt, asin, atanh
from random import Random


def simpson(f, a, b, N=4096):
    assert N % 2 == 0
    h=(b-a)/N
    total=f(a)+f(b)
    for i in range(1,N):
        total+=(4 if i%2 else 2)*f(a+i*h)
    return total*h/3


def line_metric(X,Y):
    def integrand(phi):
        c,s=cos(phi),sin(phi)
        return abs(asin(X[0]*c+X[1]*s)-asin(Y[0]*c+Y[1]*s))
    return simpson(integrand,0,pi)/pi**2


def local_F(X,V):
    def integrand(phi):
        c,s=cos(phi),sin(phi)
        return abs(V[0]*c+V[1]*s)/sqrt(1-(X[0]*c+X[1]*s)**2)
    return simpson(integrand,0,pi)/pi**2


def radial_dilog_series(r, N=20000):
    return (2/pi**2)*sum(r**(2*k+1)/(2*k+1)**2 for k in range(N))


def separation_by_independent_endpoints(X,Y,num=300000,seed=12345):
    random=Random(seed)
    hits=0
    for _ in range(num):
        a,b=2*pi*random.random(),2*pi*random.random()
        ax,ay=cos(a),sin(a)
        ux,uy=cos(b)-ax,sin(b)-ay
        s1=ux*(X[1]-ay)-uy*(X[0]-ax)
        s2=ux*(Y[1]-ay)-uy*(Y[0]-ax)
        hits+=s1*s2<0
    return hits/num


def test():
    for r in (0.20,0.55,0.84):
        observed=line_metric((0,0),(r,0))
        exact=radial_dilog_series(r)
        assert abs(observed-exact)<1.0e-7, ('radial',r,observed,exact)
        fr=local_F((r,0),(1,0))
        ft=local_F((r,0),(0,1))
        expected_fr=2/pi**2*atanh(r)/r
        expected_ft=2/pi**2*asin(r)/r
        assert abs(fr-expected_fr)<2e-7,('radial density',r,fr,expected_fr)
        assert abs(ft-expected_ft)<2e-7,('tangent density',r,ft,expected_ft)
        print('LOCAL',r,'distance=',f'{observed:.11f}','F_radial=',f'{fr:.11f}','F_tangent=',f'{ft:.11f}','ratio=',f'{fr/ft:.11f}')
    r=0.72
    for h in (0.002,0.0002):
        fd=(line_metric((r,0),(r+h,0))/h)
        ft=(line_metric((r,0),(r,h))/h)
        assert abs(fd-2/pi**2*atanh(r)/r)<0.002
        assert abs(ft-2/pi**2*asin(r)/r)<0.002
        print('FINITEDIFF',h,fd,ft)
    for alpha in (pi/5,pi/2,pi):
        X,Y=(1.,0.),(cos(alpha),sin(alpha))
        exact=alpha*(2*pi-alpha)/(2*pi*pi)
        numeric=line_metric(X,Y)
        assert abs(numeric-exact)<8e-7,('boundary',alpha,numeric,exact)
        print('BOUNDARY',alpha,'exact=',exact,'quad=',numeric)
    for X,Y in [((0,0),(0.6,0)), ((1,0),(0,1)), ((0.25,-0.20),(-0.40,0.18))]:
        predicted=line_metric(X,Y)
        actual=separation_by_independent_endpoints(X,Y)
        assert abs(predicted-actual)<0.004,('Monte Carlo',X,Y,predicted,actual)
        print('MONTECARLO',X,Y,'predicted=',f'{predicted:.8f}','observed=',f'{actual:.8f}')
    print('CHORD_CROFTON_FINSLER_METRIC_CHECK_OK')

if __name__=='__main__': test()
