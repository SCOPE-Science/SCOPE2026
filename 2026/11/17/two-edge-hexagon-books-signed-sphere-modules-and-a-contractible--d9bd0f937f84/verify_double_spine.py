"""Exhaustive finite sanity checks for the two-edge-spine hexagon book."""
from collections import deque
from itertools import combinations

def graph(h):
    V=3+3*h
    edges={(0,2),(2,1)}
    arms=[]
    for i in range(h):
        x,y,z=3+3*i,4+3*i,5+3*i
        arms.append((x,y,z))
        edges.update([(0,x),(x,y),(y,z),(z,1)])
    return V, {tuple(sorted(x)) for x in edges},arms

def complex_of(edges,n):
    adj=[set() for _ in range(n)]
    for a,b in edges: adj[a].add(b);adj[b].add(a)
    d=[]
    for s in range(n):
        q=deque([s]);dd={s:0}
        while q:
            v=q.popleft()
            for w in adj[v]:
                if w not in dd:dd[w]=dd[v]+1;q.append(w)
        assert len(dd)==n
        d.append([dd[v] for v in range(n)])
    flag=[set() for _ in range(n)]
    for a in range(n):
        flag[a]={b for b in range(a+1,n) if d[a][b]<=2}
    faces={frozenset()}
    def rec(f,cands):
        if f:faces.add(frozenset(f))
        for j,v in enumerate(cands):rec(f+[v],[w for w in cands[j+1:] if w in flag[v]])
    rec([],list(range(n)))
    return faces,d

def from_facets(facets):
    result={frozenset()}
    for f in facets:
        for k in range(1,len(f)+1):result.update(frozenset(c) for c in combinations(f,k))
    return result

def rank2(columns):
    piv={};n=0
    for col in columns:
        x=col
        while x:
            i=x.bit_length()-1
            if i in piv:x^=piv[i]
            else:piv[i]=x;n+=1;break
    return n

def bettis(F):
    layers={k:sorted([tuple(sorted(f)) for f in F if len(f)==k]) for k in range(1,1+max(map(len,F)))}
    ranks={}
    for k in layers:
        if k==1:ranks[k]=0;continue
        lower={f:i for i,f in enumerate(layers[k-1])}
        cols=[sum(1<<lower[f[:j]+f[j+1:]] for j in range(len(f))) for f in layers[k]]
        ranks[k]=rank2(cols)
    result={k-1:len(v)-ranks[k]-ranks.get(k+1,0) for k,v in layers.items()}
    result[0]-=1
    return {k:v for k,v in result.items() if v}

def signed_fixed_trace(F,perm):
    # trace reduced alternating chain gives alternating trace on reduced homology
    ans=-1
    for f in F:
        if not f:continue
        a=sorted(f);b=sorted(perm[v] for v in a)
        if b!=a:continue
        mapped=[perm[v] for v in a]; inv=sum(mapped[i]>mapped[j] for i in range(len(a)) for j in range(i+1,len(a)))
        ans+= (-1 if (len(a)-1+inv)%2 else 1)
    return ans


def check(h):
    n,edges,arms=graph(h)
    K,d=complex_of(edges,n)
    Lfac=[{0,2,*[a[0] for a in arms]},{1,2,*[a[2] for a in arms]},{0,1,2}]
    L=from_facets(Lfac)
    Ks=[]
    for x,y,z in arms:
        K_i=from_facets([{0,2,x},{1,2,z},{0,1,2},
                        # need octahedral facets from six-cycle: all triples choosing one from each opposite pair
                         *[set(v) for v in __import__('itertools').product([0,z],[x,1],[y,2])]])
        Ks.append(K_i)
    full=L.union(*Ks)
    assert full==K,(h,'facets miss',len(K-full), 'extra',len(full-K),list(K-full)[:3])
    I1=from_facets([{0,2,arms[0][0]},{1,2,arms[0][2]},{0,1,2}])
    assert Ks[0]&L==I1
    for i in range(1,h):
        xi,yi,zi=arms[i]
        I=from_facets([{0,2,xi},{1,2,zi},{0,1,2}])
        assert Ks[i]&(L.union(*Ks[:i]))==I
    b=bettis(K)
    assert b=={2:h},(h,b)
    for x,y,z in arms:assert d[x][z]==2
    refl={0:1,1:0,2:2}
    for x,y,z in arms:refl.update({x:z,y:y,z:x})
    t=signed_fixed_trace(K,refl)
    # If only H2, trace(H2)=t
    assert t==-h,(h,t)
    # swap the first two arms
    if h>=2:
        rot={i:i for i in range(n)}
        for a,bb in zip(arms[0],arms[1]):rot[a]=bb;rot[bb]=a
        tt=signed_fixed_trace(K,rot)
        assert tt==h-2,(h,tt)
    print(f'h={h} vertices={n} edges={len(edges)} faces={len(K)-1} betti={b} reflection_trace={t} swap_trace={h-2 if h>=2 else "NA"}')

if __name__=='__main__':
    for h in range(1,7):check(h)
    print('DOUBLE_SPINE_HEXAGON_RIPS_OK')
