"""Independent rational-path and symbolic checks for a finite moment obstruction.
Requires sympy. This checks finite formulas and symbolic identities; the
operator-theoretic proof is in RESULT.md.
"""
from fractions import Fraction
from sympy import symbols, Matrix, factor, cancel, S

def moments_formula(k, x):
    B = x + k - 2
    C = x + k - 1
    A = x + k
    return [S.One, B/C, B/A,
            B*(k + x*x/(x+1))/(A*A),
            B*(k + x*x/(x+2))/(A*A)]

def symbolic():
    x,k=symbols('x k', positive=True)
    g=moments_formula(k,x)
    M=Matrix([[g[i+j] for j in range(3)] for i in range(3)])
    got=factor(M.det())
    expected=-(k-2)*(k+x-2)**2*(k*x+2*k+2*x)/((k+x)**4*(x+1)**2*(x+2)*(k+x-1)**2)
    assert cancel(got-expected)==0
    d0=(k+x-2)/((k+x)*(k+x-1)**2)
    d1=(k+x-2)**2/((k+x)**2*(x+1)*(k+x-1))
    d2=x*(k+x-2)**2*(2*k*x+2*k+x*x)/((k+x)**4*(x+1)**2*(x+2))
    for n,expect in enumerate((d0,d1,d2)):
        assert cancel(g[n]*g[n+2]-g[n+1]**2-expect)==0

def by_paths(k, x, count=5):
    # All squared coefficients are rational; each vector is supported on
    # distinct descendants at a fixed time, so norm mass recurs exactly.
    a=[x+j for j in range(k)]
    u=[a[j]/a[j+1] for j in range(k-1)]
    v=x*a[-1]/(x+k)**2
    w=k*a[-1]/(x+k)**2
    rows=[[Fraction(1)] for j in range(k)]
    for n in range(1,count):
        for j in range(k-1):
            rows[j].append(u[j]*rows[j+1][n-1])
        rows[-1].append(v*rows[0][n-1]+w)
    return rows[k-2]

def grids():
    assert_count=0
    for k in range(2,51):
        for numerator in (1,2,3,5,7,11,29):
            for denom in (1,3,8,17):
                x=Fraction(numerator,denom)
                actual=by_paths(k,x)
                B=x+k-2; C=x+k-1; A=x+k
                expected=[Fraction(1), B/C, B/A,
                          B*(k+x*x/(x+1))/(A*A),
                          B*(k+x*x/(x+2))/(A*A)]
                assert actual==expected, (k,x,actual,expected)
                a,b,c,d,e=actual
                det=a*(c*e-d*d)-b*(b*e-c*d)+c*(b*d-c*c)
                formula=-(k-2)*(k+x-2)**2*(k*x+2*k+2*x)/((k+x)**4*(x+1)**2*(x+2)*(k+x-1)**2)
                assert det==formula
                assert det==0 if k==2 else det<0
                assert_count+=1
    print('PASS: symbolic determinant and three principal 2-by-2 formulas')
    print(f'PASS: exact rational graph recurrences and determinants at {assert_count} parameter pairs')
if __name__=='__main__':
    symbolic(); grids()
