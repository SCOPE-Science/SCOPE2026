from eisen import *
import math, itertools

def k1norm(X,Y,Z,P):
    X3=emul(emul(X,X),X); Y3=emul(emul(Y,Y),Y); Z3=emul(emul(Z,Z),Z)
    t1=X3; t2=emul(P,Y3); t3=emul(emul(P,P),Z3)
    t4=emul((3,0),emul(emul(P,X),emul(Y,Z)))
    return esub(eadd(eadd(t1,t2),t3),t4)

def small_elems(B):
    # Z[w] elements a+bw with |a|,|b|<=B
    for a in range(-B,B+1):
        for b in range(-B,B+1):
            yield (a,b)

def find_theta(pi1,pi2,B):
    """Search theta=X+Yt+Zt^2 with small coeffs s.t. N=pi2 * u * gamma^3?
    First: N == associate(pi2) up to rational? We test N/ pi2 is a cube in K up to unit.
    Since class number 1, N=(beta) principal automatically. Test: N = u * pi2 * eta^3 exactly.
    Approach: compute N, divide by pi2 (must be divisible), quotient must be unit* cube.
    """
    sols=[]
    # precompute small cubes? Instead: quotient q: check q/u is a cube by solving norm? Simple: q/u = eta^3 with eta bounded.
    # Alternate test: for each unit u: q*u^-1 is a cube in Z[w]: check via mod prime + bounded eta search.
    etas=list(small_elems(B))
    cubes={}
    for e in etas:
        c=emul(emul(e,e),e)
        cubes.setdefault(c, e)
    for X in small_elems(B):
        for Y in small_elems(B):
            for Z in small_elems(B):
                if X==ZERO and Y==ZERO and Z==ZERO: continue
                N=k1norm(X,Y,Z,pi1)
                if eeq(N,ZERO): continue
                if not edivides(pi2,N): continue
                q,_=edivmod(N,pi2)
                # q must equal unit * cube
                hit=None
                for u in UNITS:
                    cand=emul(q,u)  # q*u runs units; want cand = cube
                    if cand in cubes:
                        hit=(u,cubes[cand]); break
                if hit:
                    sols.append((X,Y,Z,N,q,hit))
                    return sols
    return sols

# candidates pairs with mutual sym 1:
pairs=[((1,3),(1,6)), ((-2,-3),(-5,-6)), ((4,3),(4,-3))]
# norms: 7 vs 31 etc.
for pi1,pi2 in pairs:
    print("pair",e2str(pi1),e2str(pi2),cubic_symbol(pi1,pi2),cubic_symbol(pi2,pi1))
    s=find_theta(pi1,pi2,6)
    print(" sols B=6:",[(list(map(e2str,(X,Y,Z))),e2str(N),e2str(q),e2str(u),e2str(et)) for X,Y,Z,N,q,(u,et) in s])
