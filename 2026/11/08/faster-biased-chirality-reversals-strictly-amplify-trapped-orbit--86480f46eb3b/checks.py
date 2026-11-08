"""Reproducible numerical checks for the two-state chirality-trap theorem.

Only Python's standard library is required. These finite checks supplement,
but do not replace, the analytical proof in RESULT.md.
"""
import math


def imag_resolvent(s, lam, delta, omega):
    a = lam * (1.0 - delta) / 2.0
    b = lam * (1.0 + delta) / 2.0
    det = (s + a - 1j * omega) * (s + b + 1j * omega) - a * b
    uplus = (s + lam + 1j * omega) / det
    uminus = (s + lam - 1j * omega) / det
    return ((b * uplus + a * uminus) / lam).imag


def I(s, lam, delta, omega):
    A = s * (s + lam) + omega * omega
    Q = A * A + (omega * lam * delta) ** 2
    return omega * delta * ((s + lam) ** 2 + omega * omega) / Q


def analytical_derivative_lam(s, lam, delta, omega):
    A = s * (s + lam) + omega * omega
    Q = A * A + (omega * lam * delta) ** 2
    return (2 * omega**3 * delta * lam * (1 - delta**2) *
            (lam * s + s * s + omega * omega) / Q**2)


def analytical_derivative_s(s, lam, delta, omega):
    A = s * (s + lam) + omega * omega
    Q = A * A + (omega * lam * delta) ** 2
    P = (s**5 + 4 * lam * s**4 + (6 * lam**2 + 2 * omega**2) * s**3
         + (4 * lam**3 + 4 * lam * omega**2) * s**2
         + (lam**4 + (3-delta**2) * lam**2 * omega**2 + omega**4) * s
         + (1-delta**2) * lam**3 * omega**2)
    return -2 * omega * delta * P / Q**2


def observables(kx, ky, Drot, v, lam, delta, omega):
    ix = I(kx + Drot, lam, delta, omega)
    iy = I(ky + Drot, lam, delta, omega)
    c = v*v*(ix-iy)/(2*(kx+ky))
    j = v*v*(kx*ix+ky*iy)/(kx+ky)
    return c, j


def ode_quadrature(s, lam, delta, omega, dt=0.006, horizon=28.0):
    """Independent real-time two-state evolution and Simpson quadrature."""
    n = int(round(horizon / dt))
    if n % 2: n += 1
    dt = horizon / n
    a = lam*(1-delta)/2
    b = lam*(1+delta)/2
    pi_plus = b/lam
    pi_minus = a/lam

    def velocity(y):
        p, m = y
        return ((1j*omega-a)*p+a*m, b*p+(-1j*omega-b)*m)

    def advance(y):
        q1 = velocity(y)
        q2 = velocity((y[0]+dt*q1[0]/2, y[1]+dt*q1[1]/2))
        q3 = velocity((y[0]+dt*q2[0]/2, y[1]+dt*q2[1]/2))
        q4 = velocity((y[0]+dt*q3[0], y[1]+dt*q3[1]))
        return (y[0]+dt*(q1[0]+2*q2[0]+2*q3[0]+q4[0])/6,
                y[1]+dt*(q1[1]+2*q2[1]+2*q3[1]+q4[1])/6)

    y = (1+0j, 1+0j)
    acc = 0.0
    for k in range(n+1):
        t = k*dt
        value = math.exp(-s*t)*(pi_plus*y[0]+pi_minus*y[1]).imag
        weight = (1 if k in (0,n) else 4 if k % 2 else 2)
        acc += weight*value
        if k<n: y=advance(y)
    return acc*dt/3


def test():
    assertions = 0
    def verify(truth, why):
        nonlocal assertions
        assertions += 1
        if not truth: raise AssertionError(why)

    for omega in (0.7, 2.0, 4.0):
        for lam in (0.2, 0.8, 3.0):
            for delta in (-0.8, -0.4, 0.0, 0.3, 0.9):
                for s in (0.8, 1.8, 3.7):
                    known = I(s, lam, delta, omega)
                    verify(abs(known-imag_resolvent(s,lam,delta,omega))<2e-12,
                           'resolvent disagreement')
                    dh = 1e-5
                    deriv = (I(s,lam+dh,delta,omega)-I(s,lam-dh,delta,omega))/(2*dh)
                    verify(abs(deriv-analytical_derivative_lam(s,lam,delta,omega))<1e-8,
                           'switch-rate derivative')
                    ds = (I(s+dh,lam,delta,omega)-I(s-dh,lam,delta,omega))/(2*dh)
                    verify(abs(ds-analytical_derivative_s(s,lam,delta,omega))<1e-8,
                           'Laplace-rate derivative')
                    verify(known*delta>=0, 'chirality sign')
                    if delta:
                        verify(analytical_derivative_lam(s,lam,delta,omega)*delta>0,
                               'switch monotonicity')
                        verify(analytical_derivative_s(s,lam,delta,omega)*delta<0,
                               'Laplace monotonicity')

    for lam,delta,omega,s in ((0.4,0.3,1.2,1.4),(1.0,-0.6,2.0,1.8),
                               (2.3,0.8,3.1,1.1),(0.7,0.0,1.7,1.2),
                               (1.8,-0.25,0.9,1.5)):
        numeric=ode_quadrature(s,lam,delta,omega)
        verify(abs(numeric-I(s,lam,delta,omega))<3e-8,
               f'ODE quadrature: {numeric} vs {I(s,lam,delta,omega)}')

    for kx,ky in ((1.0,3.0),(3.0,1.0),(2.0,2.0)):
        for delta in (-0.8,-0.2,0,0.3,0.85):
            curr=[]
            for lam in (0.05,0.5,1.0,4.0,30.0):
                cov,j=observables(kx,ky,0.7,1.3,lam,delta,2.1)
                ix=I(kx+0.7,lam,delta,2.1)
                iy=I(ky+0.7,lam,delta,2.1)
                xsin=1.3*ix/2
                ycos=-1.3*iy/2
                verify(abs(cov-1.3*(xsin+ycos)/(kx+ky))<1e-12,
                       'stationary cross-moment equation')
                verify(abs(j-((kx-ky)*cov+1.3*(xsin-ycos)))<1e-12,
                       'stationary current equation')
                verify((j==0 if delta==0 else j*delta>0), 'current sign')
                verify((abs(cov)<1e-15 if (delta==0 or kx==ky)
                        else cov*delta*(ky-kx)>0),'cross covariance sign')
                curr.append(abs(j))
            if delta:
                verify(all(x<y for x,y in zip(curr,curr[1:])),
                       'strict monotone circulation in switching speed')

    for kx,ky,omega,delta in ((1,2,1.3,0.3),(3,0.7,4,-0.5),
                               (2,2,0.9,0.9)):
        d=0.6
        j0=1.3**2*omega*delta/(kx+ky)*sum(
            k/((k+d)**2+omega**2) for k in (kx,ky))
        jinf=1.3**2*omega*delta/(kx+ky)*sum(
            k/((k+d)**2+(omega*delta)**2) for k in (kx,ky))
        verify(abs(jinf)>abs(j0), 'strict endpoint enhancement')
        verify(abs(observables(kx,ky,d,1.3,1e-6,delta,omega)[1]-j0)<1e-5,
               'slow switching endpoint')
        verify(abs(observables(kx,ky,d,1.3,1e7,delta,omega)[1]-jinf)<1e-5,
               'fast switching endpoint')
    print(f'PASS: {assertions} deterministic assertions; RK4/Simpson time-domain checks included')


if __name__=='__main__':
    test()
