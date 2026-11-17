"""Exact-rational supporting checks for an attracting period-three border-collision theorem.

Python 3 standard library. Run: python VERIFY.py
The analytical proof is contained in RESULT.md; these finite checks are corroboration.
"""
from fractions import Fraction as F
from itertools import product

checks = 0

def test(statement):
    global checks
    assert statement
    checks += 1

def matmul(X,Y):
    return ((X[0][0]*Y[0][0]+X[0][1]*Y[1][0], X[0][0]*Y[0][1]+X[0][1]*Y[1][1]),
            (X[1][0]*Y[0][0]+X[1][1]*Y[1][0], X[1][0]*Y[0][1]+X[1][1]*Y[1][1]))

def mul(X,z):
    return (X[0][0]*z[0]+X[0][1]*z[1], X[1][0]*z[0]+X[1][1]*z[1])

def add(X,y): return (X[0]+y[0], X[1]+y[1])

def det(X): return X[0][0]*X[1][1]-X[0][1]*X[1][0]

def trace(X): return X[0][0]+X[1][1]

def orbit(a,b,c,d,word):
    L=((a,F(1)),(-b,F(0))); R=((-c,F(1)),(-d,F(0)))
    matrices={'L':L,'R':R}
    M=((F(1),F(0)),(F(0),F(1))); v=(F(0),F(0))
    for letter in word:
        B=matrices[letter]
        M=matmul(B,M); v=add(mul(B,v),(F(1),F(0)))
    S=(1-M[0][0])*(1-M[1][1])-M[0][1]*M[1][0]
    if S==0: return M,S,None,None
    x0=((1-M[1][1])*v[0]+M[0][1]*v[1])/S
    y0=(M[1][0]*v[0]+(1-M[0][0])*v[1])/S
    z=(x0,y0); points=[z]
    for letter in word:
        z=add(mul(matrices[letter],z),(F(1),F(0)))
        points.append(z)
    return M,S,points,v

for ai,bi,ci,di in product([F(5,4),F(4,3),F(9,5)],
                           [F(1,4),F(-1,2),F(3,4)],
                           [F(4),F(7,2),F(13,5)],
                           [F(-9,2),F(1,3),F(-4,5)]):
    a,b,c,d=ai,bi,ci,di
    for word in ('LLR','LRR'):
        M,S,pts,_=orbit(a,b,c,d,word)
        if word=='LLR':
            T=-a*a*c-a*b-a*d+b*c;D=b*b*d
            n0=a*c-a*d-b*d+b+c-1
            n1=a*c-a+b*c-b*d+d-1
            n2=a*a+a*b+a+b*b-b+1
            test(trace(M)==T)
            test(det(M)==D)
            test(S==1-T+D)
            if S:
                test(pts[0][0]*S==-n0)
                test(pts[1][0]*S==-n1)
                test(pts[2][0]*S==n2)
                test(pts[3]==pts[0])
        else:
            T=a*c*c-a*d+b*c+c*d; D=b*d*d
            k=c*c-c*d-c+d*d-d+1
            test(trace(M)==T)
            test(det(M)==D)
            test(S==1-T+D)
            test(k==(d-(c+1)/2)**2+3*(c-1)**2/4)
            if S:
                test(pts[0][0]*S==k)
                test(pts[3]==pts[0])

# Rational, strictly admissible, hyperbolically attracting example.
a,b,c,d=F(4,3),F(1,4),F(4),F(-9,2)
M,S,pts,_=orbit(a,b,c,d,'LLR')
T=trace(M);D=det(M)
test(a>abs(1+b))
test(c>abs(1+d))
test(M==((F(-58,9),F(-67,12)),(F(55,8),F(6))))
test((S,1+T+D,1-D)==(F(335,288),F(79,288),F(41,32)))
test(pts[:3]==[(F(-4524,335),F(5517,335)),(F(-36,67),F(1131,335)),(F(1226,335),F(9,67))])
test(pts[0][0]<0 and pts[1][0]<0 and pts[2][0]>0)

# Supporting rational point inside the golden-ratio edge construction.
b,d=F(1,4),F(-8)
a=1+b+F(1,10000)
c=-1-d+F(1,10000)
M,S,pts,_=orbit(a,b,c,d,'LLR')
test(a>1+b and c>abs(1+d))
test(0<S and 0<1+trace(M)+det(M) and det(M)<1)
test(pts[0][0]<0 and pts[1][0]<0 and pts[2][0]>0)
print('PASS',checks,'exact-rational assertions')
