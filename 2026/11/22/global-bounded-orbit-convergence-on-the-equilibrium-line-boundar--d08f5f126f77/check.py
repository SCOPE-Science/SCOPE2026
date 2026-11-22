"""Exact symbolic checks of two polynomial dissipation identities."""
import sympy as s
x,y,z,a,b,alpha,K=s.symbols('x y z a b alpha K',real=True)
flow=s.Matrix([y,z,-a*x-y-b*z-alpha*z*z+x*y])
def ddt(h):return s.expand(s.diff(h,x)*flow[0]+s.diff(h,y)*flow[1]+s.diff(h,z)*flow[2])
W=z+b*y+x-x*x/s.Integer(2)
assert s.simplify(ddt(W).subs(a,0)+alpha*z*z)==0
H=y*y/2+x*x/2-x*x*x/6-W*x
assert s.simplify(ddt(H).subs({a:0,alpha:0})+b*y*y)==0
lam,u=s.symbols('lambda u')
J=s.Matrix([[0,1,0],[0,0,1],[0,u-1,-b]])
assert s.simplify(J.charpoly(lam).as_expr()-lam*(lam**2+b*lam+1-u))==0
print('PASS: exact W, H derivatives and transverse characteristic polynomial')
