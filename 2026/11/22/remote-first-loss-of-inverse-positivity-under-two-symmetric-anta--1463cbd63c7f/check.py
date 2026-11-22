"""Exact arithmetic checks for the two-antichord screened-path theorem.

Run: python check.py (requires SymPy). This supplements the universal algebraic proof.
"""
import sympy as s

x,a,b,d=s.symbols('x a b d')
S=s.Matrix([[a-x,-1,x,0],[-1,b-x,-d,x],
            [x,-d,b-x,-1],[0,x,-1,a-x]])
N=S.adjugate()
expected={
 (0,1): a*b-a*d*x-a*x-b*x+d*x*x+2*x*x-1,
 (0,2): -a*b*x+a*d+a*x*x+b*x*x-d*x-x,
 (0,3): d+(d+2)*x*x-2*b*x,
 (1,2): (a-x)*(a*d-(d+2)*x),
 (1,3): -a*b*x+a*d+a*x*x+b*x*x-d*x-x,
 (2,3): a*b-a*d*x-a*x-b*x+d*x*x+2*x*x-1,
}
checks=0
for (i,j),expr in expected.items():
 assert s.expand(N[i,j]-expr)==0
 checks+=1
for n in range(4,13):
 m=n-4
 D=[s.Integer(1),s.Integer(3)]
 for z in range(2,m+1): D.append(3*D[-1]-D[-2])
 dm=D[m];dp=D[m-1] if m>0 else s.Integer(0)
 bb=3-dp/dm;dd=1/dm
 disc=s.factor(bb**2-dd*(dd+2))
 tau=s.simplify(dd/(bb+s.sqrt(disc)))
 pd=(2*(bb+dd)-1)/(bb+dd+4)
 assert 0<tau<dd/4<pd<1
 checks+=1
 A=s.zeros(n)
 for i in range(n): A[i,i]=2 if i in (0,n-1) else 3
 for i in range(n-1): A[i,i+1]=A[i+1,i]=-1
 B=s.zeros(n)
 for i,j in [(0,n-2),(1,n-1)]:
  B[i,i]-=1;B[j,j]-=1;B[i,j]+=1;B[j,i]+=1
 tlo=1/(4*dm*bb)
 thi=1/(dm*bb)
 assert tlo<tau<thi<pd
 checks+=1
 for t,sign in [(s.Integer(0),1),(tlo,1),(thi,-1)]:
  M=A+t*B
  inv=M.inv()
  assert s.factor(inv[0,n-1])*sign>0
  checks+=1
  if sign==1:
   for val in inv:
    assert val>0
    checks+=1
  assert M.det()>0
  checks+=1
 # Explicit Kron complement at all rational test strengths
 for t in (s.Rational(0),tlo,thi):
  inds=[0,1,n-2,n-1]
  inside=list(range(2,n-2))
  M=A+t*B
  if inside:
   H=M.extract(inside,inside)
   K=M.extract(inds,inside)
   Z=M.extract(inds,inds)-K*H.inv()*K.T
  else: Z=M
  Si=S.subs({a:2,b:bb,d:dd,x:t})
  assert Z==Si
  checks+=1
 print(f'n={n}: D={dm}, positivity threshold={tau.evalf(12)}, SPD threshold={pd.evalf(12)}')
print('Exact checks:',checks)
