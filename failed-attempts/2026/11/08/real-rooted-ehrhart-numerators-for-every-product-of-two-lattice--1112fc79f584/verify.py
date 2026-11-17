"""Exact rational-polynomial certificate for products of lattice polygons.

Requires SymPy (tested with 1.13.1 or later). Run: python verify.py
The accompanying certificate contains complete discriminant coefficients;
no floating-point root tests enter the proof.
"""
import json
from pathlib import Path
from sympy import Poly, symbols, expand, discriminant, binomial, Rational

t,u,c,I,J,b,z = symbols('t u c I J b z')


def original_numerator(I, J, b, c):
    # Pick's polynomial for boundary counts b+3 and c+3.
    def LP(n, i, v):
        B=v+3
        return ((2*i+B-2)*Rational(1,2))*n*n + (B*Rational(1,2))*n+1
    return expand(sum(z**k*sum((-1)**(k-j)*binomial(5,k-j)*
                       LP(j,I,b)*LP(j,J,c) for j in range(k+1))
                      for k in range(5)))


def explicit_numerator(I,J,b,c):
    return expand(1 + (I*J+I*c+3*I+J*b+3*J+b*c+3*b+3*c+4)*z
        +(11*I*J+7*I*c+9*I+7*J*b+9*J+4*b*c+3*b+3*c+1)*z*z
        +(11*I*J+4*I*c+4*J*b+b*c)*z**3+I*J*z**4)


def exception(i,j,v):
    return expand(explicit_numerator(i,j,0,v))


def cert_coefficients(i):
    H = exception(i,u+1,c)
    delta = Poly(discriminant(H,z),u,c)
    cubic = Poly(discriminant(exception(i,0,c),z),c)
    return {
       'quartic_coefficients': [[a,d,int(k)] for (a,d),k in delta.terms()],
       'cubic_coefficients_ascending': [int(cubic.nth(k)) for k in range(5)],
       'quadratic_discriminant':int(discriminant(exception(i,0,0),z)),
    }


def main():
    assert expand(original_numerator(I,J,b,c)-explicit_numerator(I,J,b,c))==0
    supplied=json.loads(Path(__file__).with_name('DISCRIMINANT_CERTIFICATE.json').read_text())
    for i in (1,2,3):
        key=str(i)
        expected=cert_coefficients(i)
        assert supplied[key]==expected
        quartic=expected['quartic_coefficients']
        assert len(quartic)==28 and all(v>0 for a,d,v in quartic)
        assert len([q for q in quartic if q[0]+q[1]<=6])==28
        assert len(expected['cubic_coefficients_ascending'])==5
        assert all(v>0 for v in expected['cubic_coefficients_ascending'])
        assert expected['quadratic_discriminant']>0
        tau={1:Rational(1,5),2:Rational(1,6),3:Rational(1,8)}[i]
        witness=Poly(-exception(i,u+1,c).subs(z,-tau),u,c)
        assert all(v>=0 for v in witness.coeffs()) and witness.TC()>0
        print('case',i,'quartic',len(quartic),
              'min coefficient',min(x[2] for x in quartic),
              'cubic discriminant coefficients',expected['cubic_coefficients_ascending'],
              'witness',witness.as_expr())
    print('PASS: all exact universal coefficient identities and root-count certificates')

if __name__=='__main__': main()
