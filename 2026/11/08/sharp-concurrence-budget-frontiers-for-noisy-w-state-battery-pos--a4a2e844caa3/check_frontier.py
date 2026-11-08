"""Independent finite-dimensional checks for the W3 postselection concurrence frontier.

This script tests the explicit theorem's algebra, selected outcomes and direct
conditional density matrices. It does not replace the analytic all-state proof.
"""
import math
import numpy as np
import sympy as sp

EPS=3e-11

def concurrence(v):
    a,b,c,d = np.asarray(v,dtype=complex)
    return 2*abs(a*d-b*c)

def invariants(v):
    a,b,c,d = np.asarray(v,dtype=complex)
    N=abs(a)**2+abs(b+c)**2
    zeta=abs(b+c)**2
    return float(N),float(zeta),float(abs(a)**2)

def frontier_probability(c,p):
    return p/4+(1-p)*(4+2*c)/9

def frontier_ergotropy(c,p,energy=1):
    return 8*(1-p)*(1+c)*energy/(3*p+4*(1-p)*(1+c))

def success_witness(c):
    a=2*math.sqrt(1-c)/3
    d=math.sqrt(1-c)/3
    b=math.sqrt((4+5*c)/18)
    return np.array([a,b,b,d],dtype=complex)

def ergotropy_witness(c):
    rad=math.sqrt(max(0.,1-c*c))
    b=math.sqrt((1+rad)/2)
    d=math.sqrt((1-rad)/2)
    return np.array([0.,b,d,0.],dtype=complex)

def branch(v,p,eps=1.):
    # Pure |W3> in A, B, C order; noisy total 8 by 8.
    w=np.zeros(8,complex)
    for k in (1,2,4): w[k]=1/math.sqrt(3)
    rho=(1-p)*np.outer(w,w.conj())+p*np.eye(8)/8
    # <v| on BC, no transpose mistaken for complex conjugation.
    proj=np.kron(np.eye(2),np.asarray(v).conj().reshape(1,4))
    raw=proj @ rho @ proj.conj().T
    prob=float(np.trace(raw).real)
    eig=np.linalg.eigvalsh(raw/prob)
    H=np.diag([eps,-eps])
    ergotropy=float((np.trace(raw@H)/prob + eps*(eig[1]-eig[0])).real)
    N,zeta,q=invariants(v)
    predprob=p/4+(1-p)*N/3
    prederg=8*(1-p)*zeta*eps/(3*p+4*(1-p)*N)
    return prob,ergotropy,predprob,prederg

def main():
    checks=0
    c,p=sp.symbols('c p',real=True)
    a2=4*(1-c)/9
    d2=(1-c)/9
    b2=(4+5*c)/18
    # On the success witness, ad=2(1-c)/9 and bc=b2.
    assert sp.simplify(a2+d2+2*b2-1)==0
    assert sp.simplify(2*(b2-2*(1-c)/9)-c)==0
    assert sp.simplify(a2+4*b2-(4+2*c)/3)==0
    N=(4+2*c)/3
    assert sp.simplify(p/4+(1-p)*N/3 - (p/4+(1-p)*(4+2*c)/9))==0
    zeta=1+c
    E=8*(1-p)*zeta/(3*p+4*(1-p)*zeta)
    assert sp.simplify(E-8*(1-p)*(1+c)/(3*p+4*(1-p)*(1+c)))==0
    checks+=5
    for c in (0,0.025,0.1,0.25,0.5,0.75,0.91,1):
        v=success_witness(c)
        assert abs(np.vdot(v,v).real-1)<EPS
        assert abs(concurrence(v)-c)<EPS
        N,zeta,q=invariants(v)
        assert abs(N-(4+2*c)/3)<EPS
        checks+=4
        u=ergotropy_witness(c)
        assert abs(np.vdot(u,u).real-1)<EPS
        assert abs(concurrence(u)-c)<EPS
        assert abs(invariants(u)[1]-(1+c))<EPS
        checks+=3
        for p in (0.04,0.2,0.6,0.97):
            prob,erg,predprob,prederg=branch(v,p)
            assert abs(prob-predprob)<EPS
            assert abs(erg-prederg)<EPS
            assert abs(prob-frontier_probability(c,p))<EPS
            prob,erg,predprob,prederg=branch(u,p)
            assert abs(prob-predprob)<EPS
            assert abs(erg-prederg)<EPS
            assert abs(erg-frontier_ergotropy(c,p))<EPS
            checks+=6
    rng=np.random.default_rng(329103)
    for _ in range(12000):
        v=rng.normal(size=4)+1j*rng.normal(size=4)
        v=v/np.linalg.norm(v)
        c=concurrence(v)
        N,zeta,q=invariants(v)
        assert N <=(4+2*c)/3+1e-11
        assert zeta<=1+c+1e-11
        p=float(rng.uniform(0.01,0.99))
        assert p/4+(1-p)*N/3<=frontier_probability(c,p)+1e-11
        _,erg,_,_=branch(v,p)
        assert erg<=frontier_ergotropy(c,p)+1e-11
        checks+=4
    print(f'PASS: {checks} independent analytic/numeric assertions')

if __name__=='__main__':main()
