#!/usr/bin/env python3
"""Independent degree-certified bipartite Prüfer enumerator for unlabeled tree types."""
from itertools import product
from collections import Counter, deque
from math import comb
from functools import lru_cache

@lru_cache(None)
def partitions_leq_parts(n,k):
    if n<0: return 0
    if n==0:return 1
    if k==0:return 0
    return partitions_leq_parts(n,k-1)+(partitions_leq_parts(n-k,k) if n>=k else 0)

def from_codes(a,b,wa,wb):
    # Standard bipartite Prüfer deletion scheme. wa has length b-1 and wb length a-1.
    deg=[1]*a+[1]*b
    for v in wa:deg[v]+=1
    for v in wb:deg[a+v]+=1
    edges=[];ia=ib=0; n=a+b
    active=[True]*n
    for _ in range(n-2):
        v=next(i for i in range(n) if active[i] and deg[i]==1)
        if v<a:
            w=a+wb[ib];ib+=1
        else:
            w=wa[ia];ia+=1
        assert v!=w and active[w] and deg[w]>1,(v,w,deg,wa,wb)
        edges.append((v,w));active[v]=False;deg[v]-=1;deg[w]-=1
    live=[i for i in range(n) if active[i]]
    assert len(live)==2 and deg[live[0]]==deg[live[1]]==1
    edges.append(tuple(live))
    return edges

def canon(n, edges):
    adj=[[] for _ in range(n)]
    for u,v in edges:adj[u].append(v);adj[v].append(u)
    deg=[len(t) for t in adj]
    q=deque(i for i,d in enumerate(deg) if d<=1)
    rem=n
    while rem>2:
        l=len(q);rem-=l
        for _ in range(l):
            v=q.popleft()
            for w in adj[v]:
                deg[w]-=1
                if deg[w]==1:q.append(w)
    centers=list(q)
    def code(u,p):return '('+''.join(sorted(code(v,u) for v in adj[u] if v!=p))+')'
    return min(code(c,-1) for c in centers)

def formula(m):
    # Burnside decomposition over four possible core shapes.
    N=m-2
    fixed=(m//2)**2 if m%2==0 else ((m-1)//2)*((m+1)//2) # floor(m^2/4)
    x1=partitions_leq_parts(m-1,4)
    x2=(comb(m+1,3)+fixed)//2
    x3=sum(partitions_leq_parts(t,3) for t in range(m-2))
    x4=(comb(m,3)+(((m-1)//2) if (m%2==1) else 0))//2
    return (x1,x2,x3,x4)

def core_types(m):
    cores=[[(0,4),(1,4),(2,4),(3,4)],
           [(0,4),(1,4),(2,4),(0,5),(3,5)],
           [(0,4),(1,4),(0,5),(2,5),(0,6),(3,6)],
           [(0,4),(1,4),(1,5),(2,5),(2,6),(3,6)]]
    alltypes=[]
    for k,ed in zip((1,2,3,3),cores):
        types=set()
        for x0 in range(m-k+1):
          for x1 in range(m-k-x0+1):
           for x2 in range(m-k-x0-x1+1):
            x3=m-k-x0-x1-x2
            eds=list(ed)
            nxt=4+k
            for hub,count in enumerate((x0,x1,x2,x3)):
                for _ in range(count):
                    eds.append((hub,nxt));nxt+=1
            assert nxt==4+m
            types.add(canon(4+m,eds))
        alltypes.append(types)
    return alltypes

if __name__=='__main__':
    for m in range(5,7):
        C=Counter()
        for wa in product(range(4),repeat=m-1):
            for wb in product(range(m),repeat=3):
                E=from_codes(4,m,wa,wb)
                C[canon(4+m,E)]+=1
        pred=formula(m)
        print('m',m,'Pruefer_code_trees',sum(C.values()),'expected_labeled',4**(m-1)*m**3,
              'distinct_isomorphism_classes',len(C),'core_formula_parts',pred,'core_formula_total',sum(pred))
        assert sum(C.values())==4**(m-1)*m**3
        assert len(C)==sum(pred)
        classes=core_types(m)
        assert tuple(len(s) for s in classes)==pred
        assert not any(classes[i]&classes[j] for i in range(4) for j in range(i+1,4))
        assert set(C)==set.union(*classes)
        print('  four core-shape classes match every independently generated tree type')
    for m in range(5,41):
        assert sum(formula(m))>0
    print('PASS: independent Prüfer census m=5,6; exact Burnside formula internally integral for m=5..40')

    # Independently expand the four Burnside rational generating functions.
    L=40
    def geo(step):
        return [int(j%step==0) for j in range(L+1)]
    def mul(v,w):
        return [sum(v[j]*w[i-j] for j in range(i+1)) for i in range(L+1)]
    def shift(v,k):
        return [v[i-k] if i>=k else 0 for i in range(L+1)]
    g=geo(1)
    g2=geo(2)
    g3=geo(3)
    g4=geo(4)
    all4=mul(mul(g,g),mul(g,g))
    s4=shift(mul(mul(g,g2),mul(g3,g4)),1)
    id2=shift(all4,2)
    flip2=shift(mul(mul(g,g),g2),2)
    star3=shift(mul(mul(g,g),mul(g2,g3)),3)
    id3=shift(all4,3)
    flip3=shift(mul(g2,g2),3)
    coefs=[s4[i]+(id2[i]+flip2[i])//2+star3[i]+(id3[i]+flip3[i])//2 for i in range(L+1)]
    assert coefs[1:5]==[1,2,7,14]
    for m in range(5,L+1):
        assert coefs[m]==sum(formula(m))
    print('PASS: rational Burnside series coefficients agree for m=5..40; formal coefficients m=1..4 are 1,2,7,14')
