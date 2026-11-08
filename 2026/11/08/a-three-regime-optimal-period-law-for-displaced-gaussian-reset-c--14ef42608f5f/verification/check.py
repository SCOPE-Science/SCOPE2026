"""Independent numerical checks for an OU Gaussian endpoint-divergence trichotomy."""
import math

def objective(q,c,z):
    y=-math.expm1(-z)
    a=-math.expm1(-z/2)
    u=q+(1-q)*y
    return ((u-q)**2/u+c*a*a*(1+q/u))/z

def maximize(q,c):
    # Locate a global maximum on (0, infinity) using grid bracketing,
    # followed by golden-section maximization. This is a finite check only.
    points=[10**(-8+12*j/2400) for j in range(2401)]
    best=max(range(len(points)),key=lambda i:objective(q,c,points[i]))
    assert 0<best<len(points)-1
    lo=points[best-1];hi=points[best+1]
    gr=(math.sqrt(5)-1)/2
    a=hi-gr*(hi-lo);b=lo+gr*(hi-lo)
    for _ in range(120):
        if objective(q,c,a)<objective(q,c,b):lo=a;a=b;b=lo+gr*(hi-lo)
        else:hi=b;b=a;a=hi-gr*(hi-lo)
    z=(lo+hi)/2
    return z,objective(q,c,z)

def zlimit(c):
    # Positive root of z*N'(z)=N(z), c>2.
    def d(z):
        a=math.exp(-z/2)
        n=(1+c)-2*c*a+(c-1)*a*a
        np=c*a-(c-1)*a*a
        return z*np-n
    lo=0.00001;hi=100
    assert d(lo)>0 and d(hi)<0
    for _ in range(90):
        m=(lo+hi)/2
        if d(m)>0:lo=m
        else:hi=m
    return (hi+lo)/2

if __name__=='__main__':
    checks=0
    for q in [.001,.01,.05,.2,.5,.9]:
      for c in [0.,.2,1.,1.99,2.,2.01,3.,10.]:
        z,f=maximize(q,c)
        assert f>objective(q,c,z*.90) and f>objective(q,c,z*1.10)
        # Independently reconstruct Gaussian Jeffreys divergence.
        u=q+(1-q)*(-math.expm1(-z))
        mu=math.sqrt(c)
        delta=mu*(1-math.exp(-z/2))
        direct=(u/q+q/u-2)/2+delta**2*(1/q+1/u)/2
        assert abs(f-direct*2*q/z)<1e-10
        checks+=3
    for c in [0.,1.,1.8,2.]:
      for q in [1e-6,1e-7]:
        z,_=maximize(q,c)
        pred=2*math.sqrt(q/(2-c)) if c<2 else (6*q)**(1/3)
        assert abs(z/pred-1)<.06,(q,c,z,pred)
        checks+=1
    for c in [2.1,3.,6.]:
        z0=zlimit(c)
        z,_=maximize(1e-6,c)
        assert abs(z-z0)<.01,(z,z0)
        checks+=1
    print('PASS:',checks,'checks; illustrative optima:',[(c,round(maximize(1e-5,c)[0],6)) for c in [0,1,2,3]])
