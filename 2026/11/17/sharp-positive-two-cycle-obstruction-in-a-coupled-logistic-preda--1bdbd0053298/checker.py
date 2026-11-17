"""Reproduce exact two-step algebra and nearby hyperbolic cycles."""
import sympy as s
import mpmath as mp

x1,x2,y1,y2,a,b,c,d=s.symbols('x1 x2 y1 y2 a b c d', positive=True)
dx=x2-x1;dy=y2-y1
Rx=1/x1+1/x2;Ry=1/y1+1/y2
qx1=x2/x1-(a*(1-x1)-c*y1)
qx2=x1/x2-(a*(1-x2)-c*y2)
qy1=y2/y1-(b*(1-y1)+d*x1)
qy2=y1/y2-(b*(1-y2)+d*x2)
assert s.factor((qx1-qx2)-((Rx-a)*dx-c*dy))==0
assert s.factor((qy1-qy2)-((Ry-b)*dy+d*dx))==0
assert s.factor((qx1+qx2)-(x2/x1+x1/x2-2*a+a*(x1+x2)+c*(y1+y2)))==0
assert s.factor((qy1+qy2)-(y2/y1+y1/y2-2*b+b*(y1+y2)-d*(x1+x2)))==0
r=s.Rational(16,5)
uplus=(r+1+s.sqrt((r-3)*(r+1)))/(2*r)
uminus=(r+1-s.sqrt((r-3)*(r+1)))/(2*r)
f=lambda x: r*x*(1-x)
assert s.simplify(f(uplus)-uminus)==0
assert s.simplify(f(uminus)-uplus)==0
assert s.simplify((r*(1-2*uplus))*(r*(1-2*uminus))-s.Rational(4,25))==0
assert uminus>0 and uplus<1

mp.mp.dps=55
c0=mp.mpf('0.0001');d0=mp.mpf('0.0001')
def F(x,y,a,b,c,d): return a*x*(1-x)-c*x*y, b*y*(1-y)+d*x*y

def find(a,b,which):
    if which=='x':
        u0=float(uminus); v0=float(uplus)
        g=(mp.mpf(str(u0)),mp.mpf('0.5'),mp.mpf(str(v0)),mp.mpf('0.5'))
    else:
        u0=float(uminus);v0=float(uplus)
        g=(mp.mpf('0.5'),mp.mpf(str(u0)),mp.mpf('0.5'),mp.mpf(str(v0)))
    def eq(x,y,X,Y):
        X1,Y1=F(x,y,a,b,c0,d0)
        X2,Y2=F(X,Y,a,b,c0,d0)
        return X1-X,Y1-Y,X2-x,Y2-y
    x,y,X,Y=mp.findroot(eq,g,tol=mp.mpf('1e-45'))
    residual=max(abs(u) for u in eq(x,y,X,Y))
    assert residual<mp.mpf('1e-45')
    assert min(x,y,X,Y)>0 and max(x,y,X,Y)<1
    assert abs(x-X)+abs(y-Y)>mp.mpf('0.01')
    def J(x,y):
        return mp.matrix([[a*(1-2*x)-c0*y,-c0*x],[d0*y,b*(1-2*y)+d0*x]])
    M=J(X,Y)*J(x,y)
    tr=M[0,0]+M[1,1]; det=mp.det(M)
    roots=mp.polyroots([1,-tr,det])
    assert max(abs(z) for z in roots)<1
    return residual, [(mp.nstr(z,12)) for z in (x,y,X,Y)], [mp.nstr(z,12) for z in roots]

for a1,b1,which in [(r,mp.mpf(2),'x'),(mp.mpf(2),r,'y')]:
    res,coords,eigs=find(mp.mpf(str(a1)),mp.mpf(str(b1)),which)
    print(f'{which}: max residual {mp.nstr(res,5)}; orbit {coords}; eigenvalues {eigs}')
print('PASS: symbolic exact identities, period-two logistic construction, coupled witnesses')
