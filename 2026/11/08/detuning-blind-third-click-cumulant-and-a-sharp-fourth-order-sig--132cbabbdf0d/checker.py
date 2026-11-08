"""Exact arithmetic checks for a detuned, projectively monitored qubit.

Run with Python 3.10 or later. No third-party dependencies.
"""
from fractions import Fraction as F
from itertools import permutations
from math import factorial


def det(a):
    n = len(a)
    total = F(0)
    for p in permutations(range(n)):
        inv = sum(p[i] > p[j] for i in range(n) for j in range(i+1, n))
        term = (-1 if inv % 2 else 1)
        for i in range(n):
            term *= a[i][p[i]]
        total += term
    return total


def linear_solve(a, b):
    n = len(b)
    x = [[F(v) for v in row] + [F(b[i])] for i, row in enumerate(a)]
    for i in range(n):
        pivot = next(j for j in range(i, n) if x[j][i] != 0)
        x[i], x[pivot] = x[pivot], x[i]
        t = x[i][i]
        x[i] = [z/t for z in x[i]]
        for j in range(n):
            if j != i:
                t = x[j][i]
                x[j] = [v-t*w for v,w in zip(x[j], x[i])]
    return [row[-1] for row in x]


def logseries(a):
    """Coefficients of log(1+sum a[n] s**n), through degree four."""
    out = [F(0)]*5
    for n in range(1,5):
        out[n] = a[n] - sum(F(j,n)*out[j]*a[n-j] for j in range(1,n))
    return out


def formulas(g,k,d):
    u=(k/g)**2
    v=(d/g)**2
    P=F(512)+1600*u+48*u*u-3*u**3+(256-36*u*u)*v-(768+144*u)*v*v-192*v**3
    return (k/2,
            k*(4*d*d+8*g*g+k*k)/(16*g*g),
            k*(4*g*g+3*k*k)/(8*g*g),
            k*P/F(1024))


def from_log_inverse(g,k,d):
    m0=k*k/4+d*d
    n=[g*g*k*k, k*(m0+2*g*g), k*k, k, F(0)]
    v=[g*g*k*k, k*m0+4*g*g*k, m0+k*k+4*g*g, 2*k, F(1)]
    a=logseries([x/v[0] for x in v])
    b=logseries([x/n[0] for x in n])
    c=[x-y for x,y in zip(a,b)]
    c1=1/c[1]
    c2=-c[2]*c1*c1/c[1]
    c3=-(2*c[2]*c1*c2+c[3]*c1**3)/c[1]
    c4=-(c[2]*(c2*c2+2*c1*c3)+3*c[3]*c1*c1*c2+c[4]*c1**4)/c[1]
    return tuple(factorial(i)*x for i,x in enumerate((c1,c2,c3,c4),1))


def matrix(g,k,d,rate,s):
    # Rate denotes e**counting_field, a positive real parameter.
    A=[[F(0),F(0),F(0),-2*g],
       [F(0),k*(rate-1),F(0),2*g],
       [F(0),F(0),-k/2,d],
       [g,-g,-d,-k/2]]
    return [[(s if i==j else F(0))-A[i][j] for j in range(4)] for i in range(4)]


def numerator_denominator(g,k,d,s):
    m=(s+k/2)**2+d*d
    n=k*(s*m+g*g*(k+2*s))
    den=s*(s+k)*m+g*g*(k+2*s)**2
    return n,den


def run():
    cases=0
    for g in (F(1,2),F(1),F(2),F(7,3)):
        for k in (F(1,3),F(1),F(3,2),F(4),F(9)):
            for d in (F(0),F(1,3),F(1),F(3),F(11,2)):
                got=from_log_inverse(g,k,d)
                assert got==formulas(g,k,d), (g,k,d,got,formulas(g,k,d))
                assert got[0]>0 and got[1]>0 and got[2]>0
                for s in (F(1,3),F(5,2)):
                    n,den=numerator_denominator(g,k,d,s)
                    assert den>0 and 0<n<den
                    a=matrix(g,k,d,F(0),s)
                    x=linear_solve(a,[F(0),F(1),F(0),F(0)])
                    assert k*x[1]==n/den
                    for E in (F(1,4),F(1),F(2),F(5)):
                        assert det(matrix(g,k,d,E,s))==den-E*n
                cases+=1
    # Sample the genuine positive and negative fourth-cumulant regimes.
    assert formulas(F(1),F(1),F(0))[3]>0
    assert formulas(F(1),F(1),F(2))[3]<0
    assert formulas(F(1),F(10),F(0))[3]<0
    print('PASS: exact fourth-order series, 4x4 tilted determinant, resolvent and sign checks')
    print('parameter triples:',cases)
    print('exact determinant comparisons:',cases*2*4)


if __name__=='__main__':
    run()
