#!/usr/bin/env python3
"""Independent finite checks for sharp fixed-log-negativity qutrit work frontiers.
Run: python3 verify_frontier.py (requires NumPy). These tests do not replace the proof.
"""
import math
import numpy as np

EPS = 5e-10
ROOT2 = math.sqrt(2.0)
ROOT3 = math.sqrt(3.0)
rng = np.random.default_rng(104729)
assertions = 0

def check(predicate, info):
    global assertions
    if not predicate:
        raise AssertionError(info)
    assertions += 1

def boundaries(s):
    if not 1.0 <= s <= ROOT3 + 2e-14:
        raise ValueError('s out of physical range')
    if s >= ROOT3-1e-12:
        return (0.,0.,ROOT3/3,ROOT3/3,ROOT3/3)
    s = min(s, ROOT3)
    D = math.sqrt(max(0.0, 6.0-2.0*s*s))
    loz = (2*s-D)/6
    if s <= ROOT2:
        hiz = (s-math.sqrt(max(0.,2.-s*s)))/2
    else:
        hiz = (2*s+D)/6
    zstar = (s-math.sqrt(max(0.,4.-s*s))/ROOT3)/2
    def spread(z):
        A = max(0.,2.-s*s+2*s*z-3*z*z)
        return (s-z)*math.sqrt(A)
    biggest = spread(zstar)
    smallest = ((1+s*math.sqrt(max(0.,2.-s*s)))/2 if s <= ROOT2
                else s*D/3-D*D/12)
    return smallest, biggest, loz, hiz, zstar

def q_from_middle(s,z):
    if s >= ROOT3-1e-12:
        return np.full(3, 1/ROOT3)
    A= max(0.,2.-s*s+2*s*z-3*z*z)
    return np.array([(s-z+math.sqrt(A))/2,z,(s-z-math.sqrt(A))/2])

def random_unitary():
    Z=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3))
    Q,R=np.linalg.qr(Z)
    return Q*np.conj(np.diag(R))/np.abs(np.diag(R))

def direct_physical(q):
    p=np.square(q)
    ket=np.zeros((3,3),dtype=complex)
    ket[np.diag_indices(3)]=q
    # Random local basis rotations leave both correlation ergotropy and negativity invariant.
    ket=random_unitary()@ket@random_unitary().T
    psi=ket.reshape(9)
    rho=np.outer(psi,np.conj(psi))
    rhoA=ket@ket.conj().T
    rhoB=ket.T@ket.conj()
    lev=np.array([0.,1.,2.])
    ham=np.kron(np.diag(lev),np.eye(3))+np.kron(np.eye(3),np.diag(lev))
    E=np.vdot(psi,ham@psi).real
    ea=np.trace(rhoA@np.diag(lev)).real
    eb=np.trace(rhoB@np.diag(lev)).real
    passA=np.dot(np.sort(np.linalg.eigvalsh(rhoA))[::-1],lev)
    passB=np.dot(np.sort(np.linalg.eigvalsh(rhoB))[::-1],lev)
    Wg=E-np.linalg.eigvalsh(rho).real[::-1]@np.sort(np.diag(ham))
    Wl=(ea-passA)+(eb-passB)
    partial=rho.reshape(3,3,3,3).transpose(2,1,0,3).reshape(9,9)
    logneg=math.log(np.abs(np.linalg.eigvalsh(partial)).sum())
    return Wg-Wl, logneg

for s in np.linspace(1.,ROOT3,113):
    small,big,zlo,zhi,zstar=boundaries(float(s))
    check(zlo-EPS<=zstar<=zhi+EPS,(s,zlo,zstar,zhi))
    zvals=np.linspace(zlo,zhi,209)
    gap=big-small
    check(gap>=-EPS,(s,gap))
    spreads=[]
    for z in zvals:
        q=q_from_middle(s,z)
        check(np.all(q[:-1]+EPS>=q[1:]) and q[-1]>=-EPS,(s,z,q))
        check(abs(sum(q)-s)<EPS and abs(sum(q*q)-1)<EPS,(s,z,q))
        spread=q[0]*q[0]-q[2]*q[2]
        spreads.append(spread)
        check(small-EPS<=spread<=big+EPS,(s,z,small,spread,big))
    check(abs(min(spreads)-small)<1e-8,(s,min(spreads),small))
    check(max(spreads)<=big+EPS,(s,max(spreads),big))
    check(abs((big - (q_from_middle(s,zstar)[0]**2 - q_from_middle(s,zstar)[2]**2)))<EPS,s)
    for z in (zlo,zstar,zhi):
        q=q_from_middle(s,z)
        directW,N=direct_physical(q)
        check(abs(directW-2*(1-(q[0]*q[0]-q[2]*q[2])))<EPS,(s,z,directW,q))
        check(abs(N-2*math.log(s))<EPS,(s,z,N))

for s in (1.00001,1.001,1.1,1.4,ROOT2,1.5,1.72,ROOT3):
    small,big,zlo,zhi,zstar=boundaries(s)
    if s<ROOT2:
        check(abs(q_from_middle(s,zhi)[-1])<EPS,('rank2',s))
    else:
        q=q_from_middle(s,zhi)
        check(abs(q[0]-q[1])<EPS,('equal largest',s,q))
    if 1<s<ROOT3:
        q=q_from_middle(s,zstar)
        check(np.all(q[:-1]>q[1:]) and q[-1]>0,('unique full rank',s,q))
print('PASS:',assertions,'deterministic finite checks; source formula independent 9x9 checks and negativity matrix checks')
