"""Independent exact-coefficient and polynomial-jet checks for spherical harmonic 2-jets.
Run with: python verify.py (requires sympy and numpy).
"""
import itertools, math
import numpy as np
import sympy as sp

D,L = sp.symbols('D L', positive=True, integer=True)
q = L*(L+D-2)
R = 2*L*(2*L+D-2)
S = (2*L-2)*(2*L+D-4)
a = -L*(D-L**2+4*L-4)/((L-1)*(D+2*L-4)*(D+2*L-2))
b = 2*(L-1)/(L*(D+2*L-4)*(D+2*L-2))
c = 1/(L*(L-1)*(D+2*L-4)*(D+2*L-2))
z=sp.symbols('z')
assert sp.factor(a+b*q+c*q*(q-D+2)-1)==0
assert sp.factor(b/sp.Integer(2)+c*(q-(D-2)/2) - (1/R+1/S))==0
assert sp.factor(c/sp.Integer(4) - 1/(R*S))==0
P=sp.expand(a+b*(q-z/2)+c*(q*(q-D+2)-(q-(D-2)/2)*z+z*z/4))
assert sp.factor(P-(1-z/R)*(1-z/S))==0
for d in range(3,13):
 for l in range(2,13):
  aa,bb,cc=(sp.factor(u.subs({D:d,L:l})) for u in (a,b,c))
  assert (aa>=0)==(d <= (l-2)**2)
  assert bb>0 and cc>0
print('Algebraic polynomial identity and sharp coefficient signs: PASS')

x,y,z = sp.symbols('x y z')
vars=(x,y,z)
mons=[x**a*y**b*z**(4-a-b) for a in range(5) for b in range(5-a)]
low=[x**a*y**b*z**(2-a-b) for a in range(3) for b in range(3-a)]
lapmat=sp.Matrix([[sp.expand(sum(sp.diff(m,v,2) for v in vars)).coeff(lowm) for m in mons] for lowm in low])
null=lapmat.nullspace()
assert len(null)==9
basis=[sp.expand(sum(t*m for t,m in zip(v,mons))) for v in null]
for f in basis: assert sp.expand(sum(sp.diff(f,v,2) for v in vars))==0

def avg_sphere(poly):
 poly=sp.Poly(sp.expand(poly),vars)
 s=sp.Rational(0)
 for (i,j,k),coef in poly.terms():
  if any(n%2 for n in (i,j,k)):continue
  A=(i+j+k)//2
  def odddf(t):return sp.factorial2(t) if t>=0 else 1
  moment=sp.Rational(odddf(i-1)*odddf(j-1)*odddf(k-1),odddf(2*A+1))
  s+=coef*moment
 return sp.simplify(s)
G=np.array([[float(avg_sphere(f*g)) for g in basis] for f in basis])
phi=(1+5**0.5)/2
pts=[]
for a0,b0 in ((1.,phi),(phi,0.),(0.,1.)):
 # Explicit icosahedral orientation: (0,±1,±phi), (±1,±phi,0), (±phi,0,±1)
 pass
for v in [ (0.,sy,sz*phi) for sy in (-1,1) for sz in (-1,1)] + [(sx,sy*phi,0.) for sx in (-1,1) for sy in (-1,1)] + [(sx*phi,0.,sz) for sx in (-1,1) for sz in (-1,1)]:
 v=np.array(v); pts.append(v/np.linalg.norm(v))
assert len(pts)==12
vals=sp.lambdify((x,y,z),sp.Matrix(basis),'numpy')
grads=sp.lambdify((x,y,z),sp.Matrix([[sp.diff(f,v) for v in vars] for f in basis]),'numpy')
hesses=sp.lambdify((x,y,z),sp.Array([[[sp.diff(f,u,v) for v in vars] for u in vars] for f in basis]),'numpy')
A,B,C=(float(u.subs({D:3,L:4})) for u in (a,b,c))
Q=np.zeros((9,9))
for pt in pts:
 f=np.asarray(vals(*pt),dtype=float).reshape(9)
 du=np.asarray(grads(*pt),dtype=float).reshape((9,3))
 dd=np.asarray(hesses(*pt),dtype=float).reshape((9,3,3))
 proj=np.eye(3)-np.outer(pt,pt)
 gt=du@proj
 ht=np.einsum('ij,bjk,kl->bil',proj,dd,proj)-4*f[:,None,None]*proj[None,:,:]
 Q+=(A*np.outer(f,f)+B*(gt@gt.T)+C*np.einsum('aij,bij->ab',ht,ht))/12
err=np.max(np.abs(Q-G))
assert err<1e-11,err
print('Icosahedral H_4 Gram from independent Cartesian jets: PASS', 'max absolute error',f'{err:.4g}')
print('d=3 l=4 coefficients',A,B,C,'harmonic dimension',len(basis),'nodes',len(pts))
# Icosahedral rule is a 5-design (even moments through degree 4) but not an 8-design.
witness=False
for a0 in range(9):
 for b0 in range(9-a0):
  c0=8-a0-b0
  mon=x**a0*y**b0*z**c0
  emp=np.mean([float(sp.lambdify((x,y,z),mon,'numpy')(*p)) for p in pts])
  exact=float(avg_sphere(mon))
  if abs(emp-exact)>1e-10:
   print('Degree-eight non-design witness:',(a0,b0,c0),'moment difference',f'{emp-exact:.10g}')
   witness=True
   break
 if witness:break
assert witness
# Independent derivative-only boundary case on the 24-cell in S^3.
x4=sp.symbols('x0:4')
mons4=[]
for i in range(5):
 for j in range(5-i):
  for k in range(5-i-j):
   h=4-i-j-k
   mons4.append(x4[0]**i*x4[1]**j*x4[2]**k*x4[3]**h)
low4=[]
for i in range(3):
 for j in range(3-i):
  for k in range(3-i-j):
   h=2-i-j-k
   low4.append(x4[0]**i*x4[1]**j*x4[2]**k*x4[3]**h)
mat4=sp.Matrix([[sp.expand(sum(sp.diff(m,v,2) for v in x4)).coeff(lowm) for m in mons4] for lowm in low4])
nul4=mat4.nullspace()
assert len(nul4)==25
basis4=[sp.expand(sum(t*m for t,m in zip(v,mons4))) for v in nul4]

def moment4(poly):
 res=sp.Rational(0)
 for powers,coef in sp.Poly(sp.expand(poly),x4).terms():
  if any(t%2 for t in powers):continue
  A=sum(powers)//2
  numer=1
  for t in powers:numer*=sp.factorial2(t-1) if t else 1
  denom=1
  for j in range(A):denom*=4+2*j
  res+=coef*sp.Rational(numer,denom)
 return res
G4=np.array([[float(moment4(f*g)) for g in basis4] for f in basis4])
P4=[]
for i,j in itertools.combinations(range(4),2):
 for s1,s2 in itertools.product((-1.,1.),repeat=2):
  pt=np.zeros(4);pt[i]=s1/2**0.5;pt[j]=s2/2**0.5
  P4.append(pt)
assert len(P4)==24
va4=sp.lambdify(x4,sp.Matrix(basis4),'numpy')
gr4=sp.lambdify(x4,sp.Matrix([[sp.diff(f,v) for v in x4] for f in basis4]),'numpy')
he4=sp.lambdify(x4,sp.Array([[[sp.diff(f,u,v) for v in x4] for u in x4] for f in basis4]),'numpy')
A4,B4,C4=(float(u.subs({D:4,L:4})) for u in (a,b,c))
assert A4==0
Q4=np.zeros((25,25))
for pt in P4:
 f=np.asarray(va4(*pt),dtype=float).reshape(25)
 du=np.asarray(gr4(*pt),dtype=float).reshape((25,4))
 dd=np.asarray(he4(*pt),dtype=float).reshape((25,4,4))
 proj=np.eye(4)-np.outer(pt,pt)
 gt=du@proj
 ht=np.einsum('ij,bjk,kl->bil',proj,dd,proj)-4*f[:,None,None]*proj[None,:,:]
 Q4+=(B4*(gt@gt.T)+C4*np.einsum('aij,bij->ab',ht,ht))/24
err4=np.max(np.abs(Q4-G4))
assert err4<1e-11,err4
print('24-cell S^3 H_4 derivative-only Gram: PASS', 'max absolute error',f'{err4:.4g}')
print('d=4 l=4 coefficients',A4,B4,C4,'harmonic dimension',len(basis4),'nodes',len(P4))
# Check the node rules' asserted polynomial precision independently.
for degrees,nodes,variables,moment_fn,max_degree in [
    (3,pts,(x,y,z),avg_sphere,5),
    (4,P4,x4,moment4,4),
]:
 for deg in range(max_degree+1):
  for powers in itertools.product(range(deg+1),repeat=degrees):
   if sum(powers)!=deg:continue
   mon=sp.prod(v**p for v,p in zip(variables,powers))
   got=sum(float(np.prod(node**np.array(powers))) for node in nodes)/len(nodes)
   want=float(moment_fn(mon))
   assert abs(got-want)<1e-10,(degrees,deg,powers,got,want)
 print('Exactness of node rule through degree',max_degree,'in ambient dimension',degrees,': PASS')
