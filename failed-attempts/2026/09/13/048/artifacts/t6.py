from eisen import *
import math
def k1norm(X,Y,Z,P):
    X3=emul(emul(X,X),X); Y3=emul(emul(Y,Y),Y); Z3=emul(emul(Z,Z),Z)
    return esub(eadd(eadd(X3,emul(P,Y3)),emul(emul(P,P),Z3)),emul((3,0),emul(emul(P,X),emul(Y,Z))))
def transversal(pi):
    N=enorm(pi); q=int(math.isqrt(N))
    if q*q==N: return [(a,b) for a in range(q) for b in range(q)]
    else: return [(a,0) for a in range(N)]
def cube_roots_mod(m,pi):
    mm=emod(m,pi); return [c for c in transversal(pi) if econg(epowmod(c,3,pi),mm,pi)]
def triple_data(pi1,Th,pi3):
    X,Y,Z=Th; N3=enorm(pi3)
    rts=cube_roots_mod(pi1,pi3); out=[]
    for r in rts:
        t=emod(eadd(eadd(X,emul(Y,r)),emul(Z,emul(r,r))),pi3)
        out.append((r,emod(t,pi3)))
    return out
pi1=(1,3); pi2=(1,6); Th=((-6,-6),(-6,-3),(-3,1))
print("N=",k1norm(*Th,pi1))
# pi3 candidates with ALL values equal (defined triple symbol): need thetas(r1) all same nontrivial char
# check norm of theta: must not be divisible by pi3, and theta not in a ramified prime
for s in ["-2+-9w 67","7+-3w 79","-14+-3w 163","-29+0w 841"]:
    pass
# focus: uniform ones
for pi,N in [((-29,0),841),((22,27),619),((31,12),733),((-41,-15),1291),((-14,-39),1171),((-32,-51),1993)]:
    print("=== pi3=",e2str(pi),N)
    print(" sym13=",cubic_symbol(pi1,pi),"sym23=",cubic_symbol(pi2,pi),"sym31=",cubic_symbol(pi,pi1),"sym32=",cubic_symbol(pi,pi2))
    print(" roots of pi1 mod pi3:", [(e2str(r)) for r in cube_roots_mod(pi1,pi)])
    for r,t in triple_data(pi1,Th,pi):
        print("  r=",e2str(r),"Th(r)=",e2str(t),"div?",edivides(pi,t))
