#!/usr/bin/env python3
"""Independent numerical cross-checks for the resetting-MIPS transport theorem.

Requires only the Python standard library. Analytical proofs are in RESULT.md;
finite checks are not a substitute for universal arguments.
"""
import math
import random


def gas_density_from_flux(f, m):
    if f == 0:
        return 0.0
    return 2*f/(1+math.sqrt(max(0.0, 1-4*f/m)))


def theta_scale(m, h, mass):
    return 2*h/mass


def phase_quantile(q, m, h, mass, phase):
    assert 0 < q < 1 and m > 4 and 1 < h < m/4
    chi = theta_scale(m, h, mass)
    u0 = gas_density_from_flux(h, m)
    ut = gas_density_from_flux(h*q, m)
    if phase == 'gas':
        return (math.log(u0/ut) - 2*(u0-ut)/m)/chi
    if phase == 'droplet':
        if q >= 1/h:
            return -math.log(q)/(m*chi)
        ub = gas_density_from_flux(1, m)
        return math.log(h)/(m*chi)+(math.log(ub/ut)-2*(ub-ut)/m)/chi
    raise ValueError(phase)


def phase_gap(m,h,mass):
    chi = theta_scale(m,h,mass)
    u0,ub=gas_density_from_flux(h,m),gas_density_from_flux(1,m)
    return (math.log(u0/ub)-2*(u0-ub)/m-math.log(h)/m)/chi


def phase_w1(m,h,mass):
    chi=theta_scale(m,h,mass)
    u0,ub=gas_density_from_flux(h,m),gas_density_from_flux(1,m)
    B=lambda u: u-1.5*u*u/m+(2/3)*u*u*u/(m*m)
    return (B(u0)-B(ub)-(h-1)/m)/(h*chi)


def simpson(f,a,b,n=1000):
    assert n%2==0
    step=(b-a)/n
    s=f(a)+f(b)
    for k in range(1,n):
        s+=(4 if k%2 else 2)*f(a+k*step)
    return s*step/3


def fprime(m,h):
    return 1/gas_density_from_flux(h,m)-1/(m*h)


def fvalue(m,h):
    u,ub=gas_density_from_flux(h,m),gas_density_from_flux(1,m)
    return math.log(u/ub)-2*(u-ub)/m-math.log(h)/m


def deriv_numerator(m,h):
    return h*fprime(m,h)-fvalue(m,h)


def boundary_H(q):
    return (1+q*q)/4+q+math.log1p(-q)-(1-q*q)*math.log1p(-q*q)/4


def bisect(fun,lo,hi,n=80):
    vlo=fun(lo)
    assert vlo*fun(hi)<0
    for _ in range(n):
        mi=(lo+hi)/2
        if fun(mi)*vlo>0:
            lo=mi
        else:
            hi=mi
    return (lo+hi)/2


def independent_inverse_flux(q,m,h,mass,phase):
    # Integrate the flux ODE inverse directly, without the logarithmic antiderivative.
    chi=theta_scale(m,h,mass)
    flux0=h*q
    if phase=='gas':
        return simpson(lambda f:1/gas_density_from_flux(f,m),flux0,h,1600)/chi
    if flux0>=1:
        return simpson(lambda f:1/(m*f),flux0,h,1600)/chi
    return (simpson(lambda f:1/gas_density_from_flux(f,m),flux0,1,1600)
            +simpson(lambda f:1/(m*f),1,h,1600))/chi


def density_from_published_profile(x,m,h,mass,phase):
    """Direct implicit Lambert-profile evaluation, independent of flux quantiles."""
    chi=theta_scale(m,h,mass)
    ub=gas_density_from_flux(1,m)
    b=math.log(h)/(m*chi)
    if phase=='droplet' and x<=b:
        return m*math.exp(-m*chi*(x-b))
    if phase=='gas':
        ui=gas_density_from_flux(h,m)
        y=x
    else:
        ui=ub
        y=x-b
    if y<=0:
        return ui
    target=math.log(ui)-2*ui/m-chi*y
    lo=1e-200
    hi=ui
    for _ in range(55):
        mid=(lo+hi)/2
        lhs=math.log(mid)-2*mid/m
        if lhs>target:
            hi=mid
        else:
            lo=mid
    return (lo+hi)/2


def survival_from_published_profile(x,m,h,mass,phase):
    """Numerically integrate density in x, not the flux-coordinate ODE."""
    chi=theta_scale(m,h,mass)
    b=math.log(h)/(m*chi)
    end=b+32/chi
    if phase=='droplet' and x<=b:
        total=simpson(lambda y:density_from_published_profile(y,m,h,mass,phase),x,b,240)
        total+=simpson(lambda y:gas_density_from_flux(1,m) if y==b else
                       density_from_published_profile(y,m,h,mass,phase),b,end,600)
    else:
        total=simpson(lambda y:density_from_published_profile(y,m,h,mass,phase),x,end,600)
    return 2*total/mass


def run():
    rng=random.Random(261026149)
    checks=0
    # Compare independent flux integration and exact inverse quantiles.
    for _ in range(50):
        m=4.5+40*rng.random()
        h=1+(m/4-1)*(0.03+0.94*rng.random())
        mass=0.5+5*rng.random()
        gap=phase_gap(m,h,mass)
        assert gap>0;checks+=1
        for q in [0.05,0.2,0.5,0.9,0.99]:
            xg=phase_quantile(q,m,h,mass,'gas')
            xd=phase_quantile(q,m,h,mass,'droplet')
            assert 0 < xg-xd <=gap+2e-11, (m,h,q, xg,xd,gap);checks+=1
            if q<1/h:
                assert abs(xg-xd-gap)<2e-10;checks+=1
            for kind,x in [('gas',xg),('droplet',xd)]:
                integral=independent_inverse_flux(q,m,h,mass,kind)
                assert abs(integral-x)<2e-6*max(1,x), (kind,q,integral,x)
                checks+=1
        # W1 = mean radial distance difference by stochastic order.
        observed=simpson(lambda q:phase_quantile(q,m,h,mass,'gas')-
                                   phase_quantile(q,m,h,mass,'droplet')
                         if 0<q<1 else (gap if q==0 else 0),0,1,1000)
        pred=phase_w1(m,h,mass)
        assert abs(observed-pred)<2e-6*max(1,pred), (observed,pred,m,h)
        checks+=1
        # Source mass conservation: liquid plus gas is M/2 in one half-space.
        chi=theta_scale(m,h,mass)
        assert math.isclose((h-1)/chi+1/chi,mass/2,rel_tol=2e-14)
        checks+=1
    # Reconstruct source Lambert-type stationary profiles independently in x.
    for m,h,mass in [(8,1.5,2),(12,2,3),(5,1.1,4),(20,4,1.4)]:
        for kind in ['gas','droplet']:
            for q in [0.15,0.45,0.85]:
                x=phase_quantile(q,m,h,mass,kind)
                observed=survival_from_published_profile(x,m,h,mass,kind)
                assert abs(observed-q)<3e-5,(m,h,mass,kind,q,observed)
                checks+=1
    # Uniform phase threshold independent of total mass and kinetic parameters.
    qstar=bisect(boundary_H,0.15,0.95)
    mstar=4/(1-qstar*qstar)
    assert abs(qstar-0.67358601212129)<5e-12
    assert abs(mstar-7.3222270683788135)<5e-11
    checks+=2
    for m in [4.1,5.0,6.5,7.1,7.6,8.0,10.0,20.0,50.0,300.0]:
        end=m/4
        signs=[deriv_numerator(m,1+(end-1)*k/200) for k in range(201)]
        assert all(signs[k]>signs[k+1]-1e-13 for k in range(200))
        checks+=1
        if m<mstar:
            assert signs[-1]>0;checks+=1
        else:
            assert signs[-1]<0;checks+=1
            hstar=bisect(lambda h:deriv_numerator(m,h),1,end)
            assert 1<hstar<end
            for v in [max(1+1e-5,hstar*0.97),min(end-1e-5,hstar*1.03)]:
                assert fvalue(m,hstar)/hstar>=fvalue(m,v)/v-1e-12
                checks+=1
    # Check the proposed high-crowding limit (fixed mass M=2).
    for m in [1e3,1e4,1e5]:
        hs=bisect(lambda h:deriv_numerator(m,h),1,m/4)
        assert abs(hs-math.e)<0.2
        assert abs(phase_gap(m,hs,2)-1/math.e)<0.02
        checks+=2
    print('PASS:',checks,'standalone numerical consistency checks')
    print('threshold m* =',format(mstar,'.14f'))
    print('reference m=8,h=1.5,M=2: W_inf =',format(phase_gap(8,1.5,2),'.14f'))
    print('reference m=8,h=1.5,M=2: W_1 =',format(phase_w1(8,1.5,2),'.14f'))


if __name__=='__main__':
    run()
