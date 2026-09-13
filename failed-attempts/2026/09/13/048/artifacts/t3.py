# Redei cube search: for pair (pi1,pi2), look for theta = x + y*t + z*t^2 in O_K1 mod cubes
# where K1=K(t), t^3=pi1, satisfying N(theta) = pi2 * cube (or u*pi2*cube), with unramified conditions.
# Instead of ideal arithmetic in K1, work modulo selected prime ideals: characterize then lift via brute force
# bounded search + norm test up to units/cubes.
from eisen import *
import math

def etransversal(pi):
    """return list of residues mod pi (as pairs)"""
    N=enorm(pi); out=[]
    # Z[w] as Z-module: use fundamental domain: x+y w, x in [0,N-1]?? That gives N^2 reps, too many.
    # Better: use that O_K/(pi) has N elements: enumerate a in 0..N-1 mapped to (a,0) when N prime rational?
    # For split pi (N=p rational prime), (a,0) a=0..p-1 is a full transversal since differences divisible by pi iff p|diff.
    # For inert (pi=(q), N=q^2), transversal is (a,b), a,b in 0..q-1.
    q=int(math.isqrt(N))
    if q*q==N:
        for a in range(q):
            for b in range(q): out.append((a,b))
    else:
        for a in range(N): out.append((a,0))
    # verify size
    assert len(out)==N, (pi,N,len(out))
    return out

def e_unit_orbit(a):
    return [emul(u,a) for u in UNITS]

def is_cube_mod(a,pi):
    v=cubic_symbol(a,pi)
    if v is None: return False
    return v==0

# test: pairs with both split small: brute force theta in box: x,y,z with small coeffs
# N_{K1/K}(x+y t+z t^2) = x^3 + pi1 y^3 + pi1^2 z^3 - 3 pi1 x y z
def relnorm(x,y,z,pi1):
    return eadd(emul((x,0), (x,0)) and emul((x,0),(x,0)) if False else (x,0),(0,0)) # placeholder

# Represent K-elements as (a,b); implement K1 norm directly with coefficient tuples (each in Z[w] as pairs)
def k1norm(X,Y,Z,P):
    # X^3 + P Y^3 + P^2 Z^3 - 3 P X Y Z
    def cc(c): return c
    X3=emul(emul(X,X),X); Y3=emul(emul(Y,Y),Y); Z3=emul(emul(Z,Z),Z)
    t1=X3; t2=emul(P,Y3); t3=emul(emul(P,P),Z3)
    t4=emul((3,0),emul(emul(P,X),emul(Y,Z)))
    return esub(eadd(eadd(t1,t2),t3),t4)

# self-test: N(t)=pi1? X=0,Y=1,Z=0 -> P*1 = P. 
P=(7,0)
assert eeq(k1norm(ZERO,ONE,ZERO,P),P)
# N(t^2)=P^2: X=0,Y=0,Z=1
assert eeq(k1norm(ZERO,ZERO,ONE,P),emul(P,P))
print("k1norm ok")

# pick a concrete pair: smallest split primes: find split primes
primes=enum_primary_primes(2000)
splits=[(pi,N) for pi,N in primes if int(math.isqrt(N))**2!=N]
print("nsplit:",len(splits))
for pi,N in splits[:10]: print(e2str(pi),N,sym0:=cubic_symbol((2,0),pi))
# candidate pairs with mutual symbol 1
cands=[]
for i in range(min(12,len(splits))):
    for j in range(i+1,min(12,len(splits))):
        pi1,n1=splits[i]; pi2,n2=splits[j]
        if enorm(pi1)==enorm(pi2) and (eeq(emul(pi1,econj(pi2)),(n1,0)) or eeq(pi1,pi2)): continue
        s12=cubic_symbol(pi1,pi2); s21=cubic_symbol(pi2,pi1)
        print(e2str(pi1),n1,"vs",e2str(pi2),n2,":",s12,s21)
