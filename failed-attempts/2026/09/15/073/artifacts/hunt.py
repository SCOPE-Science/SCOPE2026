from fractions import Fraction
import itertools, random
from collections import defaultdict

def mons(nvars,deg):
    return sorted([e for e in itertools.product(range(deg+1),repeat=nvars) if sum(e)==deg])
def diff_poly(F,a):
    G=dict(F)
    for vi,ee in enumerate(a):
        for _ in range(ee):
            NG=defaultdict(Fraction)
            for e,c in G.items():
                if e[vi]>0:
                    ne=list(e); ne[vi]-=1; ne=tuple(ne)
                    NG[ne]+=c*e[vi]
            G=dict(NG)
    return G
def rank_frac(M):
    if not M or not M[0]: return 0
    R=[row[:] for row in M]; m=len(R); n=len(R[0]); r=0
    for c in range(n):
        piv=None
        for i in range(r,m):
            if R[i][c]!=0: piv=i; break
        if piv is None: continue
        R[r],R[piv]=R[piv],R[r]
        inv=R[r][c]
        for i in range(m):
            if i!=r and R[i][c]!=0:
                f=R[i][c]/inv
                for j in range(c,n): R[i][j]-=f*R[r][j]
        r+=1
    return r
def cat_matrix(F,d,i):
    src=mons(4,i); tgt=mons(4,d-i)
    tindex={b:j for j,b in enumerate(tgt)}
    M=[]
    for a in src:
        G=diff_poly(F,a)
        row=[Fraction(0)]*len(tgt)
        for e,c in G.items():
            if sum(e)==d-i and e in tindex: row[tindex[e]]=c
        M.append(row)
    return src,tgt,M
def hvec(F,d):
    return [rank_frac(cat_matrix(F,d,i)[2]) for i in range(d+1)]
def mul_rank(F,d,i,L):
    if i+1>d: return 0
    src_i=mons(4,i); src_ip1=mons(4,i+1); tgt=mons(4,d-i-1)
    tindex={b:j for j,b in enumerate(tgt)}
    D={b:diff_poly(F,b) for b in src_ip1}
    Mcomp=[]
    for a in src_i:
        row=[Fraction(0)]*len(tgt)
        for j in range(4):
            na=list(a); na[j]+=1; na=tuple(na)
            G=D[na]
            for e,c in G.items():
                if sum(e)==d-i-1 and e in tindex:
                    row[tindex[e]]+=Fraction(L[j])*c
        Mcomp.append(row)
    return rank_frac(Mcomp)
def wlp_status(F,d,L):
    h=hvec(F,d)
    for i in range(d):
        if mul_rank(F,d,i,L)<min(h[i],h[i+1]):
            return False,i
    return True,None

def rand_sparse(d,k,rng):
    M=mons(4,d)
    F=defaultdict(Fraction)
    for e in rng.sample(M,k):
        c=rng.choice([1,-1,2,-2,3])
        F[e]+=Fraction(c)
    return dict(F)

rng=random.Random(12345)
Lgen=[1,2,3,5]
found=[]
for trial in range(300):
    d=5
    k=rng.choice([4,5,6,7,8])
    F=rand_sparse(d,k,rng)
    h=hvec(F,d)
    if max(h)<6: continue
    S=max(h); N=sum(1 for x in h if x==S)
    if N<3: continue
    ok,_=wlp_status(F,d,Lgen)
    print(f"t{trial} k={k} h={h} N={N} wlp_gen={ok} {'***' if not ok else ''}")
    if not ok:
        found.append((F,h))
        break
if not found:
    print("no hit d=5; trying d=6")
    for trial in range(300,600):
        d=6; k=rng.choice([5,6,7,8])
        F=rand_sparse(d,k,rng)
        h=hvec(F,d)
        S=max(h); N=sum(1 for x in h if x==S)
        if N<3: continue
        ok,_=wlp_status(F,d,Lgen)
        print(f"t{trial} k={k} h={h} N={N} wlp_gen={ok} {'***' if not ok else ''}")
        if not ok:
            found.append((F,h)); break
print("FOUND:", len(found))
if found:
    F,h=found[0]
    print(sorted(F.items()))
