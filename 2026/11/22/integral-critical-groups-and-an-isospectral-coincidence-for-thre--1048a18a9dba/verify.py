#!/usr/bin/env python3
"""Exact critical groups of three geometric 12-line orchard arrangements.

The 19 labelled triples for each type are transcribed from
Bokowski--Pokora, arXiv:1607.05864v4, pp. 7--8, C2, C6 and C7.
No environment- or workflow-specific inputs are required.
"""
from itertools import combinations
from collections import Counter
from math import prod, gcd

TRIPLES = {
    'C2': [
        (1,2,3),(1,4,5),(1,6,7),(1,8,9),(1,10,11),
        (2,4,7),(2,6,9),(2,8,11),(2,10,12),(3,4,9),
        (3,5,7),(3,6,11),(3,8,12),(4,6,12),(4,8,10),
        (5,9,11),(7,9,10),(7,11,12),(5,6,8)],
    'C6': [
        (1,2,3),(1,4,5),(1,6,7),(1,8,9),(1,10,11),
        (2,4,7),(2,6,9),(2,8,11),(2,10,12),(3,4,9),
        (3,5,7),(3,6,11),(3,8,12),(4,6,8),(4,11,12),
        (5,6,10),(5,9,12),(7,9,11),(7,8,10)],
    'C7': [
        (1,2,3),(1,4,5),(1,6,7),(1,8,9),(1,10,11),
        (2,4,7),(2,6,9),(2,10,12),(3,4,9),(3,5,7),
        (3,6,8),(3,11,12),(4,6,11),(4,8,12),
        (5,6,10),(5,8,11),(5,9,12),(7,9,11),(7,8,10)]}

EXPECTED = {
    'C2': [2,2,6,6,6,6,6,6,672,37753632],
    'C6': [2,6,6,6,42,42,42,210,840,840],
    'C7': [2,6,6,6,42,42,42,210,840,840],
}

PRIMES = (2,3,5,7,61,307)

def build_graph(T):
    assert len(T)==19 and len(set(map(lambda t:tuple(sorted(t)),T)))==19
    for t in T: assert len(t)==3 and len(set(t))==3 and all(1<=a<=12 for a in t)
    counts=Counter(x for t in T for x in t)
    assert sorted(counts.values())==[4]*3+[5]*9
    used=Counter(tuple(sorted(p)) for t in T for p in combinations(t,2))
    assert len(used)==57 and set(used.values())=={1}
    ordinary=sorted(set(combinations(range(1,13),2))-set(used))
    assert len(ordinary)==9
    degrees_double=Counter(v for e in ordinary for v in e)
    assert sorted((counts.get(v,0),degrees_double.get(v,0)) for v in range(1,13))==[(4,3)]*3+[(5,1)]*9
    edges=[(line-1,12+i) for i,t in enumerate(T) for line in t]
    edges.extend((u-1,v-1) for u,v in ordinary)
    assert len(edges)==66
    N=31
    L=[[0]*N for _ in range(N)]
    for u,v in edges:
        L[u][u]+=1;L[v][v]+=1;L[u][v]-=1;L[v][u]-=1
    assert all(sum(row)==0 for row in L)
    assert all(L[i][i]>=3 for i in range(N))
    return L,ordinary

def reduced(L,removed):
    return [[x for j,x in enumerate(row) if j!=removed] for i,row in enumerate(L) if i!=removed]

def bareiss_det(M):
    a=[r[:] for r in M]
    n=len(a);d=1;sgn=1
    for i in range(n-1):
        if a[i][i]==0:
            j=next((j for j in range(i+1,n) if a[j][i]!=0),None)
            if j is None:return 0
            a[i],a[j]=a[j],a[i];sgn=-sgn
        pivot=a[i][i]
        for j in range(i+1,n):
            for k in range(i+1,n):
                val=a[j][k]*pivot-a[j][i]*a[i][k]
                assert val%d==0
                a[j][k]=val//d
        for j in range(i+1,n):a[j][i]=0
        d=pivot
    return sgn*a[-1][-1]

def vpmod(x,p,k):
    if x==0:return k
    v=0
    while v<k and x%p==0:x//=p;v+=1
    return v

def local_exponents(M,p,k=9):
    """Elementary row+column operations over Z/(p^k) detect Smith valuations."""
    n=len(M);q=p**k
    a=[[x%q for x in r] for r in M]
    vals=[]
    for j in range(n):
        pivot=min(((vpmod(a[r][c],p,k),r,c) for r in range(j,n) for c in range(j,n)),default=(k,j,j))
        v,r,c=pivot
        assert v<k,('inadequate modulus',p,v,j)
        a[j],a[r]=a[r],a[j]
        for row in a:row[j],row[c]=row[c],row[j]
        div=p**v;power=p**(k-v)
        unit=a[j][j]//div
        assert unit%p
        inv=pow(unit,-1,power)
        for rr in range(j+1,n):
            assert a[rr][j]%div==0
            multiplier=((a[rr][j]//div)*inv)%power
            if multiplier:
                for cc in range(j,n):
                    a[rr][cc]=(a[rr][cc]-multiplier*a[j][cc])%q
            assert a[rr][j]==0
        for cc in range(j+1,n):
            assert a[j][cc]%div==0
            multiplier=((a[j][cc]//div)*inv)%power
            if multiplier:
                for rr in range(j,n):
                    a[rr][cc]=(a[rr][cc]-multiplier*a[rr][j])%q
            assert a[j][cc]==0
        vals.append(v)
    return sorted(vals)

def factors_from_local(vals_by_p):
    n=len(next(iter(vals_by_p.values())))
    return [prod(p**vals_by_p[p][i] for p in vals_by_p) for i in range(n)]

def kron_det(L):
    # 19 trivalent exceptional components may be eliminated over Q.
    # 3 times the weighted Laplacian on 12 strict line components is integer.
    H=[]
    for i in range(11):
        row=[]
        for j in range(11):
            # remove line 12 as root
            val=3*L[i][j]
            for e in range(12,31):
                val-=L[i][e]*L[e][j]
            row.append(val)
        H.append(row)
    detH=bareiss_det(H)
    return (3**8)*detH,detH

def main():
    spectra={}
    graph_objects={}
    try:
        from sympy import Matrix,ZZ, factorint
        from sympy.matrices.normalforms import smith_normal_form
        have_sympy=True
    except ImportError:
        have_sympy=False
    for name,T in TRIPLES.items():
        L,ordinary=build_graph(T)
        A=reduced(L,0)
        det=bareiss_det(A)
        assert det>0
        checkdet,deth=kron_det(L)
        assert det==checkdet
        # A completely different root, and an exceptional-component root.
        assert bareiss_det(reduced(L,11))==det
        assert bareiss_det(reduced(L,30))==det
        loc={p:local_exponents(A,p) for p in PRIMES}
        smith=factors_from_local(loc)
        assert len(smith)==30 and prod(smith)==det
        assert all(smith[i+1]%smith[i]==0 for i in range(29))
        actual=[x for x in smith if x>1]
        assert actual==EXPECTED[name], (name,actual)
        if have_sympy:
            for root in (0,11,30):
                s=smith_normal_form(Matrix(reduced(L,root)),domain=ZZ)
                assert [abs(int(s[i,i])) for i in range(30)]==smith
            assert factorint(det)=={p:sum(v) for p,v in loc.items() if sum(v)>0}
            from sympy import Symbol
            t=Symbol('t')
            spectra[name]=Matrix(L).charpoly(t).as_expr()
        try:
            import networkx as nx
            G=nx.Graph()
            G.add_nodes_from(range(31))
            G.add_edges_from((i,j) for i in range(31) for j in range(i+1,31) if L[i][j]==-1)
            graph_objects[name]=G
        except ImportError:
            pass
        print(name,'v=31 e=66 g=36 ordinary=9', 'nontrivial=',actual)
        print('  determinant=',det,'H_det=',deth,'local=',{p:[v for v in vs if v] for p,vs in loc.items() if any(vs)})
    if have_sympy:
        from sympy import Symbol, expand
        t=Symbol('t')
        same=t*(t-7)**6*(t-3)**7*(t-2)**8*(t**3-19*t**2+107*t-155)*(t**3-17*t**2+85*t-120)**2
        assert expand(spectra['C6']-same)==0
        assert expand(spectra['C7']-same)==0
        assert expand(spectra['C2']-same)!=0
        print('C6/C7 identical Laplacian characteristic polynomials')
    if len(graph_objects)==3:
        import networkx as nx
        for x,y in (('C2','C6'),('C2','C7'),('C6','C7')):
            assert not nx.is_isomorphic(graph_objects[x],graph_objects[y])
        aut_counts={k:sum(1 for _ in nx.algorithms.isomorphism.GraphMatcher(g,g).isomorphisms_iter()) for k,g in graph_objects.items()}
        assert aut_counts=={'C2':2,'C6':12,'C7':36}
        print('nonisomorphic 31-vertex graphs; automorphism counts=',aut_counts)
    print('ORCHARD_B12_C2_C7_EXACT_INTEGRAL_COMPONENT_GROUPS_OK')
if __name__=='__main__':main()
