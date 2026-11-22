"""Exact reproducibility checks for three-particle tandem exclusion counting statistics.

Requires Python 3.10+ and SymPy >=1.12. Run: python verify.py
This program builds the local-move generator independently from bit configurations,
computes the rotation-lumped tilted first two derivatives, and checks both
symbolic expressions and full-state exact-rational Poisson equations.
"""
import itertools
import sympy as sp

q=sp.symbols('q',positive=True)
F = {
 4:sp.Integer(1),
 5:(11*q**3+7*q**2+5*q+1)/((q+1)**2*(3*q+1)),
 6:3*(9*q**4+18*q**3+12*q**2+2*q+1)/(3*q**2+6*q+1)**2,
 7:(9*q**6+54*q**5+128*q**4+146*q**3+80*q**2+38*q+13)/((q+1)*(3*q+5)*(q**2+3*q+1)**2),
 8:(9*q**6+78*q**5+245*q**4+378*q**3+294*q**2+210*q+86)/((q+1)*(3*q+7)*(q**2+4*q+2)**2),
}
J = {
 4:q+1,
 5:(3*q+1)/(q+1),
 6:9*q*(q+1)/(3*q**2+6*q+1),
 7:q*(3*q+5)/(q**2+3*q+1),
 8:q*(3*q+7)/(q**2+4*q+2),
}
EXPECTED_DERIVATIVE = {
 5:8*q**2*(7*q+3),
 6:6*(27*q**4+36*q**3+18*q**2-5),
 7:2*(36*q**8+282*q**7+955*q**6+1829*q**5+2020*q**4+945*q**3-333*q**2-522*q-152),
 8:2*(36*q**8+444*q**7+2123*q**6+5332*q**5+7238*q**4+3020*q**3-4571*q**2-5704*q-1798),
}

def states(n):
 return [x for x in itertools.product((0,1),repeat=n) if sum(x)==3]

def rotate(x,k):
 n=len(x)
 return tuple(x[(i-k)%n] for i in range(n))

def representative(x):
 return min(rotate(x,k) for k in range(len(x)))

def edges(x):
 n=len(x)
 for i in range(n):
  if x[i] and not x[(i+1)%n]:
   rate = int(x[(i-1)%n]) + q*int(x[(i+2)%n])
   if rate:
    y=list(x); y[i]=0; y[(i+1)%n]=1
    yield tuple(y), rate

def matrices(n, quotient):
 xs=states(n)
 if quotient:
  xs=sorted(set(map(representative,xs)))
 index={x:i for i,x in enumerate(xs)}
 m=len(xs)
 L=sp.zeros(m);B=sp.zeros(m)
 for src,x in enumerate(xs):
  for y,rate in edges(x):
   dst=index[representative(y) if quotient else y]
   L[dst,src]+=rate
   L[src,src]-=rate
   B[dst,src]+=rate  # includes diagonal if jump preserves orbit
 return xs,L,B

def strongly_connected(n):
 xs=states(n)
 direct={x:[y for y,rate in edges(x)] for x in xs}
 reverse={x:[] for x in xs}
 for x,neigh in direct.items():
  for y in neigh: reverse[y].append(x)
 def reach(graph):
  seen={xs[0]};stack=[xs[0]]
  while stack:
   for y in graph[stack.pop()]:
    if y not in seen:seen.add(y);stack.append(y)
  return len(seen)==len(xs)
 return reach(direct) and reach(reverse)

def cumulants(L,B,p):
 m=L.rows;one=sp.ones(1,m)
 assert all(sp.cancel(z)==0 for z in L*p)
 assert sp.cancel((one*p)[0]-1)==0
 rate=sp.factor((one*B*p)[0])
 v_rhs=sp.Matrix(B*p-rate*p)
 augmented=L.copy();augmented[m-1,:]=one;v_rhs[m-1]=0
 v=augmented.inv()*(-v_rhs)
 assert sp.simplify((one*v)[0])==0
 assert all(sp.simplify(a)==0 for a in L*v+B*p-rate*p)
 noise=sp.factor(rate+2*(one*B*v)[0])
 return rate,noise

for n in range(4,9):
 assert strongly_connected(n)
 xs,L,B=matrices(n,True)
 m=len(xs);one=sp.ones(1,m)
 eq=L.copy();eq[m-1,:]=one
 b=sp.zeros(m,1);b[-1]=1
 p=eq.inv()*b
 rate,noise=cumulants(L,B,p)
 assert sp.cancel(rate-J[n])==0,(n,rate,J[n])
 assert sp.cancel(noise/rate-F[n])==0,(n,noise/rate,F[n])
 assert sp.factor(sp.diff(rate,q)).subs(q,sp.Integer(1))>0
 print('Symbolic quotient',n,'orbit count',m,'mean',rate,'Fano',sp.factor(noise/rate))
 # Fully labelled configurations at two distinct exact-rational rate ratios.
 for r in (sp.Rational(1,2),sp.Integer(2)):
  full,LF,BF=matrices(n,False)
  LF=LF.subs(q,r);BF=BF.subs(q,r)
  weights=[r**sum(x[i]*x[(i+1)%n] for i in range(n)) for x in full]
  denom=sum(weights)
  pf=sp.Matrix([z/denom for z in weights]);assert LF*pf==sp.zeros(len(full),1)
  rf,nf=cumulants(LF,BF,pf)
  assert rf==J[n].subs(q,r)
  assert sp.cancel(nf/rf-F[n].subs(q,r))==0
  print('  full-state check',n,'q',r,'states',len(full),'PASS')

# Exact analytic sign certificates.
assert sp.factor(F[5]-1)==8*q**3/((q+1)**2*(3*q+1))
p6=9*q**4+9*q**3-3*q**2-3*q+1
assert sp.cancel(F[6]-1-2*p6/(3*q**2+6*q+1)**2)==0
seq=sp.sturm(p6,q)
sign0=[sp.sign(f.subs(q,0)) for f in seq]
signinf=[sp.sign(sp.LC(sp.Poly(f,q))) for f in seq]
assert sign0==[1,-1,-1,1,1] and signinf==[1,1,1,-1,1]
# Equal Sturm variation (2) at both endpoints rules out positive roots.
for n in (7,8):
 num,den=sp.fraction(sp.factor(F[n]-1))
 assert sp.Poly(num,q).degree()==6
 if n==7:
  assert sp.expand(num-2*(3*q**6+14*q**5+21*q**4+5*q**3-13*q**2+4))==0
 else:
  assert sp.expand(num-2*(3*q**6+22*q**5+49*q**4+37*q**3-9*q**2+29*q+29))==0
for n in range(5,9):
 numerator,den=sp.fraction(sp.factor(sp.diff(F[n],q)))
 assert sp.factor(numerator-EXPECTED_DERIVATIVE[n])==0
 coefficients=list(reversed(sp.Poly(numerator,q).all_coeffs()))
 cleaned=[sp.sign(x) for x in coefficients if x!=0]
 if n==5:assert all(x==1 for x in cleaned)
 else:
  assert cleaned[0]==-1 and cleaned[-1]==1
  assert sum(cleaned[i]!=cleaned[i+1] for i in range(len(cleaned)-1))==1
  lo,hi={6:(sp.Rational(376,1000),sp.Rational(377,1000)),7:(sp.Rational(576,1000),sp.Rational(578,1000)),8:(sp.Rational(878,1000),sp.Rational(880,1000))}[n]
  assert numerator.subs(q,lo)<0<numerator.subs(q,hi)
print('All exact symbolic, full-state and sign certificates PASS')
