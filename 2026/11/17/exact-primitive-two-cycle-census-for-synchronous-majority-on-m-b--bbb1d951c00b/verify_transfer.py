"""Exact finite transfer graph certificate, Python 3 standard library only."""
from collections import defaultdict

def bit(a,i): return (a>>i)&1

def flip(a):return ((a&1)<<1)|((a&2)>>1)|((a&4)<<1)|((a&8)>>1)

def majority(a,b,c):return int(a+b+c>=2)

def good(a,b,c):
    for out,inp in ((0,2),(2,0)):
        for row in (0,1):
            if bit(b,out+row)!=majority(bit(a,inp+row),bit(c,inp+row),bit(b,inp+1-row)):
                return False
    return True

G=[[] for _ in range(256)]
for a in range(16):
    for b in range(16):
        for c in range(16):
            if good(a,b,c):G[16*a+b].append(16*b+c)
assert sum(map(len,G))==400
S=lambda x:16*flip(x//16)+flip(x%16)
assert all(S(S(i))==i for i in range(256))
assert all(S(v) in G[S(u)] for u in range(256) for v in G[u])

# Tarjan strongly connected components (all finite possibilities checked).
index=0; stack=[]; on=set(); dfn={}; low={}; parts=[]
def visit(u):
    global index
    dfn[u]=low[u]=index;index+=1;stack.append(u);on.add(u)
    for v in G[u]:
        if v not in dfn:visit(v);low[u]=min(low[u],low[v])
        elif v in on:low[u]=min(low[u],dfn[v])
    if low[u]==dfn[u]:
        p=[]
        while True:
            v=stack.pop();on.remove(v);p.append(v)
            if v==u:break
        parts.append(set(p))
for u in range(256):
    if u not in dfn:visit(u)
cyc=[p for p in parts if len(p)>1 or any(u in G[u] for u in p)]
assert sorted(map(len,cyc))==[1,1,2,8,8,16]
keep=[p for p in cyc if S(next(iter(p))) in p]
assert sorted(map(len,keep))==[2,16]
assert all(S(next(iter(p))) not in p for p in cyc if len(p) in (1,8))

# Characteristic polynomial exact by Newton sums of traces.
def mm(A,B):
    n=len(A); out=[[0]*n for _ in range(n)]
    for i in range(n):
        for k,v in enumerate(A[i]):
            if v:
                for j,w in enumerate(B[k]):out[i][j]+=v*w
    return out

def cp(A):
    n=len(A); power=[[int(i==j) for j in range(n)] for i in range(n)]
    coeff=[1]
    traces=[]
    for k in range(1,n+1):
        power=mm(power,A)
        traces.append(sum(power[i][i] for i in range(n)))
        numer=sum(coeff[k-i]*traces[i-1] for i in range(1,k+1))
        assert numer%k==0
        coeff.append(-numer//k)
    return tuple(coeff)

def mul(p,q):
    res=[0]*(len(p)+len(q)-1)
    for i,a in enumerate(p):
        for j,b in enumerate(q):res[i+j]+=a*b
    return tuple(res)

Acomp={}
for p in keep:
    nodes=sorted(p);ind={u:i for i,u in enumerate(nodes)}
    A=[[int(v in G[u]) for v in nodes] for u in nodes]
    Acomp[len(p)]=(nodes,ind,A)
assert cp(Acomp[2][2])==(1,0,-1)

nodes,ind,A=Acomp[16];seen=set();reps=[];other=[]
for u in nodes:
    if u not in seen:
        seen.add(u);seen.add(S(u));reps.append(u)
        if S(u)!=u:other.append(u)
assert len(reps)==10 and len(other)==6

def block_basis(representatives,sign):
    # (A acting on basis vector e_u + sign*e_S(u)), read coefficient at each representative.
    out=[]
    for u in representatives:
        row=[]
        for v in representatives:
            term=A[ind[u]][ind[v]]
            if S(v)!=v:term+=sign*A[ind[u]][ind[S(v)]]
            row.append(term)
        out.append(row)
    return out
plus=block_basis(reps,1);minus=block_basis(other,-1)
p=(1,-1,2,1,1)
PPLUS=mul(mul(mul((1,-1),(1,1)),(1,-3,1)),mul((1,1,1),p))
PMINUS=mul(mul((1,-1),(1,1)),(1,1,2,-1,1))
assert cp(plus)==PPLUS,(cp(plus),PPLUS)
assert cp(minus)==PMINUS,(cp(minus),PMINUS)

# Fixed points: allowed cyclic binary words with no isolated singleton.
def fixed_by_transfer(n):
    return sum(1 for bits in range(1<<n) if all(((bits>>i)&1)==((bits>>((i-1)%n))&1) or ((bits>>i)&1)==((bits>>((i+1)%n))&1) for i in range(n)))

def Lucas(n):
    a,b=2,1
    for _ in range(n):a,b=b,a+b
    return a

def U(n):
    a,b=2,3
    for _ in range(n):a,b=b,3*b-a
    return a

def B(n):
    v=[4,1,-3,-8]
    for k in range(4,n+1):v.append(v[-1]-2*v[-2]-v[-3]-v[-4])
    return v[n]

def predicted(n):
    hn=Lucas(n)+[2,1,-1,-2,-1,1][n%6]
    pn=U(n)+(2 if n%3==0 else -1)+(2 if n%2==0 else 2*B(n))
    return hn,pn

# A separate 256-state trace calculation, sparse powers, for small n.
def trace_twisted(n):
    total=0
    for init in range(256):
        frontier={init:1}
        for _ in range(n):
            nxt=defaultdict(int)
            for a,c in frontier.items():
                for b in G[a]:nxt[b]+=c
            frontier=nxt
        total+=frontier.get(S(init),0)
    return total

for n in range(3,13):
    h,pn=predicted(n)
    assert fixed_by_transfer(n)==h
    assert trace_twisted(n)==pn,(n,trace_twisted(n),pn)
    assert pn>=h and (pn-h)%2==0
    print(f'n={n} fixed={h} period_le_2={pn} primitive_2_orbits={(pn-h)//2}')
print('TRANSFER_EXACT_OK nodes=256 edges=400 cyclic_SCCs=16,8,8,2 stable_SCCs=16,2 plus_dim=10 minus_dim=6')
