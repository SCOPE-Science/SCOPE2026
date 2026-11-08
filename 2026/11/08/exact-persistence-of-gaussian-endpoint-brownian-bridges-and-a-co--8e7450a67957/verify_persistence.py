"""Independent quadrature checks for Gaussian-endpoint bridge persistence."""
import math
from scipy.integrate import quad

PI=math.pi

def J(t):
    if t>=1:
        raise ValueError('t must be strictly below one')
    if abs(t+1)<1e-13:
        return 1.0
    if t>-1:
        return (PI/2+math.asin(t))/math.sqrt(1-t*t)
    return math.acosh(-t)/math.sqrt(t*t-1)

def exact(v,w,c,r):
    delta=v*w-c*c
    if min(v,w,r)<=0 or delta<=0:
        raise ValueError('positive definite C and positive r required')
    rho=c/math.sqrt(v*w)
    t=rho-2*r*delta/math.sqrt(v*w)
    pplus=0.25+math.asin(rho)/(2*PI)
    deficit=math.sqrt(delta)/(2*PI*math.sqrt(v*w))*J(t)
    return pplus-deficit, deficit

def from_integral(v,w,c,r):
    delta=v*w-c*c
    def inner(a):
        return quad(lambda b: -math.expm1(-2*r*a*b)*
           math.exp(-(w*a*a+v*b*b-2*c*a*b)/(2*delta)),
           0,math.inf,epsabs=2e-9,epsrel=2e-9,limit=120)[0]
    return quad(inner,0,math.inf,epsabs=2e-9,epsrel=2e-9,limit=120)[0]/(2*PI*math.sqrt(delta))

def rank_one(a,b,r):
    if a*b<=0: return 0.0
    return .5*(1-(1+4*r*a*b)**-.5)

def rank_one_quadrature(a,b,r):
    if a*b<=0:return 0.0
    return quad(lambda x: -math.expm1(-2*r*a*b*x*x)*math.exp(-x*x/2)/math.sqrt(2*PI),
                0,math.inf,epsabs=1e-11)[0]

def main():
    n=0
    cases=[(1.,1.,0.,1.),(1.,1.,0.,.5),(2.,3.,1.,1.),(2.,3.,-1.,5.),
            (1.,4.,1.8,1.),(1.,4.,-1.8,1.),(1.,1.,0.,10.),(.7,2.,.4,.3)]
    for v,w,c,r in cases:
        ans, deficit=exact(v,w,c,r)
        independent=from_integral(v,w,c,r)
        assert abs(ans-independent)<3e-8,(v,w,c,r,ans,independent)
        assert 0<ans<(0.25+math.asin(c/math.sqrt(v*w))/(2*PI))
        n+=2
    for a,b,r in [(1.,1.,.1),(1.,1.,1.),(3.,.5,2.),(-1.,-3.,3.),(-1.,2.,3.),(0.,2.,1.)]:
        assert abs(rank_one(a,b,r)-rank_one_quadrature(a,b,r))<2e-11
        n+=1
    for v,w,c in [(1.,1.,0.),(2.,3.,1.),(1.,4.,-1.8)]:
        d=v*w-c*c
        for r in (1e8,1e16,1e32):
            _,deficit=exact(v,w,c,r)
            lead=math.log(r)/(4*PI*r*math.sqrt(d))
            assert abs(deficit/lead-1)<0.2,(v,w,c,r,deficit/lead)
            n+=1
    for a,b in [(1.,1.),(.5,3.),(-2.,-1.)]:
        for r in (1e8,1e16):
            deficiency=.5-rank_one(a,b,r)
            leading=1/(4*math.sqrt(r*a*b))
            assert abs(deficiency/leading-1)<2e-4,(a,b,r,deficiency/leading)
            n+=1
    print(f'PASS: {n} independent numerical assertions')

if __name__=='__main__':main()
