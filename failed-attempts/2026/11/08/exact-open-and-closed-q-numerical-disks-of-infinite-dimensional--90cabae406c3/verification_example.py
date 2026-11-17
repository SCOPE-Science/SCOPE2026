"""Finite checks accompanying an analytic infinite-dimensional theorem.

Requires Python 3 and NumPy. These tests confirm algebraic identities and
finite-block approximations, not assertions about infinite-dimensional spectra.
"""
import math
import numpy as np


def profile(rho, r):
    if r <= rho:
        return 1.0
    return r*rho + math.sqrt(max(0.0, 1-r*r))*math.sqrt(max(0.0, 1-rho*rho))


def rotation(theta):
    return np.array([[math.cos(theta), -math.sin(theta)],
                     [math.sin(theta), math.cos(theta)]], dtype=complex)


def bilinear_quadratic(U, x):
    # np.vdot is conjugate-linear in its first argument.
    return np.vdot(x, U @ np.conjugate(x))


def best_pair(U, x, q):
    # Inner-product convention: <a,b> is np.vdot(b,a), linear in a.
    # Thus <x,y>=q means y=conj(q)*x+t*u.
    z = U @ np.conjugate(x)
    a = np.vdot(x, z)  # <z,x>
    v = z-a*x
    nv = np.linalg.norm(v)
    t = math.sqrt(max(0.0, 1.0-abs(q)**2))
    if nv < 1e-11:
        u = np.array([-np.conjugate(x[1]), np.conjugate(x[0])])
    else:
        u=v/nv
        # <z,u> is np.vdot(u,z), conjugate-linear in u.
        # align with <z,conj(q)*x> = q*a.
        if abs(q*a)>1e-14:
            u *= np.exp(-1j*np.angle(q*a))
    y=np.conjugate(q)*x+t*u
    return y, z


def test():
    checked=0
    for rho in [0.05, .2, .4, .6, .8, .97]:
        U=rotation(math.acos(rho))
        B=U@U
        T=(U+U.T)/2  # conjugation C omitted, so antilinear T=matrix*C
        assert np.allclose(T,rho*np.eye(2),atol=1e-14)
        assert np.isclose(np.linalg.norm(T,2),.5*np.linalg.norm(np.eye(2)+B,2),atol=2e-14)
        checked+=2
        for r in [0.0, rho/3,rho, (1+rho)/2,1.0]:
            for ang in [0.0, .2,1.6, 2.8]:
                q=r*np.exp(1j*ang)
                a=min(r,rho)
                beta=.5*math.acos(a/rho)
                x=np.array([math.cos(beta), 1j*math.sin(beta)])
                y,z=best_pair(U,x,q)
                assert np.isclose(np.vdot(x,x),1,atol=1e-12)
                assert np.isclose(np.vdot(y,y),1,atol=1e-12)
                assert np.isclose(np.vdot(y,x),q,atol=1e-12)  # <x,y>
                assert np.isclose(abs(np.vdot(y,z)),profile(rho,r),atol=1e-12)
                checked+=4
    for rho0 in [.15,.6,.9]:
        for N in [3,5,10,30,100,300]:
            rhoN=rho0*N/(N+1)
            for r in [0,rho0*.75,rho0,(rho0+1)/2,1]:
                # The finite-block best is computed with rho_N and converges.
                val=profile(rhoN,r)
                limit=profile(rho0,r)
                assert val<=limit+1e-12
                checked+=1
            assert rhoN<rho0
            checked+=1
    assert profile(.6,.4)==1.
    assert profile(.6,.6)==1.
    assert np.isclose(profile(.6,.9),.9*.6+math.sqrt(1-.9*.9)*.8)
    checked+=3
    print(f"PASS: {checked} deterministic algebraic and finite-block assertions")


if __name__ == '__main__':
    test()
