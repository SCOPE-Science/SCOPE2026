"""Exact finite checks for the three-dimensional twisted-baker occupation spectrum.
Run: python3 checker.py. Finite tests support, but do not prove, the limit theorem.
"""
from fractions import Fraction as Q
from itertools import product

L=((2,0,0),(0,1,0),(0,0,1))
R=((0,0,-2),(1,0,0),(0,1,0))


def mul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))

def counts(word):
    # Suffix sums of right symbols, from the last letter to the first.
    out=[0,0,0]
    j=0
    for a in reversed(word):
        out[j]+=1
        j=(j+a)%3
    return tuple(out)

def mat_counts(word):
    A=((1,0,0),(0,1,0),(0,0,1))
    for a in word:
        A=mul(R if a else L,A)
    norm2=[sum(A[i][j]**2 for i in range(3)) for j in range(3)]
    assert all(t>0 and (t & (t-1))==0 for t in norm2)
    return sorted((t.bit_length()-1)//2 for t in norm2)

def matrix_mul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))

def mgf_enum(n,u):
    z=Q(0)
    for w in product((0,1),repeat=n):
        z+=u**counts(w)[0]/2**n
    return z

def mgf_transfer(n,u):
    P=((Q(1,2),Q(1,2),0),
       (0,Q(1,2),Q(1,2)),
       (Q(1,2),0,Q(1,2)))
    A=tuple(tuple((u if i==0 else Q(1))*P[i][j] for j in range(3)) for i in range(3))
    x=(Q(1),Q(1),Q(1))
    for _ in range(n):
        x=tuple(sum(A[i][j]*x[j] for j in range(3)) for i in range(3))
    return x[0]

def rate_y(y):
    y=float(y)
    u=y*y*(1+y)/(1+y*y)
    x=y*(1+y*y)/(y*y*y+3*y+2)
    from math import log
    I=x*log(u)-log((1+y)/2)
    J=x*log(3*x)+(1-x)*log(1.5*(1-x))
    return x,I,J

def main():
    words=0
    for n in range(1,10):
        for w in product((0,1),repeat=n):
            assert mat_counts(w)==sorted(counts(w)),(n,w)
            words+=1
    exact_mgfs=0
    for n in range(1,11):
        for u in (Q(1,2),Q(2),Q(3)):
            assert mgf_transfer(n,u)==mgf_enum(n,u),(n,u)
            exact_mgfs+=1
    # Parametric cubic characteristic identity, with exact rational y values.
    for y in (Q(1,8),Q(1,4),Q(1,2),Q(1),Q(2),Q(3),Q(8)):
        u=y*y*(1+y)/(1+y*y)
        lam=(1+y)/2
        assert (2*lam-u)*(2*lam-1)**2==u
        x=y*(1+y*y)/(y**3+3*y+2)
        assert 0<x<1
    for y in (1/8,1/4,1/2,2,3,8):
        x,I,J=rate_y(y)
        assert (I>J if x<1/3 else I<J), (y,x,I,J)
    print(f"TWISTED_BAKER_THREE_STATE_LDP_CHECK_OK words={words} exact_mgfs={exact_mgfs} cubic_parameters=7 strict_iid_comparisons=6")

if __name__=='__main__':
    main()
