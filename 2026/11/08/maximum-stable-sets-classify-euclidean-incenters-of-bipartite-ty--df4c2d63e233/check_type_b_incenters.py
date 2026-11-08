"""Reproducibility checks for Type-B graph-root Euclidean inballs.

All claims for arbitrary graphs in the accompanying proof are analytic;
this script provides finite independently implemented checks only.
Requires Python 3, NumPy and SciPy.
"""
from itertools import combinations, product
from math import sqrt
import numpy as np
from scipy.spatial import ConvexHull
from scipy.optimize import linprog


def independent_sets(n, edges):
    E=[(1<<i)|(1<<j) for i,j in edges]
    return [mask for mask in range(1<<n) if all(mask&e!=e for e in E)]

def maximal_independent_sets(n, edges):
    sets=independent_sets(n,edges)
    return [s for s in sets if not any((s!=t and s&t==s) for t in sets)]

def signed_incidence(n,mask):
    ix=[j for j in range(n) if mask>>j&1]
    for signs in product((-1,1), repeat=len(ix)):
        a=np.zeros(n)
        for j,v in zip(ix,signs): a[j]=v
        yield a

def proof_predictions(n, edges):
    mis=maximal_independent_sets(n,edges)
    alpha=max(s.bit_count() for s in mis)
    maxunion=0
    for s in mis:
        if s.bit_count()==alpha: maxunion|=s
    return mis, alpha, n-maxunion.bit_count()

def convex_hull_check(n,edges):
    roots=[]
    for i,j in edges:
        for a,b in product((-1,1),repeat=2):
            v=np.zeros(n);v[i]=a;v[j]=b;roots.append(v)
    P=ConvexHull(np.array(roots))
    mis,alpha,dim=proof_predictions(n,edges)
    # A simplex normal row is (a,b) with facet a.x+b <= 0.
    # The standard Euclidean distance is -b/||a||.
    distances=-P.equations[:,-1]/np.linalg.norm(P.equations[:,:-1],axis=1)
    assert abs(distances.min()-1/sqrt(alpha))<1e-8,(n,edges,alpha,distances.min())
    # Vertices of polar should be exactly the signed maximal stable sets.
    Qverts=np.array([x for s in mis for x in signed_incidence(n,s)])
    Qhull=ConvexHull(Qverts)
    assert len(Qverts)==len(Qhull.vertices)
    # Every root is bounded by signed maximal-independent-set inequalities.
    assert max(np.max(Qverts@v) for v in roots)==1
    # The squared polar circumradius equals independence number.
    assert set(np.sum(Qverts**2,axis=1).astype(int))==set(s.bit_count() for s in mis)
    return len(P.simplices),len(Qverts),dim

def all_tree_edges(n):
    if n==2:
        yield [(0,1)];return
    for code in product(range(n),repeat=n-2):
        deg=[1]*n
        for u in code:deg[u]+=1
        result=[]
        for u in code:
            v=next(i for i in range(n) if deg[i]==1)
            result.append((u,v));deg[u]-=1;deg[v]-=1
        a,b=[i for i in range(n) if deg[i]==1]
        result.append((a,b))
        yield result

def check_path_centers(n):
    edges=[(j,j+1) for j in range(n-1)]
    mis,alpha,dim=proof_predictions(n,edges)
    assert alpha==(n+1)//2
    assert dim==(0 if n%2==0 else n//2)
    r=1/sqrt(alpha)
    q=np.array([x for s in mis for x in signed_incidence(n,s)])
    A=np.array([x for x in q]); b=np.array([1-r*np.linalg.norm(x) for x in q])
    # Polytope of incenters: A*c<=b.
    if n%2:
        k=n//2
        delta=1-sqrt(k/(k+1))
        rng=np.random.default_rng(7+n)
        for i in range(2*k):
            v=np.zeros(n)
            v[2*(i//2)+1]=delta*(1 if i%2 else -1)
            assert np.max(A@v-b)<1e-9
        for c in rng.normal(size=(40,n)):
            opt=linprog(-c,A_ub=A,b_ub=b,bounds=[(None,None)]*n,method='highs')
            assert opt.success, opt.message
            expected=delta*max(abs(c[j]) for j in range(1,n,2))
            assert abs(-opt.fun-expected)<1e-8,(n,opt.fun,expected)
    else:
        for j in range(n):
            for s in [-1,1]:
                c=np.zeros(n);c[j]=s
                opt=linprog(-c,A_ub=A,b_ub=b,bounds=[(None,None)]*n,method='highs')
                assert opt.success and abs(opt.fun)<1e-9

def main():
    checked=0
    for n in range(2,8):
        for edges in all_tree_edges(n):
            mis,alpha,d=proof_predictions(n,edges)
            assert d<= (n-1)//2,(n,edges,d)
            checked+=1
        print('tree census n=',n,'total checked=',checked)
    for n in range(2,11):
        check_path_centers(n)
    samples=[[(i,i+1) for i in range(n-1)] for n in range(2,6)]
    samples += [[(0,j) for j in range(1,n)] for n in range(3,6)]
    samples += [[(0,1),(1,2),(2,3),(3,0)]]
    total_facets=0
    for ed in samples:
        n=max(max(x) for x in ed)+1
        facets,qverts,dim=convex_hull_check(n,ed)
        total_facets+=facets
    for k in range(2,9):
        n=2*k
        # odd path on 2k-1 vertices plus a leaf at vertex index 1
        e=[(i,i+1) for i in range(n-2)]+[(1,n-1)]
        mis,a,d=proof_predictions(n,e)
        assert a==k+1 and d==k-1,(k,a,d)
    print('TYPE_B_INCENTER_CHECKS_PASSED', 'trees',checked,'convexhull_facets',total_facets, 'paths',9,'extremizers',7)

if __name__=='__main__':main()
