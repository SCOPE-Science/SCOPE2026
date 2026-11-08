"""Exact rational and symbolic checks for cyclotomic-domain metric formulas.

Finite checks are not a substitute for the unrestricted proof.
"""
from fractions import Fraction as F
import math
from sympy import symbols, Poly, cyclotomic_poly

x,y=symbols('x y')

def divided(m,a,b):
    return sum(a**(m-1-j)*b**j for j in range(m))

def main():
    tests=0
    for m in (3,5,7,9,11,13,15,21,31):
        n=m-1
        for a0 in range(-12,13):
            for b0 in range(-12,13):
                a,b=F(a0,8),F(b0,8)
                v=divided(m,a,b)
                assert v >= ((a*a+b*b)/2)**(n//2), (m,a,b,'lower radius bound')
                if v<=1:
                    assert a*a+b*b<=2
                    assert max(abs(a),abs(b))**n <= 2
                    assert not (abs(a)>1 and abs(b)>1)
                tests+=1
        h=math.sqrt(2)*(1-m**(-1/n))
        outer=2**(1/n)-1
        assert h>outer
    polys=0
    for p in (3,5,7,11,13,17,19,23,29,31):
        n=p-1
        target=sum(x**(n-j)*y**j for j in range(p))
        cp=Poly(cyclotomic_poly(p,x),x)
        hom=sum(c*x**j*y**(n-j) for (j,),c in cp.terms())
        assert hom.expand()==target.expand()
        cp2=Poly(cyclotomic_poly(2*p,x),x)
        hom2=sum(c*x**j*y**(n-j) for (j,),c in cp2.terms())
        assert hom2.expand()==target.subs(y,-y).expand()
        polys+=2
    for k in (2,3,4,5,6):
        n=2**(k-1)
        cp=Poly(cyclotomic_poly(2**k,x),x)
        hom=sum(c*x**j*y**(n-j) for (j,),c in cp.terms())
        assert hom.expand()==x**n+y**n
        polys+=1
    for m in range(3,1002,2):
        n=m-1
        delta=math.sqrt(2)*(-math.expm1(-math.log(m)/n))
        outside=math.expm1(math.log(2)/n)
        assert delta>outside
    print(f'VERIFY_OK exact_grid_points={tests} cyclotomic_identities={polys} scalar_comparisons=500 rational_exact=yes')

if __name__=='__main__':
    main()
