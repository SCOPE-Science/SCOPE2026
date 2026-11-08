#!/usr/bin/env python3
"""Independent algebraic and physical-matrix checks of a qubit feedback boundary."""
import math
from fractions import Fraction as Q
import numpy as np

# Exact rational Pythagorean parameterizations: sqrt(1-eta) and
# sqrt(eta), as well as sqrt(b(1-b)), are rational.
count = 0
for m in range(1, 8):
    for n in range(1, 9):
        v=Q(m,n+10)
        s=(1-v*v)/(1+v*v)
        eta=1-s*s
        sqrt_eta=2*v/(1+v*v)
        u=Q(m+1,n+3)
        b=u*u/(1+u*u)
        sqrt_bb=u/(1+u*u)
        assert 0<s<1 and 0<b<1 and 0<eta<1
        k=s*sqrt_eta*sqrt_bb
        z=2*b-1
        for sign in (-1,1):
            den=1+sign*s*z
            p=b*(1+sign*s)/den
            assert 0<p<1
            h=sqrt_eta*sqrt_bb/den
            assert h*h == p*(1-p)
            F=(1-eta)*p+eta*b+sign*2*k*h
            assert F==p
            count+=1
        p=b*(1+s)/(1+s*z)
        h=sqrt_eta*sqrt_bb/(1+s*z)
        derivative=(1-eta)+k*(1-2*p)/h
        assert derivative == s*(1-2*b)
        assert b<p<1
        count+=1

# Independent 4x4 unitary model at resonance for many parameters.
rng=np.random.default_rng(117)
I=np.eye(4,dtype=np.complex128)
physical_count=0
for j in range(450):
    b=float(rng.uniform(.005,.995))
    e=float(rng.uniform(0,1))
    eta=float(rng.uniform(.005,.995))
    tau=math.asin(math.sqrt(eta))
    c=math.cos(tau); z=math.sin(tau)
    # Basis |charger,battery> = |00>,|01>,|10>,|11>.
    U=I.copy()
    U[1,1]=c; U[2,2]=c
    U[1,2]=-1j*z; U[2,1]=-1j*z
    phi=float(rng.uniform(0,2*math.pi))
    a=np.array([math.sqrt(1-b), math.sqrt(b)])
    v=np.array([math.sqrt(1-e), math.sqrt(e)*np.exp(1j*phi)])
    psi=(U@np.kron(a,v)).reshape((2,2))
    p=float(np.sum(np.abs(psi[:,1])**2))
    expected=(1-eta)*e+eta*b+2*math.sqrt(eta*(1-eta)*b*(1-b)*e*(1-e))*(-math.sin(phi))
    assert abs(p-expected) < 3e-14, (p,expected)
    # Equal-conditional-energy measurement: zero diagonalize the
    # traceless Hermitian difference, using a real SU(2) rotation.
    rho=psi@psi.conj().T
    sigma=np.outer(psi[:,1],psi[:,1].conj())
    T=sigma-p*rho
    tx=float(T[0,1].real)
    tz=float((T[0,0]-T[1,1]).real/2)
    theta=math.atan2(-tz,tx)
    basis=np.array([[math.cos(theta/2),math.sin(theta/2)],[-math.sin(theta/2),math.cos(theta/2)]])
    conditional=basis@psi
    for y in conditional:
        weight=float(np.sum(np.abs(y)**2))
        if weight>1e-13:
            assert abs(float(abs(y[1])**2/weight)-p)<2e-12
    physical_count+=1

# Random nonzero detuning: check the formula against an independently
# constructed exact two-qubit Hamiltonian block.
for j in range(250):
    b=float(rng.uniform(.01,.99))
    e=float(rng.uniform(.01,.99))
    g=float(rng.uniform(.1,2))
    Delta=float(rng.uniform(-2,2))
    tau=float(rng.uniform(.1,2))
    Omega=math.hypot(g,Delta/2)
    c=math.cos(Omega*tau)
    sn=math.sin(Omega*tau)
    zz=np.zeros((4,4),dtype=np.complex128)
    zz[0,0]=1
    zz[3,3]=np.exp(-1j*Delta*tau)
    block=np.array([[Delta/2,g],[g,-Delta/2]],dtype=np.complex128)
    zz[1:3,1:3]=np.exp(-1j*Delta*tau/2)*(c*np.eye(2)-1j*sn/Omega*block)
    phi=float(rng.uniform(0,2*math.pi))
    psi=(zz@np.kron([math.sqrt(1-b),math.sqrt(b)],
                       [math.sqrt(1-e),math.sqrt(e)*np.exp(1j*phi)])).reshape(2,2)
    excitation=float(np.sum(abs(psi[:,1])**2))
    eta=(g/Omega*sn)**2
    prediction=(1-eta)*e+eta*b+2*g/Omega*sn*math.sqrt(b*(1-b)*e*(1-e))*(Delta/(2*Omega)*sn*math.cos(phi)-c*math.sin(phi))
    assert abs(excitation-prediction)<1e-12, (excitation,prediction)

# Confirm a finite exact plateau by the admissible clipping policy.
b=0.8; eta=0.5
s=math.sqrt(1-eta)
pplus=b*(1+s)/(1+s*(2*b-1))
k=math.sqrt(eta*(1-eta)*b*(1-b))
F=lambda e:(1-eta)*e+eta*b+2*k*math.sqrt(max(0,e*(1-e)))
e=0.0
path=[]
for i in range(20):
    high=F(e)
    e=min(pplus,high)
    path.append(e)
    if e==pplus:break
assert abs(path[-1]-pplus)<1e-14 and len(path)==3,(pplus,path)

# Below/at threshold a one-step target from below is impossible;
# monitor strict convergence and the critical quadratic coefficient.
for b in (.2,.5):
    eta=.5;s=math.sqrt(1-eta)
    target=b*(1+s)/(1+s*(2*b-1))
    k=math.sqrt(eta*(1-eta)*b*(1-b))
    F=lambda e:(1-eta)*e+eta*b+2*k*math.sqrt(max(0,e*(1-e)))
    e=0
    for i in range(15):
        e2=F(e)
        assert e2 > e - 1e-14 and e2 < target + 1e-14
        if target-e2 < 1e-13:
            e=e2
            break
        e=e2
    assert abs(e-target)<.002
print(f'PASS: {count} exact rational identities, {physical_count} physical-unitary/measurement checks, 250 detuned-unitary checks, three-step plateau and subcritical trajectories')
