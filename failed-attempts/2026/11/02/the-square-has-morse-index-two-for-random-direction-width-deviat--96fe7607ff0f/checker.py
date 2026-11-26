"""Reproduction checks for the four-dimensional width-deviation Hessian theorem.
Requires SymPy; numerical verification uses only the Python standard library.
"""
from math import cos, sin, pi, sqrt
import sympy as S

def symbolic():
    x,y,a,b=S.symbols('x y a b',real=True)
    v=(x,y,a,b)
    e=[S.Matrix([1+x,b]), S.Matrix([1-x,-b]),
       S.Matrix([y-1,-a]),S.Matrix([-1-y,a])]
    dot=lambda u,w:u.dot(w)
    det=lambda u,w:u[0]*w[1]-u[1]*w[0]
    # Second-order jet from exact absolute-projection correlation:
    # parallel opposites K=-dot/2+O(epsilon^3),
    # perpendicular neighbors K=(-det+dot^2/2)/pi+O(epsilon^3).
    e2=sum(dot(z,z)/2 for z in e)
    for i,j in [(0,2),(1,3)]:e2-=dot(e[i],e[j])
    for i,j in [(0,1),(1,2),(2,3),(3,0)]:
        e2+=2/S.pi*(-det(e[i],e[j])+dot(e[i],e[j])**2/2)
    e2/=4
    perimeter=sum(S.sqrt(dot(z,z)) for z in e)
    coefficient=S.pi**2*e2/perimeter**2-1
    origin={x:0,y:0,a:1,b:1}
    got0=S.simplify(coefficient.subs(origin))
    got1=[S.simplify(S.diff(coefficient,t).subs(origin)) for t in v]
    gotH=S.Matrix([[S.simplify(S.diff(coefficient,t,u).subs(origin))
                    for u in v] for t in v])
    P=S.pi
    wanted=S.Matrix([[0,P*(2-P)/64,0,0],
                     [P*(2-P)/64,0,0,0],
                     [0,0,P*(6-P)/128,P*(2+P)/128],
                     [0,0,P*(2+P)/128,P*(6-P)/128]])
    assert S.simplify(got0-(-1+P*(P+2)/16))==0
    assert got1==[0,0,0,0]
    assert gotH==wanted
    assert S.simplify(gotH.charpoly().as_expr() -
        (S.Symbol("lambda")-P/16)*(S.Symbol("lambda")-P*(P-2)/64)*
        (S.Symbol("lambda")-P*(2-P)/64)**2)==0
    assert S.simplify(gotH.det()-P**4*(P-2)**3/4194304)==0
    print('EXACT_FOUR_PARAMETER_HESSIAN_AND_MORSE_SIGNATURE_PASSED')
    return gotH

def quadrature(x,y,a,b,n=65536):
    p=[(-1.0,0.0),(float(x),float(b)),(1.0,0.0),(float(y),-float(a))]
    sw=sw2=0.0
    for j in range(n):
        theta=2*pi*(j+0.5)/n
        ux,uy=cos(theta),sin(theta)
        q=[ux*sx+uy*sy for sx,sy in p]
        w=max(q)-min(q)
        sw+=w;sw2+=w*w
    mean=sw/n; moment=sw2/n
    return moment/(mean*mean)-1

def numeric(H):
    q0=quadrature(0,0,1,1)
    assert abs(q0-(pi*(pi+2)/16-1))<3e-8
    modes=[(1,1,0,0),(1,-1,0,0),(0,0,1,1),(0,0,1,-1),
           (1,.7,-.3,.2)]
    for v in modes:
        exact=sum(float(H[i,j])*v[i]*v[j] for i in range(4) for j in range(4))
        for t in (.020,.010):
            plus=quadrature(t*v[0],t*v[1],1+t*v[2],1+t*v[3])
            minus=quadrature(-t*v[0],-t*v[1],1-t*v[2],1-t*v[3])
            numeric_second=(plus+minus-2*q0)/(t*t)
            assert abs(numeric_second-exact)<.008,(v,t,numeric_second,exact)
    print('INDEPENDENT_DIRECT_SPHERICAL_QUADRATURE_PASSED')
    print('ALL_CHECKS_PASSED')

if __name__=='__main__':
    H=symbolic()
    numeric(H)
