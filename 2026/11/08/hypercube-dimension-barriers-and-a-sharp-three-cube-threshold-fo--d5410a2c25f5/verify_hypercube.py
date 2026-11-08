"""Exact checks for Gauss--Legendre heat steps on Boolean hypercubes.

Run with Python 3, no third-party dependencies.
This supplements the analytic proof and does not replace it.
"""
from fractions import Fraction as F
from math import comb, factorial

checks = 0

def check(value, message):
    global checks
    assert value, message
    checks += 1


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def add(p, q):
    return trim([(p[i] if i < len(p) else 0) +
                 (q[i] if i < len(q) else 0)
                 for i in range(max(len(p), len(q)))])


def mul(p, q):
    out = [0] * (len(p) + len(q) - 1)
    for i, a in enumerate(p):
        for j, b in enumerate(q):
            out[i+j] += a*b
    return trim(out)


def coeff(s, j):
    return F(factorial(s) * factorial(2*s-j),
             factorial(2*s) * factorial(s-j) * factorial(j))


def pade(s, x):
    den = sum((coeff(s,j)*x**j for j in range(s+1)), F(0))
    num = sum((coeff(s,j)*(-x)**j for j in range(s+1)), F(0))
    return num/den


def K(d, r, j):
    return sum((-1)**a * comb(r,a) * comb(d-r,j-a)
               for a in range(max(0,j-(d-r)), min(r,j)+1))


def T(d, s, r, h):
    return sum((K(d,r,j)*pade(s,2*j*h) for j in range(d+1)), F(0))/2**d

# Coefficient and rational-stability facts, including the large-step factor.
for s in range(1,11):
    check(coeff(s,0)==1, f'Padé constant s={s}')
    check(coeff(s,s-1)/coeff(s,s)==s*(s+1), f'Padé leading ratio s={s}')
    for x in [F(1,100), F(1,2), F(1), F(9), F(100)]:
        y=pade(s,x)
        check(-1 < y < 1, f'A-stability on positive real axis s={s}, x={x}')
        if s%2 == 0:
            check(y>0, f'even-stage scalar positivity s={s}, x={x}')

# Walsh coefficients are zero-sum off the diagonal and have correct row sums.
for d in range(1,15):
    for r in range(d+1):
        check(sum(K(d,r,j) for j in range(d+1)) == (2**d if r == 0 else 0),
              f'Walsh coefficient normalization d={d}, r={r}')
    for j in range(d+1):
        check(sum(comb(d,r)*K(d,r,j) for r in range(d+1)) ==
              (2**d if j==0 else 0), f'Walsh row-sum identity d={d}, j={j}')

# Exact Q2 (four-cycle) and Q3 (eight-vertex cube) numerator identities.
# Numerators are written against their factored common positive denominator.
for d, expected in [
    (2, [[9,9,6,3,4], [0,3], [0,0,9,9]]),
    (3, [[18,54,66,36,44,45,24], [0,18,54,60,18,-3],
         [0,0,18,54,54,21], [0,0,0,18,54,33]])]:
    # The scalar rational function at Walsh level j is
    # (3-3*j*h+j*j*h*h)/(3+3*j*h+j*j*h*h).
    den = {j: [3,3*j,j*j] for j in range(1,d+1)}
    num = {j: [3,-3*j,j*j] for j in range(1,d+1)}
    prod = [1]
    for j in range(1,d+1):
        prod=mul(prod,den[j])
    for r in range(d+1):
        p=[0]
        for j in range(d+1):
            part = [1] if j==0 else num[j]
            for i in range(1,d+1):
                if i!=j:
                    part=mul(part,den[i])
            p=add(p,[K(d,r,j)*v for v in part])
        # d=2: T = N / ((3+3h+h^2)*(3+6h+4h^2)),
        # except r=1: 3h/(3+6h+4h^2).  Raw numerator is 4*N.
        # d=3: T = N/(2*(3+3h+h^2)*(1+3h+3h^2)*
        #                     (3+6h+4h^2)). Raw numerator is 12*N.
        if d==2:
            target = expected[r]
            if r==1:
                target = mul(target, [3,3,1])
            check(trim(p)==trim([4*v for v in target]),
                  f'Q2 symbolic identity r={r}')
        else:
            check(trim(p)==trim([12*v for v in expected[r]]),
                  f'Q3 symbolic identity r={r}')

# Exact strict bracket and unique-positive-root certificate for Q3.
p=lambda h: h**4 - 6*h**3 - 20*h**2 - 18*h - 6
lo=F(8583763463,10**9)
hi=F(8583763464,10**9)
check(p(lo)<0<p(hi), 'Q3 quartic root strict rational bracket')
check(all(v<0 for v in [-6,-18,-20,-6]), 'Q3 quartic one sign variation')
for h in [F(1,10), F(1), F(8), F(9), F(10), F(100)]:
    check((T(3,2,1,h)>0) == (h<lo), f'Q3 edge sign h={h}')
    for r in [0,2,3]:
        check(T(3,2,r,h)>0, f'Q3 nonedge/diagonal sign r={r}, h={h}')

# All-step nonnegativity on Q1 and Q2 for s=2; exact mass preservation.
for d in [1,2]:
    for h in [F(0),F(1,100),F(1),F(10),F(100),F(10000)]:
        for r in range(d+1):
            check(T(d,2,r,h)>=0, f'Q{d} nonnegative r={r},h={h}')

for d in range(1,11):
    for s in [1,2,3,4,5,6,8]:
        for h in [F(0),F(1,4),F(1),F(100)]:
            check(sum(comb(d,r)*T(d,s,r,h) for r in range(d+1))==1,
                  f'mass preservation d={d},s={s},h={h}')

# Structural all-dimensional first-neighbour large-step coefficient.
S = F(-1,2) # d=2
for d in range(3,30):
    nxt = sum((F(K(d,1,j),j) for j in range(1,d+1)), F(0))
    check(nxt>S and nxt>0, f'positive increasing S_d for d={d}')
    S=nxt
check(sum((F(K(3,1,j),j) for j in range(1,4)),F(0))==F(1,6),
      'S_3 exact leading coefficient')
for d in range(3,10):
    for s in [2,4,6,8]:
        check(T(d,s,1,F(100000))<0,
              f'eventual negative adjacent coefficient d={d}, s={s}')
for d in range(2,9):
    for s in [1,3,5,7]:
        check(T(d,s,0,F(100000))<0,
              f'eventual negative diagonal d={d}, s={s}')

# Independent eight-by-eight rational matrix identity for Q3 and two-stage Gauss.
def matmul(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)]
            for i in range(n)]

n=8
I=[[F(i==j) for j in range(n)] for i in range(n)]
L=[[F(3 if i==j else -1 if (i^j).bit_count()==1 else 0)
    for j in range(n)] for i in range(n)]
L2=matmul(L,L)
for h in [F(1,5),F(1),F(4),F(9),F(15)]:
    D=[[I[i][j]+h*L[i][j]/2+h*h*L2[i][j]/12 for j in range(n)] for i in range(n)]
    N=[[I[i][j]-h*L[i][j]/2+h*h*L2[i][j]/12 for j in range(n)] for i in range(n)]
    M=[[T(3,2,(i^j).bit_count(),h) for j in range(n)] for i in range(n)]
    DM=matmul(D,M)
    for i in range(n):
        for j in range(n):
            check(DM[i][j]==N[i][j], f'direct matrix identity h={h}, i={i},j={j}')

print(f'VERIFY_OK checks={checks}')
