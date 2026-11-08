"""Exact algebra and finite-state checks for synchronous two-walker meeting times."""
from fractions import Fraction
from itertools import combinations
import sympy as sp

a,b,p,u,v=sp.symbols('a b p u v', integer=True)
d=a+b-1
q=(1-p)/d
r=(1-p)/a
c=p+(a-1)*q
M=sp.Matrix([
    [c*c-2*p*q-(a-2)*q*q, 2*c*b*q, b*(b-1)*q*q],
    [(a-1)*r*c, p*c+b*q*(1-p), (b-1)*q*p],
    [a*(a-1)*r*r, 2*p*a*r, p*p]
])
F=sp.eye(3)-M
h=F.inv()*sp.ones(3,1)
Q=sp.factor(-sp.factor((h[0]-h[1])*F.det())*a*d**3 / ((b-1)*(1-p)**2))
R=sp.factor(-sp.factor((h[1]-h[2])*F.det())*a*d**3 / (1-p)**2)
S=sp.factor(-sp.factor((h[0]-h[2])*F.det())*a*d**3 / (1-p)**2)
assert sp.expand(S-((b-1)*Q+R))==0
assert sp.degree(Q,p)==2 and sp.degree(R,p)==2 and sp.degree(S,p)==2
assert sp.expand(Q.subs(p,0)-(a+b*b+b-1))==0
assert sp.expand(Q.subs(p,1)+2*(b-1)*(a+b-1))==0
assert sp.expand(R.subs(p,0)+b*(a*a+3*a*b-2*a+b*b-3*b))==0
assert sp.expand(R.subs(p,1)-2*(a+b-1)*(a*a+3*a*b+b*b-b))==0
assert sp.expand(S.subs(p,0)+(a-1)*(a*b+3*b*b-2*b+1))==0
assert sp.expand(S.subs(p,1)-2*(a+b-1)*(a*a+3*a*b+b-1))==0
resultant=sp.factor(sp.resultant(Q,R,p))
P=sp.factor(resultant/(-2*(a+b-1)*(a*b-2*a+b*b-2*b+1)))
Pshift=sp.Poly(sp.expand(P.subs({a:u+2,b:v+2})),u,v)
assert len(Pshift.terms())==36
assert all(coeff>0 for coeff in Pshift.coeffs())
assert sp.factor(Q.subs({a:2,b:2,p:sp.Rational(4,15)}))==-sp.Rational(41,225)
assert sp.factor(R.subs({a:2,b:2,p:sp.Rational(4,15)}))==-sp.Rational(384,225)


def fullpair(a0,b0,p0):
    n=a0+b0
    edges={i:([j for j in range(a0) if j!=i]+list(range(a0,n))) for i in range(a0)}
    edges.update({i:list(range(a0)) for i in range(a0,n)})
    transitions=[]
    for i in range(n):
        opts={i:p0}
        for j in edges[i]:opts[j]=(1-p0)/len(edges[i])
        transitions.append(opts)
    pairs=list(combinations(range(n),2))
    ix={pair:k for k,pair in enumerate(pairs)}
    A=sp.eye(len(pairs))
    for idx,(i,j) in enumerate(pairs):
        for dest1,prob1 in transitions[i].items():
            for dest2,prob2 in transitions[j].items():
                if dest1!=dest2:
                    A[idx,ix[tuple(sorted((dest1,dest2)))]]-=prob1*prob2
    vals=A.inv()*sp.ones(len(pairs),1)
    return {pair:sp.factor(vals[idx]) for idx,pair in enumerate(pairs)}

checks=0
for a0,b0 in [(2,2),(2,3),(3,2),(3,4),(4,3),(5,2)]:
    for p0 in (sp.Rational(1,5),sp.Rational(2,5),sp.Rational(3,4)):
        full=fullpair(a0,b0,p0)
        reduced=[sp.cancel(z.subs({a:a0,b:b0,p:p0})) for z in h]
        for (i,j),val in full.items():
            k=0 if i<a0 and j<a0 else (1 if i<a0<=j else 2)
            assert sp.cancel(val-reduced[k])==0, (a0,b0,p0,i,j)
            checks+=1
print('VERIFY_OK',checks,'exact state comparisons; 36 strictly positive resultant coefficients; polynomial identities confirmed')
