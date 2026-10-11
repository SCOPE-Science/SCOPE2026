#!/usr/bin/env python3
import math

EPS = 5e-11

def add(u,v): return (u[0]+v[0], u[1]+v[1])
def sub(u,v): return (u[0]-v[0], u[1]-v[1])
def mul(s,u): return (s*u[0], s*u[1])
def dot(u,v): return u[0]*v[0]+u[1]*v[1]
def norm2(u): return dot(u,u)
def norm(u): return math.sqrt(norm2(u))
def cross(u,v): return u[0]*v[1]-u[1]*v[0]
def lerp(P,Q,t): return add(mul(1.0-t,P),mul(t,Q))

def inward_normal(P,Q,inside):
    e=sub(Q,P)
    L=norm(e)
    n=(-e[1]/L,e[0]/L)
    if dot(n,sub(inside,P)) < 0.0:
        n=(-n[0],-n[1])
    return n

def foot(P,A,n):
    d=dot(n,sub(P,A))
    return sub(P,mul(d,n)), d

def check_triangle(A,B,C):
    area=abs(cross(sub(B,A),sub(C,A)))/2.0
    if area <= 1e-10: raise AssertionError('degenerate test triangle')
    a=norm(sub(C,B)); b=norm(sub(A,C)); c=norm(sub(B,A))
    S=a*a+b*b+c*c
    K=((a*a*A[0]+b*b*B[0]+c*c*C[0])/S,
       (a*a*A[1]+b*b*B[1]+c*c*C[1])/S)
    na=inward_normal(B,C,A)
    nb=inward_normal(C,A,B)
    nc=inward_normal(A,B,C)
    eq=add(add(mul(a,na),mul(b,nb)),mul(c,nc))
    if norm(eq) > 5e-12*max(a,b,c):
        raise AssertionError(('normal equilibrium',eq))
    feet=[]
    for P0,Q0,n in [(B,C,na),(C,A,nb),(A,B,nc)]:
        F,_=foot(K,P0,n); feet.append(F)
    Kc=mul(1.0/3.0,add(add(feet[0],feet[1]),feet[2]))
    if norm(sub(Kc,K)) > 5e-12*max(a,b,c):
        raise AssertionError(('pedal centroid',Kc,K))
    sharp=12.0*area*area/S
    qped=norm2(sub(feet[0],feet[1]))+norm2(sub(feet[1],feet[2]))+norm2(sub(feet[2],feet[0]))
    if abs(qped-sharp) > EPS*max(1.0,sharp):
        raise AssertionError(('pedal value',qped,sharp))
    worst=0.0
    grid=[0.0,0.13,0.37,0.71,1.0]
    for tx in grid:
      X=lerp(B,C,tx)
      for ty in grid:
        Y=lerp(C,A,ty)
        for tz in grid:
          Z=lerp(A,B,tz)
          M=mul(1.0/3.0,add(add(X,Y),Z))
          Da,_=foot(M,B,na); Db,_=foot(M,C,nb); Dc,_=foot(M,A,nc)
          q=norm2(sub(X,Y))+norm2(sub(Y,Z))+norm2(sub(Z,X))
          h=sub(M,K)
          center=3.0*(dot(na,h)**2+dot(nb,h)**2+dot(nc,h)**2)
          offset=3.0*(norm2(sub(Da,X))+norm2(sub(Db,Y))+norm2(sub(Dc,Z)))
          rhs=sharp+center+offset
          err=abs(q-rhs)/max(1.0,abs(q),abs(rhs))
          worst=max(worst,err)
          if err > EPS:
            raise AssertionError(('decomposition',tx,ty,tz,q,rhs,err))
    return worst, sharp

def main():
    triangles=[
      ((0.2,2.3),(-1.4,-0.1),(2.1,0.4)),
      ((0.0,2.0),(0.0,0.0),(3.0,0.0)),
      ((-0.7,1.2),(-2.0,-0.3),(2.8,0.0)),
      ((0.1,3.0),(-3.1,-0.2),(1.2,-0.7)),
    ]
    worst=0.0
    for T in triangles:
      e,_=check_triangle(*T); worst=max(worst,e)
    h=math.sqrt(3.0)/2.0
    A=(0.0,h); B=(-0.5,0.0); C=(0.5,0.0)
    e,sharp=check_triangle(A,B,C); worst=max(worst,e)
    if abs(sharp-0.75)>1e-13:
      raise AssertionError(('equilateral normalization',sharp))
    print('PASS worst_normalized_error=%.3e equilateral_min=%.15g' % (worst,sharp))

if __name__=='__main__':
    main()
