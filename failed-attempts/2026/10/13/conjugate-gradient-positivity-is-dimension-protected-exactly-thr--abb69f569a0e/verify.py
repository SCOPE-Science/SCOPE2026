from fractions import Fraction as F


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def mv(A, x):
    return [sum(A[i][j]*x[j] for j in range(len(x))) for i in range(len(A))]


def det2(a,b,c,d):
    return a*d-b*c


def det3(A):
    return (A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
            -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
            +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0]))


def solve3(A, b):
    M=[row[:] + [rhs] for row, rhs in zip(A,b)]
    n=3
    for col in range(n):
        pivot=next(i for i in range(col,n) if M[i][col] != 0)
        M[col],M[pivot]=M[pivot],M[col]
        q=M[col][col]
        M[col]=[v/q for v in M[col]]
        for i in range(n):
            if i==col: continue
            q=M[i][col]
            M[i]=[M[i][j]-q*M[col][j] for j in range(n+1)]
    return [M[i][-1] for i in range(n)]

A=[[F(2),F(-2),F(0)],
   [F(-2),F(4),F(-1)],
   [F(0),F(-1),F(12)]]
b=[F(2),F(4),F(1)]

assert A[0][0] == 2
assert det2(A[0][0],A[0][1],A[1][0],A[1][1]) == 4
assert det3(A) == 46
assert all(A[i][j] <= 0 for i in range(3) for j in range(3) if i != j)

# Exact inverse by solving against the coordinate vectors.
cols=[]
for j in range(3):
    e=[F(int(i==j)) for i in range(3)]
    cols.append(solve3(A,e))
Ainv=[[cols[j][i] for j in range(3)] for i in range(3)]
expected_inv=[[F(47,46),F(12,23),F(1,23)],
              [F(12,23),F(12,23),F(1,23)],
              [F(1,23),F(1,23),F(2,23)]]
assert Ainv == expected_inv
assert all(v > 0 for row in Ainv for v in row)

xstar=solve3(A,b)
assert xstar == [F(96,23),F(73,23),F(8,23)]
assert all(v > 0 for v in xstar)

x=[F(0),F(0),F(0)]
r=b[:]
p=r[:]
alpha0=dot(r,r)/dot(p,mv(A,p))
assert alpha0 == F(21,44)
x1=[x[i]+alpha0*p[i] for i in range(3)]
assert x1 == [F(21,22),F(21,11),F(21,44)]
r1=[r[i]-alpha0*mv(A,p)[i] for i in range(3)]
assert r1 == [F(43,11),F(-5,4),F(-31,11)]
beta0=dot(r1,r1)/dot(r,r)
assert beta0 == F(2285,1936)
p1=[r1[i]+beta0*p[i] for i in range(3)]
assert p1 == [F(6069,968),F(420,121),F(-3171,1936)]
alpha1=dot(r1,r1)/dot(p1,mv(A,p1))
assert alpha1 == F(20108,67599)
x2=[x1[i]+alpha1*p1[i] for i in range(3)]
assert x2 == [F(9076,3219),F(9469,3219),F(-32,3219)]
assert x2[2] < 0
print('VERIFY_OK')
