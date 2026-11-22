"""Supplementary numerical checks for exact two-state randomized order splitting.

Run with Python 3 standard library: python verify.py.
"""
import math
import itertools

N = 0

def close(a, b, tol=3e-11):
    global N
    N += 1
    if not math.isclose(a, b, rel_tol=tol, abs_tol=tol):
        raise AssertionError((a, b))

def mul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def affine_rates(a, b, h):
    s = a + b
    decay = math.exp(-s * h)
    return [[1 - a * (1 - decay) / s, a * (1 - decay) / s],
            [b * (1 - decay) / s, 1 - b * (1 - decay) / s]]

def exact_matrix(a, b, c, d, h):
    return affine_rates(a + c, b + d, h)

def order_weight(s, t, h):
    # q is the probability of reversing the AB order, i.e., using BA.
    u = math.exp(-s*h)
    v = math.exp(-t*h)
    return ((s/(s+t)) * (-math.expm1(-(s+t)*h))
            - v * (-math.expm1(-s*h))) / ((-math.expm1(-s*h))*(-math.expm1(-t*h)))

def one_step(a, b, c, d, h):
    A=affine_rates(a,b,h)
    B=affine_rates(c,d,h)
    AB=mul(A,B)
    BA=mul(B,A)
    q=order_weight(a+b,c+d,h)
    return AB,BA,q

rates=[(1,0,0,1),(2,3,5,7),(1,7,8,1),(0.1,9,2,0.1),(0,3,5,0),(13,0,0,0.4),(5,5,4,4)]
for a,b,c,d in rates:
    for h in [0.0001,0.01,0.1,0.5,1,2,6]:
        AB,BA,q=one_step(a,b,c,d,h)
        E=exact_matrix(a,b,c,d,h)
        if not 0 < q < 1:
            raise AssertionError(('invalid probability',q))
        for i in range(2):
            for j in range(2):
                close((1-q)*AB[i][j]+q*BA[i][j], E[i][j])
        for X in [AB,BA]:
            for i in range(2):
                close(sum(X[i]),1.0)
                for j in range(2):
                    if X[i][j]<-1e-12: raise AssertionError('negative probability')

# Test the exact n-step mean and variance by enumerating every pair-order word.
for a,b,c,d in [(2,0,0,3),(1,2,3,1),(0.2,5,4,0.1)]:
    h=0.21
    AB,BA,q=one_step(a,b,c,d,h)
    s=a+b; t=c+d
    u=math.exp(-s*h);v=math.exp(-t*h)
    piA=a/s; piB=c/t
    delta=(1-u)*(1-v)*(piA-piB)
    r=u*v
    for n in range(1,9):
        x0=0.37
        outcomes=[]
        for seq in itertools.product([0,1],repeat=n):
            x=x0;prob=1.0
            for choice in seq:
                X=BA if choice else AB
                prob*=q if choice else 1-q
                x=x*X[0][0]+(1-x)*X[1][0]
            outcomes.append((prob,x))
        mean=sum(p*x for p,x in outcomes)
        variance=sum(p*(x-mean)**2 for p,x in outcomes)
        target=x0*r**n+(1-r**n)*(b+d)/(s+t)
        # x tracks probability of state 0; its stationary probability is (b+d)/(s+t).
        close(mean,target)
        close(variance,q*(1-q)*delta**2*(1-r**(2*n))/(1-r*r))

# Three-state obstruction, via strict trace gap of a two-state transient block.
for h in [0.001,0.01,0.1,0.5,1,2,5,10]:
    split=2*math.exp(-1.5*h)*math.cosh(h)*math.cosh(h/2)
    exact=2*math.exp(-1.5*h)*math.cosh(math.sqrt(5)*h/2)
    if not split>exact:
        raise AssertionError((split,exact))

print('VERIFIED numerical_assertions=',N+8)
print('probability example',order_weight(2,3,1))
