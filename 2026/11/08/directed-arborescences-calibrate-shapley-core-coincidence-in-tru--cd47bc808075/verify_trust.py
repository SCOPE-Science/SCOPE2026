"""Direct finite checks of the trust-game calibration theorem.
Uses exact rational arithmetic and direct coalition/permutation enumeration.
"""
from fractions import Fraction as F
from itertools import permutations, product
from random import Random
from math import factorial

def indegrees(n,edges):
    return [sum(v==i for u,v in edges) for i in range(n)]

def v_direct(n,edges,b,mask):
    total=F(0)
    for u,v in edges:
        if mask>>u&1 and mask>>v&1:
            total+=b[v]
    for v in range(n):
        if mask>>v&1 and any(w==v and not mask>>u&1 for u,w in edges):
            total+=b[v]
    return total

def shapley(n,edges,b):
    coal=[v_direct(n,edges,b,s) for s in range(1<<n)]
    res=[F(0)]*n
    for order in permutations(range(n)):
        mask=0
        for i in order:
            new=mask | 1<<i
            res[i]+=coal[new]-coal[mask]
            mask=new
    return [x/F(factorial(n)) for x in res]

def pred(n,edges,b):
    d=indegrees(n,edges)
    t=[b[i]*F(d[i]-1,2*(d[i]+1)) for i in range(n)]
    return [d[i]*b[i]-d[i]*t[i]+sum(t[j] for u,j in edges if u==i) for i in range(n)]

def null_stationary(n,edges):
    d=indegrees(n,edges)
    mat=[[F(int(i==j)) - sum((F(1,d[j]) for u,v in edges if u==i and v==j),F(0)) for j in range(n)]+[F(0)] for i in range(n-1)]
    mat.append([F(1)]*n+[F(1)])
    for col in range(n):
        pivot=next((r for r in range(col,n) if mat[r][col]),None)
        assert pivot is not None, 'stationary uniqueness failed'
        mat[pivot],mat[col]=mat[col],mat[pivot]
        divisor=mat[col][col]
        mat[col]=[z/divisor for z in mat[col]]
        for r in range(n):
            if r!=col:
                mul=mat[r][col]
                mat[r]=[mat[r][k]-mul*mat[col][k] for k in range(n+1)]
    return [mat[i][-1] for i in range(n)]

def connected(n,edges):
    for direction in [True,False]:
        seen={0};changed=True
        while changed:
            old=len(seen)
            for u,v in edges:
                a,c=(u,v) if direction else (v,u)
                if a in seen:seen.add(c)
            changed=len(seen)!=old
        if len(seen)!=n:return False
    return True

def check(n,edges,b):
    phi=shapley(n,edges,b)
    formula=pred(n,edges,b)
    assert phi==formula,(n,edges,b,phi,formula)
    core=[indegrees(n,edges)[i]*b[i] for i in range(n)]
    assert sum(core)==v_direct(n,edges,b,(1<<n)-1)
    assert all(sum(core[i] for i in range(n) if s>>i&1)>=v_direct(n,edges,b,s) for s in range(1<<n))
    return phi

def outward_tree_count(n,edges,root):
    choices=[[u for u,v in edges if v==w] for w in range(n) if w!=root]
    if any(not c for c in choices):return 0
    vertices=[w for w in range(n) if w!=root]
    cnt=0
    for parent_choices in product(*choices):
        outgoing={w:[] for w in range(n)}
        for w,u in zip(vertices,parent_choices):outgoing[u].append(w)
        seen={root};stack=[root]
        while stack:
            for z in outgoing[stack.pop()]:
                if z not in seen:seen.add(z);stack.append(z)
        cnt+=len(seen)==n
    return cnt

def main():
    rng=Random(271828);checks=0;positive=0
    for n in [3,4]:
        all_edges=[(i,j) for i in range(n) for j in range(n) if i!=j]
        for bits in range(1<<len(all_edges)):
            edges=[e for k,e in enumerate(all_edges) if bits>>k&1]
            if min(indegrees(n,edges))<2:continue
            for _ in range(4):
                b=[F(rng.randrange(1,15),16) for i in range(n)]
                check(n,edges,b);checks+=1
            if connected(n,edges):
                d=indegrees(n,edges);g=null_stationary(n,edges)
                assert all(x>0 for x in g)
                b=[g[i]*F(2*(d[i]+1),d[i]*(d[i]-1)) for i in range(n)]
                core=[d[i]*b[i] for i in range(n)]
                assert check(n,edges,b)==core
                checks+=1;positive+=1
    tree_checks=0
    for n in [3,4]:
        all_edges=[(i,j) for i in range(n) for j in range(n) if i!=j]
        for bits in range(1<<len(all_edges)):
            edges=[e for k,e in enumerate(all_edges) if bits>>k&1]
            if min(indegrees(n,edges))<2:continue
            tau=[outward_tree_count(n,edges,i) for i in range(n)]
            d=indegrees(n,edges)
            assert all(d[i]*tau[i]==sum(tau[j] for u,j in edges if u==i) for i in range(n))
            if connected(n,edges):
                assert min(tau)>0
                b=[F(2*(d[i]+1)*tau[i],d[i]-1) for i in range(n)]
                b=[x/max(b) for x in b]
                assert check(n,edges,b)==[d[i]*b[i] for i in range(n)]
            tree_checks+=1
    for n in [5,6]:
        all_edges=[(i,j) for i in range(n) for j in range(n) if i!=j]
        for _ in range(75):
            edges=[e for e in all_edges if rng.randrange(4)!=0]
            if min(indegrees(n,edges))<2:continue
            b=[F(rng.randrange(1,31),32) for i in range(n)]
            check(n,edges,b);checks+=1
            if connected(n,edges):
                d=indegrees(n,edges);g=null_stationary(n,edges)
                b=[g[i]*F(2*(d[i]+1),d[i]*(d[i]-1)) for i in range(n)]
                assert all(x>0 for x in b)
                assert check(n,edges,b)==[d[i]*b[i] for i in range(n)]
                checks+=1;positive+=1
    edges=[(i,j) for i in range(4) for j in range(4) if i!=j and (i,j) not in [(0,1),(1,2),(2,0)]]
    g=null_stationary(4,edges)
    d=indegrees(4,edges)
    b=[g[i]*F(2*(d[i]+1),d[i]*(d[i]-1)) for i in range(4)]
    assert g==[F(2,9),F(2,9),F(2,9),F(1,3)]
    assert b==[F(2,3),F(2,3),F(2,3),F(4,9)]
    assert check(4,edges,b)==[F(4,3),F(4,3),F(4,3),F(4,3)]
    checks+=1
    print(f'EXACT_CHECKS_OK graph_parameter_checks={checks} calibrated_strongly_connected={positive} tree_identities={tree_checks}')
    print('4-vertex calibration:',list(map(str,b)),'core/Shapley:',list(map(str,[d[i]*b[i] for i in range(4)])))
if __name__=='__main__':main()
