#!/usr/bin/env python3
"""Exact Wiman--Edge basepoint canonical-ramification verifier.

Requires Python >=3.10 and SymPy. All jet/determinant arithmetic is over Q[u,p]/(u^2-u+1), using exact rational coefficients.
No external files or network calls are needed.
"""
from fractions import Fraction as Fr
from itertools import permutations
import sympy as sy
x,y,p=sy.symbols('x y p')
G=3*x*x*y*y-sy.Rational(1,2)*x*y*(1+x)*(1+y)*(1+x*y)+(1-x+x*x)*(1-y+y*y)*(1-x*y+x*x*y*y)
H=x*y*(1-x)*(1-y)*(1-x*y)
F=2*(G+p*H)
terms=[(i,j,k,Fr(int(c))) for (i,j,k),c in sy.Poly(F,x,y,p).terms()]
Z=[x*x*y*y-1,x*y*y-1,x*x*y-1,x*y-1,y-1,x-1]
zterms=[[(i,j,Fr(int(c))) for (i,j),c in sy.Poly(z,x,y).terms()] for z in Z]

class E:
 def __init__(self,d=None): self.d={k:Fr(v) for k,v in (d or {}).items() if v}
 def __add__(self,b):
  b=E.co(b);d=self.d.copy()
  for k,v in b.d.items():d[k]=d.get(k,0)+v
  return E(d)
 __radd__=__add__
 def __neg__(self):return E({k:-v for k,v in self.d.items()})
 def __sub__(self,b):return self+-E.co(b)
 def __rsub__(self,b):return E.co(b)+-self
 def __mul__(self,b):
  b=E.co(b);d={}
  for (i,a),v in self.d.items():
   for (j,c),w in b.d.items():
    k=i+j
    # u^2=u-1
    if a+c==2:
     d[(k,1)]=d.get((k,1),0)+v*w
     d[(k,0)]=d.get((k,0),0)-v*w
    else:d[(k,a+c)]=d.get((k,a+c),0)+v*w
  return E(d)
 __rmul__=__mul__
 def __truediv__(self,b):
  if isinstance(b,Fr) or isinstance(b,int):return self*E({(0,0):1/Fr(b)})
  raise ValueError('division only rational')
 def __repr__(self):return str(self.d)
 @staticmethod
 def co(z):return z if isinstance(z,E) else E({(0,0):Fr(z)})
 def polynomial(self):return sy.expand(sum(sy.Rational(v.numerator,v.denominator)*p**i*(sy.Symbol('u') if e else 1) for (i,e),v in self.d.items()))
 def has(self):return bool(self.d)

ONE=E.co(1); ZERO=E(); U=E({(0,1):Fr(1)});P=E({(1,0):Fr(1)})

def mult(a,b,N):
 c=[ZERO]*(N+1)
 for i,ai in enumerate(a[:N+1]):
  if not ai.has():continue
  for j,bj in enumerate(b[:N+1-i]):
   if bj.has():c[i+j]=c[i+j]+ai*bj
 return c

def ev(terms,X,Y,N):
 maxx=max(t[0] for t in terms);maxy=max(t[1] for t in terms)
 xp=[[ONE]+[ZERO]*N];yp=[[ONE]+[ZERO]*N]
 for i in range(maxx):xp.append(mult(xp[-1],X,N))
 for i in range(maxy):yp.append(mult(yp[-1],Y,N))
 out=[ZERO]*(N+1)
 for term in terms:
  if len(term)==4:i,j,k,c=term;scalar=E.co(c)*(P if k else ONE)
  else:i,j,c=term;scalar=E.co(c)
  z=mult(xp[i],yp[j],N)
  for n in range(N+1):out[n]=out[n]+scalar*z[n]
 return out

def jets(N):
 X=[ONE,ONE]+[ZERO]*(N-1);Y=[U]+[ZERO]*N
 # 2F_y at P=4-2u; inverse (1+u)/6
 inv=(ONE+U)/6
 for n in range(1,N+1):
  coef=ev(terms,X,Y,n)[n]
  Y[n]=-coef*inv
 # Formal implicit solution in Q[u,p]/(u^2-u+1), with F_y invertible.
 z=[ev(t,X,Y,N) for t in zterms]
 return z

def det(A):
 ans=ZERO
 for perm in permutations(range(len(A))):
  sign=(-1)**sum(perm[i]>perm[j] for i in range(len(perm)) for j in range(i+1,len(perm)))
  term=ONE
  for i,j in enumerate(perm):term=term*A[i][j]
  ans=ans+sign*term
 return ans


from itertools import combinations

def mod_special(v):
    # The smooth exceptional parameters satisfy p^2=105/4.
    q=Fr(105,4)
    d={}
    for (i,e),c in v.d.items():
        k=(i%2,e)
        d[k]=d.get(k,Fr(0))+c*q**(i//2)
    return E(d)

def minor(z,rows,cols):
    return det([[z[i][j] for j in cols] for i in rows])

def verify():
    # At (x,y)=(1,u), one has 2F_y=4-2u and inverse (1+u)/6.
    z=jets(7)
    w=minor(z,range(6),(0,1,2,3,4,5))
    assert sy.simplify(w.polynomial() - (4*p**2-105)*(4*p**2+3)**3/62208)==0
    # The top five Taylor jets drop rank precisely at p^2=105/4.
    for rows in combinations(range(6),5):
        assert not mod_special(minor(z,rows,(0,1,2,3,4))).has()
    # All six-by-six determinants with orders <=6 vanish on that locus.
    for cols in combinations(range(7),6):
        assert not mod_special(minor(z,range(6),cols)).has()
    m4=mod_special(minor(z,(0,1,2,3),(0,1,2,3)))
    assert m4.has()
    assert m4.polynomial()==4*p*sy.Symbol('u')-2*p-3*sy.Symbol('u')+27
    m5=mod_special(minor(z,(0,1,2,3,4),(0,1,2,3,5)))
    assert m5.has()
    assert m5.polynomial()==-27*p*sy.Symbol('u')-sy.Rational(81,2)*sy.Symbol('u')+81
    m6=mod_special(minor(z,range(6),(0,1,2,3,5,7)))
    assert m6.polynomial()==-486*p
    print('WIMAN_BASEPOINT_CANONICAL_RAMIFICATION_VERIFIED_OK')

if __name__=='__main__':
    verify()
