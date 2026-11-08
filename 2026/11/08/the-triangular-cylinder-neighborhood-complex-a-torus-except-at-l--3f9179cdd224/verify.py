#!/usr/bin/env python3
"""Finite exact combinatorial checks for neighborhood complexes of C3 x Cn.
No external packages. The all-n proof is in RESULT.md.
"""
from collections import Counter, defaultdict, deque
from itertools import combinations

def build(n):
    assert n >= 3
    vertex=lambda a,b: (a%3)*n+b%n
    K=set(); centers=[]
    for a in range(3):
        for b in range(n):
            e,w=vertex(a+1,b),vertex(a-1,b)
            u,d=vertex(a,b+1),vertex(a,b-1)
            N=tuple(sorted((e,w,u,d)))
            assert len(set(N))==4
            centers.append((e,w,u,d))
            for k in range(1,5):K.update(combinations(N,k))
    return K,centers

def collapse(n):
    K,centers=build(n)
    initial=Counter(map(len,K))
    def delete(lo,hi):
        lo,hi=tuple(sorted(lo)),tuple(sorted(hi))
        assert lo in K and hi in K and len(hi)==len(lo)+1
        assert all(not set(lo)<set(s) or s==hi for s in K), ('not free',n,lo,hi)
        K.remove(lo);K.remove(hi)
    for e,w,u,d in centers:
        delete((e,w,u),(e,w,u,d))
    for e,w,u,d in centers:
        delete((e,w),(e,w,d))
    expected=set()
    for e,w,u,d in centers:
        for t in ((e,u,d),(w,u,d)):
            for size in range(1,4):expected.update(combinations(sorted(t),size))
    assert K==expected,('core mismatch',n)
    assert Counter(map(len,K))==Counter({1:3*n,2:(30 if n==4 else 9*n),3:6*n}),(n,Counter(map(len,K)))
    return K,initial

def ranks2(K):
    by={d:sorted(s for s in K if len(s)==d) for d in (1,2,3)}
    R={}
    for d in (2,3):
        low={s:i for i,s in enumerate(by[d-1])}
        piv={}
        for s in by[d]:
            col=0
            for i in range(d):col^=1<<low[s[:i]+s[i+1:]]
            while col:
                k=col.bit_length()-1
                if k not in piv:piv[k]=col;break
                col^=piv[k]
        R[d]=len(piv)
    return (len(by[2])-R[2]-R[3],len(by[3])-R[3])

def surface(K):
    # For all ordinary stages n != 4 check links are cycles and orientations consistent.
    vertices={s[0] for s in K if len(s)==1}
    triangles=[s for s in K if len(s)==3]
    adjacency=defaultdict(list)
    edge_inc=Counter()
    for t in triangles:
        for i in range(3):
            e=tuple(v for j,v in enumerate(t) if j!=i)
            edge_inc[e]+=1
            adjacency[e].append(t)
    assert set(edge_inc.values())=={2}
    for v in vertices:
        link_edges=[tuple(x for x in t if x!=v) for t in triangles if v in t]
        link_vertices={x for e in link_edges for x in e}
        link_degrees=Counter(x for e in link_edges for x in e)
        assert len(link_edges)==len(link_vertices)==6 and set(link_degrees.values())=={2}
        visited={next(iter(link_vertices))};todo=list(visited)
        while todo:
            x=todo.pop()
            for e in link_edges:
                if x in e:
                    for y in e:
                        if y not in visited:visited.add(y);todo.append(y)
        assert visited==link_vertices
    # Dual triangle graph is connected, hence surface is connected.
    graph=defaultdict(list)
    for pair in adjacency.values():
        graph[pair[0]].append(pair[1]);graph[pair[1]].append(pair[0])
    reached={triangles[0]}; todo=[triangles[0]]
    while todo:
        for u in graph[todo.pop()]:
            if u not in reached:reached.add(u);todo.append(u)
    assert len(reached)==len(triangles)
    # Orientability via relative orientation of each shared directed edge.
    orientations={triangles[0]:1};todo=[triangles[0]]
    def boundary_sign(t,edge):
        i=next(i for i in range(3) if tuple(x for j,x in enumerate(t) if i!=j)==edge)
        return (-1)**i
    while todo:
        t=todo.pop()
        for i in range(3):
            e=tuple(x for j,x in enumerate(t) if j!=i)
            other=next(s for s in adjacency[e] if s!=t)
            forced=-orientations[t]*boundary_sign(t,e)*boundary_sign(other,e)
            if other in orientations:assert forced==orientations[other]
            else:orientations[other]=forced;todo.append(other)
    assert len(orientations)==len(triangles)
    assert len(vertices)-len(edge_inc)+len(triangles)==0
    return True

def n4_tietze(K):
    # Collapse maximal spanning tree in the 1-skeleton; write 2-cell relators.
    vertices=sorted(s[0] for s in K if len(s)==1)
    edges=sorted(s for s in K if len(s)==2)
    triangles=sorted(s for s in K if len(s)==3)
    parent=list(range(12)); tree=[]; generators=[]
    def find(x):
        while parent[x]!=x:x=parent[x]
        return x
    for a,b in edges:
        x,y=find(a),find(b)
        if x!=y:parent[x]=y;tree.append((a,b))
        else:generators.append((a,b))
    assert len(tree)==11 and len(generators)==19 and len(triangles)==24
    ix={e:i+1 for i,e in enumerate(generators)}
    def reduce(word):
        out=[]
        for s in word:
            if out and out[-1]==-s:out.pop()
            else:out.append(s)
        return out
    def inverse(word):return [-s for s in reversed(word)]
    def substitute(word,g,body):
        out=[]
        for x in word:
            if x==g:out+=body
            elif x==-g:out+=inverse(body)
            else:out.append(x)
        return reduce(out)
    R=[]
    for a,b,c in triangles:
        R.append(reduce([ix[e]*sign for e,sign in (((a,b),1),((b,c),1),((a,c),-1)) if e in ix]))
    live=set(range(1,20)); order=[]; substitutions=[]
    for it in range(18):
        choices=[]
        for ri,r in enumerate(R):
            for pos,g0 in enumerate(r):
                g=abs(g0)
                if g not in live or sum(abs(x)==g for x in r)!=1:continue
                w=r[pos:]+r[:pos]
                replacement=inverse(w[1:]) if w[0]==g else w[1:]
                assert all(abs(x)!=g for x in replacement)
                after=[substitute(word,g,replacement) for j,word in enumerate(R) if j!=ri]
                cost=max(map(len,after),default=0)+.003*sum(map(len,after))
                choices.append((cost,ri,g,replacement,after))
        assert choices,('stalled cancellation',it)
        _,ri,g,w,after=min(choices)
        live.remove(g); order.append(g);substitutions.append(w)
        R=after
        assert all(abs(x) in live for word in R for x in word)
    assert live=={17} and all(r==[] for r in R) and len(R)==6
    assert order==[11,19,9,18,1,2,3,4,5,6,7,8,14,10,15,12,13,16]
    return order,substitutions

def main():
    cases=0
    for n in range(3,19):
        K,initial=collapse(n)
        b1,b2=ranks2(K)
        if n==4:
            assert (b1,b2)==(1,6)
            order,w=n4_tietze(K)
            print('n=4 tree-presentation: 19 generators, 24 relators, eliminations='+','.join(map(str,order)))
            print('n=4 substitutions='+','.join(''.join(map(str,x)) if x else 'identity' for x in w))
            print('n=4 homotopy S1 wedge 6 S2: 1 generator and 6 trivial relators')
        else:
            assert (b1,b2)==(2,1)
            assert surface(K)
        cases+=1
    print('ALL_CHECKS_PASS stages='+str(cases)+' n=3..18 torus stages=15 exceptional=1')
if __name__=='__main__':main()
