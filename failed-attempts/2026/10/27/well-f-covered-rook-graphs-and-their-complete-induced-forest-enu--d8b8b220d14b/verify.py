#!/usr/bin/env python3
"""Independent finite validation for induced-forest counts of rook graphs."""
from collections import Counter
from functools import lru_cache
from math import comb, factorial
from fractions import Fraction

@lru_cache(None)
def recurrence(p,q):
    """Count selected cells using component of first row-vertex in K_{p,q}."""
    if p == 0:
        return {0: 1}
    ans=Counter(recurrence(p-1,q))  # designated vertex isolated
    for a in range(1,p+1):
        for b in range(1,q+1):
            if abs(a-b)>1: continue
            path_count=factorial(a)*factorial(b) if a==b else factorial(a)*factorial(b)//2
            factor=comb(p-1,a-1)*comb(q,b)*path_count
            for k,v in recurrence(p-a,q-b).items():
                ans[k+a+b-1]+=factor*v
    return dict(ans)

def induced_forest(mask,p,q):
    """Check acyclicity in induced rook graph directly, not its incidence picture."""
    vertices=[(i,j) for i in range(p) for j in range(q) if mask>> (i*q+j)&1]
    m=len(vertices)
    adj=[[] for _ in vertices]
    for a in range(m):
        for b in range(a+1,m):
            if vertices[a][0]==vertices[b][0] or vertices[a][1]==vertices[b][1]:
                adj[a].append(b); adj[b].append(a)
    marked=set()
    for start in range(m):
        if start in marked: continue
        stack=[(start,-1)]
        while stack:
            u, parent=stack.pop()
            if u in marked:return False
            marked.add(u)
            for v in adj[u]:
                if v!=parent:stack.append((v,u))
    return True

def maximum_formula(p,q):
    p,q=sorted((p,q))
    if p==q:return factorial(p)**2
    return explicit_integer_sum(p,q)

def explicit_integer_sum(p,q):
    return int(factorial(p)*factorial(q)*sum((Fraction(comb(p-1,c-1),2**c*factorial(c)*factorial(q-p-c)) for c in range(1,min(p,q-p)+1)),Fraction(0)))

def max_component_profile(p,q):
    p,q=sorted((p,q))
    if p==q:return {1: factorial(p)**2}
    return {c: int(Fraction(factorial(p)*factorial(q)*comb(p-1,c-1), 2**c*factorial(c)*factorial(q-p-c)))
            for c in range(1,min(p,q-p)+1)}

def component_count(mask,p,q):
    selected=[i for i in range(p*q) if (mask>>i)&1]
    todo=set(selected); c=0
    while todo:
        c+=1; start=todo.pop(); stack=[start]
        while stack:
            u=stack.pop(); row,col=divmod(u,q)
            neighbors=[v for v in list(todo) if v//q==row or v%q==col]
            for v in neighbors:todo.remove(v);stack.append(v)
    return c

def run():
    total=0
    for p,q in [(1,1),(1,4),(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4)]:
        pred=recurrence(p,q)
        obs=Counter(); obsmax=Counter(); good=set(); predicted_max_degree=min(2*min(p,q),p+q-1)
        for mask in range(1<<(p*q)):
            if induced_forest(mask,p,q):
                good.add(mask)
                obs[mask.bit_count()]+=1
                if mask.bit_count()==predicted_max_degree:
                    obsmax[component_count(mask,p,q)]+=1
        maximal=[mask for mask in good if not any((mask | (1<<v)) in good for v in range(p*q) if not (mask>>v)&1)]
        assert len(maximal)==pred[predicted_max_degree],(p,q,len(maximal),pred[predicted_max_degree])
        assert all(m.bit_count()==predicted_max_degree for m in maximal),(p,q, [m for m in maximal if m.bit_count()!=predicted_max_degree][:4])
        assert dict(obs)==pred,(p,q,dict(obs),pred)
        mx=max(k for k,v in pred.items() if v)
        assert mx==predicted_max_degree, (p,q,mx)
        assert dict(obsmax)==max_component_profile(p,q),(p,q,dict(obsmax),max_component_profile(p,q))
        assert pred[mx]==maximum_formula(p,q),(p,q,pred[mx],maximum_formula(p,q))
        total+=1<<(p*q)
        print(f'{p}x{q}: degree={mx}, maximum_sets={pred[mx]}, inclusion_maximal_sets={len(maximal)}, total_forests={sum(obs.values())}, max_components={dict(sorted(obsmax.items()))}, coefficients={dict(sorted(obs.items()))}')
    print(f'PASS; boards=10, directly checked subsets={total}')
if __name__=='__main__': run()
