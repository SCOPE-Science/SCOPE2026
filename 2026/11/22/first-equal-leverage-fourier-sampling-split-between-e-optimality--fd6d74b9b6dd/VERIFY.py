#!/usr/bin/env python3
"""Exact rational interval proof for a finite trigonometric coordinate-selection theorem."""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial, isqrt
from itertools import combinations
class IV:
 def __init__(self,a,b=None):
  self.a=F(a);self.b=F(a if b is None else b); assert self.a<=self.b
 def __add__(self,y):
  y=iv(y);return IV(self.a+y.a,self.b+y.b)
 __radd__=__add__
 def __neg__(self):return IV(-self.b,-self.a)
 def __sub__(self,y):return self+-iv(y)
 def __rsub__(self,y):return iv(y)+-self
 def __mul__(self,y):
  y=iv(y); z=[a*b for a in (self.a,self.b) for b in (y.a,y.b)];return IV(min(z),max(z))
 __rmul__=__mul__
 def __truediv__(self,y):
  y=iv(y);assert y.a*y.b>0;return self*IV(1/y.b,1/y.a)
 def __repr__(self):return str(float(self.a))+'..'+str(float(self.b))
def iv(x):return x if isinstance(x,IV) else IV(x)
def atan_interval(inv,N=20):
 x=F(1,inv);terms=[(-1)**k*x**(2*k+1)/F(2*k+1) for k in range(N+1)]
 t=sum(terms[:-1]); return IV(min(t,t+terms[-1]),max(t,t+terms[-1]))
PI=16*atan_interval(5)-4*atan_interval(239)
B=10**45;K=isqrt(2*B*B);RT2=IV(F(K,B),F(K+1,B))
def altbound(z,N,kind):
 assert z>=0 and z<=F(2)
 coeff=(0 if kind=='cos' else 1)
 a=sum(F((-1)**k, factorial(2*k+coeff))*z**(2*k+coeff) for k in range(N))
 b=a+F((-1)**N,factorial(2*N+coeff))*z**(2*N+coeff)
 return IV(min(a,b),max(a,b))
@lru_cache(None)
def trig(n,j):
 j=j%n
 if 4*j<=n: f=F(2*j,n); cs=1;ss=1
 elif 2*j<=n: f=F(n-2*j,n);cs=-1;ss=1
 elif 4*j<=3*n: f=F(2*j-n,n);cs=-1;ss=-1
 else:f=F(2*n-2*j,n);cs=1;ss=-1
 zlo=f*PI.a; zhi=f*PI.b
 # cos decreasing on [0, pi/2], sin increasing there
 cos=IV(altbound(zhi,12,'cos').a,altbound(zlo,12,'cos').b)
 sin=IV(altbound(zlo,12,'sin').a,altbound(zhi,12,'sin').b)
 return cs*cos,ss*sin
@lru_cache(None)
def gram(n,J):
 c1=iv(0);s1=iv(0);c2=iv(0);s2=iv(0)
 for j in J:
  c,s=trig(n,j);c1=c1+c;s1=s1+s
  c,s=trig(n,2*j);c2=c2+c;s2=s2+s
 k=F(len(J));n=F(n)
 return [[iv(k/n),RT2*c1/n,RT2*s1/n],[RT2*c1/n,(k+c2)/n,s2/n],[RT2*s1/n,s2/n,(k-c2)/n]]
def det(M):
 if len(M)==1:return M[0][0]
 if len(M)==2:return M[0][0]*M[1][1]-M[0][1]*M[1][0]
 return sum((1 if j%2==0 else -1)*M[0][j]*det([[M[i][h] for h in range(3) if h!=j] for i in (1,2)]) for j in range(3))
def sub(M,J):return [[M[i][j] for j in J] for i in J]
def pd(M):return all(det(sub(M,range(k))).a>0 for k in (1,2,3))
def notpsd(M):return any(det(sub(M,J)).b<0 for k in (1,2,3) for J in combinations(range(3),k))
def shift(M,t,sign):
 return [[(sign*M[i][j]+(t if i==j else 0)) for j in range(3)] for i in range(3)]
# for min bound: G - lI = shift(G,-l,+1), G-uI
# for max bound: upper I -G = shift(G,upper,-1)
def verify_eigen_interval(n,J,minlo,minhi,maxlo,maxhi):
 M=gram(n,J)
 checks=[pd(shift(M,-minlo,1)),notpsd(shift(M,-minhi,1)),pd(shift(M,maxhi,-1)),notpsd(shift(M,maxlo,-1))]
 if not all(checks):raise AssertionError((n,J,checks, minlo,minhi,maxlo,maxhi,det(shift(M,-minhi,1)),det(shift(M,maxlo,-1))))
 return True

# Each certified interval endpoint is an integer multiple of 1/100000.
# (n, representative, orbit size, min lower, min upper, max lower, max upper).
BOUNDS = [(5, (0, 1, 2, 3), 5, 39997, 40004, 99997, 100004), (6, (0, 1, 2, 3), 6, 16663, 16670, 99997, 100003), (6, (0, 1, 2, 4), 6, 49996, 50003, 99997, 100004), (6, (0, 1, 3, 4), 3, 33330, 33337, 99997, 100003), (7, (0, 1, 2, 3), 7, 7607, 7614, 98744, 98751), (7, (0, 1, 2, 4), 14, 24828, 24835, 94306, 94313), (7, (0, 1, 3, 4), 7, 18284, 18291, 89239, 89246), (7, (0, 1, 3, 5), 7, 45683, 45690, 75458, 75465), (8, (0, 1, 2, 3), 8, 3803, 3810, 96190, 96197), (8, (0, 1, 2, 4), 16, 12856, 12863, 87137, 87144), (8, (0, 1, 2, 5), 8, 24997, 25004, 90447, 90454), (8, (0, 1, 3, 4), 8, 9546, 9553, 74997, 75003), (8, (0, 1, 3, 5), 16, 27735, 27742, 72258, 72265), (8, (0, 1, 3, 6), 8, 30862, 30869, 69131, 69138), (8, (0, 1, 4, 5), 4, 14641, 14648, 85352, 85359), (8, (0, 2, 4, 6), 2, 49996, 50003, 49997, 50003), (9, (0, 1, 2, 3), 9, 2055, 2062, 92739, 92746), (9, (0, 1, 2, 4), 18, 7030, 7037, 81486, 81493), (9, (0, 1, 2, 5), 18, 15463, 15470, 83982, 83989), (9, (0, 1, 3, 4), 9, 5196, 5203, 66663, 66670), (9, (0, 1, 3, 5), 18, 16010, 16017, 67806, 67813), (9, (0, 1, 3, 6), 18, 33330, 33337, 66663, 66670), (9, (0, 1, 3, 7), 9, 18360, 18367, 66663, 66670), (9, (0, 1, 4, 5), 9, 9442, 9449, 76434, 76441), (9, (0, 1, 4, 6), 9, 23559, 23566, 66663, 66670), (9, (0, 2, 4, 6), 9, 31701, 31708, 51693, 51700)]
WINNERS = {5:(0,1,2,3),6:(0,1,2,4),7:(0,1,3,5),8:(0,2,4,6)}

def main():
    entries = {}
    for n,J,size,l,h,L,H in BOUNDS:
        unseen = set(combinations(range(n),4)) if n not in entries else None
        assert verify_eigen_interval(n,J,F(l,100000),F(h,100000),F(L,100000),F(H,100000))
        entries.setdefault(n,[]).append((J,size,l,h,L,H))
    for n, items in entries.items():
        universe=set(combinations(range(n),4))
        for J,size,*_ in items:
            orbit={tuple(sorted(((s*x+t)%n for x in J))) for s in (-1,1) for t in range(n)}
            assert min(orbit)==J
            assert size==len(orbit)
            assert orbit <= universe
            universe-=orbit
        assert not universe
        e_w=WINNERS.get(n,(0,1,3,6))
        k_w=WINNERS.get(n,(0,2,4,6))
        e=next(x for x in items if x[0]==e_w)
        k=next(x for x in items if x[0]==k_w)
        for x in items:
            if x[0]!=e_w: assert e[2]>x[3],(n,'E',e,x)
            if x[0]!=k_w: assert F(k[5],k[2])<F(x[4],x[3]),(n,'K',k,x)
    print('VERIFY_OK: 26 exhaustive dihedral orbits; exact rational spectral bounds and strict global optimization comparisons')

if __name__=='__main__': main()
