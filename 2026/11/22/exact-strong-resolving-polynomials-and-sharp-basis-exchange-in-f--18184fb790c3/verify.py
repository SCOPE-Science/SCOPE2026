#!/usr/bin/env python3
"""Independently construct two finite generalized quadrangles and test strong-resolving claims."""
from itertools import combinations
from collections import deque,Counter
from math import comb


def gq22():
    # Nonzero symplectic vectors in F_2^4 are the points of W(3,2).
    points=list(range(1,16))
    def form(a,b):
        return ((a>>0&1)*(b>>2&1) + (a>>2&1)*(b>>0&1)
              + (a>>1&1)*(b>>3&1) + (a>>3&1)*(b>>1&1))%2
    blocks=set()
    for a,b in combinations(points,2):
        if form(a,b)==0:
            blocks.add(tuple(sorted((a,b,a^b))))
    return points,sorted(blocks),2,2


def gq24():
    # 27 curves in the Schlaefli system, represented as E_i, L_ij, C_i.
    points=[('E',i) for i in range(6)]+[('L',i,j) for i,j in combinations(range(6),2)]+[('C',i) for i in range(6)]
    def cross(a,b):
        x,y=a[0],b[0]
        if x=='E' and y=='L':return a[1] in b[1:]
        if y=='E' and x=='L':return b[1] in a[1:]
        if x=='E' and y=='C':return a[1]!=b[1]
        if y=='E' and x=='C':return b[1]!=a[1]
        if x==y=='L':return not(set(a[1:])&set(b[1:]))
        if x=='L' and y=='C':return b[1] in a[1:]
        if y=='L' and x=='C':return a[1] in b[1:]
        return False
    lines=[tuple(T) for T in combinations(points,3) if all(cross(a,b) for a,b in combinations(T,2))]
    return points,lines,2,4


def test(name,build):
    P,L,s,t=build()
    p,b=len(P),len(L)
    assert p==(s+1)*(s*t+1) and b==(t+1)*(s*t+1),(name,p,b)
    I=[[int(v in B) for B in L] for v in P]
    assert all(sum(row)==t+1 for row in I)
    assert all(sum(I[i][j] for i in range(p))==s+1 for j in range(b))
    assert all(sum(I[i][j]*I[k][j] for j in range(b))<=1 for i,k in combinations(range(p),2))
    assert all(sum(I[i][j]*I[i][k] for i in range(p))<=1 for j,k in combinations(range(b),2))
    for i in range(p):
        for j in range(b):
            if not I[i][j]:
                assert sum(I[x][j]*int(any(I[i][k]*I[x][k] for k in range(b))) for x in range(p))==1
    n=p+b
    adj=[set() for _ in range(n)]
    for i in range(p):
        for j in range(b):
            if I[i][j]:adj[i].add(p+j);adj[p+j].add(i)
    d=[]
    for v in range(n):
        D=[99]*n;D[v]=0;Q=deque([v])
        while Q:
            u=Q.popleft()
            for w in adj[u]:
                if D[w]==99:D[w]=D[u]+1;Q.append(w)
        assert max(D)==4
        d.append(D)
    mm=set()
    for u,v in combinations(range(n),2):
        if all(d[w][v]<=d[u][v] for w in adj[u]) and all(d[u][w]<=d[u][v] for w in adj[v]):
            mm.add((u,v))
        expect=(u<p and v<p and d[u][v]==4) or (u>=p and v>=p and d[u][v]==4)
        assert ((u,v) in mm)==expect,(name,'MMD',u,v,d[u][v])
    # Directly check all small omitted-shore subsets against MMD independence.
    pts=Counter();lns=Counter()
    for k in range(s+2):
        for C in combinations(range(p),k):
            if all((i,j) not in mm for i,j in combinations(C,2)):pts[k]+=1
    for k in range(t+2):
        for C in combinations(range(p,n),k):
            if all((i,j) not in mm for i,j in combinations(C,2)):lns[k]+=1
    fpts={0:1,1:p,**{k:b*comb(s+1,k) for k in range(2,s+2)}}
    flns={0:1,1:b,**{k:p*comb(t+1,k) for k in range(2,t+2)}}
    assert pts==fpts,(name,pts,fpts)
    assert lns==flns,(name,lns,flns)
    # Every maximal MMD-independent subset is a full line/pencil (check via independent maximal cliques).
    point_omits=[frozenset(i for i in range(p) if I[i][j]) for j in range(b)]
    line_omits=[frozenset(j for j in range(b) if I[i][j]) for i in range(p)]
    assert len(set(point_omits))==b and len(set(line_omits))==p
    for l in point_omits:
        assert len(l)==s+1 and all((i,j) not in mm for i,j in combinations(sorted(l),2))
    for l in line_omits:
        assert len(l)==t+1 and all((p+i,p+j) not in mm for i,j in combinations(sorted(l),2))
    # Direct strong-resolving definition on every minimum basis in W(3,2).
    if n==30:
        for omit_p in point_omits:
            for omit_l in line_omits:
                omit=omit_p | {p+j for j in omit_l}
                basis=set(range(n))-omit
                for a,c in combinations(range(n),2):
                    assert any(d[w][a]==d[w][c]+d[a][c] or
                               d[w][c]==d[w][a]+d[a][c] for w in basis)
        # Independent exhaustive check of all six-omission candidates.
        good=0
        for C in combinations(range(n),6):
            if all((a,c) not in mm for a,c in combinations(C,2)):
                good+=1
        assert good==p*b==225,good
    # Bases, and exact reconfiguration by at-most-k exchanges of selected elements.
    bases=[(i,j) for i in range(b) for j in range(p)]
    def moves(k):
        graph=[set() for _ in bases]
        for a,(i,j) in enumerate(bases):
            for c in range(a+1,len(bases)):
                i2,j2=bases[c]
                dist=len(point_omits[i]-point_omits[i2])+len(line_omits[j]-line_omits[j2])
                if dist<=k:graph[a].add(c);graph[c].add(a)
        return graph
    def components(g):
        seen=set(); sizes=[]
        for i in range(len(g)):
            if i in seen:continue
            seen.add(i);Q=[i];idx=0
            while idx<len(Q):
                u=Q[idx];idx+=1
                for v in g[u]:
                    if v not in seen:seen.add(v);Q.append(v)
            sizes.append(len(Q))
        return Counter(sizes)
    for k in range(1,max(s,t)+1):
        graph=moves(k)
        classes=components(graph)
        if k==max(s,t):assert classes==Counter({p*b:1}), (name,k,classes)
        if k<min(s,t):assert classes==Counter({1:p*b}),(name,k,classes)
        if k==max(s,t):
            if s==t: expected=s*(t+1)+t*(s+1)
            elif s<t:expected=(b-1)+s*(t+1)
            else:expected=t*(s+1)+(p-1)
            assert set(map(len,graph))=={expected},(name,k,set(map(len,graph)),expected)
        print(name,'exchange k=',k,'components',sorted(classes.items()),'edges',sum(map(len,graph))//2)
    print(name,'verified','points',p,'lines',b,'MMD edges',len(mm),'strong dim',n-s-t-2,'bases',p*b,
          'point omit counts',dict(pts),'line omit counts',dict(lns))

if __name__=='__main__':
    test('W(3,2)',gq22)
    test('GQ(2,4)',gq24)
    print('ALL CHECKS PASS')
