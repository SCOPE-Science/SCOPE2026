#!/usr/bin/env python3
import math
import numpy as np

sx=np.array([[0,1],[1,0]],complex)
sy=np.array([[0,-1j],[1j,0]],complex)
sz=np.array([[1,0],[0,-1]],complex)
I=np.eye(2,dtype=complex)

def hamiltonian(J,Jz,B,b):
    return 0.5*(J*(np.kron(sx,sx)+np.kron(sy,sy))
                +Jz*np.kron(sz,sz)
                +(B+b)*np.kron(sz,I)
                +(B-b)*np.kron(I,sz))

def gibbs(J,Jz,B,b,T):
    H=hamiltonian(J,Jz,B,b)
    w,v=np.linalg.eigh(H)
    p=np.exp(-(w-w.min())/T)
    rho=(v*p)@v.conj().T
    return rho/np.trace(rho)

def concurrence_direct(J,Jz,B,b,T):
    rho=gibbs(J,Jz,B,b,T)
    yy=np.kron(sy,sy)
    R=rho@yy@rho.conj()@yy
    vals=np.linalg.eigvals(R)
    vals=np.maximum(vals.real,0.0)
    roots=sorted((math.sqrt(x) for x in vals), reverse=True)
    return max(0.0, roots[0]-roots[1]-roots[2]-roots[3])

def concurrence_formula(J,Jz,B,b,T):
    eta=math.hypot(J,b)
    Z=2*math.exp(-Jz/(2*T))*math.cosh(B/T)+2*math.exp(Jz/(2*T))*math.cosh(eta/T)
    n=math.exp(Jz/(2*T))*(J/eta)*math.sinh(eta/T)-math.exp(-Jz/(2*T))
    return 2*max(n,0.0)/Z

def threshold(J,Jz,T):
    target=math.exp(-Jz/T)
    if math.sinh(J/T)>=target:
        return 0.0
    lo=J
    hi=max(2*J,1.0)
    f=lambda eta: J*math.sinh(eta/T)/eta-target
    while f(hi)<=0:
        hi*=2
    for _ in range(100):
        mid=(lo+hi)/2
        if f(mid)>0:
            hi=mid
        else:
            lo=mid
    eta=(lo+hi)/2
    return math.sqrt(max(0.0,eta*eta-J*J))

def main():
    formula_checks=0
    for J in (0.7,1.0,1.6):
        for Jz in (0.0,0.4,1.1):
            for B in (0.0,0.8,2.0):
                for b in (0.0,0.35,1.5,5.0):
                    for T in (0.45,1.0,2.2):
                        a=concurrence_direct(J,Jz,B,b,T)
                        c=concurrence_formula(J,Jz,B,b,T)
                        assert abs(a-c)<4e-9,(J,Jz,B,b,T,a,c)
                        formula_checks+=1

    # A regime with a genuine lower activation threshold.
    J=1.0; Jz=0.0; T=2.0
    bs=threshold(J,Jz,T)
    assert bs>0
    status_checks=0
    for B in (0.0,0.8,4.0):
        assert concurrence_formula(J,Jz,B,0.8*bs,T)==0.0
        assert concurrence_formula(J,Jz,B,1.2*bs,T)>0.0
        status_checks+=2

    # Source Figure-4 parameter family: positive at large b.
    source=[]
    for Jz in (0.0,0.4,0.9):
        c=concurrence_formula(1.0,Jz,0.8,5.0,0.6)
        assert c>0.19
        source.append(c)

    # Reciprocal tail.
    tail=[]
    for J,Jz,B,T in [(1.0,0.0,0.8,0.6),(1.2,0.7,0.3,1.1),(0.8,1.0,2.0,0.9)]:
        vals=[]
        for b in (20.0,50.0,100.0):
            vals.append(abs(b)*concurrence_formula(J,Jz,B,b,T)/J)
        assert abs(vals[-1]-1)<8e-4
        assert abs(vals[-1]-1)<abs(vals[0]-1)
        tail.append(vals[-1])

    print("VERIFY_OK")
    print("direct_formula_checks =",formula_checks)
    print("phase_status_checks =",status_checks)
    print("activation_threshold_example =",bs)
    print("source_b5_concurrences =",",".join(f"{x:.12f}" for x in source))
    print("tail_ratios_at_b100 =",",".join(f"{x:.12f}" for x in tail))

if __name__=="__main__":
    main()
