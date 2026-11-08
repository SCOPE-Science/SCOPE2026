"""Exact-arithmetic verification of parametric Ehrhart sign asymptotics.
Requires only Python 3 standard library; finite tests supplement the written proof.
"""
from fractions import Fraction as F
from math import comb, factorial


def add(a,b):
    c=[F(0)]*max(len(a),len(b))
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]+=v
    return c

def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,u in enumerate(a):
        for j,v in enumerate(b): c[i+j]+=u*v
    return c

def scale(a,z):
    return [v*z for v in a]

def bernoulli_even(n):
    assert n%2==0
    A=[]
    for m in range(n+1):
        A.append(F(1,m+1))
        for j in range(m,0,-1): A[j-1]=j*(A[j-1]-A[j])
    return A[0]

def coefficient_table(r):
    """Return t-coefficients, each as a rational polynomial in c.

    Uses integer-height fiber enumeration and a Newton forward-difference
    interpolation, independent of Bernoulli-polynomial coefficient formulas.
    """
    d=r+1
    values=[]
    for t in range(d+1):
        v=[F(0)]
        for j in range(t+1):
            term=[F(1)]
            for k in range(1,r+1): term=mul(term,[F(t+k),F(j)])
            v=add(v,scale(term,F(1,factorial(r))))
        values.append(v)
    diffs=values
    result=[[F(0)] for i in range(d+1)]
    basis=[F(1)]
    for k in range(d+1):
        if k:
            basis=scale(mul(basis,[F(-(k-1)),F(1)]),F(1,k))
        for j,coef in enumerate(basis):
            result[j]=add(result[j],scale(diffs[0],coef))
        diffs=[add(diffs[i+1],scale(diffs[i],-1)) for i in range(len(diffs)-1)]
    return result

def evaluate(a,c): return sum(v*pow(c,i) for i,v in enumerate(a))

def count_direct(r,t,c):
    # Independent recursive enumeration of all coordinate totals in each section.
    def vectors_with_sum_at_most(d,bound):
        if d==0: return 1
        return sum(vectors_with_sum_at_most(d-1,bound-v) for v in range(bound+1))
    return sum(vectors_with_sum_at_most(r,t+c*j) for j in range(t+1))

def check():
    checks=0
    small=[]
    for r in range(4,13):
        rows=coefficient_table(r)
        d=r+1
        expected_negative=[]
        for k in range(d+1):
            arr=rows[k]
            while len(arr)>1 and not arr[-1]: arr.pop()
            if k==0:
                assert arr==[F(1)]; checks+=1;continue
            if k==d:
                assert arr[r]==F(1,factorial(r)*(r+1));checks+=1;continue
            if k==r:
                assert arr[r]==F(1,2*factorial(r));checks+=1;continue
            if (r+1-k)%2==0:
                h=(r+1-k)//2
                assert 1<=h<=r//2
                expected=F(comb(r+1,2*h),factorial(r)*(r+1))*bernoulli_even(2*h)
                assert arr[r]==expected and expected!=0
                checks+=2
                if expected<0: expected_negative.append(k)
            else:
                h=(r-k)//2
                assert 1<=h<=(r-1)//2
                expected=F((r+1)*comb(r,2*h),2*factorial(r-1)*r)*bernoulli_even(2*h)
                assert len(arr)<=r and arr[r-1]==expected and expected!=0
                checks+=3
                if expected<0: expected_negative.append(k)
        wanted=sorted([k for h in range(1,r//2+1) if h%2==0 for k in (r+1-2*h,r-2*h) if k>=1])
        assert sorted(expected_negative)==wanted
        assert len(wanted)==r//4+(r-1)//4
        checks+=2
        # The coefficient polynomials reproduce the source's integral lattice counts.
        for c in (0,1,3,11):
            for t in (0,1,2,3):
                L=sum(evaluate(rows[k],c)*t**k for k in range(d+1))
                expected=sum(comb(t+c*j+r,r) for j in range(t+1))
                assert L==expected and L.denominator==1
                checks+=2
        # Compare an actual large-c sign vector with the predicted eventual vector.
        for c in (10**6,10**9):
            actual=[k for k in range(1,d+1) if evaluate(rows[k],c)<0]
            assert actual==wanted,(r,c,actual,wanted)
            checks+=1
        if r<=5:
            for c in (0,1,2):
                for t in (0,1):
                    assert count_direct(r,t,c)==sum(comb(t+c*j+r,r) for j in range(t+1))
                    checks+=1
        small.append((r,expected_negative))
    print('PASS',checks,'exact assertions, r=4..12. Sample negative degrees:',small)
if __name__=='__main__': check()
