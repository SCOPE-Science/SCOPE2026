"""Exact-rational verification of a paired, noisy signed-step bilinear iteration.
All matrices and moment identities are computed using fractions.Fraction.
The theoretical proof is in RESULT.md; these checks independently test its formulas.
"""
from fractions import Fraction as F
from itertools import product

def matmul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))) for i in range(len(A)))
def transpose(A):return tuple(zip(*A))
def add(A,B):return tuple(tuple(x+y for x,y in zip(a,b)) for a,b in zip(A,B))
def sub(A,B):return tuple(tuple(x-y for x,y in zip(a,b)) for a,b in zip(A,B))
def scale(c,A):return tuple(tuple(c*x for x in a) for a in A)
def trace(A):return sum(A[i][i] for i in range(len(A)))
I=((F(1),F(0)),(F(0),F(1)))
S=((F(0),F(1)),(F(1),F(0)))
Z=((F(0),F(0)),(F(0),F(0)))

def once(r,C,variance=F(1)):
    # C is the cross-covariance E[epsilon_0 epsilon_1^T]/variance.
    Up=add(I,scale(r,S)); Um=sub(I,scale(r,S))
    assert matmul(Up,Um)==scale(1-r*r,I)
    V=scale(variance,sub(sub(add(matmul(Up,Up),I),matmul(Up,C)),matmul(transpose(C),Up)))
    return V

def risk(r,C,variance=F(1),slope=F(1)):
    assert 0<r*r<2
    # h=r/slope; finite-stationary risk of the even subsequence
    return (r/slope)**2 * trace(once(r,C,variance))/(r*r*(2-r*r))

count=0
for a,b in product(range(1,15),range(1,15)):
    r=F(a,b)
    if not (0<r*r<2):continue
    sigma=F(2,3)
    tau2=F(7,5)
    best=I if r<=1 else S
    target=2*tau2*(r*r if r<=1 else ((r-1)**2+1))/(sigma*sigma*(2-r*r))
    assert risk(r,best,tau2,sigma)==target
    independent=2*tau2*(2+r*r)/(sigma*sigma*(2-r*r))
    common=2*tau2*r*r/(sigma*sigma*(2-r*r))
    reflected=2*tau2*(1+(r-1)**2)/(sigma*sigma*(2-r*r))
    assert risk(r,Z,tau2,sigma)==independent
    assert risk(r,I,tau2,sigma)==common
    assert risk(r,S,tau2,sigma)==reflected
    assert target<=common and target<=reflected and target<independent
    # Every orthogonal cross-coupling sampled on the rational unit circle
    for k,j in ((0,1),(3,4),(5,12),(8,15),(20,21)):
        d=k*k+j*j; c=F(j*j-k*k,d); s=F(2*k*j,d)
        O=((c,-s),(s,c))
        for C in (O,transpose(O),scale(-1,O),S,scale(-1,S),I,scale(-1,I)):
            assert matmul(C,transpose(C))==I
            assert risk(r,C,tau2,sigma)>=target
            count+=1
    # confirm finite-time optimum for 1,2,7 completed pairs
    for T in (1,2,7):
        q=1-r*r
        finite=(1-q**(2*T))*target
        for C in (I,S,Z):
            observed=(1-q**(2*T))*risk(r,C,tau2,sigma)
            assert observed>=finite
            count+=1
assert risk(F(3,5),I)==F(18,41)
assert risk(F(3,5),Z)==F(118,41)
assert risk(F(6,5),S)==F(26,7)
assert risk(F(6,5),I)==F(36,7)
assert risk(F(6,5),Z)==F(86,7)
print('PASS:',count,'exact orthogonal/finite-time comparisons, analytic formulas and five rational witnesses')
