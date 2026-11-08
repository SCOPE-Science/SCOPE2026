#!/usr/bin/env python3
"""Standalone finite validations for two-point configuration space of K_{2,m}."""
from itertools import permutations,combinations
from math import comb

def cells(m):
    # vertex labels: 0=A, 1=B, 2..m+1=branch vertices
    es=[('a',i) for i in range(m)]+[('b',i) for i in range(m)]
    ends={('a',i):(0,2+i) for i in range(m)}|{('b',i):(2+i,1) for i in range(m)}
    c0=list(combinations(range(m+2),2))
    c1=[(e,z) for e in es for z in range(m+2) if z not in ends[e]]
    c2=[(i,j) for i in range(m) for j in range(m) if i!=j]
    return c0,c1,c2,ends

def act0(p,perm,flip):
    def v(x):return (1-x if flip else x) if x<2 else 2+perm[x-2]
    return tuple(sorted(v(i) for i in p))

def act1(cell,perm,flip):
    (t,i),z=cell
    def v(x):return (1-x if flip else x) if x<2 else 2+perm[x-2]
    return ((('b' if t=='a' else 'a') if flip else t,perm[i]),v(z)),(-1 if flip else 1)

def act2(c,perm,flip):
    i,j=c
    return ((perm[j],perm[i]),-1) if flip else ((perm[i],perm[j]),1)

def boundary1(c,ends):
    e,z=c; v,w=ends[e]
    return {tuple(sorted((w,z))):1,tuple(sorted((v,z))):-1}

def boundary2(c):
    i,j=c
    return {(('b',j),2+i):1,(('b',j),0):-1,(('a',i),1):-1,(('a',i),2+j):1}

def beta(i,j):
    assert i<j
    return {(('a',j),2+i):1,(('a',i),2+j):-1,(('b',j),0):1,(('b',i),0):-1}

def eval_boundary(z,ends):
    o={}
    for c,coeff in z.items():
        for k,a in boundary1(c,ends).items():o[k]=o.get(k,0)+a*coeff
    return {k:v for k,v in o.items() if v}

def reduced(z,m):
    # eliminate all q_{ji}=(b_j, middle i) by subtracting boundaries of unique squares s_{ij}
    z=dict(z)
    for i in range(m):
      for j in range(m):
       if i==j:continue
       sq=(i,j); q=(('b',j),2+i)
       t=z.get(q,0)
       if t:
        for c,a in boundary2(sq).items():z[c]=z.get(c,0)-t*a
    z={c:a for c,a in z.items() if a}
    assert all(not(t=='b' and v>=2) for (t,i),v in z)
    return z

def basis_coeff(z,m):
    z=reduced(z,m)
    # coefficient of a_j with vertex i (i<j) is the corresponding beta_ij coordinate
    cc={(i,j):z.get((('a',j),2+i),0) for i in range(m) for j in range(i+1,m)}
    rem=dict(z)
    for (i,j),t in cc.items():
      if t:
       for c,a in beta(i,j).items():rem[c]=rem.get(c,0)-t*a
    assert {c:a for c,a in rem.items() if a}=={},('basis remainder',m,rem)
    return cc

def verify(m):
    c0,c1,c2,ends=cells(m)
    assert len(c0)==comb(m+2,2) and len(c1)==2*m*m and len(c2)==m*(m-1)
    ss=[set(boundary2(s).keys()) for s in c2]
    for s in c2:
      i,j=s; q=(('b',j),2+i)
      assert sum(q in v for v in ss)==1
    for s in c2:
      b={}
      for e,k in boundary2(s).items():
       for v,t in boundary1(e,ends).items(): b[v]=b.get(v,0)+k*t
      assert all(x==0 for x in b.values())
    assert len(c1)-len(c2)==m*m+m
    assert len(c1)-len(c2)-len(c0)+1==comb(m,2)
    for i,j in combinations(range(m),2):
      assert eval_boundary(beta(i,j),ends)=={}
      assert basis_coeff(beta(i,j),m)[(i,j)]==1
    samples=list(permutations(range(m))) if m<=5 else [tuple(range(m)),tuple(reversed(range(m))),tuple((i+1)%m for i in range(m))]
    for perm in samples:
      f=sum(i==x for i,x in enumerate(perm))
      t=sum(i<perm[i] and perm[perm[i]]==i for i in range(m))
      trace_expected=comb(f,2)-t
      for flip in [False,True]:
        tr0=sum(act0(v,perm,flip)==v for v in c0)
        tr1=sum(sgn for c in c1 for img,sgn in [act1(c,perm,flip)] if img==c)
        tr2=sum(sgn for c in c2 for img,sgn in [act2(c,perm,flip)] if img==c)
        assert 1-(tr0-tr1+tr2)==(-1 if flip else 1)*trace_expected,(m,perm,flip)
        for i,j in combinations(range(m),2):
          image={}
          for c,z in beta(i,j).items():
            cc,sg=act1(c,perm,flip);image[cc]=image.get(cc,0)+z*sg
          assert not eval_boundary(image,ends)
          got=basis_coeff(image,m)
          a,b=perm[i],perm[j]
          sig=(1 if a<b else -1)*(-1 if flip else 1)
          assert got[(min(a,b),max(a,b))]==sig
          assert all(v==0 for k,v in got.items() if k!=(min(a,b),max(a,b)))
    return (m,len(c0),len(c1),len(c2),comb(m,2),len(samples)*2)

if __name__=='__main__':
 for m in range(2,8):print('OK m,V,E,F,betti1,automorphisms',*verify(m))
 print('TWO_PARTICLE_THETA_EQUIVARIANT_PASS')
