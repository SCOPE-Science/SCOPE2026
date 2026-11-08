"""Exact symbolic and rational checks for the weighted four-vertex path Gauss heat update.
Requires Python 3 and SymPy. Finite checks supplement, rather than replace, the proof.
"""
import sympy as s
from fractions import Fraction
from itertools import product

a,b,c,h=s.symbols('a b c h',positive=True)
def lap(x,y,z):
    return s.Matrix([[x,-x,0,0],[-x,x+y,-y,0],[0,-y,y+z,-z],[0,0,-z,z]])
L=lap(a,b,c);J=s.ones(4)/4;I=s.eye(4)
G=(L+J).inv()-J
expected=[(-3/a+4/b+1/c)/16,(1/a-4/b+1/c)/16,(1/a+4/b-3/c)/16]
checks=0
for (i,j),e in zip([(0,1),(1,2),(2,3)],expected):
    assert s.cancel(G[i,j]-e)==0;checks+=1
L0=lap(1,2,1);Q=12*I+6*h*L0+h*h*L0*L0
R=I-12*h*Q.inv()*L0
P=(h*h+3*h+3)*(h**4+9*h**3+30*h*h+27*h+9)
expressions=[9*h*(h**3+5*h*h+6*h+3)/P,
             3*h*h*(h**3+6*h*h+15*h+9)/P,
             3*h**3*(2*h*h+6*h+3)/P,
             9*h*(h*h+6*h+6)/P]
for (i,j),f in zip([(0,1),(0,2),(0,3),(1,2)],expressions):
    assert s.cancel(R[i,j]-f)==0;checks+=1
    assert s.cancel(R[3-i,3-j]-f)==0;checks+=1
for x,y,z in product([1,2,3,4],repeat=3):
    vals=[s.factor(t.subs({a:x,b:y,c:z})) for t in expected]
    is_exception=(x==z and y==2*x)
    assert (all(t<=0 for t in vals))==is_exception;checks+=1
for t in [s.Rational(1,100),s.Rational(1,3),1,2,12,100]:
    M=R.subs(h,t)
    assert all(M[i,j]>0 for i in range(4) for j in range(4));checks+=16
    assert all(sum(M.row(i))==1 for i in range(4));checks+=4
Lu=lap(1,1,1);Ru=I-12*h*(12*I+6*h*Lu+h*h*Lu*Lu).inv()*Lu
assert s.cancel(Ru[0,1].subs(h,12)+s.Rational(60,84973))==0;checks+=1
print('VERIFY_OK',checks)
