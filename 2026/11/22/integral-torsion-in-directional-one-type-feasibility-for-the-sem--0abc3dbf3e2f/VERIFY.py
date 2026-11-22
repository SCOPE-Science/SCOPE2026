"""Finite independent checks for the semigeneric one-type arc-feasibility Smith theorem.
Requires Python 3 and SymPy (tested with 1.13.1). No external data or network calls.
"""
from itertools import product
from collections import Counter
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def canonical_formula(k, old_n):
    """All existing-class types plus one representative of the fresh-class block."""
    types = [(i, dict(zip((j for j in range(k) if j != i), signs)))
             for i in range(k) for signs in product((0, 1), repeat=k-1)]
    z = len(types)
    mat = [[1]*(z+1) for _ in range(z+1)]
    for a, (i, alpha) in enumerate(types):
        for b, (j, beta) in enumerate(types):
            mat[a][b] = 0 if i == j else int(((int(i<j)+alpha[j]+beta[i]) % 2) == 1)
    return Matrix(mat), types


def predicted_snf(k, n):
    size = k * 2**(k-1) + 2**n
    if k == 1:
        return [1,1] + [0]*(size-2)
    if k == 2:
        return [1]*4+[3]+[0]*(size-5)
    assert k >= 3
    return ([1]*(2*k+1) + [2]*(k*k-2*k-1) + [2*(k+1)]
            + [0]*(size-k*k-1))


def compact_check():
    for k in range(1,6):
        C,_=canonical_formula(k,k)
        N=C.rows+(2**k-1)
        predicted=predicted_snf(k,k)
        D=smith_normal_form(C,domain=ZZ)
        measured=sorted([abs(int(D[i,i])) for i in range(D.rows) if D[i,i]!=0])
        assert measured==predicted[:len(measured)]
        assert N==len(predicted)
        print(f'SMITH k={k} compressed={C.rows} full={N} factors={Counter(predicted)}')


def make_base(class_sizes,flip_seed=0):
    cls=[]
    for i,s in enumerate(class_sizes):cls.extend([i]*s)
    n=len(cls)
    # Construct a nonconstant parity matrix on every pair of classes.
    bits={}
    for a in range(n):
        for b in range(a+1,n):
            if cls[a]==cls[b]:continue
            i,j=cls[a],cls[b]; low,high=min(i,j),max(i,j)
            ap = a if i==low else b
            bp = b if j==high else a
            orientation=( (ap*3+flip_seed*(low+1)+high)%2
                        ^ (bp*7+flip_seed*(high+1)+low)%2
                        ^ ((low*3+high+flip_seed)%2))
            bits[a,b] = orientation if i==low else 1-orientation
    return cls,bits


def legal(classes, arcs):
    # arcs[u,v] gives u->v for u<v and cross-class u,v; same class has no arc.
    nn=len(classes)
    by={}
    for u,c in enumerate(classes):by.setdefault(c,[]).append(u)
    for ca,xa in by.items():
        for cb,xb in by.items():
            if ca>=cb: continue
            for r in range(len(xa)):
                for t in range(r+1,len(xa)):
                    for s in range(len(xb)):
                        for v in range(s+1,len(xb)):
                            total=0
                            for u in (xa[r],xa[t]):
                                for w in (xb[s],xb[v]):
                                    bit=arcs[min(u,w),max(u,w)]
                                    if u>w:bit=1-bit
                                    total+=bit
                            if total%2:return False
    return True


def get_types(base_classes, base_arcs):
    n=len(base_classes); k=len(set(base_classes)); types=[]
    for c in range(k+1):
        old=[i for i in range(n) if base_classes[i]!=c]
        for patt in product((0,1),repeat=len(old)):
            ar=dict(base_arcs)
            for i,v in zip(old,patt):ar[i,n]=1-v
            if legal(base_classes+[c],ar):
                types.append((c,tuple(dict(zip(old,patt)).get(i,None) for i in range(n))))
    return types


def direct_arc(base_classes,base_arcs,x,y):
    n=len(base_classes);kx=len(set(base_classes)); cx,px=x;cy,py=y
    if cx==cy and cx<kx:return 0
    cy=cy if cy<kx else (kx+1 if cx==kx else kx)
    classes=base_classes+[cx,cy]
    arcs=dict(base_arcs)
    for i,p in enumerate(px):
        if p is not None:arcs[i,n]=1-p
    for i,p in enumerate(py):
        if p is not None:arcs[i,n+1]=1-p
    arcs[n,n+1]=1
    return int(legal(classes,arcs))


def check_direct():
    totals=0
    for sizes,seed in [([1],0),([2],0),([1,1],0),([2,1],1),
                       ([2,2],2),([1,1,1],0),([2,1,1],3),([1,1,1,1],1)]:
        cls,arcs=make_base(sizes,seed)
        assert legal(cls,arcs)
        types=get_types(cls,arcs)
        k=len(sizes);n=len(cls)
        assert len(types)==k*2**(k-1)+2**n,(sizes,len(types))
        # A complete, independent check of all pair-arc realizability conditions.
        for x in types:
            for y in types:
                observed=direct_arc(cls,arcs,x,y)
                cx,px=x;cy,py=y
                if cx==k or cy==k: predicted=1
                elif cx==cy:predicted=0
                else:
                    ai=cls.index(cx);aj=cls.index(cy)
                    basebit=arcs[min(ai,aj),max(ai,aj)]
                    if ai>aj:basebit=1-basebit
                    xj=px[aj]
                    yi=py[ai]
                    # px is x->old, py is y->old; old_i->y=1-yi.
                    # b(x,y)= b(old_i,old_j) xor (px_j xor basebit)
                    #          xor ((1-py_i) xor basebit).
                    predicted=basebit^xj^basebit^(1-yi)^basebit
                assert observed==predicted,(sizes,x,y,observed,predicted)
                totals+=1
        DD=Matrix([[direct_arc(cls,arcs,x,y) for y in types] for x in types])
        form=smith_normal_form(DD,domain=ZZ)
        measured=sorted(abs(int(form[i,i])) for i in range(form.rows) if form[i,i]!=0)
        target=predicted_snf(k,n)
        assert measured==target[:len(measured)],(sizes,measured,target)
        assert len(measured)+target.count(0)==len(types)
        print(f'DIRECT base={sizes}, seed={seed}, types={len(types)}, checks={len(types)**2}, exact_smith=OK')
    print('DIRECT_CHECKS',totals)

if __name__=='__main__':
    compact_check()
    check_direct()
    print('VERIFY_OK')
