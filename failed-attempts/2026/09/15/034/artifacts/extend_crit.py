# DEPRECATED by audit repair: the global Milnor-length estimate below stabilizes
# at 9 because it counts ALL FOUR affine zeros together (0,4),(3,3),(4,0),(4,4),
# not the local length at one point. Genuine localization is now in
# local_lengths.py (length 2 at (3,3), length 1 at (4,4)). This script is kept
# for the shifted-equation and Jacobian prints only; do not cite its
# "milnor-ish" numbers as local lengths.
# work in char 5. Zeros of (F1,F2) in A^2: found (0,4),(3,3),(4,0),(4,4).
# Torus critical pts: (3,3)=(-2,-2)? i.e. over F5: check which correspond to Smith's:
# over C: (-1,-1)=(4,4) and (xi,xi), xi^2=xi+1. Over F5: xi^2-xi-1=0 disc=5=0 -> xi=3 (double root!).
# So (3,3) is the collision of the two golden-ratio points. (4,4) persists. Check multiplicities/local dims.
# Also rule out zeros at infinity / on x=0 or y=0 (non-torus): (0,4),(4,0) have N=?
P=5
def evpoly(terms,a,b):
    return sum(c*pow(a,i,P)*pow(b,j,P) for (i,j),c in terms.items())%P
N={(0,0):1,(0,1):2,(1,0):2,(0,2):1,(1,1):3,(2,0):1,(1,2):1,(2,1):1}
for pt in [(0,4),(4,0),(3,3),(4,4)]:
    print(pt,"N=",evpoly(N,*pt))
# Check F1,F2 factorization to see local multiplicity at (3,3): shift u=x-3,v=y-3, expand low-degree part.
# Represent F1,F2 as integer polys then shift mod 5.
import itertools
F1={(0,0):4,(0,1):3,(0,2):4,(2,0):1,(2,1):1}
F2={(0,0):4,(1,0):3,(0,2):1,(2,0):4,(1,2):1}
def shift(A,ax,ay):
    # substitute x=u+ax, y=v+ay mod5
    from math import comb
    C={}
    for (i,j),c in A.items():
        for a in range(i+1):
            for b in range(j+1):
                k=(a,b); C[k]=(C.get(k,0)+c*comb(i,a)*pow(ax,i-a,P)*comb(j,b)*pow(ay,j-b,P))%P
    return {k:v for k,v in C.items() if v!=0}
for pt in [(3,3),(4,4)]:
    S1=shift(F1,*pt); S2=shift(F2,*pt)
    print("shifted at",pt,"F1:",sorted(S1.items()),"F2:",sorted(S2.items()))
# Jacobian determinant of (F1,F2) at each torus crit (vanishing => multiple root)
def jac(A,B,a,b):
    # dA/dx etc mod5
    def dx(A):
        C={}
        for (i,j),c in A.items():
            if i>0: C[(i-1,j)]=(C.get((i-1,j),0)+i*c)%P
        return {k:v%P for k,v in C.items() if v%P}
    def dy(A):
        C={}
        for (i,j),c in A.items():
            if j>0: C[(i,j-1)]=(C.get((i,j-1),0)+j*c)%P
        return {k:v%P for k,v in C.items() if v%P}
    def ev(A):
        return sum(c*pow(a,i,P)*pow(b,j,P) for (i,j),c in A.items())%P
    return (ev(dx(F1))*ev(dy(F2))-ev(dx(F2))*ev(dy(F1)))%P
for pt in [(3,3),(4,4)]:
    print("jac(F1,F2) at",pt,"=",jac(F1,F2,*pt))
# Milnor number estimate at (3,3): dim of k[[u,v]]/(shifted F1,F2). Compute via Macaulay-style elimination by brute force monomial basis.
def milnor(S1,S2,deg=8):
    # vector space basis of monomials degree<=deg quotient by ideal, increase deg until stable
    import numpy as np
    mons=[(i,j) for d in range(deg+1) for i in range(d+1) for j in [d-i]]
    idx={m:k for k,m in enumerate(mons)}
    eqs=[]
    for (si,S) in [(0,S1),(0,S2)]:
        pass
    # multiples m*S1, m*S2 with deg<=deg
    rows=[]
    for S in (S1,S2):
        sd=max(i+j for i,j in S)
        for (i,j) in mons:
            # multiply S by x^i y^j, keep if max deg<=deg
            ok=all(i+di+j+dj<=deg for di,dj in S)
            if not ok: continue
            row=[0]*len(mons)
            for (di,dj),c in S.items():
                row[idx[(i+di,j+dj)]]=(row[idx[(i+di,j+dj)]]+c)%P
            rows.append(row)
    # rank over F5
    M=[r[:] for r in rows]
    r=0
    piv=0
    n=len(mons)
    for c in range(n):
        pivc=None
        for k in range(r,len(M)):
            if M[k][c]%P!=0:
                pivc=k;break
        if pivc is None: continue
        M[r],M[pivc]=M[pivc],M[r]
        inv=pow(M[r][c],P-2,P)
        M[r]=[(v*inv)%P for v in M[r]]
        for k in range(len(M)):
            if k!=r and M[k][c]!=0:
                f=M[k][c]
                M[k]=[(M[k][t]-f*M[r][t])%P for t in range(n)]
        r+=1
    return len(mons)-r
for d in [4,6,8,10]:
    print("milnor-ish deg",d, milnor(shift(F1,3,3),shift(F2,3,3),d), milnor(shift(F1,4,4),shift(F2,4,4),d))
