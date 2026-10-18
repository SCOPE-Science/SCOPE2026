#!/usr/bin/env python3
import sympy as sp

x,y,z,w,t,X=sp.symbols('x y z w t X', real=True)
S=x*x+y*y+z*z+w*w
Q=(x*y+y*z+z*w)**2+(x*z+y*w)**2+(x*w)**2

# 1. Moment identity for nonnegative, phase-aligned coefficients.
# For f=a+bz+cz^2+dz^3, ||f||_4^4=S^2+2Q.
a,b,c,d=sp.symbols('a b c d', real=True)
conv=[a*a,2*a*b,b*b+2*a*c,2*a*d+2*b*c,c*c+2*b*d,2*c*d,d*d]
moment=sp.expand(sum(v*v for v in conv))
S0=a*a+b*b+c*c+d*d
Q0=(a*b+b*c+c*d)**2+(a*c+b*d)**2+(a*d)**2
assert sp.expand(moment-(S0*S0+2*Q0))==0

# 2. Boundary upper bounds for Q/S^2.
r=sp.symbols('r', real=True)
f=sp.expand(2*r*(1-r)+(1-r)**2/sp.Integer(4))
assert sp.factor(f-sp.Rational(4,7)) == -(7*r-3)**2/sp.Integer(28)
# inner-coordinate-zero boundary is sum of pair products of three squares <= 1/3.

# 3. Interior stationary-point elimination, scaling x=1.
g=[sp.diff(Q,v) for v in (x,y,z,w)]
eqs=[sp.expand(g[1]-y*g[0]),sp.expand(g[2]-z*g[0]),sp.expand(g[3]-w*g[0])]
eqs1=[e.subs(x,1) for e in eqs]
G=sp.groebner(eqs1,w,z,y,order='lex')
last=sp.factor(G.polys[-1].as_expr())
f1=y**3-3*y**2-3*y+3
f2=y**3+3*y**2-3*y-3
f3=y**4-2*y**3+5*y**2-4*y-3
f4=y**4+2*y**3+5*y**2+4*y-3
f5=243*y**8-558*y**6+372*y**4-62*y**2+3
expected=sp.factor(y*f1*f2*f3*f4*f5)
assert sp.expand(last-expected)==0

# Exact back-substitution certificates for each elimination factor.
expected_relations=[
    [w+1,y+z],
    [w-1,z-y],
    [3*w+y**3+5*y+3,-y**3-2*y+3*z],
    [3*w+y**3+5*y-3,y**3+2*y+3*z],
    [w+405*y**7-876*y**5+514*y**3-48*y,
     -405*y**6+876*y**4-514*y**2+3*z+48],
]
for fac, rels in zip([f1,f2,f3,f4,f5],expected_relations):
    GG=sp.groebner(eqs1+[fac],w,z,y,order='lex')
    for rel in rels:
        assert GG.reduce(rel)[1]==0

# Cubic f2 has exactly one positive root by Descartes; isolate it exactly.
ints2=sp.intervals(f2,eps=sp.Rational(1,10**20))
pos2=[iv for iv,m in ints2 if iv[0]>0]
assert len(pos2)==1 and all(m==1 for iv,m in ints2)
ta,tb=pos2[0]
assert ta > sp.Rational(12618,10000) and tb < sp.Rational(12619,10000)

# The octic branch has four positive roots, and every one makes z or w negative.
ints5=sp.intervals(f5,eps=sp.Rational(1,10**12))
pos5=[iv for iv,m in ints5 if iv[0]>0]
assert len(pos5)==4 and all(m==1 for iv,m in ints5)
zpoly=sp.Poly(405*y**6-876*y**4+514*y**2-48,y)
wpoly=sp.Poly(-405*y**7+876*y**5-514*y**3+48*y,y)
patterns=[]
for aa,bb in pos5:
    assert zpoly.count_roots(aa,bb)==0
    assert wpoly.count_roots(aa,bb)==0
    mid=(aa+bb)/2
    sz=sp.sign(zpoly.eval(mid)); sw=sp.sign(wpoly.eval(mid))
    assert sz*sw==-1
    patterns.append((int(sz),int(sw)))
assert patterns==[(-1,1),(1,-1),(-1,1),(1,-1)]

# The two quartic branches cannot be positive interior points by their exact relations.
# f3 branch: 3w=-(y^3+5y+3)<0 for y>0.
# f4 branch: 3z=-(y^3+2y)<0 for y>0.

# 4. Candidate value and algebraic elimination.
R=sp.factor((3*t**4+4*t**3+12*t**2+3)/(2*(1+t**2)**2))
taupoly=t**3+3*t**2-3*t-3
num=sp.together(X-R).as_numer_denom()[0]
res=sp.factor(sp.resultant(taupoly,num,t))
PX=208*X**3-1224*X**2+2268*X-1323
assert sp.expand(res-104*PX)==0
intsX=sp.intervals(PX,eps=sp.Rational(1,10**20))
posX=[iv for iv,m in intsX if iv[0]>0]
assert len(posX)==3 and all(m==1 for iv,m in intsX)
Xa,Xb=posX[-1]
assert Xa>sp.Rational(28088,10000) and Xb<sp.Rational(28089,10000)
assert sp.sign(PX.subs(X,sp.Rational(15,7)))<0
# Since the largest root is >2.8088>15/7, candidate beats every boundary point.

# 5. Direct high-precision evaluation at the algebraic positive root.
tau=sp.RootOf(taupoly,2)
val=sp.N(R.subs(t,tau),40)
k=sp.N(val**sp.Rational(1,4),40)
assert abs(float(val)-2.808840165474397)<1e-14
assert abs(float(k)-1.2945885354364894)<1e-14

print(f"VERIFY_OK groebner={len(G.polys)} octic_positive={len(pos5)} tau={sp.N(tau,18)} X={val} K={k}")
