"""Exact finite checks for the two-choice centered box-envelope BV theorem.
Python 3 standard library only; no external scientific packages required.
These finite checks supplement the analytical all-radius proof.
"""
from fractions import Fraction as F
from itertools import product
from random import Random


def predicted(r):
    return F(2*r+1+4*(r*r//4), 2*r+1)


def step_column(r, left, right):
    """BV norm of the step response for binary activation masks on its wings."""
    v = {i:F(0) for i in range(-r-1,r+2)}
    for k in range(1,r+1):
        v[-r+k] = F(k*left[k-1],2*r+1)
        v[r+1-k] = 1-F(k*right[k-1],2*r+1)
    v[r+1] = F(1)
    return sum(abs(v[i+1]-v[i]) for i in range(-r-1,r+1))


def solve(A, b):
    """Exact nonsingular rational Gaussian elimination."""
    n=len(b)
    z=[[F(A[i][j]) for j in range(n)]+[F(b[i])] for i in range(n)]
    for k in range(n):
        p=next(i for i in range(k,n) if z[i][k])
        z[k],z[p]=z[p],z[k]
        fac=z[k][k]
        z[k]=[q/fac for q in z[k]]
        for i in range(n):
            if i!=k:
                fac=z[i][k]
                if fac:z[i]=[z[i][j]-fac*z[k][j] for j in range(n+1)]
    return [z[i][-1] for i in range(n)]


def witness(r, mask):
    """Finite-support baseline enforcing a prescribed mask near a step."""
    J=list(range(-r+1,r+1))
    B=[[F(int(abs(i-j)<=r),2*r+1)-int(i==j) for j in J] for i in J]
    z=solve(B, [F(1 if mask[i] else -1) for i in J])
    g=dict(zip(J,z))
    C=F(1)+max(abs(q) for q in z)
    def f(i):return C+g.get(i,F(0))
    def step(i):return F(int(i>=1))
    def Q(h,i):return sum((h(i+s) for s in range(-r,r+1)),F(0))/F(2*r+1)
    def T(h,i):return max(h(i),Q(h,i))
    def v(i):return f(i)+step(i)
    # The chosen branch must be strict at every location where the step perturbs Q-I.
    for i in J:
        assert (Q(f,i)>f(i)) == bool(mask[i])
        assert (Q(v,i)>v(i)) == bool(mask[i])
    return sum(abs((T(v,i+1)-T(f,i+1))-(T(v,i)-T(f,i)))
               for i in range(-3*r,3*r+1))


def path_variation(values):
    return sum((abs(y-x) for x,y in zip(values,values[1:])),F(0))

for r in range(1,8):
    bits=list(product((0,1),repeat=r))
    exact=max(step_column(r,a,b) for a in bits for b in bits)
    assert exact==predicted(r),(r,exact,predicted(r))
    print('EXHAUSTIVE_BINARY_STEP_MASK_PASS',r,exact)

for r in range(1,9):
    # Choose falling indices r-1,r-3,... on both wings.
    a=tuple(int(k<r and (r-1-k)%2==0) for k in range(1,r+1))
    mask={-r+k:a[k-1] for k in range(1,r+1)}
    mask.update({r+1-k:a[k-1] for k in range(1,r+1)})
    actual=witness(r,mask)
    assert actual==predicted(r),(r,actual,predicted(r))
    print('EXACT_NONNEGATIVE_BV_WITNESS_PASS',r,actual)

rng=Random(290)
for r in range(1,8):
    for k in range(150):
        m=9*r+15
        a=[F(rng.randint(-15,15),rng.randint(1,4)) for _ in range(m)]
        b=[F(rng.randint(-15,15),rng.randint(1,4)) for _ in range(m)]
        def T(x):
            # Constant extension avoids artificial jumps at the ends.
            return [max(x[i],sum((x[min(m-1,max(0,i+t))] for t in range(-r,r+1)),F(0))/F(2*r+1)) for i in range(m)]
        out=[u-v for u,v in zip(T(a),T(b))]
        inp=[u-v for u,v in zip(a,b)]
        assert path_variation(out)<=predicted(r)*path_variation(inp)
    print('RATIONAL_TWO_INPUT_STRESS_PASS',r,150)
print('ALL_TWO_CHOICE_BV_CHECKS_PASS')
