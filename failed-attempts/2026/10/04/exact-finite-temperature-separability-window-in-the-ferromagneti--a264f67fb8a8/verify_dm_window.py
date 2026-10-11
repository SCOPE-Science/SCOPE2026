#!/usr/bin/env python3
import math

def pars(Jz,Jy,Jx):
    assert Jz<Jy<Jx<0
    a=(Jx-Jy)/2.0
    g=-(Jx+Jy)/2.0
    z=-Jz
    assert a>0 and g>0 and z+a>g
    return a,g,z

def candidates(Jz,Jy,Jx,D,tau):
    a,g,z=pars(Jz,Jy,Jx)
    nu=math.hypot(g,D)
    low=math.exp(z/(2*tau))*math.sinh(a/tau)-math.exp(-z/(2*tau))*math.cosh(nu/tau)
    high=math.exp(-z/(2*tau))*math.sinh(nu/tau)-math.exp(z/(2*tau))*math.cosh(a/tau)
    return low,high

def endpoints(Jz,Jy,Jx,tau):
    a,g,z=pars(Jz,Jy,Jx)
    u=math.exp(z/tau)*math.sinh(a/tau)
    if u<=math.cosh(g/tau):
        dm=0.0
    else:
        num=tau*math.acosh(u)
        dm=math.sqrt(max(0.0,num*num-g*g))
    np=tau*math.asinh(math.exp(z/tau)*math.cosh(a/tau))
    dp=math.sqrt(np*np-g*g)
    dc=math.sqrt((z+a)**2-g*g)
    return dm,dc,dp

def main():
    models=[
        (-3.0,-2.0,-1.0),
        (-4.0,-2.5,-0.5),
        (-2.5,-1.7,-0.8),
        (-5.0,-3.0,-2.0),
    ]
    taus=[0.15,0.25,0.5,0.8,1.2,2.0,4.0]
    cases=0
    sign_checks=0
    for model in models:
        for tau in taus:
            dm,dc,dp=endpoints(*model,tau)
            assert 0<=dm<dc<dp
            for j in range(101):
                D=dm+(dp-dm)*j/100
                lo,hi=candidates(*model,D,tau)
                scale=max(1.0,abs(lo),abs(hi))
                assert max(lo,hi)<=2e-10*scale
                sign_checks+=1
            if dm>1e-9:
                lo,hi=candidates(*model,dm*(1-1e-5),tau)
                assert max(lo,hi)>0
                sign_checks+=1
            lo,hi=candidates(*model,dp*(1+1e-5)+1e-9,tau)
            assert max(lo,hi)>0
            sign_checks+=1
            cases+=1

    model=(-3.0,-2.0,-1.0)
    dc=math.sqrt((3.0+0.5)**2-1.5**2)
    for tau in (0.1,0.07,0.05):
        dm,dc2,dp=endpoints(*model,tau)
        assert abs(dc2-dc)<1e-12
        assert abs(dm-dc)<0.03
        assert abs(dp-dc)<0.03

    print("VERIFY_OK")
    print("parameter_cases =",cases)
    print("concurrence_sign_checks =",sign_checks)
    print("source_benchmark_Dc =",dc)

if __name__=="__main__":
    main()
