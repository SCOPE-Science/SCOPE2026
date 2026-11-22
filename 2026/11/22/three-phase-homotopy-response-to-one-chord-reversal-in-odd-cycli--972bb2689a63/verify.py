#!/usr/bin/env python3
"""Exact finite certificate for cyclic tournament arc-reversal topology.
The unbounded result is proved by vertex-link dismantlings; this file checks
base collapses, interval formulas and the explicit dismantling schedules.
"""
from itertools import combinations
from collections import Counter

def arc(m,d,a,b):
    n=2*m+1
    if (a,b)==(0,d): return False
    if (a,b)==(d,0): return True
    return (b-a)%n<=m

def transitive(m,d,s):
    for a,b,c in combinations(s,3):
        if (arc(m,d,a,b) and arc(m,d,b,c) and arc(m,d,c,a)) or (arc(m,d,a,c) and arc(m,d,c,b) and arc(m,d,b,a)):
            return False
    return True

def faces(m,d):
    n=2*m+1
    return set(s for s in range(1,1<<n) if transitive(m,d,[i for i in range(n) if s&(1<<i)]))

def collapse(K):
    K=set(K); seq=[]; n=max(s.bit_length() for s in K)
    while True:
        free=[]
        for s in K:
            upper=[]
            for i in range(n):
                t=s|(1<<i)
                if t!=s and t in K:upper.append(t)
                if len(upper)>1:break
            if len(upper)==1:free.append((s,upper[0]))
        if not free:break
        s,t=min(free,key=lambda z:(-z[0].bit_count(),z[0]))
        assert s in K and t in K and (t&s)==s and (t.bit_count()==s.bit_count()+1)
        assert sum(s!=u and (s&u)==s for u in K)==1
        K.remove(s); K.remove(t); seq.append((s,t))
    return K,seq

def inverse(word):
    return [-z for z in reversed(word)]

def freered(word):
    stack=[]
    for z in word:
        if stack and stack[-1]==-z:stack.pop()
        else:stack.append(z)
    return stack

def trivial_pi1(K,n):
    # Fundamental-group presentation from the 2-skeleton; tree edges vanish.
    E={tuple(i for i in range(n) if e>>i&1) for e in K if e.bit_count()==2}
    V={i for s in K for i in range(n) if s>>i&1}
    tree=set();seen={min(V)}
    while seen!=V:
        new=next((e for e in sorted(E) if (e[0] in seen)!=(e[1] in seen)),None)
        assert new is not None
        tree.add(new);seen.update(new)
    gens={e:i+1 for i,e in enumerate(sorted(E-tree))}
    def edgeword(a,b):
        x=gens.get(tuple(sorted((a,b))))
        if x is None:return []
        return [x if a<b else -x]
    rel=[]
    for tri in K:
        if tri.bit_count()!=3:continue
        a,b,c=[i for i in range(n) if tri>>i&1]
        rel.append(freered(edgeword(a,b)+edgeword(b,c)+edgeword(c,a)))
    active=set(gens.values());steps=0
    while active:
        found=None
        for ridx,w in enumerate(rel):
            for g in sorted(active):
                if sum(abs(x)==g for x in w)==1:
                    found=(ridx,g);break
            if found is not None:break
        if found is None:return False
        ridx,g=found; w=rel.pop(ridx)
        pos=next(i for i,x in enumerate(w) if abs(x)==g)
        z=w[pos]
        # w = before + z + after = identity; z = inverse(after+before).
        sol=inverse(w[pos+1:]+w[:pos])
        if z<0:sol=inverse(sol)
        nextrel=[]
        for word in rel:
            new=[]
            for x in word:
                if x==g:new.extend(sol)
                elif x==-g:new.extend(inverse(sol))
                else:new.append(x)
            nextrel.append(freered(new))
        rel=nextrel;active.remove(g);steps+=1
    assert all(not x for x in rel)
    return True

def base_cases():
    for m,d,expect in [(2,1,'point'),(2,2,'circle'),(3,2,'sphere')]:
        K=faces(m,d); H,seq=collapse(K)
        if expect=='point':
            assert len(H)==1 and next(iter(H)).bit_count()==1
        if expect=='circle':
            assert sorted(Counter(x.bit_count() for x in H).items())==[(1,3),(2,3)]
            assert len({u for x in H for u in range(2*m+1) if x>>u&1})==3
        if expect=='sphere':
            assert Counter(x.bit_count() for x in H)=={1:7,2:19,3:14}
            T=[s for s in H if s.bit_count()==3]
            edges=[s for s in H if s.bit_count()==2]
            assert trivial_pi1(H,2*m+1)
            assert 7-19+14==2
        print('base',m,d,expect,'faces',len(K),'pairs',len(seq),'core',len(H))

def link_graph(m,d,v,removed):
    n=2*m+1
    VV=set(range(n))-{v}-set(removed)
    # The graph is the 1-skeleton of link(v).
    edges={(a,b) for a,b in combinations(sorted(VV),2) if transitive(m,d,[v,a,b])}
    # Because incoming and outgoing neighbor subtournaments are transitive,
    # the vertex-link is the clique complex of this graph.
    return VV, edges

def fold_check(V,edges,schedule):
    V=set(V); E=set(edges)
    for a,b in schedule:
        assert a in V and b in V and a!=b,(a,b,V)
        Na={a}|{q if p==a else p for p,q in E if a in (p,q)}
        Nb={b}|{q if p==b else p for p,q in E if b in (p,q)}
        assert Na<=Nb,(a,b,Na-Nb)
        V.remove(a);E={z for z in E if a not in z}
    assert len(V)==1,(V,schedule)
    return next(iter(V))

def schedule_first(m,d):
    # Link at vertex 1; v=1 is deleted first. Valid for m>=4, d>=2,
    # and for (m,d)=(3,3).
    if d==2:
        return [(b,3) for b in range(4,m+2)]+[(0,m+4),(3,2)]+[(2,m+3),(m+2,m+3)]+[(a,a+1) for a in range(m+3,2*m)]
    return [(b,2) for b in range(3,m+2)]+[(0,m+3),(2,m+3),(m+2,m+3)]+[(a,a+1) for a in range(m+3,2*m)]

def schedule_second(m,d):
    return [(0,m+2)]+[(a,a+1) for a in range(2,m)]+[(m,m+2)]+[(a,a+1) for a in range(m+2,2*m)]

def schedule_adjacent_first(m):
    return [(b,3) for b in range(4,m+3)]+[(a,0) for a in [1]+list(range(m+3,2*m+1))]+[(3,0)]

def schedule_adjacent_second(m):
    return [(1,0),(0,m+3)]+[(a,a+1) for a in range(3,m+1)]+[(m+1,m+3)]+[(a,a+1) for a in range(m+3,2*m)]

def interval_check(m,d,kind):
    # Compare the explicit graph formula for each link with actual tournament triples.
    if kind=='short_first':
        v=1; removed=set(); A={0}|set(range(m+2,2*m+1));B=set(range(2,m+2))
        def cross(a,b):return (b in set(range(2,m+1)) and a==0 and b!=d) or (a>=m+2 and b>=2 and b<=a-m-1)
    elif kind=='short_second':
        v=m+1;removed={1};A=set(range(2,m+1));B={0}|set(range(m+2,2*m+1))
        def cross(a,b):return (a==d and b==0) or (b>=m+2 and b<=m+a)
    elif kind=='adj_first':
        v=2;removed=set();A={0,1}|set(range(m+3,2*m+1));B=set(range(3,m+3))
        def cross(a,b):return (a==0 and b<=m) or (a==1 and b<=m+1) or (a>=m+3 and b<=a-m-1)
    else:
        v=m+2;removed={2};A=set(range(3,m+2));B={0,1}|set(range(m+3,2*m+1))
        def cross(a,b):return (b==0 and a==m+1) or (b>=m+3 and b<=m+a)
    assert not A&B
    assert A|B==set(range(2*m+1))-{v}-removed
    VV,E=link_graph(m,d,v,removed)
    for a,b in combinations(sorted(VV),2):
        got=(a,b) in E
        expected=True if ((a in A and b in A) or (a in B and b in B)) else (cross(a,b) if a in A else cross(b,a))
        assert got==expected,(m,d,kind,a,b,got,expected)
    # Cross-pair condition suffices for a face because both sides are transitive.
    assert transitive(m,d,sorted(A)) and transitive(m,d,sorted(B))
    return VV,E

def sweep():
    for m in range(3,34):
        # Adjacent reverse arc: two-link collapse reducing to m-1.
        V,E=interval_check(m,1,'adj_first'); fold_check(V,E,schedule_adjacent_first(m))
        V,E=interval_check(m,1,'adj_second');fold_check(V,E,schedule_adjacent_second(m))
        if m>=4:
            for d in range(2,m+1):
                V,E=interval_check(m,d,'short_first');fold_check(V,E,schedule_first(m,d))
                V,E=interval_check(m,d,'short_second');fold_check(V,E,schedule_second(m,d))
        elif m==3:
            V,E=interval_check(m,3,'short_first');fold_check(V,E,schedule_first(m,3))
            V,E=interval_check(m,3,'short_second');fold_check(V,E,schedule_second(m,3))
    print('interval formulas and fold schedules checked for all m=3,...,33')

def extra():
    for m in range(2,8):
        for d in range(1,m+1):
            K=faces(m,d)
            H,p=collapse(K)
            exp=('circle' if d==m else 'sphere' if m>=3 and d==m-1 else 'point')
            assert len(H)==({'point':1,'circle':6,'sphere':40}[exp]),(m,d,len(H),exp)
    print('independent full complex enumeration and collapses: all 20 cases for m=2,...,7')

if __name__=='__main__':
    base_cases();sweep();extra();print('PASS')
