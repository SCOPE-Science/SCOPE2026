#!/usr/bin/env python3
"""Exact Rule 110 sixth-/seventh-return space-time graph reconstruction.
This checker uses only the Python standard library; no precomputed data files.
"""
from collections import defaultdict

RULE=110

def update(a,b,c):
    return (RULE >> ((a<<2)|(b<<1)|c)) & 1

def build(T):
    q=1<<T
    edges=[[] for _ in range(q*q)]
    for a in range(q):
        for b in range(q):
            # Allowed c bitwise independently according to a,b and next-time b.
            possibilities=[0]
            for t in range(T):
                opts=[bit for bit in (0,1) if update((a>>t)&1,(b>>t)&1,bit)==((b>>((t+1)%T))&1)]
                possibilities=[x|(bit<<t) for x in possibilities for bit in opts]
                if not possibilities: break
            edges[a*q+b]=[b*q+c for c in possibilities]
    return edges

def scc(edges):
    # Iterative Kosaraju; handles every vertex without external libraries.
    N=len(edges); rev=[[] for _ in range(N)]
    for u,outs in enumerate(edges):
        for v in outs:rev[v].append(u)
    seen=bytearray(N); order=[]
    for root in range(N):
        if seen[root]:continue
        seen[root]=1;st=[(root,0)]
        while st:
            u,i=st[-1]
            if i<len(edges[u]):
                v=edges[u][i];st[-1]=(u,i+1)
                if not seen[v]:seen[v]=1;st.append((v,0))
            else:order.append(u);st.pop()
    seen=bytearray(N);comps=[]
    for root in reversed(order):
        if seen[root]:continue
        seen[root]=1; st=[root];comp=[]
        while st:
            u=st.pop();comp.append(u)
            for v in rev[u]:
                if not seen[v]:seen[v]=1;st.append(v)
        if len(comp)>1 or comp[0] in edges[comp[0]]:comps.append(comp)
    return comps

def closure(T,expected_size,expected_edges):
    G=build(T)
    numedges=sum(map(len,G)); assert numedges==expected_edges,(T,numedges)
    comps=scc(G)
    lens=sorted(map(len,comps))
    assert lens==[1,expected_size],(T,lens)
    big=next(c for c in comps if len(c)>1)
    assert next(c for c in comps if len(c)==1)==[0]
    E=sum(v in set(big) for u in big for v in G[u])
    assert E==({6:13,7:84}[T]),(T,E)
    return G,big

# Temporal height 6 has three recurrent components, rather than the two of height 7.
G6=build(6); c6=scc(G6)
assert sum(map(len,G6))==4097
assert sorted((len(c),sum(v in set(c) for u in c for v in G6[u])) for c in c6)==[(1,1),(4,4),(9,9)]
assert 0 in next(c for c in c6 if len(c)==1)
# Verify time columns in the 4-cycle have vertical period two, and
# those in the 9-cycle vertical period three; this excludes period six.
def column_time_period(u, d):
    return all(((u>>t)&1)==((u>>((t+d)%6))&1) for t in range(6))
assert all(column_time_period(u//64,2) and column_time_period(u%64,2) for c in c6 if len(c)==4 for u in c)
assert all(column_time_period(u//64,3) and column_time_period(u%64,3) for c in c6 if len(c)==9 for u in c)

G7,C=closure(7,63,16385)
S=set(C); ordered=sorted(C); ix={u:i for i,u in enumerate(ordered)};K=len(C)
adj=[0]*K
for u in C:
    for v in G7[u]:
        if v in S:adj[ix[u]]|=1<<ix[v]

def multiply_rows(rows):
    out=[0]*K
    for i,mask in enumerate(rows):
        while mask:
            low=mask&-mask; j=low.bit_length()-1
            out[i]|=adj[j];mask-=low
    return out

rows=[1<<i for i in range(K)]
allowed=[];root=ix[193]; loops_at_root=set(); counts={}
for n in range(1,41):
    rows=multiply_rows(rows)
    hit=sum((rows[i]>>i)&1 for i in range(K))
    counts[n]=hit
    if hit:allowed.append(n)
    if (rows[root]>>root)&1:loops_at_root.add(n)

allowed_through_30=[9,11,14,17,18,20,22,23,25,26,27,28,29]
assert [n for n in allowed if n<=30]==allowed_through_30
assert all(n in loops_at_root for n in [9]+list(range(31,40)))
# With cycles based at 193, add the length-nine closed walk to each base
# length 31,...,39, establishing every spatial length n>=31.
# Numeric trace (with multiplicities) is distinct from Boolean reachability.
selected={9:63,11:77,14:14,17:119,18:63,20:420}
traces={}
for n in selected:
    total=0
    for start in range(K):
        vec=[0]*K;vec[start]=1
        for _ in range(n):
            nxt=[0]*K
            for u,val in enumerate(vec):
                if val:
                    for v in G7[ordered[u]]:
                        if v in S:nxt[ix[v]]+=val
            vec=nxt
        total+=vec[start]
    traces[n]=total
assert traces==selected,(traces,selected)
# The all-zero fixed point is the only fixed state: check height-one graph.
G1=build(1);c1=scc(G1);assert len(c1)==1 and c1[0]==[0]
print('PASS: T=6 total edges=4097; recurrent SCCs (1,1),(4,4),(9,9), hence no primitive temporal six-cycles.')
print('PASS: T=7 total edges=16385; recurrent SCCs (1,1),(63,84), no other recurrent states.')
print('PASS: allowed circumference below 31:',allowed_through_30)
print('PASS: common root 193 has length-9 and length-31..39 closed walks; all n>=31 occur.')
print('PASS: Rule 110 period-seven orbit counts n=9,11,14,17,18,20:',[(n,traces[n]//7) for n in (9,11,14,17,18,20)])
