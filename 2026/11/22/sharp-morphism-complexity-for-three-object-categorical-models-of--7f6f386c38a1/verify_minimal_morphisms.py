#!/usr/bin/env python3
"""Exact finite checks for the sharp morphism count in projective-plane wedges.
Finite computations supplement, but do not prove, the general construction.
"""
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

def model(r):
    assert isinstance(r,int) and r>=1
    # Hom(0,1) = (f_0,...,f_r), Hom(1,2) = (g_0,...,g_r)
    # Composition H_{j,k}: j names f_j, k names g_k.
    hmap={}
    for j in range(r+1):
        for k in range(r+1):
            if j==0 and k==0: name='hub'
            elif j==0 or k==0: name=('cycle',j or k)
            elif j==k: name='hub'
            else: name=('leaf',j,k)
            hmap[j,k]=name
    hs=sorted(set(hmap.values()),key=str)
    return hmap,hs

def check(r):
    hmap,hs=model(r)
    assert hmap[0,0]=='hub'
    assert all(hmap[0,k]==('cycle',k) for k in range(1,r+1))
    assert all(hmap[j,0]==('cycle',j) and hmap[j,j]=='hub' for j in range(1,r+1))
    a=b=r+1;c=len(hs)
    assert c==r*r+1,(r,c)
    # bipartite incidence graph, r 4-cycles sharing one f_0 edge,
    # all remaining edges pendant.
    cnt={h:0 for h in hs}
    for j in range(a):
        for k in range(b):cnt[hmap[j,k]]+=1
    assert cnt['hub']==r+1
    assert all(cnt[('cycle',j)]==2 for j in range(1,r+1))
    assert all(cnt[('leaf',j,k)]==1 for j in range(1,r+1) for k in range(1,r+1) if j!=k)
    v=b+c;e=a*b
    assert e-v+1==r
    # Normalize arrows f,g,h as 1-cells; triangles as composable pairs.
    rows=a+b+c;cols=a*b
    d1=Matrix.zeros(3,rows)
    for j in range(a):d1[0,j]=-1;d1[1,j]=1
    for k in range(b):d1[1,a+k]=-1;d1[2,a+k]=1
    for idx in range(c):d1[0,a+b+idx]=-1;d1[2,a+b+idx]=1
    d2=Matrix.zeros(rows,cols)
    for j in range(a):
        for k in range(b):
            col=j*b+k;h=hs.index(hmap[j,k]);d2[j,col]=1;d2[a+k,col]=1;d2[a+b+h,col]=-1
    assert d1*d2==Matrix.zeros(3,cols)
    sd=smith_normal_form(d2,domain=ZZ)
    diag=[abs(int(sd[i,i])) for i in range(min(sd.shape)) if sd[i,i]]
    assert len(diag)==cols
    assert [x for x in diag if x>1]==[2]*r,(r,diag)
    assert rows-2-cols==0
    return {'r':r,'homset_cardinalities':[a,b,c], 'nonidentity_morphisms':rows,'nerve_2simplices':cols,'H1_smith_factors':[2]*r,'H2_rank':0}

if __name__=='__main__':
    import json
    for r in range(1,6):print(json.dumps(check(r),sort_keys=True))
    print('PASS 5 exact chain-complex tests')
