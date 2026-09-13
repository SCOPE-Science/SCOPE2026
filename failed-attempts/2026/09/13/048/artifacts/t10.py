# Key realization: my "theta" with N=pi2*1^3 is NOT in O_K1 necessarily integral? coeffs are in Z[w] so yes integral.
# But the Galois-equivariance failure + non-exact division suggests arithmetic error: Q should have N(Q)=1 since
# N(sigma Th)=sigma(N(Th))=N(Th) (N in K fixed by sigma). N(Q)=N(S)/N(Th)=1. But computed N(Q)=79+9w != 1.
# So the rounded quotient is NOT the true quotient: S/Th in K1 has non-integral coefficients (denominator pi2).
# Right: Q = Qnum/N with Qnum=S^2 S1, N=pi2: need exact divisibility by pi2 in Z[w]; remainders nonzero mean Q not integral.
# That's FINE: Q in K1, allow fractional. The Galois question is whether Q is a cube in K1 (fractional allowed).
# Multiply through: is Qnum * pi2^2... hmm: Q = Qnum/pi2. Q = C^3 ? with C in K1 (fractional).
# Clear denominators: write C = Gamma/pi2^k? Standard: Q cube in K1 iff Qnum*pi2 ( = Q*pi2^2) is ... let me think:
# Q = Qnum/pi2. If Q=C^3, N(Q)=1 so N(C)^3=1, N(C)=unit. Qnum = pi2*C^3. Alternatively check Qnum*pi2^2 = (pi2*C)^3/pi2 ... 
# Simplest: Q is a cube in K1 iff Qnum*pi2^2 is a cube in O_K1 up to...: Q*pi2^3/... Q = Qnum/pi2; pi2 = N(Th).
# Q*C^3... Let D = pi2*C: D^3 = pi2^3 Q = pi2^2 Qnum. So: Q cube in K1 <=> pi2^2*Qnum is a cube in K1 (then C=D/pi2).
# And D can be taken integral if Qnum integral (D^3 integral => D integral since O_K1 integrally closed... K1 is a
# field, O_K1 = integral closure; D^3 in O_K1 => D in O_K1). So test: is pi2^2*Qnum a cube in O_K1?
# Even simpler sufficient approach: search MANY thetas (all small solutions of N=pi2*unit*cube) and test the
# equivariance condition via the exact cube test with denominator clearing.
from eisen import *
def kmul(A,B,P):
    X1,Y1,Z1=A; X2,Y2,Z2=B
    c0=eadd(emul(X1,X2),emul(P,eadd(emul(Y1,Z2),emul(Z1,Y2))))
    c1=eadd(eadd(emul(X1,Y2),emul(Y1,X2)),emul(emul(P,Z1),Z2))
    c2=eadd(eadd(emul(X1,Z2),emul(Z1,X2)),emul(Y1,Y2))
    return (c0,c1,c2)
def ksigma(A): return (A[0],emul(OMEGA,A[1]),emul(W2,A[2]))
def knorm(A,P):
    X,Y,Z=A
    X3=emul(emul(X,X),X); Y3=emul(emul(Y,Y),Y); Z3=emul(emul(Z,Z),Z)
    return esub(eadd(eadd(X3,emul(P,Y3)),emul(emul(P,P),Z3)),emul((3,0),emul(emul(P,X),emul(Y,Z))))
def kpow(A,n,P):
    R=((1,0),(0,0),(0,0))
    while n>0:
        if n&1: R=kmul(R,A,P)
        A=kmul(A,A,P); n>>=1
    return R
def kscale(s,A): return (emul(s,A[0]),emul(s,A[1]),emul(s,A[2]))

def is_cube_in_O(M,P,B):
    """Is M in O_K1 a cube of an integral element with coeffs in box?"""
    rng=range(-B,B+1)
    for a in rng:
     for b in rng:
      for c in rng:
       for d in rng:
        for e in rng:
         for f in rng:
            E=((a,b),(c,d),(e,f))
            if kpow(E,3,P)==M: return E
    return None

def galois_cocycle_cube_test(Th,P,B):
    """Return C with C^3 = sigma(Th)/Th (as fractional OK) or None. Method: D^3 = P2^2 * S^2*S1."""
    S=ksigma(Th); S1=ksigma(S)
    Qnum=kmul(kmul(S,S,P),S1,P)
    N=knorm(Th,P)
    M=kscale(emul(N,N),Qnum)  # N^2 * Qnum; D^3 = M for D=N*C... check: D=N*C => D^3=N^3 Q=N^2 Qnum. yes
    D=is_cube_in_O(M,P,B)
    return D, M

pi1=(1,3); Th=((-6,-6),(-6,-3),(-3,1))
D,M=galois_cocycle_cube_test(Th,pi1,3)
print("M=",list(map(e2str,M)))
print("D=",None if D is None else list(map(e2str,D)))
