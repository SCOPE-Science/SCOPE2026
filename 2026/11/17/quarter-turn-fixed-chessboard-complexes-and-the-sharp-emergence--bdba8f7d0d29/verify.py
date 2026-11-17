#!/usr/bin/env python3
"""Exact finite checks for quarter-turn fixed square-chessboard complexes.

Dependencies: Python 3.10+ and SymPy 1.14.0 (only for integer Smith forms).
The general geometric and homotopy statements require the proof in RESULT.md.
"""
import itertools
import json
from math import comb, factorial
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def qrotate(p,n):
    i,j=p
    return (j,n-1-i)


def rooks_ok(cells):
    return len(cells)==len({i for i,j in cells})==len({j for i,j in cells})


def orbits(n):
    seen=set(); ans=[]
    for x in itertools.product(range(n),repeat=2):
        if x in seen: continue
        o=[]; y=x
        while y not in o:
            o.append(y); y=qrotate(y,n)
        assert y==x
        seen.update(o)
        ans.append(frozenset(o))
    return ans


def direct_quotient(n):
    allowed=[o for o in orbits(n) if rooks_ok(o)]
    for i,o in enumerate(allowed):
        assert len(o)==(1 if (n%2 and len(o)==1) else 4)
        for j in range(i):
            # A pair of orbit vertices spans an edge iff both orbits together are rooks.
            assert (rooks_ok(o|allowed[j])) == (not bool({a for a,b in o}&{a for a,b in allowed[j]}))
    m=n//2
    if n%2:
        centers=[o for o in allowed if len(o)==1]
        others=[o for o in allowed if len(o)==4]
        assert centers==[frozenset({(m,m)})]
        assert len(others)==2*comb(m,2)
        assert all(rooks_ok(centers[0]|o) for o in others)
        allowed=others
    
    labels=[]
    for o in allowed:
        used={a for a,b in o}
        assert len(used)==4
        pairs=tuple(sorted({min(a,n-1-a) for a in used}))
        assert len(pairs)==2
        labels.append(pairs)
    from collections import Counter
    c=Counter(labels)
    assert (len(c)==comb(m,2) and set(c.values())=={2}) if m>=2 else len(allowed)==0
    for i,j in itertools.combinations(range(len(allowed)),2):
        # Compare independently computed cell attacks to the edge-disjoint rule.
        assert rooks_ok(allowed[i]|allowed[j]) == set(labels[i]).isdisjoint(labels[j])
    f=[0]*(m//2)
    candidates=[(i,j,t) for i in range(m) for j in range(i+1,m) for t in range(2)]
    def extend(start,occupancy,length):
        if length: f[length-1]+=1
        for k in range(start,len(candidates)):
            i,j,t=candidates[k]
            bits=(1<<i)|(1<<j)
            if not occupancy&bits:
                extend(k+1,occupancy|bits,length+1)
    extend(0,0,0)
    expected=[factorial(m)//(factorial(m-2*k)*factorial(k)) for k in range(1,m//2+1)]
    assert f==expected, (n,f,expected)
    if n%2:
        cone_faces=[(f[k]+(f[k-1] if k>0 else 1)) for k in range(len(f))]+([f[-1]] if f else [1])
        return {'n':n,'allowed_orbits':len(allowed)+1,'model':'cone-on-twofold-inflated-matching-complex','f_vector':cone_faces}
    return {'n':n,'allowed_orbits':len(allowed),'model':'twofold-inflated-matching-complex','f_vector':f}


def matching_faces(m):
    edges=list(itertools.combinations(range(m),2))
    arr=[[] for _ in range(m//2)]
    def rec(start,used,face):
        if face: arr[len(face)-1].append(tuple(face))
        for i in range(start,len(edges)):
            a,b=edges[i]
            if a not in used and b not in used:
                rec(i+1,used|{a,b},face+[i])
    rec(0,set(),[])
    return arr


def boundary(faces_prev, faces_curr):
    idx={f:i for i,f in enumerate(faces_prev)}
    M=[[0]*len(faces_curr) for _ in faces_prev]
    for j, f in enumerate(faces_curr):
        for k in range(len(f)):
            M[idx[f[:k]+f[k+1:]]][j]=(-1)**k
    return Matrix(M)


def smith_diagonal(A):
    S=smith_normal_form(A,domain=ZZ)
    a=[int(S[i,i]) for i in range(min(S.rows,S.cols)) if S[i,i]]
    return sorted(abs(i) for i in a)


def ordinary_matching_snf(m):
    fs=matching_faces(m)
    fsizes=[len(a) for a in fs]
    if not fs: return {'m':m,'face_counts':[],'boundary_snf':[]}
    # Boundary in dimension 0 is augmentation onto C_{-1} of rank 1.
    lists=[];prev=[()]
    for faces in fs:
        if len(faces)==0: continue
        B=boundary(prev,faces)
        diag=smith_diagonal(B)
        lists.append({'rank':len(diag),'nonunit_factors':[x for x in diag if x!=1]})
        prev=faces
    return {'m':m,'face_counts':fsizes,'boundary_snf':lists}


def main():
    odd=[direct_quotient(n) for n in range(1,14,2)]
    even=[direct_quotient(n) for n in range(2,15,2)]
    snf=[ordinary_matching_snf(m) for m in range(2,8)]
    # M7 is connected, has 21 vertices, 105 edges, 105 triangles,
    # augmented boundary ranks 1,20,84 with a single diagonal 3 on d2.
    x=snf[-1]
    assert x['face_counts']==[21,105,105]
    assert [b['rank'] for b in x['boundary_snf']]==[1,20,85], x
    assert x['boundary_snf'][-1]['nonunit_factors']==[3], x
    # Strictly integral computation supplies the rank/torsion input to the inflation formula.
    # M7 second homology rank is 105-85=20, in agreement with the literature.
    out={'odd':odd,'even':even,'ordinary_matching_smith':snf}
    print(json.dumps(out,indent=2))
    print('QUARTER_TURN_CHESSBOARD_EXACT_CHECK_PASS')

if __name__=='__main__':
    main()
