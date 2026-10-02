"""Full Xprs evaluation with s-power tracked as integer exponent of s (not s^2).
Redo cleanly: polys dict {(ep,er,es): c}.
K[a][b]: s^2(1-u)(1-v) -> es=2; r(1-u^2)(1-v^2)S -> as before with es=0.
F via G-convolution. Then prefactor row i=1: multiply by s(1-u): B'[0][y] = s*F(1,j) - s*F(0,j) i.e. es+1 shift.
"""
from collections import defaultdict

ONE={(0,0,0):1}; R={(0,1,0):1}; P_={(1,0,0):1}; R2={(0,2,0):1}; S2={(0,0,2):1}
def padd(a,b):
    c=dict(a)
    for k,v in b.items(): c[k]=c.get(k,0)+v
    return {k:v for k,v in c.items() if v!=0}
def pmul(a,b):
    c=defaultdict(int)
    for k1,v1 in a.items():
        for k2,v2 in b.items():
            c[(k1[0]+k2[0],k1[1]+k2[1],k1[2]+k2[2])]+=v1*v2
    return {k:v for k,v in c.items() if v!=0}
def pscale(a,s):
    return {k:v*s for k,v in a.items() if v*s!=0}

D=6
S=[[None]*(D+1) for _ in range(D+1)]
S[0][0]=dict(ONE)
for a in range(D+1):
    for b in range(D+1):
        if a==0 and b==0: continue
        t={}
        if a>0: t=padd(t,pmul(R,S[a-1][b]))
        if b>0: t=padd(t,pmul(R,S[a][b-1]))
        if a>0 and b>0:
            t=padd(t,pscale(pmul(padd(R2,pscale(P_,-1)),S[a-1][b-1]),-1))
        S[a][b]=t
def getS(a,b):
    if a<0 or b<0: return {}
    return S[a][b]
def merge_add(a,b): return padd(a,b)
def merge_sub(a,b): return padd(a,{k:-v for k,v in b.items()})

def K(a,b):
    tot={}
    for (da,db),s in [((0,0),1),((1,0),-1),((0,1),-1),((1,1),1)]:
        if a==da and b==db:
            tot=merge_add(tot, {(0,0,2):s})
    for (da,db),s in [((0,0),1),((2,0),-1),((0,2),-1),((2,2),1)]:
        if a-da>=0 and b-db>=0:
            q=getS(a-da,b-db)
            for (ep,er,es),c in q.items():
                tot[(ep,er+1,es)]=tot.get((ep,er+1,es),0)+s*c
    return {k:v for k,v in tot.items() if v!=0}

def F(a,b):
    tot={}
    for k in range(0, min(a,b+1)+1):
        if b-k-1>=0: tot=merge_add(tot, K(a-k,b-k-1))
        if a-k-1>=0: tot=merge_sub(tot, K(a-k-1,b-k))
    return tot

def smul1u(p0,p1):
    # s*(p0 + p1): factor (s+s u)=s(1+u)
    a={(e[0],e[1],e[2]+1):v for e,v in p0.items()}
    b={(e[0],e[1],e[2]+1):v for e,v in p1.items()}
    return merge_add(a,b)

idx=list(range(1,7)); m=len(idx)
B=[[None]*m for _ in range(m)]
for x,i in enumerate(idx):
    for y,j in enumerate(idx):
        if y>x:
            if x==0:
                B[x][y]=smul1u(F(i,j),F(i-1,j))
            else:
                B[x][y]=F(i,j)

def poly_add(a,b): return padd(a,b)
def poly_mul(a,b): return pmul(a,b)
def pf_poly(B):
    n=len(B)
    def rec(rem):
        if not rem: return {(0,0,0):1}
        i=rem[0]; tot={}
        for k in range(1,len(rem)):
            j=rem[k]
            s=1 if (k-1)%2==0 else -1
            sub=rec(rem[1:k]+rem[k+1:])
            prod=poly_mul(B[i][j],sub)
            if s<0: prod={kk:-vv for kk,vv in prod.items()}
            tot=poly_add(tot,prod)
        return tot
    return rec(list(range(n)))

X=pf_poly(B)
print("terms:",len(X),"total:",sum(X.values()))
from collections import Counter
cs=Counter(); cr=Counter(); cp=Counter()
for (ep,er,es),v in X.items():
    cs[es]+=v; cr[er]+=v; cp[ep]+=v
print("S-marg:",dict(sorted(cs.items())))
print("R-marg:",dict(sorted(cr.items())))
print("P-marg:",dict(sorted(cp.items())))
# negativity check
neg=[(k,v) for k,v in X.items() if v<0]
print("neg terms:",len(neg), neg[:10])
import json
json.dump({f"{a},{b},{c}":v for (a,b,c),v in X.items()}, open("output/artifacts/Xprs7_full.json","w"))
