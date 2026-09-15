"""Principal series engine for extended affine Hecke of type G2, equal param q=i."""
from collections import deque
import numpy as np

Q = 1j  # q = i

S1 = ( -1,1,0,1 )  # [[-1,1],[0,1]] action of s1 on (c1,c2)
S2 = ( 1,0,3,-1 )  # [[1,0],[3,-1]]
def mm(A,B):
    a1,b1,c1,d1=A; a2,b2,c2,d2=B
    return (a1*a2+b1*c2, a1*b2+b1*d2, c1*a2+d1*c2, c1*b2+d1*d2)
MID=(1,0,0,1)

def build_W0():
    seen={MID:[]}
    q=deque([MID])
    while q:
        M=q.popleft()
        for i,S in enumerate([S1,S2]):
            N=mm(S,M)
            if N not in seen:
                seen[N]=seen[M]+[i+1]
                q.append(N)
    return seen
SEEN=build_W0()
print("W0 order", len(SEEN))
WORDS = sorted(SEEN.values(), key=lambda w:(len(w),w))
print("lengths:", sorted(len(w) for w in WORDS))
print(WORDS)
MAT2IDX={}
for idx,w in enumerate(WORDS):
    M=MID
    SMAP={1:S1,2:S2}
    for s in w:
        M=mm(SMAP[s],M)
    assert M not in MAT2IDX
    MAT2IDX[M]=idx
def mat_of_word(w):
    M=MID
    SMAP={1:S1,2:S2}
    for s in w:
        M=mm(SMAP[s],M)
    return M
LENS=[len(w) for w in WORDS]
print("maxlen",max(LENS))

def left_mult_by_s(s,widx):
    w=WORDS[widx]
    SMAP={1:S1,2:S2}
    Mw=mat_of_word(w)
    N=mm(SMAP[s],Mw)
    uidx=MAT2IDX[N]
    if LENS[uidx]==LENS[widx]+1:
        return [(1.0+0j,uidx)]
    elif LENS[uidx]==LENS[widx]-1:
        return [(Q-1,widx),(Q,uidx)]
    else:
        raise AssertionError((s,w,LENS[widx],LENS[uidx]))

for i in range(12):
    print(i,WORDS[i],left_mult_by_s(1,i),left_mult_by_s(2,i))

def s1_act(v):
    c1,c2=v; return (-c1+c2,c2)
def s2_act(v):
    c1,c2=v; return (c1,3*c1-c2)
def act_s(s,e):
    return s1_act(e) if s==1 else s2_act(e)

def lp_add(a,b):
    c=dict(a)
    for k,v in b.items():
        c[k]=c.get(k,0)+v
        if abs(c[k])<1e-12: del c[k]
    return c
def lp_mul(a,b):
    c={}
    for k1,v1 in a.items():
        for k2,v2 in b.items():
            k=(k1[0]+k2[0],k1[1]+k2[1])
            c[k]=c.get(k,0)+v1*v2
    return {k:v for k,v in c.items() if abs(v)>1e-12}
def lp_scale(a,s):
    return {k:v*s for k,v in a.items() if abs(v*s)>1e-12}
def mon(e): return {e:1.0+0j}
ONE={(0,0):1.0+0j}

def Qpoly(x,s):
    sx=act_s(s,x)
    if sx==x: return {}
    a=(1,0) if s==1 else (0,1)
    dx=(x[0]-sx[0],x[1]-sx[1])
    k=dx[0] if s==1 else dx[1]
    assert (k*a[0],k*a[1])==dx,(x,sx,dx,k)
    base=(sx[0]+a[0],sx[1]+a[1])
    res={}
    if k>0:
        for j in range(k):
            e=(base[0]+j*a[0],base[1]+j*a[1])
            res[e]=res.get(e,0)+1.0
    else:
        for j in range(-k):
            e_exp=k+1+j
            e=(sx[0]+e_exp*a[0],sx[1]+e_exp*a[1])
            res[e]=res.get(e,0)-1.0
    return {kk:vv+0j for kk,vv in res.items()}

for x in [(1,0),(0,1),(1,1),(2,3),(-1,2),(3,-1)]:
    for s in [1,2]:
        qp=Qpoly(x,s)
        a=(1,0) if s==1 else (0,1)
        mina={(0,0):1.0,(-a[0],-a[1]):-1.0}
        prod=lp_mul(mina,qp)
        expect={x:1.0,act_s(s,x):-1.0} if act_s(s,x)!=x else {}
        keys=set(prod)|set(expect)
        ok=all(abs(prod.get(k,0)-expect.get(k,0))<1e-9 for k in keys)
        if not ok: print("FAIL",x,s)
print("Qpoly ok")

# descent: find s,v with w = s v reduced
def descend(widx):
    w=WORDS[widx]
    if not w: return None
    Mw=mat_of_word(w)
    SMAP={1:S1,2:S2}
    for cand in [1,2]:
        Mv=mm(SMAP[cand],Mw)  # since S^2=1
        if Mv in MAT2IDX and LENS[MAT2IDX[Mv]]==LENS[widx]-1:
            return (cand,MAT2IDX[Mv])
    raise AssertionError(w)

_memo={}
def theta_times_Tw(x,widx):
    key=(x,widx)
    if key in _memo: return _memo[key]
    n=12
    if widx==0:
        r=[{} for _ in range(n)]; r[0]=mon(x); _memo[key]=r; return r
    s,vidx=descend(widx)
    sx=act_s(s,x)
    rec=theta_times_Tw(sx,vidx)
    out=[{} for _ in range(n)]
    for u,poly in enumerate(rec):
        if not poly: continue
        for (c,z) in left_mult_by_s(s,u):
            out[z]=lp_add(out[z],lp_scale(poly,c))
    Qp=Qpoly(x,s)
    if Qp:
        for y,cy in Qp.items():
            rec2=theta_times_Tw(y,vidx)
            for u,poly in enumerate(rec2):
                if not poly: continue
                out[u]=lp_add(out[u],lp_scale(poly,cy*(Q-1)))
    _memo[key]=out
    return out

def eval_poly(poly,t):
    s=0j
    for (e1,e2),c in poly.items():
        s+=c*(t[0]**e1)*(t[1]**e2)
    return s

def principal_series_mats(t):
    n=12
    T1=np.zeros((n,n),dtype=complex); T2=np.zeros((n,n),dtype=complex)
    for w in range(n):
        for c,u in left_mult_by_s(1,w): T1[u,w]+=c
        for c,u in left_mult_by_s(2,w): T2[u,w]+=c
    X1=np.zeros((n,n),dtype=complex); X2=np.zeros((n,n),dtype=complex)
    for w in range(n):
        r1=theta_times_Tw((1,0),w); r2=theta_times_Tw((0,1),w)
        for u in range(n):
            X1[u,w]=eval_poly(r1[u],t); X2[u,w]=eval_poly(r2[u],t)
    return {"T1":T1,"T2":T2,"X1":X1,"X2":X2}

def check_relations(M):
    T1,T2,X1,X2=M["T1"],M["T2"],M["X1"],M["X2"]
    q=Q; e1=np.eye(12)
    r={}
    r["quad1"]=float(np.linalg.norm(T1@T1-(q-1)*T1-q*e1))
    r["quad2"]=float(np.linalg.norm(T2@T2-(q-1)*T2-q*e1))
    A=T1@T2; B=T2@T1
    r["braid"]=float(np.linalg.norm(A@A@A-B@B@B))
    r["Xcomm"]=float(np.linalg.norm(X1@X2-X2@X1))
    try:
        X1inv=np.linalg.inv(X1)
        lhs=T1@X1-X1inv@T1
        rhs=(q-1)*(e1+X1)
        r["bern1"]=float(np.linalg.norm(lhs-rhs))
    except Exception as ex:
        r["bern1"]=str(ex)
    return r

if __name__=="__main__":
    M0=principal_series_mats((2.0+0j,3.0+0j))
    print(check_relations(M0))
