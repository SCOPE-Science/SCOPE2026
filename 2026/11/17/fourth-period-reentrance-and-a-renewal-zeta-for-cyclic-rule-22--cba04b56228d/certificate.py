#!/usr/bin/env python3
"""Exact Rule 22 time-column graph and fourth-period orbit certificate.
Standard-library Python 3.10+. Run: python3 certificate.py
"""
from collections import Counter

def graph(height):
    width=1 << height
    g={}
    for a in range(width):
        for b in range(width):
            u=(a,b)
            for c in range(width):
                ok=True
                for j in range(height):
                    v=(a>>j&1)*4+(b>>j&1)*2+(c>>j&1)
                    if (22>>v&1)!=(b>>((j+1)%height)&1):
                        ok=False
                        break
                if ok:
                    g.setdefault(u,set()).add((b,c))
    return {u:sorted(v) for u,v in sorted(g.items())}

def components(g):
    adj={v:g.get(v,[]) for v in set(g)|{w for vv in g.values() for w in vv}}
    indices={}; low={}; stack=[]; active=set(); out=[]
    def visit(v):
        indices[v]=low[v]=len(indices)
        stack.append(v);active.add(v)
        for w in adj[v]:
            if w not in indices:
                visit(w);low[v]=min(low[v],low[w])
            elif w in active:low[v]=min(low[v],indices[w])
        if low[v]==indices[v]:
            s=[]
            while True:
                w=stack.pop(); active.remove(w);s.append(w)
                if w==v:break
            if len(s)>1 or v in adj[v]:out.append(sorted(s))
    for v in sorted(adj):
        if v not in indices:visit(v)
    return sorted(out,key=lambda s:(-len(s),s))

def block(g,vertices):
    pos={v:i for i,v in enumerate(vertices)}
    M=[[0]*len(vertices) for _ in vertices]
    for v in vertices:
        for w in g.get(v,[]):
            if w in pos:M[pos[v]][pos[w]]+=1
    return M

def matmul(A,B):
    m=len(A);C=[[0]*m for _ in range(m)]
    for i in range(m):
        for k in range(m):
            if A[i][k]:
                for j in range(m):
                    if B[k][j]:C[i][j]+=A[i][k]*B[k][j]
    return C

def det_series(M):
    m=len(M);power=[[int(i==j) for j in range(m)] for i in range(m)]
    traces=[]
    for n in range(1,m+1):
        power=matmul(power,M)
        traces.append(sum(power[i][i] for i in range(m)))
    coeff=[1]
    for k in range(1,m+1):
        num=-sum(coeff[k-i]*traces[i-1] for i in range(1,k+1))
        assert num%k==0
        coeff.append(num//k)
    return coeff

def multiply(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]+=x*y
    return c

def simple_cycles(g,vertices):
    idx={v:i for i,v in enumerate(vertices)};cycles=[];ss=set(vertices)
    for start in vertices:
        seen={start};path=[start]
        def dfs(v):
            for w in g.get(v,[]):
                if w==start:cycles.append(tuple(path))
                elif w in ss and idx[w]>idx[start] and w not in seen:
                    seen.add(w);path.append(w);dfs(w);path.pop();seen.remove(w)
        dfs(start)
    return cycles

def count_four(n,P):
    tr=[0]*(n+1)
    for k in range(1,n+1):
        tr[k]=-k*(P[k] if k<len(P) else 0)-sum(P[i]*tr[k-i] for i in range(1,min(k,len(P)-1)+1))
    assert tr[n]%2==0
    return tr[n]//2

def main():
    gs={t:graph(t) for t in (1,2,4)}
    cs={t:components(gs[t]) for t in gs}
    assert {t:sorted(map(len,cs[t]),reverse=True) for t in cs}=={1:[2,1],2:[4,2,1],4:[18,18,4,2,1]}
    H=gs[4]; large=cs[4][:2]
    rotate=lambda x:((x<<1)&15)|(x>>3)
    assert {tuple(map(rotate,v)) for v in large[0]}==set(large[1])
    repeat=lambda x:x|(x<<2)
    small={tuple(map(repeat,v)) for V in cs[2] for v in V}
    assert small=={v for V in cs[4][2:] for v in V}
    for u in gs[2]:
        for v in gs[2][u]:
            assert tuple(map(repeat,v)) in H.get(tuple(map(repeat,u)),[])
    A=block(H,large[0]);B=block(H,large[1])
    Q5=[1,-1,1,-1,0,-1];Q6=[1,0,0,0,1,1,1]
    P=multiply(multiply([1,1],Q5),Q6)
    assert det_series(A)==det_series(B)==P+[0]*(18-len(P)+1)
    cyc=simple_cycles(H,large[0]);freq=Counter(map(len,cyc))
    assert freq=={8:1,9:2,10:3,11:2,12:1}
    shared=set.intersection(*(set(c) for c in cyc))
    assert shared=={(5,6),(5,9),(6,5),(9,5)}
    allowed={8,9,10,11,12}|set(range(16,101))
    attainable={0}
    for n in range(1,101):
        if any(n-k in attainable for k in (8,9,10,11,12)):attainable.add(n)
    assert attainable-{0}==allowed
    for n in range(1,101):
        assert (count_four(n,P)>0)==(n in allowed)
    print('PASS Rule 22 four-step transfer certificate')
    print('Active component sizes height1,height2,height4: [2,1], [4,2,1], [18,18,4,2,1]')
    print('Two 18-vertex components exchanged by temporal phase rotation')
    print('Small component correspondence with height-two repetition: verified')
    print('One large component: 18 vertices, 22 edges')
    print('det(I-zA) coefficients degree 18:',P+[0]*(18-len(P)+1))
    print('Simple directed cycle lengths:',dict(sorted(freq.items())))
    print('Common vertices of all simple cycles:',sorted(shared))
    print('Exact primitive-four length set through n=100 checked against semigroup')
    print('Counts n=3..30:',[(n,count_four(n,P)) for n in range(3,31)])
if __name__=='__main__':main()
