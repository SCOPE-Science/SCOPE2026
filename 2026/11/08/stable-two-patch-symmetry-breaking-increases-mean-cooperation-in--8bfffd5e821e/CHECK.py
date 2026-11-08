"""Exact symbolic checks for a two-patch ecological public-goods bifurcation."""
import sympy as s

u, v = s.symbols('u v')
z = 1-u-v
r = s.Rational(9, 4)
b = s.Rational(1, 10)
d = s.Rational(23, 160)
epsilon = s.Rational(1, 100)
Fz = (1-z)*(1-2*z)/4
fD = r*u*(2+z)/3
fC = fD-Fz
local = s.Matrix([u*(z*(b+fC)-d), v*(z*(b+fD)-d)])
Q = {u: s.Rational(1, 10), v: s.Rational(2, 5)}
assert local.subs(Q) == s.zeros(2, 1)
assert s.factor(Fz-(1+(r-1)*z**2-r*(1+z+z**2)/3)) == 0
assert s.factor(fD-r*u*(1-(1+z+z**2)/3)/(1-z)) == 0
J = local.jacobian([u, v]).subs(Q)
assert J == s.Matrix([[s.Rational(39,800), -s.Rational(9,200)],
                      [s.Rational(49,200),-s.Rational(13,100)]])
assert s.trace(J) == -s.Rational(13,160)
assert J.det() == s.Rational(3,640)
k = s.symbols('k')
A = J-2*epsilon*s.diag(1,k)
assert s.factor(A.det()-(583-46*k)/80000) == 0
kc = s.Rational(583, 46)
assert s.trace(A.subs(k,kc)) == -s.Rational(6527,18400)
h = s.Matrix([1,s.Rational(23,36)])
ell = s.Matrix([s.Rational(7056,6527),-s.Rational(828,6527)])
assert A.subs(k,kc)*h == s.zeros(2,1)
assert ell.T*A.subs(k,kc) == s.zeros(1,2)
assert ell.dot(h) == 1
crossing = ell.dot(s.diff(A,k)*h)
assert crossing == s.Rational(529,326350)

# Independent stationary-series calculation, with p as half of the
# cooperator density difference between the two patches.
p = s.symbols('p')
m1,m2,q3,D=s.symbols('m1 m2 q3 D')
u_bar=s.Rational(1,10)+m1*p**2
v_bar=s.Rational(2,5)+m2*p**2
q=s.Rational(23,36)*p+q3*p**3

def subf(uu,vv):
    return s.Matrix([s.expand(expr.subs({u:uu,v:vv},simultaneous=True))
                     for expr in local])
plus=subf(u_bar+p,v_bar+q)
minus=subf(u_bar-p,v_bar-q)
mean=[s.expand((a+b)/2).coeff(p,2) for a,b in zip(plus,minus)]
diff=[s.expand((a-b)/2).coeff(p,3) for a,b in zip(plus,minus)]
eqns=mean+[diff[0],diff[1]-2*epsilon*(kc*q3+D*s.Rational(23,36))]
sol=s.solve(eqns,[m1,m2,q3,D],dict=True)
assert len(sol)==1
sol=sol[0]
assert sol=={
 m1:s.Rational(27467,4050),
 m2:s.Rational(262103,64800),
 q3:-s.Rational(456554941,4199040),
 D:s.Rational(26872626977,13711680)
}
assert s.factor(sol[m1]/sol[D]-s.Rational(464961376,134363134885))==0
assert sol[D]>0 and sol[m1]>0

# Independently reconstruct the cubic center coefficient from
# second- and third-derivative multilinear forms.
H2=s.Matrix([(s.diff(x,u,2)*h[0]**2 +2*s.diff(x,u,v)*h[0]*h[1]
               +s.diff(x,v,2)*h[1]**2).subs(Q) for x in local])
w=-J.inv()*H2/2
assert w==s.Matrix([sol[m1],sol[m2]])
H3=s.Matrix([sum(s.binomial(3,i)*s.diff(x,u,3-i,v,i)*h[0]**(3-i)*h[1]**i
                 for i in range(4)).subs(Q) for x in local])
Bhw=s.Matrix([(s.diff(x,u,2)*h[0]*w[0]+s.diff(x,u,v)*(h[0]*w[1]+h[1]*w[0])
                  +s.diff(x,v,2)*h[1]*w[1]).subs(Q) for x in local])
cubic=s.factor(ell.dot(Bhw+H3/6))
assert cubic == -s.Rational(26872626977,8458992000)
assert s.factor(cubic+crossing*sol[D])==0
print('Exact identities, stationary branch, and stability signs verified.')
print('kappa critical =',kc,'mean cooperator slope =',sol[m1]/sol[D])
