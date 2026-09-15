from fractions import Fraction
import itertools
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
def pw(form,p):
    cur={(0,0,0,0):Fraction(1)}
    for _ in range(p):
        nxt=defaultdict(Fraction)
        for e1,c1 in cur.items():
            for e2,c2 in form.items():
                ne=tuple(e1[k]+e2[k] for k in range(4))
                nxt[ne]+=c1*c2
        cur=dict(nxt)
    return dict(cur)
def lin(a,b,c,dd):
    return {(1,0,0,0):Fraction(a),(0,1,0,0):Fraction(b),(0,0,1,0):Fraction(c),(0,0,0,1):Fraction(dd)}
def add(*Fs):
    r=defaultdict(Fraction)
    for F in Fs:
        for e,c in F.items(): r[e]+=c
    return dict(r)

forms=[lin(1,0,0,0),lin(0,1,0,0),lin(0,0,1,0),lin(0,0,0,1),lin(1,1,1,1),lin(1,2,3,4),lin(1,-1,2,0),lin(0,1,-1,3),lin(2,1,0,1)]
for s in (6,7,8):
    F=add(*[pw(f,6) for f in forms[:s]])
    h=hvec(F,6)
    S=max(h); N=sum(1 for x in h if x==S)
    print(f"s={s} h={h} S={S} N={N}")
    for L in ([1,1,1,1],[1,2,3,5]):
        print("  L",L,[mul_rank(F,6,i,L) for i in range(6)],"need",[min(h[i],h[i+1]) for i in range(6)])
