#!/usr/bin/env python3
"""Self-contained exact-root and directed integer-interval checks for the seven-square Fourier bound."""
from fractions import Fraction
from collections import defaultdict
Q=10**15

def floor_div(a,b): return a//b
def ceil_div(a,b): return -((-a)//b)
class I:
 def __init__(self,lo,hi=None):
  if hi is None: hi=lo
  self.a=int(lo); self.b=int(hi)
  assert self.a<=self.b
 def __add__(x,y):
  y=cast(y);return I(x.a+y.a,x.b+y.b)
 __radd__=__add__
 def __neg__(x):return I(-x.b,-x.a)
 def __sub__(x,y):return x+(-cast(y))
 def __rsub__(x,y):return cast(y)+(-x)
 def __mul__(x,y):
  y=cast(y); p=[a*b for a in (x.a,x.b) for b in (y.a,y.b)]
  return I(floor_div(min(p),Q),ceil_div(max(p),Q))
 __rmul__=__mul__
 def __truediv__(x,y):
  y=cast(y); assert not(y.a<=0<=y.b)
  if y.a<0: return (-x)/(-y)
  p=[(a*Q,b) for a in (x.a,x.b) for b in (y.a,y.b)]
  return I(min(floor_div(a,b) for a,b in p),max(ceil_div(a,b) for a,b in p))
 def __rtruediv__(x,y):return cast(y)/x
 def __repr__(x):return f'[{x.a/Q:.12f},{x.b/Q:.12f}]'
def cast(z):return z if isinstance(z,I) else I(int(z*Q))

def run():
 a=Fraction(1142138768653,10**12);b=Fraction(1142138768654,10**12)
 f=lambda x:2*x**3+x*x-2*x-2
 assert f(a)<0<f(b) and a>1 and b<2
 assert 6*a*a+2*a-2>0
 s=I(a.numerator*Q//a.denominator,ceil_div(b.numerator*Q,b.denominator))
 F=(1-s/2)/(s*s+6)
 B=[[cast(min(i+1,j+1)) - ( (int(j>=4)+int(i>=4)) /s ) - s*(int(i>=4 and j>=6)+int(i>=6 and j>=4)) -F*((i+1)*(j+1)) for j in range(7)] for i in range(7)]
 # The numerical convention for the reciprocal term: 1/s, not an integer divided by interval.
 for i in (1,2,3):
  for j in (0,6):assert B[i][j].a>0
 P=[[B[i][j] for j in range(7)]for i in range(7)]
 for i in (1,2,3):
  for j in (0,6):P[i][j]=P[j][i]=I(0)
 P[5][6]=P[5][6]-s/2
 P[6][5]=P[6][5]-s/2
 # Exact algebraic null identity: at the cubic root, F(s)*(s^2+6)=1-s/2=s^2-1/s.
 # For v=(s^2-1,0,...,0,1), B v=(0,s/2,s,3s/2,0,s/2,0).
 for k in range(7):
  v_expr=P[k][0]*(s*s-1)+P[k][6]
  assert v_expr.a<=0<=v_expr.b,('null enclosure',k,v_expr)
 # Sylvester certificate: the 6x6 principal block P[0:6,0:6] is positive definite.
 A=[[P[i][j] for j in range(6)]for i in range(6)]
 pivots=[]
 for k in range(6):
  pivot=A[k][k]; assert pivot.a>0,('Sylvester pivot',k,pivot)
  pivots.append((pivot.a/Q,pivot.b/Q))
  for i in range(k+1,6):
   for j in range(i,6): A[j][i]=A[i][j]= A[i][j]-A[i][k]*A[k][j]/pivot
 assert len(pivots)==6
 # P has exact rank-six PSD by its exact null vector and a positive principal block.
 d=defaultdict(list)
 for i in range(1,8):
  for j in range(i,8):d[i*i+j*j].append((i,j))
 assert {n:pair for n,pair in d.items() if len(pair)>1}=={50:[(1,7),(5,5)]}
 print('PASS: rational cubic isolation; six rigorous positive LDL pivots',pivots)
 print('PASS: null-vector interval enclosures; nonnegative correction; first-square collision')
 print('value enclosure',2-((s*s)*(s*s)-4*s+6)/(s*s+6)/(s*s+6))
if __name__=='__main__':run()
