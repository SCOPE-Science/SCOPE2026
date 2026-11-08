#!/usr/bin/env python3
"""Independent numerical consistency tests for a reset-age saddle and stationary Gaussian mixture."""
import math

def F(u):
    if u < 0.015:
        # F(u) = integral_0^u (1-exp(-v))^2 dv (series)
        # Direct high-precision via Simpson keeps cancellation controlled at small u.
        n = 48
        h = u/n
        return h/3*sum((1 if j in (0,n) else (4 if j%2 else 2))*(-math.expm1(-j*h))**2 for j in range(n+1))
    q = math.exp(-u)
    return u-1.5+2*q-0.5*q*q

def fprime(u):
    return (-math.expm1(-u))**2

def z_at(u):
    return 2*F(u)/(-math.expm1(-u))

def saddle(z):
    a,b=0.0,max(1.0,z+3.0)
    while z_at(b)<z:
        b*=2
    for _ in range(95):
        m=(a+b)*0.5
        if z_at(m)<z: a=m
        else: b=m
    return (a+b)/2

def J(z):
    u=saddle(z)
    return u+z*z/(4*F(u))

def logsumexp(vals):
    m=max(vals)
    return m+math.log(sum(math.exp(v-m) for v in vals))

def stationary_logdensity(R,z,v0=0.0):
    # Midpoint quadrature in reset age u, independent from minimizer solver.
    # Fixed deterministic unit heading is a valid special case of bounded propulsion.
    steps=12000
    stop=max(10.0, 5.0+saddle(z))
    dx=stop/steps
    logs=[]
    for j in range(steps):
        u=(j+0.5)*dx
        f=F(u)
        if f<=0:continue
        mean=v0*(u-1+math.exp(-u))  # D=tau=1
        x=math.sqrt(R)*z
        logs.append(math.log(R/(4*math.pi))-math.log(f)-R*u-(x-mean)**2/(4*f))
    return logsumexp(logs)+math.log(dx)

def E_F(R):
    return 1/R-1.5+2*R/(R+1)-R/(2*(R+2))

def test():
    count=0
    for u in (0.001,0.02,0.15,0.5,1,2,8):
        # Independent composite midpoint quadrature of kernel.
        n=8000
        integ=u/n*sum((-math.expm1(-(j+0.5)*u/n))**2 for j in range(n))
        assert abs(F(u)-integ)<2e-8*max(1,F(u)),(u,F(u),integ)
        eps=1e-5*max(1,u)
        assert abs((F(u+eps)-F(max(0,u-eps)))/(2*eps)-fprime(u))<3e-5
        count+=2
    zz=(.008,.025,.1,.25,.5,1,2,4,10,20)
    prevgap=0
    for z in zz:
        u=saddle(z)
        y=1-math.exp(-u)
        assert abs(z_at(u)-z)<1e-10*max(1,z)
        value=J(z)
        assert 0<value-z<1.5
        assert value-z>prevgap
        prevgap=value-z
        e=1e-5*z
        deriv=(J(z+e)-J(z-e))/(2*e)
        assert abs(deriv-1/y)<2e-7*max(1,1/y),(z,deriv,1/y)
        e=1e-3*z
        assert J(z+e)+J(z-e)-2*J(z)<0
        count+=5
    for z in (.00001,.0001,.001):
        ratio=J(z)/((4/3)*math.sqrt(3*z/2))
        assert abs(ratio-1)<.03
        count+=1
    assert abs((J(30)-30)-1.5)<.001
    count+=1
    for R in (1,5,30,200):
        # Independent integration of exponential-age variance.
        n=120000
        end=max(20/R,0.3)
        h=end/n
        num=h*sum(R*math.exp(-R*(j+.5)*h)*F((j+.5)*h) for j in range(n))
        theo=2/(R*(R+1)*(R+2))
        assert abs(num/theo-1)<.00002,(R,num,theo)
        assert abs(E_F(R)/theo-1)<2e-9
        count+=2
    trials=[]
    for z in (0.5,1.5,3):
        j=J(z)
        for R in (50,200,800):
            for v0 in (0,2):
                est=-stationary_logdensity(R,z,v0)/R
                tolerance=3.1/math.sqrt(R)+.08
                assert abs(est-j)<tolerance,(z,R,v0,est,j,tolerance)
                trials.append((z,R,v0,round(est,6),round(j,6)))
                count+=1
    # Independent stationary mixture ratio for frozen headings (parallel/antiparallel).
    for z in (0.5,1.5,3.0):
        u=saddle(z)
        coefficient=2*(u-1+math.exp(-u))/(1-math.exp(-u))
        errors={-1:[],1:[]}
        for R in (100,400,1600):
            passive=stationary_logdensity(R,z,0)
            for alignment in (-1,1):
                contrast=(stationary_logdensity(R,z,alignment*2)-passive)/math.sqrt(R)
                err=abs(contrast-alignment*coefficient)
                assert err<3.0/math.sqrt(R)+0.03, (z,R,alignment,contrast,coefficient)
                errors[alignment].append(err)
                count+=1
        # Exact stationary mixture convergence improves with increasing rate.
        for alignment in (-1,1):
            err=errors[alignment]
            assert err[0]>err[1]>err[2],(z,alignment,err)
            count+=1
    print("Passed",count,"independent numerical checks")
    print("Sample stationary mixture estimates (z,R,propulsion,estimate,rate):")
    for t in trials:
        if t[1] in (50,800):print(t)
if __name__=="__main__":
    test()
