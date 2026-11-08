#!/usr/bin/env python3
"""Exact symbolic checks for stationary-moment inversion in a stopped active particle.
Requires SymPy; no network or data files. Run: python verify.py
"""
import sympy as sp

a,b,u,t,w=sp.symbols('a b u t w',positive=True)
Q=sp.Matrix([[-a,0,a],[0,-a,a],[b/2,b/2,-b]])
V=sp.diag(1,-1,0)
pi=sp.Matrix([b/(2*(a+b)),b/(2*(a+b)),a/(a+b)])
assert sp.simplify(Q.T*pi)==sp.zeros(3,1)
M=[None]*7
vec=pi
M[0]=sp.Integer(1)
checks=1
for n in range(1,7):
    vec=(n*sp.eye(3)-Q.T).inv()*n*V*vec
    M[n]=sp.factor(sum(vec))
    assert sp.simplify((n*sp.eye(3)-Q.T)*vec-n*V*(pi if n==1 else prev))==sp.zeros(3,1)
    if n%2: assert M[n]==0
    prev=vec
    checks+=1
for n in (1,2,3):
    target=sp.factor(sp.factorial2(2*n-1)*sp.prod(b+2*j for j in range(n)) /
                     (sp.prod(a+2*j+1 for j in range(n))*sp.prod(a+b+2*j for j in range(n))))
    assert sp.factor(M[2*n]-target)==0
    checks+=1

# Fixed-variance parametrization u=E[X^2]; t=u(a+1), u<t<1.
a_of=t/u-1
b_of=t*(t-u)/(u*(1-t))
assert sp.factor(M[2].subs({a:a_of,b:b_of}, simultaneous=True)-u)==0
checks+=1
K=sp.factor(M[4].subs({a:a_of,b:b_of}, simultaneous=True)/u**2)
R=sp.factor(M[6].subs({a:a_of,b:b_of}, simultaneous=True)/(u*M[4].subs({a:a_of,b:b_of}, simultaneous=True)))
K0=3*(t*t-3*t*u+2*u)/((t+2*u)*(t+u-2*t*u))
R0=5*(t*t-5*t*u+4*u)/((t+4*u)*(t+3*u-4*t*u))
assert sp.factor(K-K0)==0 and sp.factor(R-R0)==0
checks+=2
P=(5*u-3)*t*t+(2-6*u)*t+3*u-u*u
assert sp.factor(sp.diff(K0,t)+6*u*P/((t+2*u)**2*(t+u-2*t*u)**2))==0
checks+=1
assert sp.factor(P.subs(t,u)-5*u*(1-u)**2)==0
assert sp.factor(P.subs(t,1)+(1-u)**2)==0
assert sp.factor(K0.subs(t,u)-1/u)==0
assert sp.factor(K0.subs(t,1)-3/(1+2*u))==0
checks+=4

# The symmetric cross-multiplication identities determine all possible
# distinct pairs that share both K and R.
S,T=sp.symbols('S T')
def diffnumer(f):
    num,den=sp.fraction(sp.factor(f))
    return sp.factor((num*den.subs(t,w)-num.subs(t,w)*den)/(t-w))
G=diffnumer(K0)
H=diffnumer(R0)
Gplain=(3*u-1)*(t+w)+(3-5*u)*t*w+u*u-3*u
Hplain=(7*u-1)*(t+w)+(3-9*u)*t*w+u*u-7*u
assert sp.factor(G/Gplain).free_symbols<= {u}
assert sp.factor(H/Hplain).free_symbols<= {u}
assert sp.factor(G/Gplain)!=0 and sp.factor(H/Hplain)!=0
checks+=2
sol=sp.solve([(3*u-1)*S+(3-5*u)*T+u*u-3*u,
              (7*u-1)*S+(3-9*u)*T+u*u-7*u],(S,T),dict=True)
assert sol==[{S:(u+3)/2,T:(u+1)/2}]
assert sp.factor(t*t-sol[0][S]*t+sol[0][T]-(t-1)*(t-(u+1)/2))==0
checks+=2

# A concrete exact collision in (second, fourth) moments.
p1={a:sp.Integer(1),b:sp.Integer(4)}
p2={a:sp.Rational(6,5),b:sp.Rational(44,5)}
for q in (p1,p2):
    assert M[2].subs(q)==sp.Rational(2,5)
    assert M[4].subs(q)==sp.Rational(9,35)
    checks+=2
assert M[6].subs(p1)==sp.Rational(4,21)
assert M[6].subs(p2)==sp.Rational(288,1519)
assert M[6].subs(p1)-M[6].subs(p2)==sp.Rational(4,4557)
checks+=3

# Independent rational-grid checks: original generator versus closed moments.
for av in (sp.Rational(1,3),sp.Rational(2,3),sp.Integer(1),sp.Rational(6,5),sp.Integer(2),sp.Integer(5)):
 for bv in (sp.Rational(1,4),sp.Rational(2,3),sp.Integer(1),sp.Integer(4),sp.Rational(44,5)):
    q={a:av,b:bv}
    for n in (1,2,3):
      formula=sp.factorial2(2*n-1)*sp.prod(bv+2*j for j in range(n)) / (sp.prod(av+2*j+1 for j in range(n))*sp.prod(av+bv+2*j for j in range(n)))
      assert M[2*n].subs(q)==formula
      checks+=1

print(f"PASS: {checks} exact checks; three-moment identifiability and two-moment fold verified")
