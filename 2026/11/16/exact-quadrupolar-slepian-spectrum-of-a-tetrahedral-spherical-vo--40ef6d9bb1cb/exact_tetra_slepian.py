import sympy as S
x,y,z=S.symbols('x y z',real=True)
xyz=(x,y,z);r2=x*x+y*y+z*z
sq=S.sqrt
E=S.Matrix([1,1,1])/sq(3);U=S.Matrix([1,-1,0])/sq(2);V=S.Matrix([1,1,-2])/sq(6)
X=S.Matrix([x,y,z]);t=E.dot(X);a=U.dot(X);b=V.dot(X)
q=[(3*t*t-r2)/2, sq(3)*t*a,sq(3)*t*b,sq(3)*(a*a-b*b)/2,sq(3)*a*b]
q=[S.expand(i) for i in q]
W=[S.Matrix(k)/sq(3) for k in [(1,1,-1),(1,-1,1),(-1,1,1)]]
# outward normals and matching endpoints
normals=[S.Matrix(k)/sq(2) for k in [(-1,-1,0),(-1,0,-1),(0,-1,-1)]]
c=-S.Rational(1,3);s=2*sq(2)/3
unit={ (1,0):s, (0,1):1-c,
(3,0):s-s**3/3,(2,1):(1-c**3)/3,(1,2):s**3/3,(0,3):S.Rational(2,3)-c+c**3/3 }
edge=[]
for n in normals:
 v=[w for w in W if S.simplify(n.dot(w))==0]
 assert len(v)==2
 va=v[0]; vb=S.simplify((v[1]-c*va)/s)
 assert S.simplify(va.dot(vb))==0
 edge.append((n,va,vb))
ct,st=S.symbols('ct st')
# integrate tangent normal derivative for homogeneous harmonic h2 or h4
cache={}
def boundary(h):
 h=S.expand(h)
 if h in cache:return cache[h]
 grads=[S.diff(h,i) for i in xyz]
 out=S.Integer(0)
 for n,va,vb in edge:
  f=S.expand(sum(n[i]*grads[i] for i in range(3)))
  zexpr=S.expand(f.subs(dict(zip(xyz,[va[i]*ct+vb[i]*st for i in range(3)])), simultaneous=True))
  pol=S.Poly(zexpr,ct,st)
  out+=sum(coeff*unit[power] for power,coeff in pol.terms() if coeff!=0)
 res=S.simplify(S.radsimp(out));cache[h]=res
 return res

def lap(p):return S.expand(sum(S.diff(p,t,2) for t in xyz))
def integrate(p):
 p=S.expand(p)
 c0=S.simplify(lap(lap(p))/120)
 h2=S.expand((lap(p)-20*c0*r2)/14)
 h4=S.expand(p-r2*h2-r2**2*c0)
 assert S.simplify(lap(h2))==0 and S.simplify(lap(h4))==0
 return S.simplify(S.pi*c0-boundary(h2)/6-boundary(h4)/20)

M=S.zeros(5,5)
for i in range(5):
 for j in range(i,5):
  M[i,j]=S.simplify(5*integrate(q[i]*q[j])/(4*S.pi));M[j,i]=M[i,j]
  print(i,j,M[i,j],flush=True)
# Exact closed-form matrix and spectral assertions.
p=S.pi
A=S.Rational(1,4)+11*S.sqrt(3)/(54*p)
B=S.Rational(1,4)-7*S.sqrt(3)/(27*p)
C=-S.sqrt(6)/(27*p)
Z=S.Rational(1,4)+S.sqrt(3)/(9*p)
T=S.Matrix([[Z,0,0,0,0],
            [0,A,0,0,C],
            [0,0,A,C,0],
            [0,0,C,B,0],
            [0,C,0,0,B]])
assert all(S.simplify(v)==0 for v in M-T)
plus=S.Rational(1,4)+(S.sqrt(219)-S.sqrt(3))/(36*p)
minus=S.Rational(1,4)-(S.sqrt(219)+S.sqrt(3))/(36*p)
assert S.simplify(A+B-plus-minus)==0
assert S.simplify(A*B-C*C-plus*minus)==0
assert S.simplify(S.trace(T)-S.Rational(5,4))==0
assert 219>75
print('Exact triangle, harmonic decomposition, matrix and spectral assertions: PASS')
print('Spectrum:',[(S.N(minus,15),2),(S.N(Z,15),1),(S.N(plus,15),2)])
