"""Exact symbolic audit of a graph heat square-function onset identity."""
import sympy as S

a,u,v=S.symbols('a u v',real=True)
p=S.Matrix([1/S.sqrt(2),0,-1/S.sqrt(2)])
q=S.Matrix([1/S.sqrt(6),-2/S.sqrt(6),1/S.sqrt(6)])
F=[a*p[i]+(u+S.I*v)*q[i] for i in range(3)]
D=S.factor(sum(S.expand_complex(z*S.conjugate(z))**2 for z in F))
G=[S.expand((a*a*p[i]**2+(u*u+v*v)*q[i]**2)/4+S.Rational(3,8)*a*u*p[i]*q[i]) for i in range(3)]
assert S.simplify(D/16-sum(t*t for t in G)-S.Rational(7,384)*a*a*u*u)==0
assert S.simplify(sum(p[i]*q[i] for i in range(3)))==0
L=S.Matrix([[1,-1,0,0],[-1,2,-1,0],[0,-1,2,-1],[0,0,-1,1]])
r=S.sqrt(2)
fm=S.Matrix([(1+r)/2,S.Rational(1,2),-S.Rational(1,2),-(1+r)/2])
fp=S.Matrix([(1-r)/2,S.Rational(1,2),-S.Rational(1,2),(-1+r)/2])
f=S.Matrix([1,1,-1,-1])
assert fm+fp==f
assert (L*fm-(2-r)*fm).applyfunc(S.simplify)==S.zeros(4,1)
assert (L*fp-(2+r)*fp).applyfunc(S.simplify)==S.zeros(4,1)
l1,l2=2-r,2+r
assert S.simplify(l1*l2/(l1+l2)**2-S.Rational(1,8))==0
vec=[S.simplify(fm[k]**2/4+fp[k]**2/4+2*S.Rational(1,8)*fm[k]*fp[k]) for k in range(4)]
assert vec==[S.Rational(5,16),S.Rational(3,16),S.Rational(3,16),S.Rational(5,16)]
assert sum(z*z for z in vec)==S.Rational(17,64)
assert sum(z**4 for z in f)==4
assert S.Rational(17,256)>S.Rational(1,16)
print('PASS: exact P3 complex deficit, P4 spectrum, witness, and strict four-vertex onset')
