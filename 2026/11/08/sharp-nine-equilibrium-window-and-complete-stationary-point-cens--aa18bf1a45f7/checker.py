#!/usr/bin/env python3
"""Reproduce exact polynomial identities and the real-equilibrium census."""
import sympy as S
x,y,h=S.symbols('x y h', real=True)
P=-2*h-y+x*x-4*x*y-y*y-S.Rational(2,3)*x**3-3*x*x*y-5*x*y*y+S.Rational(7,3)*y**3
Q=-h+x+S.Rational(1,2)*x*x+3*x*y+2*y*y-S.Rational(4,3)*x**3-3*x*x*y+3*x*y*y+S.Rational(25,6)*y**3
lines=[2*x+y,x-2*y-1,x+3*y+1]
xs=[-y/2,2*y+1,-3*y-1]
qs=[(50*y**3+15*y**2-12*y-24*h)/24,-(75*y**3+90*y**2+24*y+6*h-1)/6,(25*y**3+75*y**2+36*y+5-6*h)/6]
assert S.expand(P-2*Q-S.prod(lines))==0
for i in range(3):
 assert S.expand(Q.subs(x,xs[i])-qs[i])==0
Ds=[-S.Rational(125,768)*(6*h-1)*(120*h+7),-S.Rational(25,16)*(2700*h**2-900*h-181),-S.Rational(25,16)*(300*h**2-1900*h+79)]
for q,d in zip(qs,Ds): assert S.simplify(S.discriminant(q,y)-d)==0
J=S.Matrix([[S.diff(P,x),S.diff(P,y)],[S.diff(Q,x),S.diff(Q,y)]])
tr=S.trace(J);det=S.factor(J.det())
tr_by=[5*y*(5*y-2)/4,-5*y*(5*y+4)/2,-5*(15*y**2+18*y+4)/2]
det_by=[-(5*y-1)*(5*y+2)**3/8,-(5*y+2)**2*(75*y**2+60*y+8)/2,(5*y+2)**2*(25*y**2+50*y+12)/2]
for xx,t,d in zip(xs,tr_by,det_by):
 assert S.expand(tr.subs(x,xx)-t)==0
 assert S.expand(det.subs(x,xx)-d)==0
z={x:S.Rational(1,5),y:-S.Rational(2,5),h:S.Rational(1,6)}
assert all(k.subs(z)==0 for k in [P,Q,*lines])
assert S.factor(qs[0].subs(h,S.Rational(1,6)))==(2*y-1)*(5*y+2)**2/24
assert S.simplify(det.subs(z))==0 and tr.subs(z)==2
lo=[-S.Rational(7,120),S.Rational(1,6)-8*S.sqrt(3)/45,S.Rational(19,6)-13*S.sqrt(13)/15]
hi=[S.Rational(1,6),S.Rational(1,6)+8*S.sqrt(3)/45,S.Rational(19,6)+13*S.sqrt(13)/15]
assert lo[1]<lo[0]<lo[2]<hi[0]<hi[1]<hi[2]
def c(h0,l,u):
 if h0==l or h0==u: return 2
 return 3 if l<h0<u else 1
for h0,expected in [(-1,3),(-S.Rational(1,10),5),(0,7),(S.Rational(1,20),9),(S.Rational(1,10),9),(S.Rational(1,6),6),(S.Rational(1,3),7),(S.Rational(1,2),5),(7,3)]:
 count=sum(c(h0,l,u) for l,u in zip(lo,hi))-2*int(h0==S.Rational(1,6))
 if h0==S.Rational(1,20): assert count==9
 # independently count distinct exact real roots on each line
 independent=sum(len(S.polys.polytools.intervals(S.Poly(q.subs(h,h0),y),eps=S.Rational(1,1000000))) for q in qs)-2*int(h0==S.Rational(1,6))
 assert count==independent,(h0,count,independent)
 # source code's exact intervals verify numerator roots, not floating approximations
 print(f'h={h0}: {count} distinct real equilibria')
# Exact algebraic isolation at h=1/10, and source-sink-saddle spectra
h0=S.Rational(1,10)
kinds=[]
for xx,q,tt,dd in zip(xs,qs,tr_by,det_by):
 for interval,multiplicity in S.polys.polytools.intervals(S.Poly(q.subs(h,h0),y),eps=S.Rational(1,10**9)):
  left,right=interval
  # sign determined by interval arithmetic using separation away from zero
  midpoint=(left+right)/2
  tS=S.sign(tt.subs(y,midpoint)); dS=S.sign(dd.subs(y,midpoint))
  assert tS!=0 and dS!=0 and multiplicity==1
  kind='saddle' if dS<0 else 'source' if tS>0 else 'sink'
  kinds.append(kind)
assert sorted(kinds)==sorted(['saddle']*5+['source']*2+['sink']*2)
print('Exact polynomial identities: PASS; nine-point phase portrait: 5 saddles, 2 sources, 2 sinks')
