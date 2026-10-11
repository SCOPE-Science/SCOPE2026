#!/usr/bin/env python3
import math
import numpy as np

sx=np.array([[0,1],[1,0]],complex)
sy=np.array([[0,-1j],[1j,0]],complex)
sz=np.array([[1,0],[0,-1]],complex)
paulis=[sx,sy,sz]

def hamiltonian(J,Jz,D):
    return J*(np.kron(sx,sx)+np.kron(sy,sy))+Jz*np.kron(sz,sz)+D*(np.kron(sx,sy)-np.kron(sy,sx))

def gibbs(J,Jz,D,T):
    H=hamiltonian(J,Jz,D)
    w,v=np.linalg.eigh(H)
    p=np.exp(-(w-w.min())/T)
    rho=(v*p)@v.conj().T
    return rho/np.trace(rho)

def corr_matrix(rho):
    C=np.zeros((3,3),float)
    for i,a in enumerate(paulis):
        for j,b in enumerate(paulis):
            C[i,j]=np.trace(rho@np.kron(a,b)).real
    return C

def analytic_corr(J,Jz,D,T):
    R=math.hypot(J,D)
    Z=2*math.exp(-Jz/T)+2*math.exp(Jz/T)*math.cosh(2*R/T)
    cp=2*math.exp(Jz/T)*math.sinh(2*R/T)/Z
    cz=2*(math.exp(Jz/T)*math.cosh(2*R/T)-math.exp(-Jz/T))/Z
    return R,cp,cz

def h2(x):
    if x<=0 or x>=1:
        return 0.0
    return -x*math.log2(x)-(1-x)*math.log2(1-x)

def discord_exact(J,Jz,D,T):
    R=math.hypot(J,D)
    Z=2*math.exp(-Jz/T)+2*math.exp(Jz/T)*math.cosh(2*R/T)
    probs=[
        math.exp(-Jz/T)/Z,
        math.exp(-Jz/T)/Z,
        math.exp((Jz-2*R)/T)/Z,
        math.exp((Jz+2*R)/T)/Z,
    ]
    S=-sum(p*math.log2(p) for p in probs if p>0)
    _,cp,cz=analytic_corr(J,Jz,D,T)
    c=max(cp,cz)
    return 1-S+h2((1+c)/2)

def coeff(J,Jz,D):
    R=math.hypot(J,D)
    if Jz>=R:
        return R*R/math.log(2)
    return (R*R+Jz*Jz)/(2*math.log(2))

def main():
    corr_checks=0
    boundary_checks=0
    for J,Jz,D in [
        (1.0,0.2,0.5),
        (1.0,1.0,0.7),
        (1.0,2.0,0.4),
        (0.7,1.6,1.0),
        (1.3,1.3,0.0),
    ]:
        for T in (0.35,0.8,1.7,4.0,9.0):
            rho=gibbs(J,Jz,D,T)
            s=np.linalg.svd(corr_matrix(rho),compute_uv=False)
            R,cp,cz=analytic_corr(J,Jz,D,T)
            target=np.array(sorted([cp,cp,cz],reverse=True))
            assert np.max(np.abs(np.sort(s)[::-1]-target))<2e-11
            corr_checks+=1
            if abs(Jz-R)>1e-12:
                assert (cz>cp)==(Jz>R)
                boundary_checks+=1

    asymptotic_checks=0
    for J,Jz,D in [
        (1.0,0.2,0.5),
        (1.0,1.8,0.3),
        (1.0,1.25,0.75),
        (0.6,1.4,1.1),
    ]:
        C=coeff(J,Jz,D)
        errs=[]
        for T in (80.0,160.0,320.0):
            val=T*T*discord_exact(J,Jz,D,T)
            errs.append(abs(val-C))
        assert errs[-1] < errs[0]
        assert errs[-1] < 0.02*max(1.0,C)
        asymptotic_checks+=1

    print("VERIFY_OK")
    print("correlation_spectrum_checks =",corr_checks)
    print("optimizer_boundary_checks =",boundary_checks)
    print("high_temperature_cases =",asymptotic_checks)
    J,Jz=1.0,1.5
    print("example_switch_Dz =",math.sqrt(Jz*Jz-J*J))

if __name__=="__main__":
    main()
