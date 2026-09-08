"""Fast exact W1/W2sq table for 12 fixed pairs (stdlib only).
Primal: exhaustive 8! assignment enumeration (integer). Dual: Hungarian (integer).
Writes certificates.json. No stochastic search, no splitting proof."""
import json, itertools

def manh(a,b): return abs(a[0]-b[0])+abs(a[1]-b[1])

def hungarian(cost):
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
    uu=u[1:]; vv=v[1:]
    assert sum(uu)+sum(vv)==val
    for i in range(n):
        for j in range(n): assert uu[i]+vv[j]<=cost[i][j]
    return val,assign,uu,vv

def brute(cost):
    n=len(cost); best=None; bestp=None
    for perm in itertools.permutations(range(n)):
        s=0
        for i in range(n): s+=cost[i][perm[i]]
        if best is None or s<best: best=s; bestp=list(perm)
    return best,bestp

SUITE=[
 ("P01",4,[(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3)],[(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3)]),
 ("P02",4,[(0,0),(0,0),(0,3),(0,3),(3,0),(3,0),(3,3),(3,3)],[(0,1),(0,2),(1,0),(2,0),(1,3),(2,3),(3,1),(3,2)]),
 ("P03",4,[(0,0),(1,1),(2,2),(3,3),(0,0),(1,1),(2,2),(3,3)],[(0,3),(1,2),(2,1),(3,0),(0,3),(1,2),(2,1),(3,0)]),
 ("P04",4,[(0,0),(0,3),(3,0),(3,3),(0,1),(3,2),(1,0),(2,3)],[(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1)]),
 ("P05",4,[(1,1),(1,1),(0,0),(0,3),(3,0),(3,3),(0,2),(3,2)],[(0,1),(2,1),(0,0),(0,3),(3,0),(3,3),(0,2),(3,2)]),
 ("P06",4,[(0,0),(0,2),(1,1),(1,3),(2,0),(2,2),(3,1),(3,3)],[(0,1),(0,3),(1,0),(1,2),(2,1),(2,3),(3,0),(3,2)]),
 ("P07",5,[(0,0),(0,1),(0,2),(0,3),(1,0),(1,1),(1,2),(1,3)],[(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(2,3)]),
 ("P08",5,[(0,0),(0,0),(0,4),(0,4),(4,0),(4,0),(4,4),(4,4)],[(2,2),(2,2),(2,2),(2,2),(2,2),(2,2),(2,2),(2,2)]),
 ("P09",5,[(2,0),(2,1),(2,2),(2,3),(2,4),(0,2),(4,2),(2,2)],[(0,2),(1,2),(2,2),(3,2),(4,2),(2,0),(2,4),(2,2)]),
 ("P10",5,[(0,0),(1,1),(2,2),(3,3),(4,4),(0,4),(4,0),(2,2)],[(0,4),(1,3),(2,2),(3,1),(4,0),(0,0),(4,4),(2,2)]),
 ("P11",5,[(0,1),(0,2),(0,3),(1,0),(1,4),(4,1),(4,2),(4,3)],[(1,1),(1,2),(1,3),(0,2),(4,2),(3,1),(3,2),(3,3)]),
 ("P12",5,[(0,0),(0,0),(0,0),(0,0),(4,4),(4,4),(4,4),(4,4)],[(0,4),(0,4),(0,4),(0,4),(4,0),(4,0),(4,0),(4,0)]),
]
out=[]
for pid,g,S,T in SUITE:
    C1=[[manh(a,b) for b in T] for a in S]
    C2=[[manh(a,b)**2 for b in T] for a in S]
    b1,p1=brute(C1); b2,p2=brute(C2)
    v1,a1,u1,w1=hungarian(C1); v2,a2,u2,w2=hungarian(C2)
    assert v1==b1 and v2==b2
    # verify claimed optimal perms attain optimum
    assert sum(C1[i][a1[i]] for i in range(8))==b1
    assert sum(C2[i][a2[i]] for i in range(8))==b2
    out.append({"id":pid,"grid":g,"S":S,"T":T,
      "W1_num8":b1,"W1":f"{b1}/8","W1_perm":a1,"W1_u":u1,"W1_v":w1,
      "W2sq_num8":b2,"W2sq":f"{b2}/8","W2_perm":a2,"W2_u":u2,"W2_v":w2})
    print(pid,"W1=%d/8"%b1,"W2sq=%d/8"%b2,"ok",flush=True)
with open("output/artifacts/certificates.json","w") as f:
    json.dump({"pairs":out,
      "convention":"8 tokens of mass 1/8; W1=W1_num8/8, W2sq=W2sq_num8/8; perms/primal plans pi[i,j]=1/8 iff j==perm[i]; (u,v) integer assignment-dual certificates with u[i]+v[j]<=c[i][j], sum(u)+sum(v)=opt"},f,indent=1)
print("wrote certificates.json")
