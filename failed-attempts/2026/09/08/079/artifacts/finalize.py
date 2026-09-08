"""Integrate P05' (strict splitting) + midpoint triple into certificates; exact phi via LP-free vertex reasoning.
For grid phi: solve max bal.phi s.t. |diff|<=1 on edges by brute-force-free exact LP:
use simple exact simplex implemented carefully here (standard form, Fractions)."""
import json, itertools
from fractions import Fraction

def manh(a,b): return abs(a[0]-b[0])+abs(a[1]-b[1])
N4=[(x,y) for x in range(4) for y in range(4)]
N5=[(x,y) for x in range(5) for y in range(5)]
def adj(N):
    S=set(N); e=[]
    for (x,y) in N:
        for (dx,dy) in ((1,0),(0,1)):
            if (x+dx,y+dy) in S: e.append((N.index((x,y)),N.index((x+dx,y+dy))))
    return e
A4=adj(N4); A5=adj(N5)

def hung(cost):
    n=len(cost); u=[0]*(n+1); v=[0]*(n+1); p=[0]*(n+1); way=[0]*(n+1)
    for i in range(1,n+1):
        p[0]=i; j0=0; minv=[10**18]*(n+1); used=[False]*(n+1)
        while True:
            used[j0]=True; i0=p[j0]; delta=10**18; j1=0
            for j in range(1,n+1):
                if used[j]: continue
                cur=cost[i0-1][j-1]-u[i0]-v[j]
                if cur<minv[j]: minv[j]=cur; way[j]=j0
                if minv[j]<delta: delta=minv[j]; j1=j
            for j in range(n+1):
                if used[j]: u[p[j]]+=delta; v[j]-=delta
                else: minv[j]-=delta
            j0=j1
            if p[j0]==0: break
        while j0:
            j1=way[j0]; p[j0]=p[j1]; j0=j1
    assign=[0]*n
    for j in range(1,n+1): assign[p[j]-1]=j-1
    val=sum(cost[i][assign[i]] for i in range(n))
    return val,assign,[x for x in u[1:]],[x for x in v[1:]]

def max_phi_exact(N,edges,bal):
    """Exact LP: max bal'.phi s.t. |phi_a-phi_b|<=1 via simplex (Fractions), Dantzig pivoting.
    Standard form: phi=a-b (a,b>=0); for each undirected edge: phi_u-phi_v+s1=1, -phi_u+phi_v+s2=1."""
    n=len(N); m=len(edges)
    nv=2*n+2*m; nr=2*m
    A=[[Fraction(0)]*nv for _ in range(nr)]; b=[Fraction(1)]*nr
    for k,(e1,e2) in enumerate(edges):
        A[2*k][e1]+=1; A[2*k][e2]-=1; A[2*k][n+e1]-=1; A[2*k][n+e2]+=1; A[2*k][2*n+2*k]=Fraction(1)
        A[2*k+1][e1]-=1; A[2*k+1][e2]+=1; A[2*k+1][n+e1]+=1; A[2*k+1][n+e2]-=1; A[2*k+1][2*n+2*k+1]=Fraction(1)
    c=[Fraction(0)]*nv
    for i in range(n): c[i]=-Fraction(bal[i]); c[n+i]=Fraction(bal[i])
    basis=[2*n+r for r in range(nr)]
    nonbas=[j for j in range(nv) if j not in basis]
    # Binv
    Binv=[[Fraction(int(r==s)) for s in range(nr)] for r in range(nr)]
    def Avec(j): return [A[r][j] for r in range(nr)]
    for it in range(20000):
        cB=[c[j] for j in basis]
        y=[sum(cB[r]*Binv[r][k] for r in range(nr)) for k in range(nr)]
        enter=None
        for j in nonbas:
            Aj=Avec(j)
            rc=c[j]-sum(y[k]*Aj[k] for k in range(nr))
            if rc<0: enter=j; break
        if enter is None: break
        Ae=Avec(enter)
        dcol=[sum(Binv[r][k]*Ae[k] for k in range(nr)) for r in range(nr)]
        xb=[sum(Binv[r][k]*b[k] for k in range(nr)) for r in range(nr)]
        lr=-1; rat=None
        for r in range(nr):
            if dcol[r]>0:
                q=xb[r]/dcol[r]
                if rat is None or q<rat: rat=q; lr=r
        assert lr>=0, "unbounded?"
        # pivot update of Binv: newBinv*B_new = I; standard row ops
        piv=dcol[lr]
        pro= Binv[lr][:]
        Binv[lr]=[v/piv for v in pro]
        for r in range(nr):
            if r==lr: continue
            f=dcol[r]
            Binv[r]=[Binv[r][s]-f*Binv[lr][s] for s in range(nr)]
        basis[lr]=enter
        nonbas=[j for j in range(nv) if j not in set(basis)]
    cB=[c[j] for j in basis]
    xb=[sum(Binv[r][k]*b[k] for k in range(nr)) for r in range(nr)]
    sol=[Fraction(0)]*nv
    for r in range(nr): sol[basis[r]]=xb[r]
    phi=[sol[i]-sol[n+i] for i in range(n)]
    val=sum(Fraction(bal[i])*phi[i] for i in range(n))
    return phi,val

cert=json.load(open("output/artifacts/certificates.json"))

# add P05' and midpoint rows
EXTRA=[
 ("P05S",4,[(0,0),(0,3),(3,0),(2,0),(0,2),(3,2),(1,1),(1,1)],[(0,0),(0,3),(3,0),(2,0),(0,2),(1,2),(3,3),(3,3)],
  "STRICT-SPLIT extremal: 2/8 at (1,1) vs doubled (3,3); every optimal plan splits (nonsplit gap W1 4/8, W2sq 20/8)"),
 ("M1",4,[(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3)],[(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(3,3)],
  "midpoint axiom: full displacement S->T at speed 2 (W1 16/8, W2sq 32/8)"),
 ("M2",4,[(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3)],[(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3)],
  "midpoint axiom: first half S->MID (W1 8/8, W2sq 8/8)"),
 ("M3",4,[(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3)],[(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2),(3,3)],
  "midpoint axiom: second half MID->T (W1 8/8, W2sq 8/8)"),
]
for pid,g,S,T,desc in EXTRA:
    C1=[[manh(a,b) for b in T] for a in S]
    C2=[[manh(a,b)**2 for b in T] for a in S]
    v1,a1,u1,w1=hung(C1); v2,a2,u2,w2=hung(C2)
    cert["pairs"].append({"id":pid,"grid":g,"S":[list(p) for p in S],"T":[list(p) for p in T],
      "desc":desc,"W1_num8":v1,"W1":"%d/8"%v1,"W1_perm":a1,"W1_u":u1,"W1_v":w1,
      "W2sq_num8":v2,"W2sq":"%d/8"%v2,"W2_perm":a2,"W2_u":u2,"W2_v":w2})
    print(pid,"W1=%d/8"%v1,"W2sq=%d/8"%v2,flush=True)

# exact grid phis for ALL pairs via simplex
phis={}
for p in cert["pairs"]:
    N=N4 if p["grid"]==4 else N5; E=A4 if p["grid"]==4 else A5
    mu=[0]*len(N); nu=[0]*len(N)
    for q in p["S"]: mu[N.index(tuple(q))]+=1
    for q in p["T"]: nu[N.index(tuple(q))]+=1
    bal=[mu[i]-nu[i] for i in range(len(N))]
    phi,val=max_phi_exact(N,E,bal)
    assert val==p["W1_num8"],(p["id"],val,p["W1_num8"])
    for a,b in E: assert abs(phi[a]-phi[b])<=1
    assert all(v.denominator==1 for v in phi),(p["id"],phi)
    phis[p["id"]]=[int(v) for v in phi]
    print(p["id"],"phi val",val,"int ok",flush=True)
json.dump(phis,open("output/artifacts/grid_phis.json","w"),indent=1)
json.dump(cert,open("output/artifacts/certificates.json","w"),indent=1)
print("saved all;",{k:(sum(1 for v in ph if v!=0)) for k,ph in phis.items()})
