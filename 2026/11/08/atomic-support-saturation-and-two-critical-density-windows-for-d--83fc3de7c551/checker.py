#!/usr/bin/env python3
"""Independent finite checks for modal face-profile saturation of directed cups.
Only standard-library Python is used. Evaluates finite faces with the paper's
weak three-valued semantics; no external services or validation status implied.
"""
from itertools import product
from math import prod
from fractions import Fraction

U,F,T = -1,0,1

def neg(x):
    return U if x==U else 1-x

def conj(x,y):
    return U if U in (x,y) else int(x==T and y==T)

def make(types):
    # A vertex is represented as (color, local Boolean value, local index).
    vs=tuple((c,val,i) for c,vals in enumerate(types) for i,val in enumerate(vals))
    faces=[]
    for mask in range(1,1<<len(vs)):
        face=tuple(vs[j] for j in range(len(vs)) if mask & (1<<j))
        if len({v[0] for v in face})==len(face): faces.append(face)
    faces=tuple(faces)
    cidx={v:i for i,v in enumerate(vs)}
    variable_edges=tuple((x,y) for x in vs for y in vs if x[0]!=y[0])
    atype={v:(v[0],v[1]) for v in vs}
    sig={face:tuple(sorted(atype[x] for x in face)) for face in faces}
    return vs, faces, variable_edges, atype, sig

def census_formula(vs, edges):
    sizes={u:sum(1 for v in vs if (v[0],v[1])==u) for u in set((v[0],v[1]) for v in vs)}
    return prod((2**sizes[v]-1)**sizes[u]+1
                for u in sizes for v in sizes if u[0]!=v[0])

def modal_test(vs,faces,edges,atype,sig,mask):
    r={(x,y) for j,(x,y) in enumerate(edges) if mask>>j &1}
    r.update((x,x) for x in vs)
    support={x: frozenset(atype[y] for y in vs if (x,y) in r and x[0]!=y[0]) for x in vs}
    hom=all(support[x]==support[y] for x in vs for y in vs if atype[x]==atype[y])
    # Compute every vertex proposition, negations and nested modalities (sample basis).
    def atom(col,face):
        vv=[v for v in face if v[0]==col]
        return U if not vv else (T if vv[0][1] else F)
    def box(col,values):
        out={}
        for face in faces:
            xx=[v for v in face if v[0]==col]
            if not xx: out[face]=U;continue
            x=xx[0]
            accessible=[values[z] for z in faces if x in z and all((x,y) in r for y in z)]
            defined=[v for v in accessible if v!=U]
            out[face]= U if not defined else (F if F in defined else T)
        return out
    pa={face:atom(0,face) for face in faces}
    pb={face:atom(1,face) for face in faces} if len(set(x[0] for x in vs))>1 else pa
    fml=[pa,pb]
    for a in sorted(set(v[0] for v in vs)):
        for p in (pa,pb):
            fml.append(box(a,p))
            fml.append(box(a,{face:neg(q) for face,q in p.items()}))
    for a in sorted(set(v[0] for v in vs)):
        for b in sorted(set(v[0] for v in vs)):
            fml.append(box(a,box(b,pa)))
            fml.append(box(a,box(b,pb)))
    if hom:
        assert all(all(ff[face]==ff[other] for face in faces for other in faces
                       if sig[face]==sig[other]) for ff in fml), "Same-signature faces separated despite homogeneity"
    # Verify exact singleton modal test for all atom classes using diamond_a Lit_(b,value).
    for x in vs:
        for y in vs:
            if x[0]==y[0]: continue
            u=atype[y]
            def lit(face):
                vv=[z for z in face if z[0]==u[0]]
                return U if not vv else (T if atype[vv[0]]==u else F)
            litval={face:lit(face) for face in faces}
            diamond={face:neg(z) for face,z in box(x[0],{f:neg(z) for f,z in litval.items()}).items()}
            f=(x,)
            assert (diamond[f]==T)==(u in support[x]), "Diamond failed to identify target type"
    return hom

def check(types):
    vs,faces,edges,atype,sig=make(types)
    n=len(edges)
    if n>13: raise ValueError('enumeration too large')
    modal_ok=[modal_test(vs,faces,edges,atype,sig,mask) for mask in range(1<<n)]
    actual=sum(modal_ok)
    predicted=census_formula(vs,edges)
    assert actual==predicted,(types,actual,predicted)
    sizes={u:sum(1 for v in vs if (v[0],v[1])==u) for u in set((v[0],v[1]) for v in vs)}
    for p in [Fraction(1,3),Fraction(1,2),Fraction(2,3)]:
        brute=sum(p**mask.bit_count()*(1-p)**(n-mask.bit_count())
                  for mask,ok in enumerate(modal_ok) if ok)
        exact=prod((1-p)**(sizes[u]*sizes[v])+(1-(1-p)**sizes[v])**sizes[u]
                  for u in sizes for v in sizes if u[0]!=v[0])
        assert brute==exact,(types,p,brute,exact)
    print('CASE',types,'vertices',len(vs),'arrows',n,'faces',len(faces),'homogeneous',actual,'total',1<<n)

if __name__=='__main__':
    for case in [ [[0],[0]], [[0,0],[0]], [[0,0],[0,0]], [[0,0],[0,1]], [[0,1],[0,1]], [[0],[0],[0]] ]:
        check(case)
    print('ALL_CHECKS_OK')
