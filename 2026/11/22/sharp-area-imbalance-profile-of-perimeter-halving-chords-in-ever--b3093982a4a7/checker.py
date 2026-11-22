"""Independent exact normalized triangle-cap optimization checks.
No external dependencies.  Any coordinates are unnecessary because each cap-to-whole area ratio equals xy/(uv).
"""
from fractions import Fraction
from random import Random

def predicted(a,b,c):
 a,b,c=sorted((a,b,c));s=(a+b+c)/2
 return s*s/(4*a*b) if a>=s/2 else (s-a)/b

def exact_vertex_max(u,v,s):
 lo=max(Fraction(0),s-v)
 hi=min(u,s)
 assert lo<=hi
 p=min(hi,max(lo,s/2))
 return p*(s-p)/(u*v)

def brute(a,b,c):
 s=(a+b+c)/2
 return max(exact_vertex_max(a,b,s),exact_vertex_max(a,c,s),exact_vertex_max(b,c,s))

def run():
 rng=Random(715251)
 checks=0
 for k in range(25000):
  t=sorted((rng.randint(1,2000) for i in range(3)))
  if t[0]+t[1]<=t[2]:continue
  a,b,c=[Fraction(x,1001) for x in t]
  p=predicted(a,b,c);v=brute(a,b,c)
  assert p==v,(t,p,v)
  assert Fraction(9,16)<=p<1,(t,p)
  checks+=3
 assert predicted(Fraction(1),Fraction(1),Fraction(1))==Fraction(9,16)
 assert predicted(Fraction(1,10),Fraction(1),Fraction(1))==Fraction(19,20) # check? s=1.05 ; (1.05-.1)/1=.95
 print('checks',checks+2)
if __name__=='__main__':run()

# A separate coordinate-geometry implementation for sampled perimeter antipodes.
def coordinate_validation():
 from math import sqrt
 rng=Random(72385)
 def twice_area(poly):
  return abs(sum(x*y2-x2*y for (x,y),(x2,y2) in zip(poly,poly[1:]+poly[:1])))
 count=0
 for k in range(90):
  aa,bb,cc=sorted(rng.uniform(.3,1.1) for _ in range(3))
  if aa+bb<=cc:continue
  # Triangle A-B-C-A, edge lengths c,a,b.
  xx=(bb*bb+cc*cc-aa*aa)/(2*cc)
  yy=sqrt(bb*bb-xx*xx)
  V=[(0.,0.),(cc,0.),(xx,yy)]
  ends=[0.,cc,cc+aa,cc+aa+bb]; P=ends[-1];s=P/2
  def pt(t):
   t=t%P
   for i in range(3):
    if ends[i]<=t<=ends[i+1]:
     frac=(t-ends[i])/(ends[i+1]-ends[i]);X=V[i];Y=V[(i+1)%3]
     return (X[0]*(1-frac)+Y[0]*frac,X[1]*(1-frac)+Y[1]*frac)
   raise RuntimeError()
  denom=twice_area(V)
  ratio=0.0
  for j in range(3600):
   start=P*j/3600;stop=start+s
   chain=[pt(start)]
   for edge in ends[1:]+[e+P for e in ends[1:]]:
    if start+1e-9<edge<stop-1e-9:chain.append(pt(edge))
   chain.append(pt(stop))
   cap=twice_area(chain)/denom
   ratio=max(ratio,cap,1-cap)
  truth=float(predicted(Fraction(str(aa)),Fraction(str(bb)),Fraction(str(cc))))
  assert ratio<=truth+1e-8,(aa,bb,cc,ratio,truth)
  assert ratio>=truth-1.0e-3,(aa,bb,cc,ratio,truth)
  count+=1
 print('independent coordinates validated',count,'triangles x 3600 chords')

if __name__=='__main__': coordinate_validation()
