"""Analytic and independent numerical checks for weak seasonal transmission.
Run with the Python 3 standard library: python verify_phase.py
"""
import math


def coefficient(a, d, b, c, omega, phase):
    s = math.sqrt((d - a)**2 / 4 + b*c)
    r = (d - a) / (2*s)
    return (b*c / (2*(4*s*s + omega*omega)) *
            (s*((1+r*r)*math.cos(phase) - (1-r*r))
             + omega*r*math.sin(phase)))


def riccati_coefficient(a, d, b, c, omega, phase):
    # A distinct calculation via the first two variational equations.
    s = math.sqrt((d-a)**2 / 4 + b*c)
    y0 = (s + (a-d)/2)/b
    forcing = c*complex(math.cos(phase),math.sin(phase))-b*y0*y0
    response = forcing / complex(2*s,omega)
    mean_y1_squared = abs(response)**2/2
    mean_cos_y1 = response.real/2
    mean_y2 = (-b*mean_y1_squared-2*b*y0*mean_cos_y1)/(2*s)
    return b*(mean_y2 + mean_cos_y1)


def exponent(a, d, b, c, omega, phase, eps):
    # Integrate the four fundamental matrix entries using classic RK4;
    # this method is algorithmically independent of the Riccati calculation.
    T = 2*math.pi/omega
    steps = 2048
    h = T/steps
    z = (1.,0.,0.,1.)  # row-major identity

    def rhs(t,v):
        bnow = b*(1+eps*math.cos(omega*t))
        cnow = c*(1+eps*math.cos(omega*t+phase))
        return (-a*v[0]+bnow*v[2], -a*v[1]+bnow*v[3],
                cnow*v[0]-d*v[2], cnow*v[1]-d*v[3])

    for k in range(steps):
        t=k*h
        k1=rhs(t,z)
        k2=rhs(t+h/2,tuple(z[j]+h*k1[j]/2 for j in range(4)))
        k3=rhs(t+h/2,tuple(z[j]+h*k2[j]/2 for j in range(4)))
        k4=rhs(t+h,tuple(z[j]+h*k3[j] for j in range(4)))
        z=tuple(z[j]+h*(k1[j]+2*k2[j]+2*k3[j]+k4[j])/6 for j in range(4))
    leading=(z[0]+z[3]+math.sqrt((z[0]-z[3])**2+4*z[1]*z[2]))/2
    return math.log(leading)/T


def main():
    checks=0
    examples=[(1.,2.,1.,2.,1.),(1.,1.,1.,1.,1.),
              (3.,1.,1.,3.,2.),(.7,1.8,1.,.9,3.),
              (.9,2.4,1.4,.7,.65)]
    phases=[-3.,-2.,-1.,-.3,0.,.17,.75,1.5,2.8]
    for a,d,b,c,omega in examples:
        s=math.sqrt((d-a)**2/4+b*c)
        r=(d-a)/(2*s)
        opt=math.atan2(omega*r,s*(1+r*r))
        if a!=d:
            assert abs(opt)>1e-12
        peak=coefficient(a,d,b,c,omega,opt)
        trough=coefficient(a,d,b,c,omega,opt+math.pi)
        assert peak>=-1e-13 and trough<0
        checks+=3
        for phase in phases+[opt,opt+math.pi]:
            q=coefficient(a,d,b,c,omega,phase)
            assert abs(q-riccati_coefficient(a,d,b,c,omega,phase))<1e-12*(1+abs(q))
            checks+=1
            eps=.035
            plus=exponent(a,d,b,c,omega,phase,eps)
            minus=exponent(a,d,b,c,omega,phase,-eps)
            baseline=exponent(a,d,b,c,omega,phase,0)
            numerical=(plus+minus-2*baseline)/(2*eps*eps)
            assert abs(numerical-q)<2.2e-4*(1+abs(q))
            assert abs(plus-minus)<2e-8
            checks+=2
        for phase in (opt-.35,opt+.21,opt+math.pi):
            assert peak>=coefficient(a,d,b,c,omega,phase)-1e-13
            checks+=1
    assert abs(coefficient(1,2,1,2,1,0)-1/30)<1e-14
    assert abs(coefficient(1,2,1,2,1,math.pi)+3/10)<1e-14
    checks+=2
    for eps in (-.75,-.33,0,.28,.6):
        assert abs(exponent(1,1,1,1,1,0,eps))<5e-12
        checks+=1
    print('PASS',checks,'checks: independent Riccati calculation and RK4 monodromy integration')


if __name__=='__main__':
    main()
