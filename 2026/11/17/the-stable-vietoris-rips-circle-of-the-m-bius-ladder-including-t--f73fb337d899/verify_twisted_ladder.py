"""Independent finite checks for graph-metric Rips complexes of Mobius ladders.

Only Python standard library is needed. Finite checks support, but do not
replace, the all-parameter covering-space proof in RESULT.md.
"""
from collections import deque
from itertools import combinations

def graph(n):
    size=2*n
    adj=[set() for _ in range(size)]
    for x in range(size):
        for y in ((x-1)%size,(x+1)%size,(x+n)%size):
            adj[x].add(y);adj[y].add(x)
    return adj

def distances(adj):
    out=[]
    for start in range(len(adj)):
        d={start:0};q=deque([start])
        while q:
            a=q.popleft()
            for b in adj[a]:
                if b not in d:d[b]=d[a]+1;q.append(b)
        out.append([d[j] for j in range(len(adj))])
    return out

def coordinates(n,x):
    return (x%n, x//n)

def stripdist(x,y):
    return abs(x[0]-y[0])+abs(x[1]-y[1])

def tau(x,n,k):
    return (x[0]+k*n,(x[1]+k)%2)

def unique_lift(x,y,n,r):
    choices=[tau(y,n,k) for k in range(-3,4) if stripdist(x,tau(y,n,k))<=r]
    assert len(choices)==1,(n,r,x,y,choices)
    return choices[0]

def clique_euler(d,r):
    N=len(d)
    compat=[sum(1<<j for j in range(N) if j>i and d[i][j]<=r) for i in range(N)]
    totals={}
    def recur(s, cand, size):
        if size: totals[size]=totals.get(size,0)+1
        while cand:
            bit=cand&-cand; i=bit.bit_length()-1; cand-=bit
            recur(s|bit,cand&compat[i],size+1)
    recur(0,(1<<N)-1,0)
    # reduced Euler characteristic = sum_{nonempty simplices} (-1)^dim - 1
    return sum((-1)**(k-1)*count for k,count in totals.items())-1,totals

def run_case(n,r,compute_euler=True):
    assert r>=2 and n>=3*r
    adj=graph(n);d=distances(adj);N=len(adj)
    for x in range(N):
        for y in range(N):
            a,b=coordinates(n,x),coordinates(n,y)
            cover_d=min(stripdist(a,tau(b,n,k)) for k in range(-3,4))
            assert d[x][y]==cover_d,(n,r,x,y,d[x][y],cover_d)
    edges=0; triangles=0
    for x in range(N):
        for y in range(x+1,N):
            if d[x][y]>r:continue
            edges+=1
            px=coordinates(n,x);ly=unique_lift(px,coordinates(n,y),n,r)
            assert stripdist(px,ly)<=r
    for x,y,z in combinations(range(N),3):
        if not (d[x][y]<=r and d[y][z]<=r and d[z][x]<=r):continue
        triangles+=1
        px=coordinates(n,x)
        ly=unique_lift(px,coordinates(n,y),n,r)
        lz=unique_lift(px,coordinates(n,z),n,r)
        assert stripdist(ly,lz)<=r,(n,r,x,y,z,ly,lz)
    out={'n':n,'r':r,'vertices':N,'edges_at_r':edges,'triangles_at_r':triangles}
    if compute_euler:
        red,faces=clique_euler(d,r)
        assert red==-1,(n,r,red,faces)
        out['reduced_euler']=red
        out['nonempty_simplices']=sum(faces.values())
    return out

def all_faces(d,r):
    """Explicit simplices in increasing vertex order, for finite boundary checks."""
    N=len(d)
    compat=[sum(1<<j for j in range(i+1,N) if d[i][j]<=r) for i in range(N)]
    out={}
    def rec(prefix,cand):
        if prefix:out.setdefault(len(prefix),[]).append(prefix)
        while cand:
            bit=cand&-cand;j=bit.bit_length()-1;cand-=bit
            rec(prefix+(j,),cand&compat[j])
    rec((),(1<<N)-1)
    return out

def binary_rank(vectors):
    pivots={}
    for v in vectors:
        while v:
            j=v.bit_length()-1
            if j in pivots:v^=pivots[j]
            else:pivots[j]=v;break
    return len(pivots)

def reduced_mod2_betti(n,r):
    faces=all_faces(distances(graph(n)),r)
    boundary_rank=[0]
    for j in range(2,max(faces)+1):
        idx={s:i for i,s in enumerate(faces[j-1])}
        columns=[]
        for s in faces[j]:
            col=0
            for i in range(j):col|=1<<idx[s[:i]+s[i+1:]]
            columns.append(col)
        boundary_rank.append(binary_rank(columns))
    boundary_rank.append(0)
    b=[len(faces[j])-boundary_rank[j-1]-boundary_rank[j] for j in range(1,max(faces)+1)]
    b[0]-=1
    return b

def boundary_examples():
    # A strict lower-bound sample is no longer a circle, even if it has
    # the same Euler characteristic. Check actual boundary-matrix ranks.
    for n,r,expected in [(5,2,{2:1}),(8,3,{3:1})]:
        betti=reduced_mod2_betti(n,r)
        observed={i:b for i,b in enumerate(betti) if b}
        assert observed==expected,(n,r,observed)
        print('BELOW_BOUNDARY',n,r,'mod2_reduced_betti',observed)

if __name__=='__main__':
    for r in range(2,6):
        for n in (3*r,3*r+1,3*r+2):
            print('STABLE_CASE',run_case(n,r,compute_euler=(r<=4 or n==3*r)))
    boundary_examples()
    print('TWISTED_LADDER_STABLE_RIPS_CHECKS_OK')
