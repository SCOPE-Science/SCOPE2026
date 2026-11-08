"""Independent numerical diagnostics for a Poisson mixture induced by a shared Brownian reset age."""
import math
from scipy.integrate import quad
from scipy.special import erfc, gamma, gammaln

checks = 0

def near(a, b, rel=2e-10, absolute=2e-12):
    global checks
    assert abs(a-b) <= absolute + rel*max(abs(a),abs(b)), (a,b)
    checks += 1


def density_crossing(D, t):
    return quad(lambda x: 0.5*erfc(x/math.sqrt(4*D*t)), 0, math.inf,
                epsabs=1e-12)[0]


def pgf_integral(lam,z):
    return quad(lambda y: 2*y*math.exp(-y*y+lam*y*(z-1)),0,math.inf,
                epsabs=1e-12)[0]


def pgf_closed(lam,z):
    b=lam*(z-1)
    return 1+b*math.sqrt(math.pi)/2*math.exp(b*b/4)*erfc(-b/2)


def exact_logpmf(lam,q):
    a=math.sqrt(q/2)
    scale=(q+1)*math.log(a)-a*a-lam*a
    def f(v):
        y=a+v
        return math.exp((q+1)*math.log(y)-y*y-lam*y-scale) if y>0 else 0
    vmin=-min(a,20)
    val=quad(f,vmin,20,epsabs=1e-12,epsrel=1e-11,limit=200)[0]
    return math.log(2)+q*math.log(lam)-gammaln(q+1)+scale+math.log(val)


def asymptotic_logpmf(lam,q):
    return -math.log(2)/2+(q/2)*math.log(math.e*lam*lam/(2*q))-lam*math.sqrt(q/2)+lam*lam/8

for D in [.2,1.0,3.5]:
    for t in [.15,1,5]:
        near(density_crossing(D,t),math.sqrt(D*t/math.pi))

for lam in [.4,1,2.5,4]:
    for z in [0,.15,.4,.8,.95,1.0]:
        near(pgf_integral(lam,z),pgf_closed(lam,z),rel=3e-9)
    for k in range(5):
        moment=quad(lambda y: 2*y*math.exp(-y*y)*(lam*y)**k,0,math.inf)[0]
        near(moment,lam**k*gamma(1+k/2))
    mean=lam*math.sqrt(math.pi)/2
    variance=mean+lam*lam*(1-math.pi/4)
    near(variance,mean+lam*lam-mean*mean)
    k3=lam**3*math.sqrt(math.pi)*(math.pi-3)/4
    computed=lam**3*gamma(2.5)-3*mean*lam**2+2*mean**3
    near(k3,computed)

# Finite-time mean equality with independently resetting particles.
for D,rho,r,t in [(1,2,3,.3),(.3,.7,1.8,2),(2,4,.5,3)]:
    c=rho*math.sqrt(D/math.pi)
    avg=c*(math.exp(-r*t)*math.sqrt(t) + quad(lambda u:r*math.exp(-r*u)*math.sqrt(u),0,t)[0])
    near(avg,rho*math.sqrt(D/r)*math.erf(math.sqrt(r*t))/2)
    # Endpoint atom controls the finite-time high-count law.
    a=c*math.sqrt(t)
    ratios=[]
    for q in [30,100,400]:
        integ=quad(lambda v:v**(q+1)*math.exp(r*t*(1-v*v)+a*(1-v)),0,1,
                   epsabs=1e-12)[0]
        correction=2*r*t*integ
        original=quad(lambda u: r*math.exp(r*(t-u)+a*(1-math.sqrt(u/t)))*(math.sqrt(u/t))**q,
                      0,t,epsabs=1e-12)[0]
        near(correction,original)
        ratios.append(correction/(2*r*t/q))
    assert abs(ratios[2]-1)<abs(ratios[0]-1)
    checks+=1

for lam in [.5,1.5,3]:
    errs=[]
    for q in [80,320,1280]:
        exact=exact_logpmf(lam,q)
        approx=asymptotic_logpmf(lam,q)
        errs.append(abs(exact-approx))
    assert errs[-1]<errs[0] and errs[-1]<.13, (lam,errs)
    checks+=1
    q=1280
    exact=exact_logpmf(lam,q)
    assert abs(-exact/(q*math.log(q))-.5)<.23
    checks+=1

print(f"PASS {checks} analytical-identity and numerical diagnostics")
