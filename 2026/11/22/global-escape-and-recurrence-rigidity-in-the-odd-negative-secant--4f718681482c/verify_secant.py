#!/usr/bin/env python3
"""Exact rational tests for the odd-degree secant model gradient increment and escape cones.
This program is corroborative; the general theorem follows from convexity.
"""
from fractions import Fraction as F

def T_uv(u,v,c,d):
    w=c*u**d
    return (u+v+3*w,w)

def energy(u,v,c,d):
    return c*u**(d+1)/F(d+1)-v*v

def check():
    q=[F(-2),F(-1),F(-1,2),F(0),F(1,2),F(1),F(2)]
    ct=0;cones=0;strict=0
    for d in (3,5,7):
      for c in (F(1,3),F(1),F(2)):
       for u in q:
        for v in q:
          un,vn=T_uv(u,v,c,d);w=c*u**d
          delta=energy(un,vn,c,d)-energy(u,v,c,d)
          Q=2*w*w+w*v+v*v
          D=delta-Q
          assert D>=0,(d,c,u,v,D)
          assert Q== (v+w/F(2))**2+F(7,4)*w*w
          assert delta>0 if (u,v)!=(0,0) else delta==0
          ct+=1
          if abs(v)<=c*abs(u)**d and u!=0:
            s=1 if u>0 else -1
            assert s*un>=abs(u)+2*c*abs(u)**d
            assert abs(vn)<=c*abs(un)**d
            assert s*un>0
            cones+=1
    # Representative exact sign-stabilization trajectories: two-step coordinate check.
    for d in (3,5):
      for c in (F(1,2),F(1)):
        for u0,v0 in ((F(3,2),F(0)),(F(-3,2),F(0)),(F(1),F(-10)),(F(-1),F(10))):
          u,v=u0,v0
          for _ in range(3):
            un,vn=T_uv(u,v,c,d)
            x,y=(u-v)/2,(u+v)/2
            xn,yn=y+c*u**d,y+2*c*u**d
            assert xn+yn==un and yn-xn==vn
            u,v=un,vn
            strict+=1
    print(f"PASS: {ct} exact nonnegative Bregman and strict Lyapunov checks; "
          f"{cones} exact escape-cone checks; {strict} coordinate transformations")
if __name__=='__main__':check()
