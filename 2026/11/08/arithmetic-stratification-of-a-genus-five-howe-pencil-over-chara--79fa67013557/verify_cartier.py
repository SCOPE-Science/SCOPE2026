"""Exact Cartier coefficients and geometric rank strata for a characteristic-seven Howe family.
Run: python verify_cartier.py
"""
from itertools import product
P = 7
# f=(x^4-1)(x^4-a)=u^2-(a+1)u+a, u=x^4
# polynomial arithmetic over F7[a]; polynomials represented as sparse dict.
def add(A,B):
    c=A.copy()
    for e,v in B.items(): c[e]=(c.get(e,0)+v)%P
    return {e:v for e,v in c.items() if v}
def mul(A,B):
    c={}
    for e,x in A.items():
        for f,y in B.items(): k=(e[0]+f[0],e[1]+f[1]);c[k]=(c.get(k,0)+x*y)%P
    return {e:v for e,v in c.items() if v}
def power(A,k):
    v={(0,0):1}
    for _ in range(k):v=mul(v,A)
    return v
f={(2,0):1,(1,1):P-1,(1,0):P-1,(0,1):1}
cube=power(f,3)
# coefficient of u^m: represent a-polynomial
coeff=lambda m:{j:c for (i,j),c in cube.items() if i==m}
want={1:{2:4,3:4},3:{0:6,1:5,2:5,3:6},5:{0:4,1:4}}
# explicit identities equivalent to -3a^2(a+1), -(a-2)(a+1)(a+3), -3(a+1)
for m,d in want.items():
    assert coeff(m)==d,(m,coeff(m),d)

def evalpol(d,a):return sum(c*pow(a,e,P) for e,c in d.items())%P
masks={}
for a in range(P):
    if a in (0,1):continue
    d=[evalpol(coeff(j),a) for j in (1,3,5)]
    rank=(d[0]!=0)+(d[1]!=0)+(d[2]!=0)
    # A semilinear Hasse--Witt matrix has nonzero positions (1,3), (2,2), (3,1).
    # Both off-diagonal entries vanish simultaneously for a!=0,1.
    stable=(2 if d[0]*d[2] else 0)+(1 if d[1] else 0)
    assert rank==stable
    f_rank=stable
    a_number=5-rank  # 2 supersingular quartic elliptic quotients
    masks[a]=(f_rank,a_number)
assert masks=={2:(2,3),3:(3,2),4:(2,3),5:(3,2),6:(0,5)},masks
# Algebraic-closure exhaustive root reasoning: coeff(1) and coeff(5)
# both vanish only when a=-1 among a != 0,1; coeff(3) at -1,2,4.
assert [a for a in range(P) if evalpol(coeff(3),a)==0]==[2,4,6]
assert [a for a in range(P) if evalpol(coeff(1),a)==0]==[0,6]
assert [a for a in range(P) if evalpol(coeff(5),a)==0]==[6]
print('CARTIER_EXACT_OK',masks)
