"""Exact checks for shared-key fringe intervals in random search trees.
No external packages are required. Run: python bst_common_fringe_verify.py
"""
from fractions import Fraction
from itertools import permutations
from math import factorial

def one_prob(n, a, b):
    k = b-a+1
    if k==n: return Fraction(1)
    d=(a>0)+(b<n-1)
    return [Fraction(1),Fraction(1,k+1),Fraction(2,(k+1)*(k+2))][d]

def beta_int(a,b):
    return Fraction(factorial(a)*factorial(b),factorial(a+b+1))

def one_separator(k,l,left_exists,right_exists):
    # Integral of A_k(t) A_l(t): each A conditional on the separator's priority.
    # Product expansion in t^r (1-t)^s.
    t1=[(0,k,Fraction(1))] if not left_exists else [(1,k,Fraction(1)),(0,k+1,Fraction(1,k+1))]
    t2=[(0,l,Fraction(1))] if not right_exists else [(1,l,Fraction(1)),(0,l+1,Fraction(1,l+1))]
    return sum((c*d*beta_int(a+u,b+v) for a,b,c in t1 for u,v,d in t2),Fraction(0))

def joint_prob(n,I,J):
    a,b=I;c,d=J
    if I==J:return one_prob(n,a,b)
    # Strict nesting: conditioning on the larger interval being fringe
    if a<=c and d<=b:
        return one_prob(n,a,b)*one_prob(b-a+1,c-a,d-a)
    if c<=a and b<=d:
        return one_prob(n,c,d)*one_prob(d-c+1,a-c,b-c)
    if a>c:
        return joint_prob(n,J,I)
    if c<=b:return Fraction(0) # crossing intervals
    if c==b+1:return Fraction(0) # adjacent intervals cannot both be fringe
    if c==b+2:
        return one_separator(b-a+1,d-c+1,a>0,d<n-1)
    return one_prob(n,a,b)*one_prob(n,c,d)

def fringe_intervals(p):
    n=len(p)
    # Independent recursive construction of the Cartesian tree from priority order.
    out=set()
    def walk(a,b):
        if a>b:return
        root=min(range(a,b+1),key=lambda i:p[i])
        out.add((a,b));walk(a,root-1);walk(root+1,b)
    walk(0,n-1)
    return out

def check_exact(n):
    intervals=[(i,j) for i in range(n) for j in range(i,n)]
    singles={I:0 for I in intervals}
    pairs={(I,J):0 for z,I in enumerate(intervals) for J in intervals[z+1:]}
    count=0
    for p in permutations(range(n)):
        F=fringe_intervals(p)
        count+=1
        for I in F: singles[I]+=1
        for I,J in pairs:
            if I in F and J in F: pairs[I,J]+=1
    tests=0
    for I,c in singles.items():
        assert Fraction(c,count)==one_prob(n,*I),(n,I,c)
        tests+=1
    for (I,J),c in pairs.items():
        assert Fraction(c,count)==joint_prob(n,I,J),(n,I,J,c,Fraction(c,count),joint_prob(n,I,J))
        tests+=1
    # Two independent trees: joint probability squares one-tree probability.
    for (I,J),c in pairs.items():
        assert Fraction(c*c,count*count)==joint_prob(n,I,J)**2
        tests+=1
    return tests

def check_mean(n,k):
    # Two-tree shared size-k interval expectation computed from independent priorities.
    exact=sum((one_prob(n,a,a+k-1)**2 for a in range(n-k+1)),Fraction(0))
    if k==n: return exact==1
    formula=Fraction(4*max(n-k-1,0),(k+1)**2*(k+2)**2)+Fraction(2,(k+1)**2)
    return exact==formula

if __name__=='__main__':
    total=0
    for n in range(2,8):
        c=check_exact(n)
        print('n',n,'exact assertions',c)
        total+=c
        for k in range(1,n+1):
            assert check_mean(n,k)
            total+=1
    print('PASS',total,'exact rational checks')
