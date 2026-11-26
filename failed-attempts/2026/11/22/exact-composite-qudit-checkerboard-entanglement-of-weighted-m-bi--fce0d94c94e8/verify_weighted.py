"""Check exact Smith factors for weighted twisted cycles against the 2x2 recurrence.

Finite verification only. The symbolic all-size proof is in RESULT.md.
"""
from math import gcd
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

def direct(n,w):
    assert n % 2 and n>=3
    b=[[0]*n for _ in range(n)]
    for i in range(n):
        b[i][i] = 1             # rim forward
        b[i][(i-1)%n] += 1     # rim backward
        b[i][(i+(n-1)//2)%n] += w  # opposite rung
    return Matrix(b)

def factors(n,w):
    p,q=0,1
    seq=[p,q]
    for k in range(1,n+1):
        p,q=q,-w*q-p
        seq.append(q)
    g=gcd(abs(seq[n]),abs(seq[n-1]+1))
    C=Matrix([[0,-1],[1,-w]])
    M=C**n-Matrix.eye(2)
    determinant=int(M.det())
    if determinant==0:
        return [1]*(n-2)+([0,0] if g==0 else [g,0])
    return [1]*(n-2)+[g,abs(determinant)//g]

for n in range(3,18,2):
    for w in range(-6,7):
        A=direct(n,w)
        d=[abs(int(smith_normal_form(A,domain=ZZ)[i,i])) for i in range(n)]
        f=factors(n,w)
        assert d==f,(n,w,d,f)
    print('weighted n=',n,'pass 13 weights')
print('WEIGHTED_SMITH_PASS')
