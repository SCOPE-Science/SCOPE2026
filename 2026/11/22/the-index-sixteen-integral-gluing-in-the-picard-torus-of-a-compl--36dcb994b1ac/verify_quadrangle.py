#!/usr/bin/env python3
"""Exact integral S4-cycle-lattice certificate for a complete-quadrangle six-line union.
Run: python3 verify_quadrangle.py   (requires SymPy >=1.12).
"""
import itertools as it
from collections import deque
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form
from sympy.polys.domains import ZZ

labels = range(4)
lines = list(it.combinations(labels,2))
diagonals = sorted({tuple(sorted((e,tuple(sorted(set(labels)-set(e)))))) for e in lines})
vertices = sorted([('v',i) for i in labels] + [('e',e) for e in lines]
                  + [('m',m) for m in diagonals],key=str)
edges=[]
for e in lines:
    for i in e:edges.append(tuple(sorted((('e',e),('v',i)),key=str)))
    d=next(d for d in diagonals if e in d)
    edges.append(tuple(sorted((('e',e),('m',d)),key=str)))
edges.sort(key=str)
assert (len(vertices),len(edges))==(13,18)
edge_idx={e:i for i,e in enumerate(edges)}
adj={v:[] for v in vertices}
for edge in edges:
    a,b=edge
    adj[a].append((b,edge));adj[b].append((a,edge))
visited={vertices[0]};queue=deque([vertices[0]]);tree=[]
while queue:
    v=queue.popleft()
    for w,e in sorted(adj[v],key=str):
        if w not in visited:
            visited.add(w);queue.append(w);tree.append(e)
assert len(visited)==13 and len(tree)==12
non_tree=[e for e in edges if e not in tree]
assert len(non_tree)==6
adj_tree={v:[] for v in vertices}
for edge in tree:
    a,b=edge
    adj_tree[a].append((b,edge));adj_tree[b].append((a,edge))
cycles=[]
for edge in non_tree:
    a,b=edge
    queue=deque([b]);parents={b:None}
    while queue and a not in parents:
        x=queue.popleft()
        for w,f in adj_tree[x]:
            if w not in parents:
                parents[w]=(x,f);queue.append(w)
    c=sp.zeros(18,1);c[edge_idx[edge]]=1
    x=a
    while x!=b:
        parent,te=parents[x]
        c[edge_idx[te]]+=1 if te==(parent,x) else -1
        x=parent
    cycles.append(c)
B=sp.Matrix.hstack(*cycles)
# Chain boundary must vanish. Each non-tree edge coordinate gives identity.
boundary=sp.zeros(13,18)
for j,(a,b) in enumerate(edges):
    boundary[vertices.index(a),j]=-1
    boundary[vertices.index(b),j]=1
assert boundary*B==sp.zeros(13,6)
assert sp.Matrix([[B[edge_idx[e],j] for j in range(6)] for e in non_tree])==sp.eye(6)

def image_vertex(v,p):
    typ,x=v
    if typ=='v':return (typ,p[x])
    if typ=='e':return (typ,tuple(sorted(p[a] for a in x)))
    return (typ,tuple(sorted(tuple(sorted(p[a] for a in e)) for e in x)))

def action(p):
    A=sp.zeros(18)
    for e in edges:
        a,b=e
        x,y=image_vertex(a,p),image_vertex(b,p)
        image_edge=tuple(sorted((x,y),key=str))
        A[edge_idx[image_edge],edge_idx[e]]=1 if (x,y)==image_edge else -1
    F=sp.Matrix([[ (A*B)[edge_idx[e],j] for j in range(6)] for e in non_tree])
    assert A*B==B*F
    return F
permutations=list(it.permutations(range(4)))
F_all={p:action(p) for p in permutations}
for p in permutations:
    assert F_all[p].det() in (-1,1)
    for r in permutations:
        composition=tuple(p[r[i]] for i in labels)
        assert F_all[p]*F_all[r]==F_all[composition]

# Klein-four eigenspaces over Q; each rank-two lattice has a primitive basis.
D=[(1,0,3,2),(2,3,0,1),(3,2,1,0)]
W=[sp.Matrix([[0,1],[1,0],[0,0],[1,0],[0,0],[0,1]]),
   sp.Matrix([[0,-1],[-1,0],[0,0],[1,0],[0,-2],[0,1]]),
   sp.Matrix([[0,-1],[-1,0],[-2,0],[1,0],[0,0],[0,1]])]
for i in range(3):
    assert W[i].rank()==2
    for j in range(3):
        assert F_all[D[j]]*W[i]==(1 if i==j else -1)*W[i]
    assert sp.gcd_list([int(W[i][a,0]*W[i][b,1]-W[i][b,0]*W[i][a,1])
                        for a,b in it.combinations(range(6),2)])==1
C=sp.Matrix.hstack(*W)
assert abs(C.det())==16
assert all(v.q==1 for v in (2*C.inv()))
assert smith_normal_form(C,domain=ZZ).diagonal()==sp.diag(1,1,2,2,2,2).diagonal()

# Explicit integral conjugacies for all five possible Frobenius classes.
I=sp.eye(6)
e=[I[:,i] for i in range(6)]
classes={
    '1^4':(0,1,2,3),
    '2 1^2':(1,0,2,3),
    '2^2':(1,0,3,2),
    '3 1':(1,2,0,3),
    '4':(1,2,3,0)}
seeds={
    '1^4':I,
    '2 1^2':sp.Matrix.hstack(e[0],e[3],e[1],e[5],e[2],-e[4]),
    '2^2':sp.Matrix.hstack(e[0],e[5],e[1],e[3],e[2],e[4])}
F3=F_all[classes['3 1']]
seeds['3 1']=sp.Matrix.hstack(e[0],F3*e[0],F3**2*e[0],e[1],F3*e[1],F3**2*e[1])
F4=F_all[classes['4']]
a=sp.Matrix([-1,-1,-1,-1,1,-1]);b=sp.Matrix([-1,-1,-1,0,0,0])
seeds['4']=sp.Matrix.hstack(a,F4*a,F4**2*a,F4**3*a,b,F4*b)
rot2=sp.Matrix([[0,-1],[1,0]])
def shift(d):
    X=sp.zeros(d)
    for i in range(d):X[(i+1)%d,i]=1
    return X
normal={
    '1^4':I,
    '2 1^2':sp.diag(shift(2),shift(2),shift(2)),
    '2^2':sp.diag(shift(2),shift(2),-1,-1),
    '3 1':sp.diag(shift(3),shift(3)),
    '4':sp.diag(shift(4),rot2)}
for label,p in classes.items():
    F=F_all[p];U=seeds[label]
    assert abs(U.det())==1, (label,U.det())
    assert F*U==U*normal[label]
    for q in (2,3,5,7,11,13,17):
        diag=smith_normal_form(q*I-F,domain=ZZ).diagonal()
        actual=[abs(int(x)) for x in diag if abs(int(x))>1]
        expected={
            '1^4':[q-1]*6,
            '2 1^2':[q*q-1]*3,
            '2^2':[q+1]*2+[q*q-1]*2,
            '3 1':[q**3-1]*2,
            '4':[q*q+1,q**4-1]}[label]
        assert actual==[v for v in expected if v>1],(label,q,actual,expected)
    print(label,'F-characteristic=',sp.factor(F.charpoly().as_expr()),'unimodular-basis-det=',U.det())
# Point counting by normalization: (#fixed six lines)*(q+1) - (#fixed branches) + (#fixed singular points)
point_factors={}
for label,p in classes.items():
    fixed_lines=sum(tuple(sorted(p[i] for i in e))==e for e in lines)
    fixed_singular=sum(p[i]==i for i in labels)+sum(image_vertex(('m',m),p)==('m',m) for m in diagonals)
    fixed_branches=sum(image_vertex(a,p)==a and image_vertex(b,p)==b for a,b in edges)
    point_factors[label]=(fixed_lines,fixed_singular,fixed_branches)
print('fixed (lines, singular, branches)',point_factors)
assert point_factors=={'1^4':(6,7,18),'2 1^2':(2,3,4),'2^2':(2,3,2),'3 1':(0,1,0),'4':(0,1,0)}
print('QUADRANGLE_FROBENIUS_INTEGRAL_LATTICE_OK')
