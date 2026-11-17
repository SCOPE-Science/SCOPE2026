"""Finite consistency checks for a single displaced Chebyshev--Lobatto node.

Run with Python 3; uses only the standard library. This is not a proof
of the asymptotic theorem, which is established analytically.
"""
import math


def critical_v(tau):
    assert 0 < tau < 1
    def derivative(v):
        return (math.pi * math.cos(math.pi*v)
                + tau*(math.pi*v*math.cos(math.pi*v)-math.sin(math.pi*v))/v**2)
    a, b = 1e-7, 0.5
    for _ in range(55):
        m = (a+b)/2
        if derivative(m) > 0:
            a = m
        else:
            b = m
    return (a+b)/2


def cardinal_values(n, theta):
    q = -math.sin(theta)*math.sin(n*theta)
    x = math.cos(theta)
    out = []
    for j in range(n+1):
        node = math.cos(math.pi*j/n)
        denominator = n*(x-node)*(-1 if j%2 else 1)
        if j == 0 or j == n:
            denominator *= 2
        out.append(q/denominator)
    return out


def displaced_lebesgue(n, tau, u, crosscheck=False):
    k = n//2
    theta = (k+u)*math.pi/n
    theta_y = (k+tau)*math.pi/n
    ell = cardinal_values(n,theta)
    ell_y = cardinal_values(n,theta_y)
    denominator = ell_y[k]
    transformed = [ell[j]-ell_y[j]*ell[k]/denominator
                   if j!=k else ell[k]/denominator for j in range(n+1)]
    assert abs(sum(transformed)-1) < 2e-7
    if crosscheck:
        x = math.cos(theta)
        y = math.cos(theta_y)
        xk = math.cos(k*math.pi/n)
        for j in range(n+1):
            if j == k:
                continue
            xj = math.cos(math.pi*j/n)
            value = ell[j]*(x-y)/(x-xk)*(xj-xk)/(xj-y)
            assert abs(value-transformed[j]) < 2e-7
    return sum(abs(t) for t in transformed)


def run():
    checks = 0
    for tau in (0.25,0.5,0.75):
        v = critical_v(tau)
        h = lambda z: math.sin(math.pi*z)*(1+tau/z)
        assert 0 < v < 0.5
        checks += 1
        assert h(v)>h(0.5) and h(v)>1 and h(v)>math.pi*tau
        checks += 3
        c=2/math.pi*h(v)
        for w in [j/100 for j in range(1,51)]:
            assert h(v)+1e-9>=h(w)
            checks += 1
        residuals=[]
        for n in (100,300,1000,2500,7000):
            val=displaced_lebesgue(n,tau,-v,crosscheck=n<=1000)
            r=val-c*math.log(n)
            assert abs(r)<9
            residuals.append(r)
            checks+=2
        # Numerically the constant additive term stabilizes as n increases;
        # this is a diagnostic of the analytically derived logarithmic coefficient.
        assert abs(residuals[-1]-residuals[-2])<0.015
        checks+=1
    print('PASS:', checks, 'finite assertions (not an infinite proof)')
    for tau in (0.25,0.5,0.75):
        v=critical_v(tau)
        coefficient=2/math.pi*math.sin(math.pi*v)*(1+tau/v)
        print('tau=%.2f v=%.12f leading_coefficient=%.12f'%(tau,v,coefficient))

if __name__=='__main__':
    run()
