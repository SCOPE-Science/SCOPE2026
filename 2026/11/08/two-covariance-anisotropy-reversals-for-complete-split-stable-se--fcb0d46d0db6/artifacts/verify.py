"""Exact checks for split-graph stable-set polytope volume/vertex covariance."""
from fractions import Fraction as F
from itertools import product
from math import comb, sqrt


def block_matrices(p, q):
    N = p+2**q
    u=2**(q-2)
    g=F(u*((q+1)*p+2**q),N*N)
    h=F(2**q,N*N)
    k2=F(p*q*2**(2*q-2),N**4)
    ai=F(u,N)
    ac=F(1,N)
    trv=g+h
    detv=g*h-k2
    assert detv==F(2**(2*q-2),N**3)
    D=p+q+1
    a=F((q+1)*(q+2),12*D*(D+1))
    b=F(1,D*(D+1))
    var=F(p*(q+1),D*D*(D+1))
    gv=a+F(q,4)*var
    hv=var/p
    kv2=F(q,4*p)*var*var
    trl=gv+hv
    detl=gv*hv-kv2
    assert detl==a*hv
    Tv=(q+1)*p+2**q+4
    Tl=(4*q+2)*p+(q+1)*(q+2)+12
    Sv=F(Tv*Tv,4*N)
    Sl=F(Tl*Tl,12*(q+2)*D)
    assert Sv==trv*trv/detv
    assert Sl==trl*trl/detl
    assert g>ai>=ac>h and gv>a>=b>hv
    assert k2>0 and kv2>0
    return (trv, detv, trl, detl, Sv, Sl, ai, ac, a, b)


def enum_vertex_cov(p,q):
    vs=[]
    for x in product((0,1),repeat=q):vs.append(tuple(x)+(0,)*p)
    for j in range(p):vs.append((0,)*q+tuple(int(i==j) for i in range(p)))
    N=len(vs); m=q+p
    mu=[F(sum(v[i] for v in vs),N) for i in range(m)]
    C=[[F(sum(v[i]*v[j] for v in vs),N)-mu[i]*mu[j] for j in range(m)] for i in range(m)]
    v=block_matrices(p,q)
    ai,ac=v[6:8];u=2**(q-2)
    NN=p+2**q
    for i in range(q):
      for j in range(q):
       want=F(2**(q-1),NN) if i==j else F(2**(q-2),NN)
       want-=F(2**(2*q-2),NN**2)
       assert C[i][j]==want
    for i in range(p):
      for j in range(p):
       assert C[q+i][q+j]==F(int(i==j),NN)-F(1,NN**2)
    for i in range(q):
      for j in range(p):
       assert C[i][q+j]==-F(2**(q-1),NN**2)
    return len(vs),len(C)*len(C)


def cff(p,q):
  t=2**q
  return 3*(q+2)*(p+q+1)*((q+1)*p+t+4)**2-(p+t)*((4*q+2)*p+(q+1)*(q+2)+12)**2


def main():
  nv=nc=0
  for q in range(2,7):
    for p in range(2,8):
      vs,cs=enum_vertex_cov(p,q);nv+=vs;nc+=cs
  nparams=0
  for q in range(2,80):
    for p in [2,3,4,5,6,7,8,9,q,2**q,2**q//q,max(2,2**q//q),2**q*3//q,10**6,10**10]:
      if p<2:continue
      *_,sv,sl,_,_,_,_=block_matrices(p,q)
      assert (sv>sl)-(sv<sl)==(cff(p,q)>0)-(cff(p,q)<0)
      nparams+=1
  for q in range(4,80):
    assert cff(F(0),q)>0
    assert cff(F(2**q,q),q)<0
    # Positive leading cubic coefficient follows (q-1)^2(3q+2).
  for p in range(2,100):
    assert cff(p,2)>0
    assert (cff(p,3)==0)==(p==2)
    assert cff(p,3)>=0
  assert cff(4,4)<0
  assert cff(6,4)==0
  assert cff(2,3)==0
  assert cff(52,7)==0
  print(f'SPLIT_VERTEX_VOLUME_COVARIANCE_CHECKS_PASSED vertices={nv} entries={nc} profiles={nparams}')
if __name__=='__main__':main()
