"""Exact checks for the four-step axial regular-tetrahedron facet-foot theorem.

Python 3 standard library only. All arithmetic, including geometry, is rational.
"""
from fractions import Fraction as F


def add(a,b):
    n=max(len(a),len(b)); return tuple((a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(n))
def sub(a,b):
    n=max(len(a),len(b)); return tuple((a[i] if i<len(a) else 0)-(b[i] if i<len(b) else 0) for i in range(n))
def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return tuple(out)
def scale(a,c):return tuple(c*x for x in a)
def deriv(a):return tuple(i*a[i] for i in range(1,len(a)))
def equal(a,b):
    n=max(len(a),len(b));assert all((a[i] if i<len(a) else 0)==(b[i] if i<len(b) else 0) for i in range(n)),(a,b)

def dot(x,y):return sum((a*b for a,b in zip(x,y)), F(0))
def subvec(x,y):return tuple(a-b for a,b in zip(x,y))
def cross(x,y):return (x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0])
def V(a,b,c):return ((a,b,b),(b,a,b),(b,b,a),(c,c,c))
def algebraic_step(a,b,c):
    D=(a+b-2*c)**2+2*(c-b)**2
    assert D>0
    return (c*(a-b)*(a+b-2*c)/D,c*(a-b)*(c-b)/D,(a+2*b)/3)
def geometric_step(vertices):
    out=[]
    for omit in range(4):
        face=[v for i,v in enumerate(vertices) if i!=omit]
        n=cross(subvec(face[1],face[0]),subvec(face[2],face[0]))
        n2=dot(n,n)
        assert n2>0
        lam=dot(n,face[0])/n2
        out.append(tuple(lam*w for w in n))
    return tuple(out)
def normalized_xy(a,b,c):
    p=a-b; assert p!=0
    return ((a+2*b-3*c)/p,(a+2*b)/p)
def iterate(x,y):return (-(2*x*y+1)/(y-x),1/x)
def x4_formula(z):return 2*(35*z**3-36*z**2+30*z-2)/((z+2)*(17*z*z-16*z+8))

def run():
    # Polynomial equalities used in the universal proof.
    A=scale((-2,30,-36,35),2)
    B=mul((2,1),(8,-16,17))
    equal(add(A,scale(B,2)),scale(mul((1,2),(7,-11,13)),4))
    equal(sub(A,scale(B,2)),scale(mul(mul((-1,1),(-1,1)),(-1,1)),36))
    equal(sub(mul(deriv(A),B),mul(A,deriv(B))),scale(mul(mul((-1,1),(-1,1)),(8,-4,23)),108))
    # Independent three-dimensional facet hyperplane feet, including four iterates.
    tests=0
    for numerator in range(1,119):
        z=F(-numerator,60)
        if not (-2<z<0):continue
        t=(z+2)/3
        a,b,c=t,t-1,t
        x,y=F(-2),z
        for i in range(4):
            assert x<y<0
            original=V(a,b,c)
            actual=geometric_step(original)
            an,bn,cn=algebraic_step(a,b,c)
            expected=V(an,bn,cn)
            assert actual==expected,(z,i,actual,expected)
            a,b,c=an,bn,cn
            x,y=iterate(x,y)
            assert normalized_xy(a,b,c)==(x,y)
            tests+=1
        assert x==x4_formula(z)
        ratio=(x*x+2)/6
        if z<F(-1,2):assert ratio>1
        elif z>F(-1,2):assert ratio<1
        else:assert ratio==1
    print('PASS: 3 universal polynomial identities; %d exact facet-projection iterations; normalized dynamics; fourth-step formula and sign' % tests)
if __name__=='__main__':run()
