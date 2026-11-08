"""Independent numerical checks of the stated stationary Gaussian-mixture formulas.
All calculations use only the Python standard library. Numerical checks are not proofs.
"""
import math


def cov(t, gamma, dv, method):
    y = math.exp(-gamma * t)
    kappa = dv / gamma**2
    s = dv / gamma
    if method == "zero":
        a = (kappa / gamma) * (2*gamma*t-3+4*y-y*y)
        b = kappa * (1-y)**2
        c = s*(1-y*y)
    else:
        a = 2*kappa*(t-(1-y)/gamma)
        b = kappa*(1-y)
        c = s
    return a, b, c


def simpson(f, a, b, count=6000):
    assert count % 2 == 0
    step = (b-a)/count
    total = f(a)+f(b)
    for i in range(1, count):
        total += (4 if i % 2 else 2)*f(a+i*step)
    return total*step/3


def conditional(x, gamma, dv, rate, method):
    kappa = dv/gamma**2
    beta = math.sqrt(rate/kappa)
    t_center = x/(2*math.sqrt(kappa*rate))
    end = t_center+20*math.sqrt(x)+20/rate+5/gamma
    def weight(t):
        a,b,c = cov(t, gamma, dv, method)
        if a <= 0:
            return 0,0,0
        w = rate*math.exp(-rate*t-x*x/(2*a)+beta*x)/math.sqrt(2*math.pi*a)
        return w,b*x/a,c-b*b/a
    def integrate_moment(fn):
        return simpson(lambda t: (lambda w,m,v: w*fn(t,m,v))(*weight(t)), 0.00001,end)
    total=integrate_moment(lambda t,m,v:1)
    vmean=integrate_moment(lambda t,m,v:m)/total
    vsecond=integrate_moment(lambda t,m,v:m*m+v)/total
    age=integrate_moment(lambda t,m,v:t)/total
    age2=integrate_moment(lambda t,m,v:t*t)/total
    return total,vmean,vsecond-vmean*vmean,age,age2-age*age


def run():
    for gamma,dv,rate in ((1.0,1.0,1.0),(1.6,2.4,0.7)):
        kappa=dv/gamma**2
        s=dv/gamma
        beta=math.sqrt(rate/kappa)
        for t in (0.3,1.0,3.0,5.0):
            a0,b0,c0=cov(t,gamma,dv,'zero')
            am,bm,cm=cov(t,gamma,dv,'maxwell')
            y=math.exp(-gamma*t)
            assert all(v>0 for v in (a0,am,c0,cm,a0*c0-b0*b0,am*cm-bm*bm))
            assert abs((am-a0)-(kappa/gamma)*(1-y)**2)<1e-9
            assert abs((bm-b0)-kappa*y*(1-y))<1e-9
            assert abs((cm-c0)-s*y*y)<1e-9
        for method in ('zero','maxwell'):
            d=(1.5 if method=='zero' else 1.0)/gamma
            for x in (50.0,100.0):
                norm,m,v,age,vage=conditional(x,gamma,dv,rate,method)
                # norm is p_X(x)*exp(beta*x).
                expected=0.5*beta*math.exp(-rate*d)
                assert abs(norm/expected-1)<0.003, (method,x,'tail',norm,expected)
                assert abs(m-math.sqrt(kappa*rate))<0.005, (method,x,'velocity',m)
                assert abs(v-s)<0.005, (method,x,'var velocity',v)
                exact_age=x/(2*math.sqrt(kappa*rate))+d+1/(2*rate)
                assert abs(age-exact_age)<0.05, (method,x,'age',age,exact_age)
                expected_agevar=x/(4*math.sqrt(kappa)*rate**1.5)+1/(2*rate**2)
                assert abs(vage/expected_agevar-1)<0.01, (method,x,'agevar',vage,expected_agevar)
    print('PASS: covariance identities, positive definiteness, two-parameter tail normalization, conditional velocity, age shift and age fluctuation checks.')


if __name__=='__main__':
    run()
