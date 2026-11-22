"""Reproduce exact moment constants and finite-time Poincare diagnostics.

Only exact rational identities and finite numerical comparisons are checked;
no numerical test is used to certify an asymptotic theorem.
"""
from fractions import Fraction
from math import comb, pi, sqrt
from scipy.integrate import solve_ivp
from scipy.optimize import brentq


def moment_fraction(j):
    """I_j/(2 pi), exactly."""
    return Fraction(comb(2*j+2,j+1),4**(j+1))


def moment(j):
    return 2*pi*float(moment_fraction(j))


def positive_return(r, a1=1., a2=0., N=2, m=2, n=3):
    """One full positive-axis return from (x,y)=(0,r)."""
    def vf(t,z):
        x,y=z
        return (y-a1*x**(2*N)-a2*x**(2*m+1)-x**(2*n+1),-x)
    def up(t,z):
        return z[0]
    up.direction=1
    sol=solve_ivp(vf,(0.,7.1),(0.,r),events=up,
                  rtol=3e-12,atol=3e-14,max_step=.05)
    assert sol.success and len(sol.t_events[0])>=2
    t=sol.t_events[0][-1]
    y=sol.y_events[0][-1,1]
    assert t>5.5 and y>0
    return y,t


def run():
    # Exact rational identity and dimensionless ratios.
    assert moment_fraction(2)==Fraction(5,16)
    assert moment_fraction(3)==Fraction(35,128)
    assert moment_fraction(2)/moment_fraction(3)==Fraction(8,7)
    I_m,I_n=moment(2),moment(3)
    ustar=sqrt(8/7)
    K=2*I_n*ustar**6
    assert abs(K-80*pi/49)<2e-14
    assert Fraction(1,6)/moment_fraction(3)==Fraction(64,105)

    # The even-only system is locally reversible and has return height r.
    for a1 in (-2.0, 1.0, 3.0):
        for r in (0.09,0.15,0.2):
            got,_=positive_return(r,a1=a1,a2=0.,n=99)
            assert abs(got-r)<2e-10,(a1,r,got)

    # The critical weak-focus displacement, divided by its leading term.
    errs=[]
    for r in (0.24,0.18,0.13):
        next_r,_=positive_return(r)
        ratio=(r-next_r)/(I_n*r**7)
        errs.append(abs(ratio-1))
        assert abs(ratio-1)<0.09,(r,ratio)
    assert errs[-1]<errs[0]

    # Unique small cycle: amplitude, weak attraction and physical period.
    errors=[]
    for delta in (0.45,0.32,0.24):
        a2=-delta**2
        def displacement(r):
            return positive_return(r,a2=a2)[0]-r
        root=brentq(displacement,0.75*delta,1.55*delta,xtol=4e-13)
        h=3e-4*delta
        mult=(positive_return(root+h,a2=a2)[0]-
              positive_return(root-h,a2=a2)[0])/(2*h)
        ratio=(1-mult)/(K*delta**6)
        _,period=positive_return(root,a2=a2)
        assert root>0 and 0<mult<1 and abs(period-2*pi)<.1
        assert abs(root/delta-ustar)<.075
        assert abs(ratio-1)<.25
        errors.append(abs(root/delta-ustar))
        print(f'delta={delta:.2f}; r/delta={root/delta:.8f}; multiplier ratio={ratio:.8f}; period={period:.8f}')
    assert errors[2]<errors[1]<errors[0]

    # Nonlinear scaled transient compared with the asymptotic ODE.
    delta=.38
    a2=-delta**2
    u0=.75
    ds=delta**6
    steps=round(.12/ds)
    u=u0
    for _ in range(steps):
        u=positive_return(delta*u,a2=a2)[0]/delta
    def drift(t,z):
        v=z[0]
        return [I_m*v**5-I_n*v**7]
    ode=solve_ivp(drift,(0,steps*ds),[u0],rtol=1e-12,atol=1e-14)
    assert abs(u-ode.y[0,-1])<.007, (u,ode.y[0,-1])
    print(f'scaled slow-time numerical comparison: {u:.9f} vs {ode.y[0,-1]:.9f}')
    print('PASS: exact moments, reversibility, critical local displacement, cycle scaling and finite slow-time comparison.')

if __name__=='__main__':
    run()
