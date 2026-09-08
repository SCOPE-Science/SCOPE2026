"""Exact Gram-spectrum / Gerzon-gap verification for 7 committed equiangular configs in R^4-R^6.
Only stdlib (Fractions) + numpy (float cross-check). All PSD proofs are exact Fraction LDL.
Run: python3 verify_all.py  -> exits 0 with VERIFY_OK iff every line passes.
Committed integer matrices M=kG (k clears denominators); G=v Gram of unit vectors.
"""
from fractions import Fraction
import numpy as np, itertools

def F2M(Mint):
    return [[Fraction(x) for x in row] for row in Mint]

def ldl_exact(B):
    n=len(B); A=[row[:] for row in B]; piv=[]; log=[]
    for k in range(n):
        j=max(range(k,n), key=lambda i: A[i][i])
        log.append(f"stage {k}: maxdiag={A[j][j]} (row {j})")
        if A[j][j]<0: return False,None,piv,log+[f"FAIL neg pivot {A[j][j]}"]
        if A[j][j]==0:
            if any(A[i][j]!=0 for i in range(k,n) if i!=j) or any(A[j][i]!=0 for i in range(k,n) if i!=j):
                return False,None,piv,log+["FAIL zero pivot w/ nonzero offdiag"]
            piv.append(Fraction(0)); log.append(f"stage {k}: pivot 0 (rank skip)"); continue
        if j!=k:
            A[k],A[j]=A[j],A[k]
            for row in A: row[k],row[j]=row[j],row[k]
            log.append(f"stage {k}: swap {k}<->{j}")
        pk=A[k][k]; piv.append(pk)
        for i in range(k+1,n):
            lik=A[i][k]/pk
            for jj in range(k+1,n): A[i][jj]-=lik*A[k][jj]
        for i in range(k+1,n): A[i][k]=Fraction(0); A[k][i]=Fraction(0)
        log.append(f"stage {k}: pivot {pk}")
    return True, sum(1 for p in piv if p>0), piv, log

def frac_det(B):
    n=len(B); A=[row[:] for row in B]; d=Fraction(1)
    for k in range(n):
        j=max(range(k,n), key=lambda i: abs(A[i][k]))
        if A[j][k]==0: return Fraction(0)
        if j!=k: A[k],A[j]=A[j],A[k]; d=-d
        d*=A[k][k]
        for i in range(k+1,n):
            f=A[i][k]/A[k][k]
            for jj in range(k,n): A[i][jj]-=f*A[k][jj]
    return d

def hist(Mint, scale):
    from collections import Counter
    c=Counter()
    n=len(Mint)
    for i in range(n):
        for j in range(i+1,n): c[abs(Fraction(Mint[i][j],scale))]+=1
    return dict(sorted(c.items()))

def check(Mint, scale, d, name, kind):
    M=F2M(Mint); n=len(M)
    ok,rank,piv,log=ldl_exact(M)
    ev=np.linalg.eigvalsh(np.array(Mint,float))
    ger=d*(d+1)//2; gap=ger-n
    assert ok, f"{name} not PSD"
    assert rank<=d, f"{name} rank {rank} > d={d}: not embeddable"
    print(f"== {name} [{kind}] n={n} d={d} rank={rank} scale={scale}")
    print(f"   pivots={[str(p) for p in piv]}")
    print(f"   float eig: {np.round(ev,6).tolist()} Gerzon={ger} gap={gap}")
    print(f"   |.| histogram: {{{', '.join(f'{str(k)}: {v}' for k,v in hist(Mint,scale).items())}}}")
    return {"name":name,"n":n,"d":d,"rank":rank,"pivots":[str(p) for p in piv],
            "float_eig":[round(float(x),6) for x in ev],"gerzon":ger,"gap":gap,
            "histogram":{str(k):v for k,v in hist(Mint,scale).items()}}

R=[]
# C1: R4 6 lines alpha=1/3, M=3G; E=negated pairs {(0,1),(0,2),(0,3),(0,4),(1,4),(2,3)}
E={(0,1),(0,2),(0,3),(0,4),(1,4),(2,3)}
M1=[[3 if i==j else (-1 if ((min(i,j),max(i,j)) in E) else 1) for j in range(6)] for i in range(6)]
R.append(check(M1,3,4,"C1 R4 6-line alpha=1/3 (N(4) max witness)","equi"))
print("   det M1[0:4,0:4] =", frac_det([row[0:4] for row in F2M(M1)[0:4]]), "(rank>=4 cert)")
# C2: R4 regular simplex 5 lines, <vi,vj>=-1/4; M=4G diag 4 offdiag -1
M2=[[4 if i==j else -1 for j in range(5)] for i in range(5)]
R.append(check(M2,4,4,"C2 R4 5-line simplex alpha=1/4","equi"))
# C3: R5 regular simplex 6 lines, <vi,vj>=-1/5; M=5G diag 5 offdiag -1
M3=[[5 if i==j else -1 for j in range(6)] for i in range(6)]
R.append(check(M3,5,5,"C3 R5 6-line simplex alpha=1/5","equi"))
# C4: R5 10-line Petersen alpha=1/3, M=3G
A=np.zeros((10,10))
for i in range(5):
    A[i,(i+1)%5]=A[(i+1)%5,i]=1; A[5+i,5+((i+2)%5)]=A[5+((i+2)%5),5+i]=1; A[i,5+i]=A[5+i,i]=1
S=np.ones((10,10))-np.eye(10)-2*A
M4=[[int(round(3*(1 if i==j else 0)+S[i,j])) for j in range(10)] for i in range(10)]
R.append(check(M4,3,5,"C4 R5 10-line Petersen alpha=1/3 (N(5) max witness)","equi"))
for r in itertools.combinations(range(10),5):
    dd=frac_det([[F2M(M4)[i][j] for j in r] for i in r])
    if dd!=0: print("   rank-5 minor",r,"det =",dd); break
# C5: R6 6-line alpha=1/5 empty-graph (all +): M=5G diag 5 offdiag +1
M5=[[5 if i==j else 1 for j in range(6)] for i in range(6)]
R.append(check(M5,5,6,"C5 R6 6-line alpha=1/5 (ladder base)","equi"))
# C6: R6 16-line Clebsch alpha=1/3, M=3G
gens=[1,2,4,8,15]; A16=np.zeros((16,16))
for x in range(16):
    for g in gens: A16[x,x^g]=1
S16=np.ones((16,16))-np.eye(16)-2*A16
M6=[[int(round(3*(1 if i==j else 0)+S16[i,j])) for j in range(16)] for i in range(16)]
R.append(check(M6,3,6,"C6 R6 16-line Clebsch alpha=1/3 (N_{1/3}(6) max witness)","equi"))
# C7: R4 8-pt two-distance near-miss {|.|}={0,1/2}: two MUBs, G=[[I,H/2],[H/2,I]], M=2G
H=[[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]]
M7=[[0]*8 for _ in range(8)]
for i in range(8):
    for j in range(8):
        if i==j: M7[i][j]=2
        elif i<4 and j<4: M7[i][j]=0
        elif i>=4 and j>=4: M7[i][j]=0
        else: M7[i][j]=H[i if i<4 else j][j-4 if i<4 else i-4]
R.append(check(M7,2,4,"C7 R4 8-pt two-distance near-miss {|.|}={0,1/2} (MUB pair)","two-dist"))

# (e) maximality witnesses
print("MAXIMALITY:")
print("  C1 n=6 = N(4)=6 (van Lint-Seidel/Lemmens-Seidel); rank 4 cert above.")
print("  C4 n=10 = N(5)=10 (Lemmens-Seidel); rank-5 minor det nonzero cert above.")
rb=Fraction(6*(1-Fraction(1,9)),1-Fraction(6,9))
print(f"  C6 n=16 = relative bound d(1-a^2)/(1-d a^2) at d=6,a=1/3: {rb} = 16 (SCOPE023); rank<=6 cert above.")
# (f) exclusion for C1: all 64 bordered B=[[M1,s],[s,3]] PSD ones have rank 5 > 4
MF1=F2M(M1); npsd=nrankok=0
for bits in range(64):
    s=[Fraction(1 if (bits>>i)&1 else -1) for i in range(6)]
    B=[row[:]+[s[i]] for i,row in enumerate(MF1)]; B.append(s[:]+[Fraction(3)])
    ok,r,piv,log=ldl_exact(B)
    if ok:
        npsd+=1
        if r<=4: nrankok+=1; print("UNEXPECTED feasible extension",bits)
print(f"EXCLUSION C1: {npsd}/64 bordered patterns PSD, {nrankok} with rank<=4 -> no 7th 1/3-line in R4 extends C1. PROVED." if nrankok==0 else "EXCLUSION FAILED")
assert nrankok==0
print("VERIFY_OK")
