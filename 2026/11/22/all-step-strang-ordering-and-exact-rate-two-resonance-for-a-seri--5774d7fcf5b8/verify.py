"""Independent high-precision spot checks for the serial-reaction Strang theorem.

Run with Python 3.10+: python verify.py.  Uses only the standard library.
The universal inequalities are proved analytically in RESULT.md; grid checks
are supplementary and do not certify all real rates or times.
"""
from decimal import Decimal, localcontext
from fractions import Fraction
from itertools import product


def matmul(a,b):
    return [[sum(a[i][k]*b[k][j] for k in range(3))
             for j in range(3)] for i in range(3)]


def kernels(a,b,t):
    e=Decimal.exp
    aa=e(-a*t)
    bb=e(-b*t)
    if a==b:
        two=Decimal(1)-(Decimal(1)+a*t)*aa
    else:
        two=Decimal(1)-aa-a*(aa-bb)/(b-a)
    q_a=(1-e(-a*t/2))*(1-bb)
    q_b=(1-aa)*(1-e(-b*t/2))
    return two, q_a, q_b


def A(a,t):
    p=Decimal.exp(-a*t)
    return [[p,1-p,Decimal(0)],
            [Decimal(0),Decimal(1),Decimal(0)],
            [Decimal(0),Decimal(0),Decimal(1)]]


def B(b,t):
    p=Decimal.exp(-b*t)
    return [[Decimal(1),Decimal(0),Decimal(0)],
            [Decimal(0),p,1-p],
            [Decimal(0),Decimal(0),Decimal(1)]]


def sinhc(z):
    if z==0: return Decimal(1)
    return (Decimal.exp(z)-Decimal.exp(-z))/(2*z)


def test():
    with localcontext() as ctx:
        ctx.prec=65
        comparisons=0
        equalities=0
        for a0,b0,t0 in product((1,2,3,5,8,13), (1,2,3,5,8,13),
                               (Fraction(1,100),Fraction(1,10),Fraction(1,2),
                                Fraction(1),Fraction(3),Fraction(7))):
            a,b,t=[Decimal(q.numerator)/Decimal(q.denominator)
                   if isinstance(q,Fraction) else Decimal(q)
                   for q in (a0,b0,t0)]
            exact,qa,qb=kernels(a,b,t)
            ma=matmul(matmul(A(a,t/2),B(b,t)),A(a,t/2))
            mb=matmul(matmul(B(b,t/2),A(a,t)),B(b,t/2))
            tol=Decimal('1e-52')
            assert abs(ma[0][2]-qa)<tol and abs(mb[0][2]-qb)<tol
            assert abs(ma[0][0]-Decimal.exp(-a*t))<tol
            assert abs(mb[0][0]-Decimal.exp(-a*t))<tol
            assert exact > (qa+qb)/2
            if a>b:
                assert qa>qb and abs(exact-qa)<abs(exact-qb)
            elif b>a:
                assert qb>qa and abs(exact-qb)<abs(exact-qa)
            else:
                assert abs(qa-qb)<tol
            ba=b*t*Decimal.exp(-(a+b)*t/2)*(sinhc((a-b)*t/2)-sinhc(b*t/2))
            bb=a*t*Decimal.exp(-(a+b)*t/2)*(sinhc((b-a)*t/2)-sinhc(a*t/2))
            assert abs((qa-exact)-ba)<tol and abs((qb-exact)-bb)<tol
            assert (qa-exact>0)==(a>2*b) if a!=2*b else abs(qa-exact)<tol
            assert (qb-exact>0)==(b>2*a) if b!=2*a else abs(qb-exact)<tol
            if a==2*b: assert abs(qa-exact)<tol; equalities+=1
            if b==2*a: assert abs(qb-exact)<tol; equalities+=1
            comparisons+=1
        # More rate/time choices, including small gaps around the 2:1 resonance.
        for aa,bb in product(range(10,71), range(10,71)):
            a=Decimal(aa)/10; b=Decimal(bb)/10
            t=Decimal(3)/7
            exact,qa,qb=kernels(a,b,t)
            assert exact>(qa+qb)/2
            if a>b: assert abs(exact-qa)<abs(exact-qb)
            if b>a: assert abs(exact-qb)<abs(exact-qa)
            comparisons+=1
        print('PASS',comparisons,'high-precision cases;',equalities,'rate-two exactness cases')

if __name__=='__main__':
    test()
