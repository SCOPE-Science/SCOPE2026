from eisen import *
import math
# Why do mixed (0,1,2) cases occur? Because Th(r) depends on choice of r1 | pi3 in K1.
# Per theory, the triple symbol should be read at the distinguished prime ABOVE pi3 determined by the
# Heisenberg extension splitting data... Actually for pi3 splitting completely in K1=K(pi1^{1/3}) (which holds iff
# (pi1/pi3)=1), pi3 splits into 3 primes in K1 (since pi3 != pi1, unramified). The Redei extension is unramified at
# pi3 iff theta is a local cube at each prime above pi3; the triple symbol measures Frobenius in Gal(R/K1)~C3
# at the chosen prime r1. Different r1 give different values CONJUGATE under Gal(K1/K)?? Let's examine:
# values should differ by the action: triple symbol is well-defined only when theta can be chosen s.t. R/K1
# unramified at pi3? Recall Redei: [p1,p2,p3]= Art_{R/K1}(P3)(cuberoot(theta))/cuberoot(theta) where P3 is a prime
# above p3 chosen with extra condition. Hmm.
#
# Alternative classical viewpoint (Redei triple symbol for Q): the symbol is symmetric-ish and well defined
# because the local Artin values at different primes above p3 coincide when the extension is unramified there.
# If R/K1 is RAMIFIED at some prime above pi3, values differ. So the correct pi3 must be one where theta is a
# LOCAL CUBE at every prime above pi3, i.e. Th(r) is a cube mod pi3 for the corresponding r? But our Th(r) has
# char 1 or 2 = NOT a cube. So for uniform-nontrivial cases, theta is NOT a local cube => R/K1 ramified at pi3?
# That contradicts the standard requirement that R/K be unramified outside pi1,pi2.
#
# Wait: for the Q-Redei symbol, R/Q(sqrt(p1),sqrt(p2))... the condition for [p1,p2,p3] to be defined includes
# p3 splitting in Q(sqrt p1, sqrt p2) etc. And the value is defined via Frobenius of a prime above p3 that is
# chosen to have degree 1. If values at different primes differ, the symbol would be ambiguous; classical theory
# shows they agree when defined.
#
# Let me reconsider: maybe theta must ALSO satisfy congruence conditions at ramified primes (Redei's
# "minimally ramified" conditions), and different theta choices (mod cubes) give different extensions; only the
# right one is unramified at pi3. So our found theta (minimal norm solution) may need adjustment by unit/cube
# multiples to achieve the unramified condition. Actually the obstruction: theta defined only mod cubes; the
# extension R=K1(cuberoot theta) is well-defined independent of representative. So ramification at pi3 is
# intrinsic. For pi3 with uniform NONTRIVIAL value, R/K1 IS ramified at pi3 (residue char nontriv => totally
# ramified Artin?). Hmm, that gives ramification at pi3, violating "ramification exactly at pi1,pi2".
#
# Hold on: for Kummer C3 extension R/K1 given by theta, prime P|pi3 (unramified, degree 1) splits iff theta mod P
# is a cube, is inert iff non-cube. If inert, Frobenius = nontrivial element of Gal(R/K1). The triple symbol
# [pi1,pi2,pi3] IS that Frobenius element! So nontrivial value = inert = fine. It does NOT mean ramified.
# Ramified would be theta = 0 mod P. Since our Th(r) != 0 mod pi3, R/K1 is UNRAMIFIED at pi3, just inert.
# Different P's (the 3 primes above pi3) may have different Frobenius — but they are conjugate primes; their
# Frobenius elements are conjugate in Gal(R/K). Since Gal(R/K1) is central?? in Heisenberg group, conjugates
# are equal! So all three primes have the SAME Frobenius. Hence uniform value = well-defined symbol; mixed
# values indicate... hmm, mixed values can't happen for a Galois extension? Unless R/K is not Galois over K?
# R=K1(cuberoot theta) with theta in K1: is R/K Galois? Gal closure needs Galois action on theta. Since
# K1/K is Galois (contains roots of unity), and theta... R/K Galois iff sigma(theta)/theta is a cube for all
# sigma in Gal(K1/K). Our theta may fail this! Then R/K isn't Galois and values legitimately differ.
#
# So the task: find theta with N=pi2*cube AND Galois-equivariance (sigma(theta) = theta * cube up to...).
# Standard Redei construction: theta = Norm_{K1}^{?}... Actually Amano's construction: theta in K1 with
# N(theta)=pi2 and theta = 1 mod ... plus the condition that R/K is Galois comes automatically from
# the norm condition?? Let's verify computationally: compute sigma(theta)/theta and test if cube in K1.
# Need arithmetic in K1 = K[t]/(t^3-pi1): elements as triples; sigma: t -> w*t.

from eisen import *
def kadd(A,B): return (eadd(A[0],B[0]),eadd(A[1],B[1]),eadd(A[2],B[2]))
def kmul(A,B,P):
    X1,Y1,Z1=A; X2,Y2,Z2=B
    # (X1+Y1 t+Z1 t^2)(X2+Y2 t+Z2 t^2), t^3=P
    c0=eadd(emul(X1,X2),emul(emul(P,eadd(emul(Y1,Z2),emul(Z1,Y2))),(1,0)))
    c1=eadd(eadd(emul(X1,Y2),emul(Y1,X2)),emul(emul(P,Z1),Z2))
    c2=eadd(eadd(emul(X1,Z2),emul(Z1,X2)),emul(Y1,Y2))
    return (c0,c1,c2)
def kpow(A,n,P):
    R=((1,0),(0,0),(0,0))
    while n>0:
        if n&1: R=kmul(R,A,P)
        A=kmul(A,A,P); n>>=1
    return R
def ksigma(A):
    # t -> w t: (X, Y, Z) -> (X, wY, w^2 Z)
    return (A[0],emul(OMEGA,A[1]),emul(W2,A[2]))
def knorm(A,P):
    X,Y,Z=A
    X3=emul(emul(X,X),X); Y3=emul(emul(Y,Y),Y); Z3=emul(emul(Z,Z),Z)
    return esub(eadd(eadd(X3,emul(P,Y3)),emul(emul(P,P),Z3)),emul((3,0),emul(emul(P,X),emul(Y,Z))))
def kdivmod_bruteforce(A,B,P,Bound):
    # solve A = Q*B with Q coeffs bounded: linear algebra over Z? Use norm trick: Q = A*B1*B2/N(B) where B1,B2 conjugates
    B1=ksigma(B); B2=ksigma(B1)
    N=knorm(B,P)
    # N in K; Q_num = A*B1*B2 in K1, Q = Q_num/N
    Qn=kmul(kmul(A,B1,P),B2,P)
    Q=[]
    for c in Qn:
        q,r=edivmod(c,N)
        if not eeq(r,ZERO): return None
        Q.append(q)
    return tuple(Q)

pi1=(1,3); pi2=(1,6); Th=((-6,-6),(-6,-3),(-3,1))
print("N(Th)=",knorm(Th,pi1))
S=ksigma(Th)
print("sigma(Th)=",list(map(e2str,S)))
# compute Q = sigma(Th)/Th in K1
Q=kdivmod_bruteforce(S,Th,pi1,6)
print("Q=sigma(Th)/Th:", None if Q is None else list(map(e2str,Q)))
# Is Q a cube in K1? search bounded eta with eta^3=Q (up to unit)
def find_cuberoot(Q,P,B):
    for a in range(-B,B+1):
        for b in range(-B,B+1):
            for c in range(-B,B+1):
                for d in range(-B,B+1):
                    for e in range(-B,B+1):
                        for f in range(-B,B+1):
                            E=((a,b),(c,d),(e,f))
                            if kpow(E,3,P)==Q: return E
    return None
print("searching cuberoot of Q, B=2...")
R=find_cuberoot(Q,pi1,2)
print("cuberoot:",None if R is None else list(map(e2str,R)))
