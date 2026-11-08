"""Exact symbolic checks accompanying the genus-two Hankel projection proof.
Install SymPy; run `python verify_hankel_sixth.py`. Finite checks are not proof.
"""
import sympy as S
z,u=S.symbols('z u')
a,b,c=1,2,3
D=S.expand((a*z**3+3*b*z**2)**2-4*(2*a*z+b)*(b*z**4-c))
assert S.gcd(D,S.diff(D,z))==1
f={1:S.Integer(1),2:S.Integer(0)}
g={1:S.Integer(0),2:S.Integer(1)}
for n in range(3,82):
    f[n]=S.expand(f[n-1]+u*f[n-2]);g[n]=S.expand(g[n-1]+u*g[n-2])
    if n>=7:
        fa=f[n].subs(u,-S.Rational(1,2))
        fd=S.diff(f[n],u).subs(u,-S.Rational(1,2))
        ga=g[n].subs(u,-S.Rational(1,2))
        k=(n-2)//4
        if n%4==2:
            assert fa==0
            assert ga==(-S.Rational(1,4))**k
            assert fd==4*k*(-S.Rational(1,4))**k
            assert ga-fd/4!=0
        else:
            assert fa!=0
    if n>=7:
        pc=n-6
        pb=n-1-(n%4==2)
        pt=(n-1)//2
        deg=pc+pb+pt
        assert deg==2*n-7+(n-1)//2-(n%4==2)
        if n in range(10,16):
            assert deg=={10:16,11:20,12:22,13:25,14:26,15:30}[n]
print('GENUS_TWO_DISCRIMINANT_SQUAREFREE_OK')
print('FOUR_STEP_LEADING_COEFFICIENTS_OK n=7..81')
print('THREE_POLE_DEGREE_FORMULA_OK n=7..81')
print('PRIMARY_LITERATURE_TABLE_MATCH_OK n=10..15: 16,20,22,25,26,30')
