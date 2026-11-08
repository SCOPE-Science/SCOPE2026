#!/usr/bin/env python3
"""Exact finite checks of polygonal moment-angle dihedral cohomology characters.

Uses only Python standard library. Coordinates are 0,...,n-1; the cycle has
edges {i,i+1 mod n}; dihedral symmetries send i to i+a or a-i mod n.
"""
from itertools import combinations
from math import comb, gcd


def parity(permutation):
    seen = [False] * len(permutation)
    cycles = 0
    for i in range(len(permutation)):
        if not seen[i]:
            cycles += 1
            j = i
            while not seen[j]:
                seen[j] = True
                j = permutation[j]
    return (-1) ** (len(permutation) - cycles)


def restricted_parity(p, entries):
    ordered = sorted(entries)
    ix = {x: i for i, x in enumerate(ordered)}
    assert set(map(lambda i: p[i], ordered)) == set(ordered)
    return parity([ix[p[i]] for i in ordered])


def sym(n, a, reflected):
    return [(a - i) % n if reflected else (a + i) % n for i in range(n)]


def component_action_trace(n, subset, p):
    I = set(subset)
    remaining = set(subset)
    components = []
    while remaining:
        node = min(remaining)
        remaining.remove(node)
        stack = [node]
        comp = {node}
        while stack:
            v = stack.pop()
            for w in ((v - 1) % n, (v + 1) % n):
                if w in remaining:
                    remaining.remove(w)
                    comp.add(w)
                    stack.append(w)
        components.append(comp)
    fixed = sum({p[v] for v in comp} == comp for comp in components)
    return restricted_parity(p, I) * (fixed - 1)


def dga_action_trace(n, subset, p):
    I = set(subset)
    if {p[i] for i in I} != I:
        return 0
    trace0 = restricted_parity(p, I)
    trace1 = sum(restricted_parity(p, I - {i}) for i in I if p[i] == i)
    trace2 = 0
    for i in I:
        j = (i + 1) % n
        if j in I and {p[i], p[j]} == {i, j}:
            trace2 += restricted_parity(p, I - {i, j})
    return trace1 - trace0 - trace2


def coefficient(A, k):
    return A[k] if k < len(A) else 0


def mul(A, B):
    ans = [0] * (len(A) + len(B) - 1)
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            ans[i+j] += a*b
    return ans


def powpoly(A, exponent):
    v = [1]
    for _ in range(exponent):
        v = mul(v, A)
    return v


def reflection_poly(n, axis):
    if n % 2:
        return [-x for x in mul(powpoly([1,0,-1],(n-3)//2),[1,0,0,1])]
    if axis % 2 == 0:
        return [-x for x in powpoly([1,0,-1], n//2)]
    return [-x for x in mul(powpoly([1,0,-1],n//2-1),[1,0,1])]


def predicted(n, k, a, reflected):
    if reflected:
        return coefficient(reflection_poly(n,a),k)
    if a == 0:
        return (k-1)*comb(n,k)-n*comb(n-2,k-2)
    d=n//gcd(n,a)
    if k%d: return 0
    return -((-1)**((d-1)*(k//d))) * comb(n//d,k//d)


def dcell(n, vset, uset):
    """Differential in a multigraded squarefree Koszul block."""
    out={}
    U=sorted(uset)
    V=set(vset)
    for t,j in enumerate(U):
        W=V|{j}
        if len(W)>2: continue
        if len(W)==2:
            x,y=sorted(W)
            if (y-x)%n not in (1,n-1):continue
        key=(frozenset(W),frozenset(set(U)-{j}))
        out[key]=out.get(key,0)+(-1)**t
    return out


def gcell(vset, uset, p):
    U=sorted(uset)
    after=[p[i] for i in U]
    ordered=sorted(after)
    rank={x:i for i,x in enumerate(ordered)}
    e=parity([rank[z] for z in after])
    return (frozenset(p[i] for i in vset), frozenset(after)),e


def check_equivariance(n, p, vset, uset):
    A=dcell(n,vset,uset)
    left={}
    for (V,U),coef in A.items():
        key,e=gcell(V,U,p)
        left[key]=left.get(key,0)+coef*e
    key,e=gcell(vset,uset,p)
    right={k:coef*e for k,coef in dcell(n,*key).items()}
    assert left==right,('dga equivariance',n,p,vset,uset,left,right)


def top_character(n, a, reflected):
    p=sym(n,a,reflected)
    return parity(p)*(-1 if reflected else 1)

if __name__=='__main__':
    trace_tests=0
    equivariance_tests=0
    lefschetz_tests=0
    quotient_tests=0
    # Independent fixed-component and Koszul-cell calculations.
    for n in range(4,12):
        for reflected in (False, True):
            for a in range(n):
                p=sym(n,a,reflected)
                for k in range(2,n-1):
                    total_components=0
                    total_cells=0
                    for subset in combinations(range(n),k):
                        if {p[i] for i in subset} == set(subset):
                            total_components+=component_action_trace(n,subset,p)
                            total_cells+=dga_action_trace(n,subset,p)
                    value=predicted(n,k,a,reflected)
                    assert total_components==total_cells==value, ('character',n,k,a,reflected,total_components,total_cells,value)
                    trace_tests+=1
                alt=1+sum((-1)**(k+1)*predicted(n,k,a,reflected) for k in range(2,n-1))
                alt+=(-1)**(n+2)*top_character(n,a,reflected)
                assert alt==0,('lefschetz',n,a,reflected,alt)
                lefschetz_tests+=1
    # Direct Koszul differential equivariance, not using component counts.
    for n in range(4,9):
        for reflected in (False, True):
            for a in range(n):
                p=sym(n,a,reflected)
                for k in range(2,n-1):
                    for I in combinations(range(n),k):
                        check_equivariance(n,p,(),I)
                        equivariance_tests+=1
                        for i in I:
                            check_equivariance(n,p,(i,),set(I)-{i})
                            equivariance_tests+=1
    # Independently compute top action from the full-support Koszul cochains.
    for n in range(4,20):
        I=set(range(n))
        for reflected in (False,True):
            for a in range(n):
                p=sym(n,a,reflected)
                t0=restricted_parity(p,I)
                t1=sum(restricted_parity(p,I-{i}) for i in I if p[i]==i)
                t2=sum(restricted_parity(p,I-{i,(i+1)%n})
                       for i in range(n)
                       if {p[i],p[(i+1)%n]}=={i,(i+1)%n})
                assert t2-t1+t0==top_character(n,a,reflected),('top dga',n,a,reflected)
    # Exact all-degree transfer average and rational top class.
    for n in range(4,27):
        for k in range(2,n-1):
            s=sum(predicted(n,k,a,refl) for refl in (False,True) for a in range(n))
            assert s%(2*n)==0 and s>=0, ('quotient',n,k,s)
            quotient_tests+=1
        tops=sum(top_character(n,a,refl) for refl in (False,True) for a in range(n))//(2*n)
        assert tops==(1 if n%4==3 else 0),('top quotient',n,tops)
    print('POLYGON_HIGH_DIHDERAL_COHOMOLOGY_PASS')
    print('independent_fixed_component_and_Koszul_character_checks',trace_tests)
    print('direct_Koszul_equivariance_checks',equivariance_tests)
    print('graded_Lefschetz_checks',lefschetz_tests)
    print('integral_transfer_average_checks',quotient_tests)
    print('full_support_top_Koszul_character_checks',sum(2*n for n in range(4,20)))
    print('top_rational_quotient_class_nonzero_iff_n_mod_4_equals_3')
    for n in (7,8,9,10,11):
        values=[sum(predicted(n,k,a,refl) for refl in (False,True) for a in range(n))//(2*n) for k in range(4,n-1)]
        print('n',n,'higher_degree_quotient_betti',values)
