#!/usr/bin/env python3
"""Exact algebraic checks for the one-line cubic's scheme of lines.
Only the Python standard library is used. Finite checks supplement the proof.
"""
from fractions import Fraction
from itertools import product

# det of the Sylvester matrix of u^3+9u^2+6u+1 and 3u^2+6u+2.
sylvester=[[1,9,6,1,0],[0,1,9,6,1],[3,6,2,0,0],[0,3,6,2,0],[0,0,3,6,2]]
def determinant(A):
 a=[[Fraction(x) for x in row] for row in A]; det=Fraction(1); n=len(a)
 for i in range(n):
  pivot=next((j for j in range(i,n) if a[j][i]),None)
  if pivot is None:return 0
  if pivot!=i:a[i],a[pivot]=a[pivot],a[i];det=-det
  p=a[i][i];det*=p
  for j in range(i+1,n):
   c=a[j][i]/p
   for k in range(i+1,n):a[j][k]-=c*a[i][k]
   a[j][i]=Fraction(0)
 return det
assert determinant(sylvester)==-1, determinant(sylvester)
# Koszul resolution gives (1-t^9)(1-t^12)/(1-t)(1-t^4).
free=[sum(1 for k in range(n//4+1) if n-4*k>=0) for n in range(40)]
def h(n):return free[n] if n>=0 else 0
coeff=[h(n)-h(n-9)-h(n-12)+h(n-21) for n in range(40)]
assert coeff[:17]==[1,1,1,1,2,2,2,2,3,2,2,2,2,1,1,1,1]
assert not any(coeff[17:]);assert sum(coeff)==27

# Enumerate all 2-subspaces of Fp^4, each once by reduced row echelon bases.
def rref_subspaces(p):
 for i in range(3):
  for j in range(i+1,4):
   free1=[k for k in range(i+1,4) if k!=j]
   free2=[k for k in range(j+1,4)]
   for v in product(range(p), repeat=len(free1)+len(free2)):
    a=[0]*4;b=[0]*4;a[i]=b[j]=1
    for k,x in zip(free1,v[:len(free1)]):a[k]=x
    for k,x in zip(free2,v[len(free1):]):b[k]=x
    yield a,b

def cubic_coeff(A,B):
 x,y,z,t=A;X,Y,Z,T=B
 return [
  x*y*y+y*t*t+z*z*z,
  X*y*y+2*x*y*Y+Y*t*t+2*y*t*T+3*z*z*Z,
  x*Y*Y+2*X*y*Y+y*T*T+2*Y*t*T+3*z*Z*Z,
  X*Y*Y+Y*T*T+Z*Z*Z]
for p in [2,3,5,7]:
 lines=[(tuple(A),tuple(B)) for A,B in rref_subspaces(p)
        if all(x%p==0 for x in cubic_coeff(A,B))]
 assert len(lines)==1,(p,lines)
 assert lines[0]==((1,0,0,0),(0,0,0,1)),(p,lines)
 print('F_%d: exactly one projective line'%p)

# Checking the chart elimination for formal random integers by direct expansion.
for a,b,c,d in [(-3,2,1,5),(0,0,0,0),(4,5,-2,1),(-7,-8,3,2)]:
 A=[1,a,c,0];B=[0,b,d,1]
 F=cubic_coeff(A,B)
 assert F==[a*a+c**3,2*a*b+3*c*c*d,b*b+a+3*c*d*d,b+d**3],F
 ap=-d**6-3*c*d*d;bp=-d**3
 formal=cubic_coeff([1,ap,c,0],[0,bp,d,1])
 assert formal==[c**3+9*c*c*d**4+6*c*d**8+d**12,
                 3*c*c*d+6*c*d**5+2*d**9,0,0],formal
print('Sylvester resultant = -1, weighted Hilbert length=27, socle weight=16')
print('ALL_CHECKS_PASSED')
