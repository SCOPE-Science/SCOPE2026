#!/usr/bin/env python3
"""Reproduce the exact sketched-Hamiltonian formulas and finite consistency checks."""
import math
import numpy as np
from scipy.integrate import quad
from scipy.special import roots_jacobi

def probability(k, gamma):
    nu=k-1
    def integrand(theta):
        c=math.sin(theta/2)**2
        return (gamma*gamma*c*c/(1+gamma*gamma*c*c))**(nu/2)
    return quad(integrand,0,math.pi,epsabs=3e-13,epsrel=3e-13)[0]/math.pi

def experiment(k,gamma,n=100000,seed=1):
    rng=np.random.default_rng(seed)
    X=rng.standard_normal((n,k,2))
    y=rng.standard_normal((n,k))
    Xt=np.transpose(X,(0,2,1))
    z=np.linalg.solve(Xt@X,Xt@y[...,None])[:,:,0]
    return np.mean(gamma*(np.hypot(z[:,0],z[:,1])-z[:,0])/2>1)

def check():
    for gam in (0.05,0.25,0.75,1.5):
        H=np.eye(4);H[0,1]=H[1,0]=gam;H[1,1]+=gam**2
        assert np.min(np.linalg.eigvalsh(H))>0
        V=np.eye(4)[:,[0,2]]
        J=np.block([[np.zeros((2,2)),np.eye(2)],[-np.eye(2),np.zeros((2,2))]])
        assert np.allclose(V.T@J@V,np.array([[0,1],[-1,0]]))
        assert np.allclose(V.T@H@V,np.eye(2))
        for k in (2,3,5,8):
            q=probability(k,gam)
            assert 0<q<1
            print(f'k={k} gamma={gam} exact_indefinite={q:.9f}')
    for k in (2,3,5):
        g=.75
        q=probability(k,g)
        obs=experiment(k,g,n=120000,seed=410+k)
        sigma=math.sqrt(q*(1-q)/120000)
        print(f'MC k={k} gamma={g} observed={obs:.7f} exact={q:.7f} z={(obs-q)/sigma:.2f}')
        assert abs(obs-q)<6*sigma+0.0005
    for k in (2,3,5,8):
        nu=k-1
        target=math.comb(2*nu,nu)/4**nu
        for gam in (0.01,0.003):
            rel=probability(k,gam)/gam**nu/target
            print(f'small-coupling k={k} g={gam} normalized={rel:.12f}')
            assert abs(rel-1) < (nu+1)*gam**2
    for g in (0.5,1.,2.):
        for k in (60,120):
            nu=k-1
            p=probability(k,g)
            q=(g*g/(1+g*g))**(nu/2)*math.sqrt((1+g*g)/(math.pi*nu))
            print(f'large-k k={k} gamma={g} exact={p:.12g} asymptotic={q:.12g} ratio={p/q:.6f}')
            assert 0.9<p/q<1.1
    rng=np.random.default_rng(13)
    for k in (2,3,6):
        for j in range(50):
            gam=0.1+1.1*rng.random()
            H=np.eye(4);H[0,1]=H[1,0]=gam;H[1,1]+=gam**2
            V=np.eye(4)[:,[0,2]]
            Theta=rng.standard_normal((k,4))/np.sqrt(k)
            X=Theta@V
            z=np.linalg.lstsq(X,Theta[:,1],rcond=None)[0]
            Hhat=(np.linalg.lstsq(X,Theta@H@V,rcond=None)[0]);Hhat=(Hhat+Hhat.T)/2
            Htheory=np.eye(2)+gam*np.array([[z[0],z[1]/2],[z[1]/2,0]])
            assert np.allclose(Hhat,Htheory,atol=1e-8,rtol=1e-8)
            lam=1+gam/2*(z[0]-np.linalg.norm(z))
            assert np.isclose(lam,np.min(np.linalg.eigvalsh(Hhat)))
    print('SCIENTIFIC_CHECKS_OK')
if __name__=='__main__':check()
