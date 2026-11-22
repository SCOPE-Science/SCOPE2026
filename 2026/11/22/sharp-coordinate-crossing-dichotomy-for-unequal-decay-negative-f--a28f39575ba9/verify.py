#!/usr/bin/env python3
"""Independent finite checks for the angular comparison identities and examples."""
import cmath
import math

cases = 0
for a,b in [(1.0,1.0),(1.4,0.8),(0.3,2.2)]:
    omega = math.sqrt(a*b)
    for delta in [-1.3*omega,-1.0*omega,-0.8*omega,0.0,0.35*omega,0.8*omega,omega,1.3*omega]:
        gamma_bar = abs(delta)+omega+1
        gamma1,gamma2=gamma_bar+delta,gamma_bar-delta
        assert gamma1>0 and gamma2>0
        # Constant affine coupled solution from first-coordinate equality with second difference 1.
        def X(t):
            if abs(delta)<omega-1e-12:
                w=math.sqrt(omega**2-delta**2)
                return -a*math.exp(-gamma_bar*t)*math.sin(w*t)/w
            elif abs(abs(delta)-omega)<1e-12:
                return -a*t*math.exp(-gamma_bar*t)
            else:
                nu=math.sqrt(delta**2-omega**2)
                return -a*math.exp(-gamma_bar*t)*math.sinh(nu*t)/nu
        for t in [0.1,0.5,1.0,1.7]:
            assert X(t)<0
            cases+=1
        if abs(delta)<omega-1e-12:
            w=math.sqrt(omega**2-delta**2)
            T=math.pi/w
            assert abs(X(T)) <1e-12
            assert X(.95*T)<0
            # Elementary half-turn integral using Simpson quadrature.
            def f(theta): return omega+delta*math.sin(2*theta)
            n=40000; h=math.pi/n
            I=h/3*(1/f(math.pi/2)+1/f(3*math.pi/2)+sum((4 if j%2 else 2)/f(math.pi/2+j*h) for j in range(1,n)))
            assert abs(I-T)<2e-9,(I,T)
            cases+=1

# Numerical independent phase tests for nonautonomous secant coefficients.
for delta in [-.95,-.5,0.0,.4,.95,1.1]:
    omega=1.0
    tmax=min(8.,math.pi/math.sqrt(1-delta**2)*.99) if abs(delta)<1 else 8.
    n=12000; dt=tmax/n
    theta=math.pi/2
    def speed(t,ang):
        a=.2+.8*(.5+.5*math.sin(2.3*t))
        b=.15+.85*(.5+.5*math.cos(1.7*t))
        return b*math.cos(ang)**2+a*math.sin(ang)**2+delta*math.sin(2*ang)
    for i in range(n):
        t=i*dt
        k1=speed(t,theta);k2=speed(t+dt/2,theta+dt*k1/2)
        k3=speed(t+dt/2,theta+dt*k2/2);k4=speed(t+dt,theta+dt*k3)
        theta+=dt*(k1+2*k2+2*k3+k4)/6
        assert theta < 1.5*math.pi-1e-7,(delta,i,theta)
        cases+=1
print(f'PASS: {cases} independent analytic, quadrature and variable-slope angle tests.')
