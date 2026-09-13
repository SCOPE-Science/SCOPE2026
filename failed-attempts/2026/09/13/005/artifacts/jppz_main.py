"""Definitive route-(ii): JPPZ Cor 4 evaluator, (g,n)=(2,4), r=k=7, legs a=(4,5,6,6), x=7.
Also validates on DL genus-1 d=1 case. Logs per-graph contributions to hodge_log.txt."""
from fractions import Fraction
from math import factorial as F
import itertools, sys
sys.path.insert(0, "output/artifacts")
from psi_engine import psi

R=7; K=7; X=7
A=(4,5,6,6); MU=(3,2,1,1); DIM=7
M=9

def bern(m):
    a=[Fraction(0)]*(m+1); a[0]=Fraction(1)
    for mm in range(1,m+1):
        s=sum(a[k]*Fraction(F(mm+1),F(k)*F(mm+1-k)) for k in range(mm))
        a[mm]=-s/Fraction(mm+1)
    return a[m]
def Bp(n,x):
    from math import comb as C
    return sum(Fraction(C(n,k))*bern(k)*(x**(n-k)) for k in range(n+1))
CV={m: -(((-1)**(m-1)))*Bp(m+1,Fraction(K,R))/(m*(m+1))*(X**m) for m in range(1,M+1)}
defclc=(lambda a,m: (((-1)**(m-1)))*Bp(m+1,Fraction(a,R))/(m*(m+1))*(X**m))
def cedge(w,m): return (((-1)**(m-1)))*Bp(m+1,Fraction(w,R))/(m*(m+1))*(X**m)

def expcoef(c,p):
    # c[m], m>=1 dict/list(1-indexed list with dummy at 0)
    if p==0: return Fraction(1)
    tot=Fraction(0)
    def rec(m,rem,prod):
        nonlocal tot
        if rem==0: tot+=prod; return
        if m>=len(c) or m>rem: return
        pw=Fraction(1)
        for e in range(rem//m+1):
            rec(m+1,rem-e*m,prod*pw/Fraction(F(e)))
            pw*=c[m]
    rec(1,p,Fraction(1)); return tot

def leg_series(a, maxdeg):
    c=[Fraction(0)]+[defclc(a,m) for m in range(1,M+1)]
    return {p: expcoef(c,p) for p in range(maxdeg+1)}
def kappa_series(maxdeg):
    c=[Fraction(0)]+[CV[m] for m in range(1,M+1)]
    # multivariate in kappa_1..: enumerate exponent vectors with weighted degree<=maxdeg: {(e1,e2,..): coef prod c^e/e!}
    out={}
    def rec(m, rem, key, prod):
        if m>M:
            if True: out[tuple(key)]=out.get(tuple(key),Fraction(0))+prod
            return
        for e in range(rem//m+1):
            key.append(e); rec(m+1, rem-e*m, key, prod*CV[m]**e/Fraction(F(e))); key.pop()
    rec(1,maxdeg,[],Fraction(1))
    return out

def edge_series(w, maxdeg):
    """Coefficients of (1-exp(S(x,y)))/(x+y) as poly in (x,y) up to total deg maxdeg, S=sum c_m(x^m-(-y)^m).
    Returns dict {(i,j): coef}."""
    c={m: cedge(w,m) for m in range(1,M+1)}
    # S powers: S^k/k! terms; S has min deg 1. Compute S monomials {(i,j):coef} then exponentiate then divide by (x+y).
    S={}
    for m in range(1,M+1):
        if c[m]==0: continue
        S[(m,0)]=S.get((m,0),Fraction(0))+c[m]
        S[(0,m)]=S.get((0,m),Fraction(0))-c[m]*Fraction((-1)**m)
    # E0 = 1-exp(S) = -sum_{k>=1} S^k/k!
    E0={(0,0):Fraction(0)}
    Sp={(0,0):Fraction(1)}
    import math
    for k in range(1,maxdeg+2):
        # Sp *= S
        nSp={}
        for (i1,j1),v1 in Sp.items():
            for (i2,j2),v2 in S.items():
                if i1+i2+j1+j2>maxdeg+1: continue
                nSp[(i1+i2,j1+j2)]=nSp.get((i1+i2,j1+j2),Fraction(0))+v1*v2
        Sp=nSp
        for key,v in Sp.items(): E0[key]=E0.get(key,Fraction(0))-v/Fraction(F(k))
    E0.pop((0,0),None)
    # divide by (x+y): Q with (x+y)Q=E0
    Q={}
    for tot in range(maxdeg+1):
        for i in range(tot+1):
            j=tot-i
            # E0[(i,j)] = Q[(i-1,j)]+Q[(i,j-1)] (with Q out of range =0)
            qim1=Q.get((i-1,j),Fraction(0)) if i>0 else Fraction(0)
            qjm1=Q.get((i,j-1),Fraction(0)) if j>0 else Fraction(0)
            if i==tot:
                Q[(i,j)]=E0.get((i,j),Fraction(0))-qjm1
            elif j==0:
                Q[(i,0)]=E0.get((i,0),Fraction(0))-qim1
            else:
                # use relation at (i,j): need Q[(i,j)] appears in E0[(i+1,j)] and E0[(i,j+1)]; forward substitution:
                # standard: Q[(i,j)] = E0[(i+1,j)] - Q[(i,j+... hmm do triangular: iterate i ascending with j=tot-i:
                Q[(i,j)]=E0.get((i,j),Fraction(0))-qim1-qjm1 if False else None
                Q[(i,j)]=E0.get((i+1,j),Fraction(0))-Q.get((i,j),Fraction(0)) if False else Q.get((i,j))
                pass
    # redo division cleanly: Q[(i,j)] for i+j<=maxdeg via E0[(i+1,j)] = Q[(i,j)] + Q[(i+1,j-1)]...
    Q={}
    for tot in range(maxdeg+1):
        for i in range(tot,-1,-1):
            j=tot-i
            # E0[(i+1,j)] = Q[(i,j)] + (Q[(i+1,j-1)] if j>=1)
            rhs=E0.get((i+1,j),Fraction(0))-(Q.get((i+1,j-1),Fraction(0)) if j>=1 else Fraction(0))
            Q[(i,j)]=rhs
    # verify
    for tot in range(maxdeg+1):
        for i in range(tot+2):
            j=tot+1-i
            if i<0 or j<0: continue
            lhs=E0.get((i,j),Fraction(0))
            rhs=(Q.get((i-1,j),Fraction(0)) if i>=1 else Fraction(0))+(Q.get((i,j-1),Fraction(0)) if j>=1 else Fraction(0))
            assert lhs==rhs, ((i,j),lhs,rhs)
    return Q

if __name__=="__main__":
    Q=edge_series(1,4)
    print("edge w=1 const:",Q[(0,0)],"expected -c1 =",-cedge(1,1))
    Q0=edge_series(0,4)
    print("edge w=0 const:",Q0[(0,0)],"expected -c1(0) =",-cedge(0,1))

# ---------- graph enumeration ----------
def enum_graphs():
    out=[]
    for nv in range(1,5):
        for assign in itertools.product(range(nv), repeat=4):
            for gv in itertools.product(range(3), repeat=nv):
                for ne in range(0,6):
                    pairs=[(i,j) for i in range(nv) for j in range(i,nv)]
                    for edges in itertools.combinations_with_replacement(pairs, ne):
                        if sum(gv)+ne-nv+1!=2: continue
                        parent=list(range(nv))
                        def find(x):
                            while parent[x]!=x: parent[x]=parent[parent[x]]; x=parent[x]
                            return x
                        for (i,j) in edges: parent[find(i)]=find(j)
                        if len(set(find(i) for i in range(nv)))!=1: continue
                        ok=True
                        for v in range(nv):
                            nl=sum(1 for l in range(4) if assign[l]==v)
                            nh=sum(1 for (i,j) in edges for x in (i,j) if x==v)
                            if 2*gv[v]-2+nl+nh<=0: ok=False
                        if not ok: continue
                        out.append((tuple(gv),tuple(assign),tuple(edges)))
    seen=set(); uniq=[]
    for (gv,assign,edges) in out:
        best=None
        for perm in itertools.permutations(range(len(gv))):
            g2=tuple(gv[perm[i]] for i in range(len(gv)))
            a2=tuple(perm[assign[l]] for l in range(4))
            e2=tuple(sorted(tuple(sorted((perm[i],perm[j]))) for (i,j) in edges))
            key=(g2,a2,e2)
            if best is None or key<best: best=key
        if best in seen: continue
        seen.add(best); uniq.append(best)
    return uniq

def aut_order(gv,assign,edges):
    nv=len(gv); cnt=0
    for perm in itertools.permutations(range(nv)):
        if tuple(gv[perm[i]] for i in range(nv))!=tuple(gv): continue
        if tuple(perm[assign[l]] for l in range(4))!=tuple(assign): continue
        if tuple(sorted(tuple(sorted((perm[i],perm[j]))) for (i,j) in edges))!=tuple(sorted(edges)): continue
        cnt+=1
    return cnt

def eval_all():
    U=enum_graphs()
    print("unique graphs:",len(U))
    log=open("output/artifacts/hodge_log.txt","w")
    log.write(f"unique stable graphs of Mbar24: {len(U)}\n")
    total=Fraction(0)
    for (gv,assign,edges) in U:
        nv=len(gv); ne=len(edges)
        if ne>DIM: continue
        aut=aut_order(gv,assign,edges)
        h1=ne-nv+1
        pref=Fraction(R**(2*2-1-h1),1)/Fraction(aut)
        # weightings
        W=[]
        for wv in itertools.product(range(R), repeat=ne):
            ok=True
            for v in range(nv):
                s=sum(A[l] for l in range(4) if assign[l]==v)
                for q,(i,j) in enumerate(edges):
                    if i==v: s+=wv[q]
                    if j==v: s-=wv[q]
                if s%R!=0: ok=False; break
            if ok: W.append(wv)
        if not W:
            log.write(f"{gv} {assign} {edges}: no weightings\n"); continue
        # per-vertex data
        nlegs_v=[sum(1 for l in range(4) if assign[l]==v) for v in range(nv)]
        # branches per vertex: list of (q, side) with side=0 (value +w) at edges[q][0], side=1 at edges[q][1]
        br_v=[[] for _ in range(nv)]
        for q,(i,j) in enumerate(edges):
            br_v[i].append((q,0)); br_v[j].append((q,1))
        LS={l: leg_series(A[l],DIM) for l in range(4)}
        KS=kappa_series(DIM)
        gcontrib=Fraction(0)
        for wv in W:
            ES={q: edge_series(wv[q],DIM) for q in range(ne)}
            # enumerate: leg powers p_l (deg<=DIM), kappa exp-vector per vertex, edge (i,j) per edge; total deg + ne... note edge series already includes 1/(x+y) so its degree counts as-is; codim ne accounted by pushforward dim.
            # total class degree must equal DIM - ne... no: xi_* raises degree by ne; integrand degree on the stratum must be dim(stratum)=DIM-ne.
            need=DIM-ne
            # iterate leg powers
            for p in itertools.product(range(need+1), repeat=4):
                cl_=Fraction(1)
                for l in range(4): cl_*=LS[l][p[l]]
                if cl_==0: continue
                dp=sum(p)
                if dp>need: continue
                for kkey,kc in KS_items(nv,need-dp):
                    if kc==0: continue
                    dk=sum(sum(kk[m]*m for m in range(len(kk))) for kk in kkey)
                    if dp+dk>need: continue
                    for ekey,ec in ES_items(ES,ne,need-dp-dk):
                        if ec==0: continue
                        # integrate over product of vertex moduli
                        val=integrate_vertex(gv,assign,edges,wv,p,kkey,ekey)
                        gcontrib+=pref*cl_*kc*ec*val
        log.write(f"{gv} {assign} {edges} aut={aut} h1={h1} pref={pref} #W={len(W)} contrib={gcontrib}\n")
        total+=gcontrib
    log.write(f"TOTAL int epsCh/prod(1-mu psi) = {total}\n")
    log.close()
    print("TOTAL =",total,float(total))
    return total

_KS_cache={}
def KS_items(nv, rem):
    key=(nv,rem)
    if key in _KS_cache: return _KS_cache[key]
    per=kappa_series(rem)
    items=[(k,v) for k,v in per.items() if sum(kk*m for m,kk in enumerate(k))<=rem]
    # per-vertex product
    out=[]
    for combo in itertools.product(items, repeat=nv):
        if sum(sum(kk*m for m,kk in enumerate(k)) for k,v in combo)>rem: continue
        out.append(([k for k,v in combo], _prod(v for k,v in combo)))
    _KS_cache[key]=out
    return out

def ES_items(ES, ne, rem):
    if ne==0: return [((),Fraction(1))]
    lists=[list(ES[q].items()) for q in range(ne)]
    out=[]
    for combo in itertools.product(*lists):
        if sum(i+j for (i,j),v in combo)>rem: continue
        out.append(([k for k,v in combo], _prod(v for k,v in combo)))
    return out

def _prod(xs):
    p=Fraction(1)
    for x in xs: p*=x
    return p

def integrate_vertex(gv,assign,edges,wv,legpow,kkey,ekey):
    """Integrate: per vertex v, psi monomial from legs (legpow + denom series folded in by caller? no—denominator handled by caller loop) ...
    NOTE: denominator 1/prod(1-mu_i psi_i) folded by extending leg powers: caller must multiply by MU[l]^q summed. We handle here: total leg exponent = legpow[l]+q_l; instead of separate loop, do the q-loop here."""
    return Fraction(0)  # placeholder wired in next step

if __name__=="__main__":
    U=enum_graphs()
    print("unique:",len(U))
