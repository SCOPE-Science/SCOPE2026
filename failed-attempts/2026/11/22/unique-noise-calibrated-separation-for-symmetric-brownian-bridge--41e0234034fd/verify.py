"""Reproduce symbolic identities and finite consistency checks for a two-site Brownian-bridge IMSE design."""
import sympy as S

x,y,t,h,eta,a,z=S.symbols('x y t h eta a z', real=True)
Kxx=x*(1-x)
Kyy=y*(1-y)
Kxy=x*(1-y)
Cxx=x*x*(1-x)**2/3
Cyy=y*y*(1-y)**2/3
Cxy=x*(1-y)*(2*y-x*x-y*y)/6

# Independent piecewise integration of squared-kernel cross products.
Cxy_direct=(S.integrate(t*t*(1-x)*(1-y),(t,0,x))
            +S.integrate(x*(1-t)*t*(1-y),(t,x,y))
            +S.integrate(x*y*(1-t)**2,(t,y,1)))
assert S.factor(Cxy-Cxy_direct)==0
assert S.factor(Cxy.subs(y,x)-Cxx)==0

D=(Kxx+eta)*(Kyy+eta)-Kxy**2
G=S.factor(((Kyy+eta)*Cxx+(Kxx+eta)*Cyy-2*Kxy*Cxy)/D)
Gs=S.factor(G.subs({x:(1-a)/2,y:(1+a)/2}))
G_formula=(1-a)**2*(2*eta*(1+a)**2+a*(1-a)*(1+3*a))/(12*(1-a+2*eta)*(a*(1-a)+2*eta))
assert S.factor(Gs-G_formula)==0

q=(32*eta**3*z**6+(144*eta**3+40*eta**2)*z**5
   +(256*eta**3+112*eta**2+16*eta)*z**4
   +(224*eta**3+98*eta**2+18*eta+2)*z**3
   +(96*eta**3+18*eta**2-2*eta-1)*z**2
   +(16*eta**3-10*eta**2-4*eta)*z-2*eta**2)
identity=S.diff(G_formula,a)+(1-a)**7*q.subs(z,a/(1-a))/(6*(1-a+2*eta)**2*(a*(1-a)+2*eta)**2)
assert S.factor(identity)==0
assert S.factor(q.subs(z,S.Rational(1,2))-3*eta*(6*eta+1)*(18*eta+1)/4)==0
assert S.factor(S.diff(G_formula,a).subs(a,0)-1/(12*(1+2*eta)**2))==0

# Every co-located pair is dominated by co-location at the midpoint.
v=S.symbols('v',positive=True)
R=2*v**2/(3*(eta+2*v))
assert S.factor(S.diff(R,v)-4*v*(eta+v)/(3*(eta+2*v)**2))==0
assert S.factor(G_formula.subs(a,0)-R.subs(v,S.Rational(1,4)))==0

# The positive Descartes root lies in (0,1/2) for all positive noise.
assert S.factor(q.subs(z,0)+2*eta**2)==0

# Rational consistency checks against the general two-point formula, including coincident sites.
checks=0
for ev in [S.Rational(1,100),S.Rational(1,5),S.Rational(1,2),S.Integer(1),S.Integer(5)]:
    for j in range(1,15):
        aa=S.Rational(j,42)
        xx=(1-aa)/2
        yy=(1+aa)/2
        assert S.factor(G.subs({x:xx,y:yy,eta:ev})-G_formula.subs({a:aa,eta:ev}))==0
        checks+=1

# Roots are supplementary numerical illustrations, not an infinite-domain proof.
for ev in (S.Rational(1,100),S.Rational(1,10),S.Integer(1),S.Integer(10)):
    root=S.nsolve(q.subs(eta,ev),(0,S.Rational(1,2)),solver='bisect',verify=False)
    root=float(root)
    assert 0 < root < .5
    left=(1-root)/2
    assert 0 < left < .5
    print('noise',ev,'separation',format(root/(1+root),'.12f'),'sites',format((1-root/(1+root))/2,'.12f'),format((1+root/(1+root))/2,'.12f'))
print('PASS: symbolic identities and',checks,'exact rational consistency checks; uniqueness and limits are analytic arguments')
