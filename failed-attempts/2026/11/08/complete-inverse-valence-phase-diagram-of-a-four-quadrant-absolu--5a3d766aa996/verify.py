"""Exact rational checks of inverse-branch geometry for the four-quadrant map."""
from fractions import Fraction as F

def inverse(a,c,u,v):
    solutions=set()
    for sx in (1,-1):
        for sy in (1,-1):
            # input x=sx*p, y=sy*q, p,q>=0; output (U,V)=(p+a*sy*q, sx*p+c*q)
            A, B, C, D = F(1),a*sy,F(sx),c
            det=A*D-B*C
            if det==0: continue
            p=(D*u-B*v)/det
            q=(-C*u+A*v)/det
            if p>=0 and q>=0:
                x,y=sx*p,sy*q
                assert abs(x)+a*y==u and x+c*abs(y)==v
                solutions.add((x,y))
    return solutions

def theorem(a,c,u,v):
    S=u+v; D=v-u; E=a*v-c*u; G=-E; R=a*v+c*u
    if c<a:
        return 1
    if c>a:
        if S<0 or R<0: return 0
        if (u,v)==(0,0): return 1
        if S==0 or R==0: return 1
        if D==0 or E==0: return 3
        if D>0 and E<0: return 4
        return 2
    raise ValueError('boundary handled separately')

checks=0
for a,c in [(F(1),F(2)),(F(2),F(1)),(F(2),F(3)),(F(3),F(2)),(F(1),F(3)),(F(3),F(1)),(F(3,2),F(7,4)),(F(7,4),F(3,2))]:
    for U in range(-15,16):
        for V in range(-15,16):
            actual=len(inverse(a,c,F(U),F(V)))
            expected=theorem(a,c,F(U),F(V))
            assert actual==expected,(a,c,U,V,actual,expected)
            checks+=1
    # critical rays included, even for nonintegral slopes
    for k in range(1,11):
        for U,V in [(k,k),(k,-k),(a*k,c*k),(-a*k,c*k)]:
            assert len(inverse(a,c,U,V))==theorem(a,c,U,V),(a,c,U,V)
            checks+=1
# Degenerate c=a: for points in interior of upper halfplane away from diagonal, one inverse from regular sectors.
for a in [F(1),F(2),F(5,3)]:
 for U in range(-15,16):
  for V in range(-15,16):
   S=F(U+V);D=F(V-U)
   sol=inverse(a,a,F(U),F(V))
   if S>0 and D!=0:assert len(sol)==1,(a,U,V,sol)
   if S<0: assert len(sol)==0,(a,U,V,sol)
   checks+=1
# Infinite fibers at the singular parameter: check distinct exact rational witnesses.
for a in (F(1), F(2), F(5,3)):
    for U in range(-8,9):
        for k in range(1,11):
            q=F(10+k+abs(U))*F(1)
            p=F(U)+a*q
            assert p>=0
            x,y=-p,-q
            assert abs(x)+a*y==U and x+a*abs(y)==-U
            checks+=1
    for U in range(1,9):
        for k in range(1,10):
            q=F(U*k,10*a.numerator)
            # ensure q < U/a; use q=U*k/(10*a) instead
            q=F(U*k,10)/a
            x,y=F(U)-a*q,q
            assert x>0 and y>0
            assert abs(x)+a*y==U and x+a*abs(y)==U
            checks+=1
print('VERIFY_OK checks='+str(checks))
