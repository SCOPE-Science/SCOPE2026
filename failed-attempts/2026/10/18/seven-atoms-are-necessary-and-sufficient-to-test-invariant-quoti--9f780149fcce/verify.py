"""Independent finite checks for equivariant 3-register quotient test."""
from itertools import product
from collections import deque

def patt(t):
    d={}; q=[]
    for z in t:
        if z not in d:d[z]=len(d)
        q.append(d[z])
    return tuple(q)

def supp(t): return frozenset(t)

def graphs_connected(n):
    cells={}
    for t in product(range(n),repeat=3):
        cells.setdefault(patt(t),[]).append(t)
    assert len(cells)==5
    count=0
    for p,P in cells.items():
      for q,Q in cells.items():
        # Connected disjointness graph, bipartite if distinct patterns.
        vertices=[(0,t) for t in P]+ ([(1,t) for t in Q] if p!=q else [])
        adj={v:[] for v in vertices}
        if p==q:
          for i,x in enumerate(P):
            for y in P[i+1:]:
              if supp(x).isdisjoint(y):
                adj[(0,x)].append((0,y));adj[(0,y)].append((0,x))
        else:
          for x in P:
            for y in Q:
              if supp(x).isdisjoint(y):
                adj[(0,x)].append((1,y));adj[(1,y)].append((0,x))
        seen={vertices[0]}; todo=deque(seen)
        while todo:
          for y in adj[todo.popleft()]:
            if y not in seen: seen.add(y);todo.append(y)
        assert len(seen)==len(vertices),(p,q,len(seen),len(vertices))
        count+=1
    return count

def relation(t,u):
    if len(supp(t))==len(supp(u))==3:
        return supp(t)==supp(u) or supp(t).isdisjoint(u)
    return t==u

def class_signature(t):
    if len(supp(t))<3:return ('singleton',t)
    a=tuple(sorted(supp(t)));comp=tuple(x for x in range(6) if x not in supp(t))
    return ('pair',min(a,comp))

B=list(product(range(6),repeat=3))
for x in B:
    for y in B:
        assert relation(x,y)==(class_signature(x)==class_signature(y))
assert graphs_connected(7)==25
z=(0,1,2);x=(3,4,5);y=(3,4,6)
assert relation(x,z) and relation(z,y) and not relation(x,y)
print('THREE_REGISTER_VERIFY_OK 6_atom_classes=equivalence 7_atom_disjoint_graphs=25 7_atom_counterexample=true')
