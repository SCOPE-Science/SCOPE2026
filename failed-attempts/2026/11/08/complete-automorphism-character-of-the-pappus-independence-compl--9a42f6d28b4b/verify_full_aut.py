#!/usr/bin/env python3
"""Reproducible topological and full-symmetry calculations for the Pappus graph.
Requires Python >=3.9 standard library only.
"""
from collections import Counter, defaultdict, deque
from math import gcd

N=18
LCF=(5,7,-7,7,-7,-5)*3
EDGE=set()
for i in range(N):
    for j in ((i+1)%N,(i+LCF[i])%N):
        EDGE.add(tuple(sorted((i,j))))
assert len(EDGE)==27
ADJ=[0]*N
for i,j in EDGE:
    ADJ[i]|=1<<j;ADJ[j]|=1<<i
assert all(m.bit_count()==3 for m in ADJ)

def automorphisms():
    # Exhaustive constraint-preserving backtracking over bijections.
    mapping=[-1]*N; used=0; ans=[]
    def rec(used,depth):
        if depth==N:
            ans.append(tuple(mapping));return
        # Nonrandom canonical backtracking strategy; all candidate images inspected.
        v=max((i for i in range(N) if mapping[i]==-1),key=lambda i:(sum(bool(ADJ[i]>>j&1) for j in range(N) if mapping[j]!=-1),-i))
        for w in range(N):
            if used>>w&1:continue
            if all(bool(ADJ[v]>>u&1)==bool(ADJ[w]>>mapping[u]&1) for u in range(N) if mapping[u]!=-1):
                mapping[v]=w;rec(used|1<<w,depth+1);mapping[v]=-1
    rec(0,0)
    return sorted(ans)

def compose(p,q):return tuple(p[q[i]] for i in range(N))
def inverse(p):
    q=[None]*N
    for i,j in enumerate(p):q[j]=i
    return tuple(q)
def cycles(p):
    seen=0;cyc=[]
    for i in range(N):
        if not (seen>>i)&1:
            a=[];x=i
            while not (seen>>x)&1:
                seen|=1<<x;a.append(x);x=p[x]
            assert x==i
            cyc.append(tuple(a))
    return cyc

def get_order(p):
    a=1
    for c in cycles(p):
        a=a*len(c)//gcd(a,len(c))
    return a

def independence_faces():
    good=bytearray(1<<N);good[0]=1
    for m in range(1,1<<N):
        a=m&-m;v=a.bit_length()-1;s=m^a
        good[m]=bool(good[s] and not(ADJ[v]&s))
    return good, [m for m in range(1,1<<N) if good[m]]

def morse():
    good,faces=independence_faces()
    assert len(faces)==2597
    assert [sum(m.bit_count()==d+1 for m in faces) for d in range(9)]==[18,126,438,801,756,348,90,18,2]
    order=(11,9,0,16,2,15,10,3,5,17,14,6,7,8,4,1,13,12)
    mark=bytearray(1<<N)
    mark[0]=3
    pairs={}
    for v in order:
        b=1<<v
        for m in faces:
            if m&b or mark[m]!=0:continue
            if good[m|b] and mark[m|b]==0:
                mark[m]=1;mark[m|b]=2;pairs[m]=m|b
    critical=[m for m in faces if not mark[m]]
    assert len(pairs)==1293
    assert Counter(m.bit_count()-1 for m in critical)=={0:1,4:10}
    # Entire directed Hasse graph: paired covers are reversed.
    indeg={m:0 for m in faces}
    forward=defaultdict(list)
    covers=0
    for high in faces:
        m=high
        while m:
            b=m&-m;low=high^b;m^=b
            if low==0:continue
            covers+=1
            if pairs.get(low)==high:u,v=low,high
            else:u,v=high,low
            indeg[v]+=1;forward[u].append(v)
    q=deque(m for m in faces if indeg[m]==0)
    visited=0
    while q:
        u=q.popleft();visited+=1
        for v in forward[u]:
            indeg[v]-=1
            if indeg[v]==0:q.append(v)
    assert covers==11430,(covers)
    assert visited==len(faces)
    return faces,critical

def trace_quotient(p):
    # Invariant faces consist of whole permutation cycles, and contribute
    # (-1)^(number of selected cycles + 1) to reduced Lefschetz.
    allowed=[]
    for c in cycles(p):
        mask=sum(1<<i for i in c)
        if all(not(mask>>u&1 and mask>>v&1) for u,v in EDGE):
            allowed.append(mask)
    qadj=[0]*len(allowed)
    for i,a in enumerate(allowed):
        for j,b in enumerate(allowed):
            if i<j and any((a>>u&1 and b>>v&1) or (a>>v&1 and b>>u&1) for u,v in EDGE):
                qadj[i]|=1<<j;qadj[j]|=1<<i
    # Weighted sum I(Q,-1) via recurrence: I(Q,-1)=I(Q-v,-1)-I(Q-N[v],-1).
    from functools import lru_cache
    @lru_cache(None)
    def I(S):
        if not S:return 1
        b=S&-S;i=b.bit_length()-1
        return I(S^b)-I(S&~(b|qadj[i]))
    return -I((1<<len(allowed))-1)

def main():
    faces,critical=morse()
    print('GRAPH vertices=18 edges=27 degree=3')
    print('MORSE faces=%d pairs=1293 critical=%s Hasse_covers=11430 DAG=PASS'%(len(faces),dict(Counter(m.bit_count()-1 for m in critical))))
    autos=automorphisms(); assert len(autos)==216
    aset=set(autos);e=tuple(range(N))
    assert e in aset
    assert all(inverse(g) in aset for g in autos)
    assert all(compose(g,h) in aset for g in autos for h in autos)
    print('AUTOMORPHISMS count=216 exhaustive_permutation_search=PASS closure=PASS')
    chars={g:trace_quotient(g) for g in autos}
    unseen=set(autos);classes=[]
    while unseen:
        r=min(unseen)
        conj={compose(compose(g,r),inverse(g)) for g in autos}
        assert conj<=unseen
        assert len({chars[g] for g in conj})==1
        unseen-=conj
        classes.append((r,conj))
    classes.sort(key=lambda x:(get_order(x[0]),len(x[1]),chars[x[0]],x[0]))
    print('CONJUGACY_CLASSES count='+str(len(classes)))
    for i,(rep,cls) in enumerate(classes):
        o=get_order(rep);shape=','.join('%d:%d'%(k,v) for k,v in sorted(Counter(map(len,cycles(rep))).items()))
        print('CLASS %02d size=%d order=%d cycle_lengths=%s trace=%d representative=%s'%(i,len(cls),o,shape,chars[rep],','.join(map(str,rep))))
    assert len(classes)==13
    assert sum(chars.values())==0
    assert sum(v*v for v in chars.values())==2*216
    assert chars[tuple((i+6)%N for i in range(N))]==-2
    assert Counter(chars.values())=={10:1,2:36,-2:21,0:54,1:32,-1:72}
    print('FULL_CHARACTER dimension=10 invariant_dimension=0 complex_character_inner_product=2')
    print('PUBLISHED_SUBGROUP_CHECK order3_shift6_trace=-2')
    print('PAPPUS_FULL_AUT_PASS')
if __name__=='__main__':main()
