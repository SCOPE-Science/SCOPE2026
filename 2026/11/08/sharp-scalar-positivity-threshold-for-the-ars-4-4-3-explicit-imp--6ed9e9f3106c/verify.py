"""Exact symbolic reproduction of the ARS(4,4,3) scalar EIN sign frontier.

Requires Python >=3.10 and SymPy >=1.12. Run: python verify.py
"""
import sympy as sp

r,t,x,u,v=sp.symbols('r t x u v',real=True)
F=sp.Rational
E=sp.zeros(5); I=sp.zeros(5)
for i,j,c in [(1,0,F(1,2)),(2,0,F(11,18)),(2,1,F(1,18)),
              (3,0,F(5,6)),(3,1,-F(5,6)),(3,2,F(1,2)),
              (4,0,F(1,4)),(4,1,F(7,4)),(4,2,F(3,4)),(4,3,-F(7,4))]:
    E[i,j]=c
for i,j,c in [(1,1,F(1,2)),(2,1,F(1,6)),(2,2,F(1,2)),
              (3,1,-F(1,2)),(3,2,F(1,2)),(3,3,F(1,2)),
              (4,1,F(3,2)),(4,2,-F(3,2)),(4,3,F(1,2)),(4,4,F(1,2))]:
    I[i,j]=c
assert all(sp.simplify(sum(E[i,j] for j in range(5))-sum(I[i,j] for j in range(5)))==0 for i in range(5))
Y=[sp.Integer(1)]
for i in range(1,5):
    Y.append(sp.cancel((1-t*sum((I[i,j]+(r-1)*E[i,j])*Y[j] for j in range(i)))/(1+t/2)))
R=sp.factor(Y[4])
P=sp.factor(R.subs(t,2*x/(1-x)))
poly=sp.Poly(P,x)
assert poly.degree()==4
bern=[sp.factor(sum(poly.nth(j)*sp.binomial(k,j)/sp.binomial(4,j)
                    for j in range(k+1))) for k in range(5)]
expected=[sp.Integer(1),(2-r)/2,(3-r)*(1-r)/3,
          (3-r*(r-3)**2)/3,(1-r)*(7*r**3+36*r**2-90*r+18)/18]
assert all(sp.simplify(bern[k]-expected[k])==0 for k in range(5))
assert sp.simplify(P-sum(bern[k]*sp.binomial(4,k)*x**k*(1-x)**(4-k) for k in range(5)))==0
Q=7*r**3+36*r**2-90*r+18
assert Q.subs(r,F(22,100))>0 and Q.subs(r,F(221,1000))<0
roots=sp.polys.polytools.intervals(Q,eps=F(1,10**12))
assert len(roots)==3 and roots[1][0][0] > 0 and roots[1][0][1]<F(1,3)
assert sp.simplify(sp.limit(R,t,sp.oo)-expected[4])==0
H=56*r**4+328*r**3-1656*r**2+2052*r-729
assert sp.simplify(R.subs(t,4)+H/729)==0
assert sp.simplify(H.subs(r,F(3,2)+u)-(56*u**4+664*u**3+576*u**2+54*u+F(27,2)))==0
Hq=sp.Poly(sp.expand(H.subs(r,1+v/2)),v)
Hb=[sp.factor(sum(Hq.nth(j)*sp.binomial(k,j)/sp.binomial(4,j)
                  for j in range(k+1))) for k in range(5)]
assert Hb==[sp.Integer(51),F(89,2),sp.Integer(24),F(27,4),F(27,2)]
assert sp.simplify(R.subs({r:1,t:4})+F(17,243))==0
for rv in [F(1,25),F(1,5),F(22,100),F(221,1000),F(1,4),F(1,2),F(9,10),F(1,1),F(3,2),F(2,1),F(5,1)]:
    for tv in [F(1,100),F(1,2),F(1,1),F(2,1),F(4,1),F(10,1),F(100,1)]:
        c=sp.factor(R.subs({r:rv,t:tv}))
        xp=sp.factor(P.subs({r:rv,x:tv/(tv+2)}))
        assert c==xp
print('VERIFY_OK: exact tableau, rational update, five Bernstein coefficients, root isolation, two sharp sign certificates, and 77 rational step identities')
