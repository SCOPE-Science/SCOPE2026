"""Numerical checks of exact exponential-space SBP forward-Euler spectrum.

No finite check substitutes for the algebraic all-phase proof.
"""
import math
import numpy as np

def coefficients(beta):
    if beta == 0:
        return 1., 1.
    c=beta/math.expm1(beta)
    d=beta/(-math.expm1(-beta))
    return c,d

def threshold(beta):
    if beta == 0:
        return 0.
    c,d=coefficients(beta)
    return min(2/(c+d),(c-d)**2/(2*c*d*(c+d)))

def symbol(beta,nu,theta):
    c,d=coefficients(beta)
    z=np.exp(-1j*theta)
    return np.eye(2,dtype=complex)+nu*np.array([[-c,c*(-1+2*z)],[d,-d]],dtype=complex)

def real_ring(beta,nu,m):
    c,d=coefficients(beta)
    A=np.eye(2*m)
    for j in range(m):
        A[2*j,2*j] += -nu*c
        A[2*j,2*j+1] += -nu*c
        A[2*j,2*((j-1)%m)+1] += 2*nu*c
        A[2*j+1,2*j] += nu*d
        A[2*j+1,2*j+1] += -nu*d
    return A

def check():
    rng=np.random.default_rng(1642)
    total=0
    for beta in (0.,0.03,0.1,.5,1.,1.762747174,2.,3.,6.):
        c,d=coefficients(beta)
        H=np.diag([1/(2*c),1/(2*d)])
        D=np.array([[-c,c],[-d,d]])
        assert np.allclose(H@D+D.T@H,np.diag([-1.,1.]),atol=1e-10)
        assert np.allclose(D@np.array([1.,1.]),0.)
        if beta!=0:
            V=np.array([1.,math.exp(beta)])
            assert np.allclose(D@V,beta*V,atol=1e-10)
        h=threshold(beta)
        for m in (2,3,5,8,16,29):
            nu=max(0.00001,h*.77) if h>0 else .06
            A=real_ring(beta,nu,m)
            all_eig=np.sort_complex(np.linalg.eigvals(A))
            block_eig=np.sort_complex(np.concatenate([np.linalg.eigvals(symbol(beta,nu,2*math.pi*j/m)) for j in range(m)]))
            assert np.allclose(np.sort(all_eig.real),np.sort(block_eig.real),atol=1e-8)
            assert np.allclose(np.sort(all_eig.imag),np.sort(block_eig.imag),atol=1e-8)
            for j in range(m):
                x=2*math.pi*j/m
                c0=d0=None
                g=symbol(beta,nu,x)
                p=nu*(c+d);q=2*nu*nu*c*d;z=complex(math.cos(x),-math.sin(x))
                assert abs(np.trace(g)-(2-p))<1e-10
                assert abs(np.linalg.det(g)-(1-p+q*(1-z)))<1e-10
                total+=1
        if beta>0:
            for theta in np.linspace(0,math.pi,170):
                assert np.max(np.abs(np.linalg.eigvals(symbol(beta,h*.99,theta)))) < 1+1e-8
                total+=1
    b=2*math.asinh(1)
    v=threshold(b)
    c,d=coefficients(b)
    assert abs(v-2/(c+d))<1e-12
    assert abs(8*c*d/(c+d)**2-1)<1e-12
    for m in (2,3,5,17,29):
        G=real_ring(b,v,m)
        shift=np.zeros_like(G)
        for j in range(m):
            shift[2*j,2*((j-1)%m)]=1
            shift[2*j+1,2*((j-1)%m)+1]=1
        assert np.allclose(G@G,shift,rtol=0,atol=2e-13)
        total+=1
    # Detect failure above both branches with dense Fourier phases.
    for beta in (.5,1.,1.7,1.8,3.,8.):
        nu=threshold(beta)*1.12
        radii=[max(abs(t) for t in np.linalg.eigvals(symbol(beta,nu,x))) for x in np.geomspace(1e-4,math.pi,450)]
        assert max(radii)>1+1e-9,(beta,max(radii))
        total+=1
    # Series beta->0 and beta->infinity.
    for b in (.01,.03,.1):
        assert abs(threshold(b)/(b*b/4)-1)<.01
    for b in (8.,12.,16.):
        assert abs(threshold(b)*b/2-1)<.01
    print('VERIFY_OK', 'checks',total,'critical_beta',2*math.asinh(1),'critical_nu',v,'resonance_verified',True)
if __name__=='__main__':check()
