from eisen import *
import math

def k1norm(X,Y,Z,P):
    X3=emul(emul(X,X),X); Y3=emul(emul(Y,Y),Y); Z3=emul(emul(Z,Z),Z)
    return esub(eadd(eadd(X3,emul(P,Y3)),emul(emul(P,P),Z3)),emul((3,0),emul(emul(P,X),emul(Y,Z))))

def transversal(pi):
    N=enorm(pi); q=int(math.isqrt(N))
    if q*q==N:
        return [(a,b) for a in range(q) for b in range(q)]
    else:
        return [(a,0) for a in range(N)]

def cube_roots_mod(m,pi):
    N=enorm(pi); out=[]
    for c in transversal(pi):
        if econg(epowmod(c,3,pi),emod(m,pi),pi):
            out.append(emod(c,pi))
    return out

def triple_values(pi1,pi2,Th,pi3):
    # Th=(X,Y,Z); for each r1 root of t^3=pi1 mod pi3, compute (Th(r1))^((N3-1)/3)
    X,Y,Z=Th
    N3=enorm(pi3)
    rts=cube_roots_mod(pi1,pi3)
    vals=[]
    for r in rts:
        t=emod(eadd(eadd(X,emul(Y,r)),emul(Z,emul(r,r))),pi3)
        if edivides(pi3,t):
            vals.append((r,'ZERO-DIVISIBLE'))
            continue
        v=epowmod(t,(N3-1)//3,pi3)
        if econg(v,ONE,pi3): vals.append((r,0))
        elif econg(v,OMEGA,pi3): vals.append((r,1))
        elif econg(v,W2,pi3): vals.append((r,2))
        else: vals.append((r,'BAD'))
    return vals

# use pair pi1=1+3w (7), pi2=1+6w (31), theta from t4
pi1=(1,3); pi2=(1,6)
X=(-6,-6);Y=(-6,-3);Z=(-3,1)
print("N check:",k1norm(X,Y,Z,pi1), "want",pi2)
# list candidate pi3: primary primes with sym 1 vs both
primes=enum_primary_primes(2000)
cands=[]
for pi,N in primes:
    if eeq(pi,pi1) or eeq(pi,pi2): continue
    if enorm(pi)==enorm(pi1) and eeq(emul(pi,econj(pi1)),(enorm(pi1),0)): continue
    if enorm(pi)==enorm(pi2) and eeq(emul(pi,econj(pi2)),(enorm(pi2),0)): continue
    if cubic_symbol(pi1,pi)==0 and cubic_symbol(pi2,pi)==0:
        cands.append((pi,N))
print("ncands:",len(cands))
for pi,N in cands[:40]:
    vals=triple_values(pi1,pi2,(X,Y,Z),pi)
    vs=set(v for _,v in vals)
    print(e2str(pi),N,vals,"NONTRIV" if vs!={0} else "")
