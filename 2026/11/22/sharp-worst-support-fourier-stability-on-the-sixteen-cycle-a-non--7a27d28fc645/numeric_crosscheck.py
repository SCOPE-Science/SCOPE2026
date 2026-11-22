#!/usr/bin/env python3
"""Independent floating-point corroboration of exact cyclotomic inequalities.
Floating point is diagnostic only; exact conclusions use certificate.py.
"""
import cmath,math
from itertools import combinations
N=16
F=[[cmath.exp(2j*math.pi*r*c/N) for c in range(N)] for r in range(N)]

def jacobi_min_eigenvalue(H):
 n=len(H);a=[[0.0]*(2*n) for _ in range(2*n)]
 for i in range(n):
  for j in range(n):
   z=H[i][j]; a[i][j]=z.real; a[i][j+n]=-z.imag
   a[i+n][j]=z.imag; a[i+n][j+n]=z.real
 m=2*n
 for _ in range(600):
  p,q=max(((i,j) for i in range(m) for j in range(i+1,m)),key=lambda z:abs(a[z[0]][z[1]]))
  if abs(a[p][q])<1e-12:break
  tau=(a[q][q]-a[p][p])/(2*a[p][q])
  t=(1 if tau>=0 else -1)/(abs(tau)+math.sqrt(1+tau*tau))
  c=1/math.sqrt(1+t*t);s=t*c
  app=a[p][p];aqq=a[q][q];apq=a[p][q]
  a[p][p]=app-t*apq;a[q][q]=aqq+t*apq;a[p][q]=a[q][p]=0
  for k in range(m):
   if k==p or k==q:continue
   akp=a[k][p];akq=a[k][q]
   a[k][p]=a[p][k]=c*akp-s*akq
   a[k][q]=a[q][k]=s*akp+c*akq
 return min(a[i][i] for i in range(m))

def gram(R,C):
 V=[[F[r][c] for c in C] for r in R]
 return [[sum(V[r][i].conjugate()*V[r][j] for r in range(4)) for j in range(4)] for i in range(4)]

def main():
 for R in [(0,1,2,3),(0,1,2,7),(0,1,3,14)]:
  lo=float('inf');w=[]
  for C in combinations(range(N),4):
   eig=jacobi_min_eigenvalue(gram(R,C))
   if eig<lo-1e-8:lo=eig;w=[C]
   elif abs(lo-eig)<1e-8:w.append(C)
  print('ROW',R,'MIN_SQUARED',format(lo,'.12f'),'COLUMN_MINIMIZERS',len(w),'FIRST',w[:4]);
  assert lo>0
  if R==(0,1,3,14):assert lo>0.001
  else:assert lo<0.001
 print('DIAGNOSTIC_NUMERIC_PASS')
if __name__=='__main__':main()
