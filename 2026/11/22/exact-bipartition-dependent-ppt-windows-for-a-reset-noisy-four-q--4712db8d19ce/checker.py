#!/usr/bin/env python3
"""Reproducible exact and finite checks for the four-qubit Dicke resetting theorem.
Requires Python 3 and SymPy. No downloaded data is needed.
"""
import sympy as sp

r = sp.symbols('r', positive=True)
indices = (3, 5, 6, 9, 10, 12)
rho0 = sp.zeros(16)
for i in indices:
    for j in indices:
        rho0[i, j] = sp.Rational(1, 6)

def replace_bit(i, k, b):
    return i & ~(1 << (3-k)) | (b << (3-k))

def local_channel(A, lam, k):
    out = sp.zeros(16)
    mask = 1 << (3-k)
    for i in range(16):
        for j in range(16):
            val = lam * A[i, j]
            if ((i ^ j) & mask) == 0:
                val += (1-lam)*sum(A[replace_bit(i,k,b), replace_bit(j,k,b)] for b in (0,1))/2
            out[i,j] = val
    return out

def pt(A, subsystem):
    B = sp.zeros(16)
    for i in range(16):
        for j in range(16):
            a,b=i,j
            for k in subsystem:
                bit=1 << (3-k)
                if ((a ^ b) & bit):
                    a ^= bit
                    b ^= bit
            B[i,j]=A[a,b]
    return B

# Calculate polynomial coefficients by exact interpolation of the full local channel.
nodes = [sp.Rational(j,4) for j in range(5)]
mats=[]
for lam in nodes:
    M = rho0
    for k in range(4):
        M = local_channel(M, lam, k)
    mats.append(M)
coeffs=[sp.zeros(16) for _ in range(5)]
z = sp.symbols('z')
for lam,M in zip(nodes,mats):
    poly=sp.Poly(sp.prod((z-t)/(lam-t) for t in nodes if t!=lam),z)
    for power in range(5):
        coeffs[power] += poly.nth(power)*M
stationary=sp.simplify(sum(((r/(r+j))*coeffs[j] for j in range(5)),sp.zeros(16)))
assert sp.simplify(stationary.trace()-1)==0,stationary.trace()
assert sp.simplify(stationary-stationary.T)==sp.zeros(16)
# Independent generator stationarity equation, depolarization rate gamma=1.
L = sum((local_channel(stationary,0,k)-stationary for k in range(4)),sp.zeros(16))
assert sp.simplify(L+r*(rho0-stationary))==sp.zeros(16)

Q=(r+2)*(r+4)
a=sp.sqrt(9*r*r+60*r+112)
b=sp.sqrt(3*r*r+20*r+44)
sp1=[((r+3)/(6*Q),4),((3*r*r+10*r+6-r*a)/(12*Q),2),((3*r*r+10*r+6+r*a)/(12*Q),2),((1-2*r)/(4*(r+4)),1),(1/(4*(r+4)),4),((6*r*r+23*r+6)/(12*Q),1),((6-r)/(12*Q),2)]
sp2=[(1/(2*Q),1),((1-r)*(r+3)/(6*Q),1),((2*r+3)/(6*Q),2),((5*r*r+14*r+6-sp.sqrt(3)*r*b)/(12*Q),1),((5*r*r+14*r+6+sp.sqrt(3)*r*b)/(12*Q),1),((4*r*r+17*r+6)/(12*Q),2),((6-7*r-4*r*r)/(12*Q),2),((r+6)/(12*Q),4),((r+1)*(r+3)/(6*Q),2)]
assert sum(m for _,m in sp1)==16 and sum(m for _,m in sp2)==16
# Rational threshold and algebraic positivity checks.
assert sp.simplify((3*r*r+10*r+6)**2-r*r*(9*r*r+60*r+112)-12*(2*r*r+10*r+3))==0
assert sp.simplify((5*r*r+14*r+6)**2-3*r*r*(3*r*r+20*r+44)-4*(4*r**4+20*r**3+31*r*r+42*r+9))==0

total=0
for rat in [sp.Rational(1,10),sp.Rational(49,100),sp.Rational(1,2),sp.Rational(55,100),sp.Rational(63,100),sp.Rational(64,100),sp.Rational(3,4),sp.Rational(1),sp.Rational(11,10),sp.Rational(5),sp.Rational(6),sp.Rational(7),sp.Rational(20)]:
    R=stationary.subs(r,rat)
    for subs,spec in [((0,),sp1),((0,1),sp2)]:
        vals=sorted([float(v.subs(r,rat).evalf(16)) for v,m in spec for _ in range(m)])
        import numpy as np
        got=sorted(np.linalg.eigvalsh(np.array(pt(R,subs),dtype=float)).tolist())
        assert max(abs(a-b) for a,b in zip(vals,got))<1e-11,(rat,subs)
        total+=16
    eig=np.linalg.eigvalsh(np.array(R,dtype=float))
    assert min(eig)>0
    total+=1
print('PASS: 4x4 depolarizing interpolation, stationary generator, two full PT spectra, positive state; component checks:',total)

# Fully symbolic characteristic-polynomial certificates in each exact support block.
t=sp.symbols('t')
D=12*Q
Epair=t*t-t*(3*r*r+10*r+6)/(6*Q)+(2*r*r+10*r+3)/(12*Q*Q)
Fpair=t*t-t*(5*r*r+14*r+6)/(6*Q)+(4*r**4+20*r**3+31*r*r+42*r+9)/(36*Q*Q)
bs1={
    (0,9,10,12): (t-(r+3)/(6*Q))**2*Epair,
    (3,5,6,15): (t-(r+3)/(6*Q))**2*Epair,
    (1,2,4,11,13,14):(t-(1-2*r)/(4*(r+4)))*(t-1/(4*(r+4)))**2*(t-(6*r*r+23*r+6)/(12*Q))*(t-(6-r)/(12*Q))**2,
    (7,):t-1/(4*(r+4)),(8,):t-1/(4*(r+4))}
bs2={
    (0,5,6,9,10,15): (t-1/(2*Q))*(t-(1-r)*(r+3)/(6*Q))*(t-(2*r+3)/(6*Q))**2*Fpair,
    (1,2,7,11): (t-(4*r*r+17*r+6)/(12*Q))*(t-(6-7*r-4*r*r)/(12*Q))*(t-(r+6)/(12*Q))**2,
    (4,8,13,14): (t-(4*r*r+17*r+6)/(12*Q))*(t-(6-7*r-4*r*r)/(12*Q))*(t-(r+6)/(12*Q))**2,
    (3,):t-(r+1)*(r+3)/(6*Q),(12,):t-(r+1)*(r+3)/(6*Q)}
for subs,byblock in (((0,),bs1),((0,1),bs2)):
    A=pt(stationary,subs)
    for b,expected in byblock.items():
        B=A.extract(list(b),list(b))
        exact=B.charpoly(t).as_expr()
        assert sp.cancel(exact-expected)==0,(subs,b)
        # Confirm no off-block couplings so the factorization gives the full spectrum.
        for i in b:
            for j in set(range(16))-set(b):
                assert A[i,j]==0,(subs,b,i,j)
        print('symbolic characteristic block passed',subs,b)
print('PASS: all exact partial-transpose characteristic polynomials')
