"""Exact Seidel characteristic-polynomial comparison for three witnesses; requires SymPy."""
import sympy as sp
x=sp.Symbol('x')
n=8
expected={
 39516:(x-1)*(x+1)*(x*x-5)*(x**4-22*x*x+101),
 39527:(x*x-5)*(x**6-23*x**4+123*x*x-37),
 43885:(x-1)*(x+1)*(x*x-13)*(x**4-14*x*x+29),
}
for g in expected:
 adj=[[0]*n for _ in range(n)]
 bit=0
 for i in range(1,n):
  for j in range(i+1,n):
   adj[i][j]=adj[j][i]=(g>>bit)&1;bit+=1
 seidel=sp.Matrix(n,n,lambda i,j:0 if i==j else 1-2*adj[i][j])
 polynomial=sp.factor(seidel.charpoly(x).as_expr())
 assert sp.expand(polynomial-expected[g])==0
 print('MASK',g,'CHARPOLY',polynomial)
print('SPECTRA_DISTINCT_OK')
