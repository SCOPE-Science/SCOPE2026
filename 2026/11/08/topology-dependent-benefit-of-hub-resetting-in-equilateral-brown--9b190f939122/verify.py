"""Standalone reproducibility checks for diffusion on an equilateral metric star.

Requires only the Python standard library. This script checks finite-difference
backward equations independently of the closed-form transform; it also checks
the dimensionless asymptotics, optimality onset and limiting optimizer.
"""
import math


def phi_exact(m, z):
    c = math.cosh(z)
    return c / (1.0 + m * math.sinh(z) ** 2)


def phi_difference(m, z, n):
    # Discretize D f''=s f on each arm of length 1, s/D=z*z.
    # Use 2(f[n-1]-f[n])=z*z/n**2*f[n] at reflecting endpoints.
    t = z*z / (n*n)
    alpha = 1.0 + t/2.0
    rr_next, rr_cur = 1.0, alpha  # reflection solution at n and n-1
    for j in range(n-1, 0, -1):
        rr_prev = (2.0+t)*rr_cur-rr_next
        rr_next, rr_cur = rr_cur, rr_prev
    # rr_cur now R[0], rr_next R[1]
    arm_ratio = rr_next/rr_cur
    u_prev, u_cur = 1.0, 0.0  # initial values at 0 and 1
    v_prev, v_cur = 0.0, 1.0
    for j in range(1,n):
        u_prev,u_cur = u_cur,(2.0+t)*u_cur-u_prev
        v_prev,v_cur = v_cur,(2.0+t)*v_cur-v_prev
    return 1.0/(u_cur+v_cur*(m-(m-1)*arm_ratio))


def t_dimensionless(m,z):
    if z == 0.0:
        return m-0.5
    # numerically stable near zero via series
    if z < 0.01:
        return m-.5 + (5.-4.*m)*z*z/24.0 + (62.*m-61.)*z**4/720.0
    c=math.cosh(z)
    return (m*c-1.0-(m-1.0)/c)/(z*z)


def f_limit(z):
    if z == 0.0: return 1.0
    c=math.cosh(z)
    return (c-1.0/c)/(z*z)


def golden_min(f,a=0.00001,b=5.0):
    gr=(math.sqrt(5)-1)/2
    c=b-gr*(b-a); d=a+gr*(b-a)
    for _ in range(170):
        if f(c)<f(d): b,d,c=d,c,d-gr*(d-a)
        else: a,c,d=d,d,a+gr*(b-d)
    x=(a+b)/2
    return x,f(x)


def main():
    total=0
    for m in (1,2,3,5,9):
        for z in (0.5,1.0,1.7,2.4):
            approx=phi_difference(m,z,3200)
            exact=phi_exact(m,z)
            assert abs(approx-exact)<0.00010, (m,z,approx,exact)
            total+=1
            # Exact transform is consistent with renewal MFPT formula.
            t=t_dimensionless(m,z)
            assert abs(t-(1/exact-1)/(z*z))<1e-10
            total+=1
    # Perturbative one-arm no-benefit / multi-arm benefit.
    for m in (1,2,3,5,10,100):
        x,val=golden_min(lambda z:t_dimensionless(m,z))
        if m==1:
            assert abs(val-.5)<1e-7 and x<0.001, (m,x,val)
        else:
            assert val<m-.5 and x>0.2, (m,x,val)
        total+=1
    # Pointwise derivative of normalized MFPT is strictly negative in m.
    for z in (0.3,0.7,1.4,2.2):
        values=[t_dimensionless(m,z)/(m-.5) for m in (1,2,3,5,20,100)]
        assert all(a>b for a,b in zip(values,values[1:])), (z,values)
        total+=1
    zstar,fstar=golden_min(f_limit)
    assert 1.60611<zstar<1.60612 and .85526<fstar<.85527
    total+=1
    assert abs(t_dimensionless(10000,zstar)/(10000-.5)-fstar)<2e-5
    total+=1
    print(f"PASS: {total} independent boundary and optimization diagnostics")
    print(f"limiting optimizer z={zstar:.12f}, limiting normalized MFPT={fstar:.12f}")
    print(f"limiting gain fraction={1-fstar:.12f}")


if __name__=='__main__': main()
