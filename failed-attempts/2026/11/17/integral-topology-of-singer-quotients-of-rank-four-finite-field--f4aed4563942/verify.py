"""Finite quotient building chain verifier; pure computations; q=2,3."""
from itertools import product
from collections import defaultdict
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

def do(q):
    d=4
    zero=(0,)*d
    vecs=[v for v in product(range(q),repeat=d) if v!=zero]
    def span(basis):
        ans=set()
        for coef in product(range(q),repeat=len(basis)):
            w=tuple(sum(a*b[i] for a,b in zip(coef,basis))%q for i in range(d))
            if w!=zero: ans.add(w)
        return frozenset(ans)
    ranks={1:set(),2:set(),3:set()}
    ranks[1]={span([v]) for v in vecs}
    for U in ranks[1]:
        u=next(iter(U))
        for v in vecs:
            if v not in U:
                ranks[2].add(span([u,v]))
    for U in ranks[2]:
        u=next(iter(U)); w=next(v for v in U if v not in span([u]))
        for v in vecs:
            if v not in U:
                ranks[3].add(span([u,w,v]))
    assert tuple(map(len,[ranks[k] for k in (1,2,3)]))==({2:(15,35,15),3:(40,130,40)})[q]
    for coeff in product(range(q),repeat=4):
        if coeff[0]==0:continue
        def trans(v):
            v0,v1,v2,v3=v
            return ((-coeff[0]*v3)%q,(v0-coeff[1]*v3)%q,(v1-coeff[2]*v3)%q,(v2-coeff[3]*v3)%q)
        seen=set(); v=(1,0,0,0)
        for i in range((q**4-1)//(q-1)):
            u=span([v]); seen.add(u); v=trans(v)
        if len(seen)==(q**4-1)//(q-1) and span([v])==span([(1,0,0,0)]):
            break
    else:raise Exception('no singer')
    print('q, Singer polynomial, orbit length:',q,coeff,len(seen))
    space={U:i for i,U in enumerate(sorted([U for k in (1,2,3) for U in ranks[k]],key=lambda z:(len(z),tuple(sorted(z)))))}
    dim={space[U]:k for k in (1,2,3) for U in ranks[k]}
    byid={i:U for U,i in space.items()}
    im={space[U]:space[frozenset(trans(v) for v in U)] for U in space}
    assert all(dim[i]==dim[j] for i,j in im.items())
    cells0={(i,) for i in dim}
    cells1={(i,j) for i,j in product(dim,repeat=2) if dim[i]<dim[j] and byid[i]<byid[j]}
    cells2={(i,j,k) for i,j,k in product(dim,repeat=3) if dim[i]==1 and dim[j]==2 and dim[k]==3 and byid[i]<byid[j]<byid[k]}
    def canon(c):
        z=c;best=c
        for _ in range((q**4-1)//(q-1)):
            z=tuple(im[i] for i in z)
            if z<best:best=z
        assert z==c
        return best
    c0=sorted({canon(c) for c in cells0});c1=sorted({canon(c) for c in cells1});c2=sorted({canon(c) for c in cells2});
    idx=[{c:i for i,c in enumerate(cs)} for cs in (c0,c1,c2)]
    D1=Matrix.zeros(len(c0),len(c1))
    for j,c in enumerate(c1):
        for s,t in [(-1,(c[0],)),(1,(c[1],))]:D1[idx[0][canon(t)],j]+=s
    D2=Matrix.zeros(len(c1),len(c2))
    for j,c in enumerate(c2):
        for s,t in [(1,(c[1],c[2])),(-1,(c[0],c[2])),(1,(c[0],c[1]))]:D2[idx[1][canon(t)],j]+=s
    assert D1*D2==Matrix.zeros(len(c0),len(c2))
    # Matrix describing d_2 after eliminating all tree edges from d_1: the cycle basis are non-tree edges.
    parent=list(range(len(c0)))
    def find(a):
        while parent[a]!=a:a=parent[a]
        return a
    tree=[];nontree=[]
    for j,c in enumerate(c1):
        a=idx[0][canon((c[0],))];b=idx[0][canon((c[1],))]
        if find(a)!=find(b):
            parent[find(a)]=find(b);tree.append(j)
        else:nontree.append(j)
    assert len(tree)==len(c0)-1
    # For a connected graph, fundamental cycles from all non-tree edges define a Z-basis of ker d1,
    # whose nontree coordinates are literal corresponding edge coordinates.
    red=D2[nontree,:]
    D=smith_normal_form(red,domain=ZZ)
    vals=[abs(int(D[i,i])) for i in range(min(D.shape)) if D[i,i]]
    assert vals.count(1)==len(vals)-1 and vals[-1]==q*q+1,vals
    assert len(c2)-len(vals)==q**3-q**2
    print('q=%d cell_orbits=(%d,%d,%d) d1rank=%d reduced_D2_smith_ones=%d torsion=%d H2rank=%d'%(q,len(c0),len(c1),len(c2),len(tree),len(vals)-1,vals[-1],len(c2)-len(vals)))
    N=(q**4-1)//(q-1)
    orbit_nontrivial={i:0 for i in (1,2,3)}
    for c in c0:
        u=c[0]; z=u; size=0
        for _ in range(N):
            size+=1; z=im[z]
            if z==u:break
        if size<N:orbit_nontrivial[dim[u]]+=1
    assert orbit_nontrivial=={1:0,2:1,3:0},orbit_nontrivial
    g=im.copy()
    for exponent in range(1,N):
        fixed=[i for i in dim if g[i]==i]
        predicted=q*q+1 if exponent%(q*q+1)==0 else 0
        assert len(fixed)==predicted,(exponent, len(fixed),predicted)
        assert all(dim[i]==2 for i in fixed)
        g={i:im[g[i]] for i in dim}
    print('fixed_point_exponents_pass=%d singular_middle_rank_orbit=1'%(N-1))
for q in (2,3):do(q)
print('SINGER_BUILDING_QUOTIENT_CHAIN_PASS q=2,3')
