"""Exact finite checks of the Frobenius-preserving injection in multiplicity four.
Public-domain reproducibility checker, Python 3 stdlib only.
"""
from collections import defaultdict

def valid(a,b,c):
    return min(a,b,c)>=1 and b<=2*a and c<=a+b and a<=b+c+1 and b<=2*c+1

def frob(a,b,c):
    return max(4*a+1,4*b+2,4*c+3)-4

def semigroup_contains(n,a,b,c):
    if n==0:return True
    if n<0:return False
    t=(0,4*a+1,4*b+2,4*c+3)
    return n>=t[n%4]

def real_leaf(a,b,c):
    F=frob(a,b,c)
    # Every minimal generator other than 4 is an Apéry element and at most F+4;
    # a right generator x is effective when no sum of two positive members equals x.
    for x in range(4,F+5):
        if semigroup_contains(x,a,b,c) and x>F:
            if not any(semigroup_contains(i,a,b,c) and semigroup_contains(x-i,a,b,c) for i in range(1,x)):
                return False
    return True

def family(a,b,c):
    if a==b+c+1:return 'A'
    if c==a+b:return 'B'
    if b==2*a and a<=c<=2*a-2:return 'C'
    if b==2*c+1 and c+1<=a<=2*c:return 'D'
    return '-'

def map_target(a,b,c):
    F=frob(a,b,c)
    if a==b+c+1:
        return a,b,c+1
    if c==a+b:
        return a+1,b,c
    if b==2*a and a<=c<=2*a-2:
        return a+1,b,c
    if b==2*c+1 and c+1<=a<=2*c:
        return a,b,c+1
    raise ValueError('not leaf')

def leaf_formula(h,r):
    if r==1:
        return max(0,min(h-2,(2*h-1)//3))
    if r==2:
        return max(0,(h-1)//2)
    if r==3:
        return h-(h+2)//3
    raise ValueError(r)

def total_formula(h,r):
    if r==1:
        return sum(max(0,min(h-1,2*c+1)-max(1,h-1-c)+1) for c in range(1,h))
    if r==2:
        return (h//2+1)*((h+1)//2)
    if r==3:
        return sum(max(0,min(h,2*a)-max(1,h-a)+1) for a in range(1,h+1))
    raise ValueError(r)

def main():
    # Count and all-image check via coordinate enumeration; compare
    # independently with effective-generator definition and direct F.
    byF=defaultdict(list)
    H=75
    for a in range(1,H+1):
        for b in range(1,H+1):
            for c in range(1,H+1):
                if valid(a,b,c):
                    F=frob(a,b,c)
                    if F<=4*H-1:
                        byF[F].append((a,b,c))
    leaves_checked=0
    for F in range(3,4*H):
        if F%4==0:continue
        t=byF[F]
        h={1:(F+3)//4,2:(F+2)//4,3:(F+1)//4}[F%4]
        leaves=[x for x in t if real_leaf(*x)]
        families=[x for x in t if family(*x)!='-']
        assert set(leaves)==set(families),(F,leaves,families)
        assert len(leaves)==leaf_formula(h,F%4),(F,len(leaves),leaf_formula(h,F%4))
        assert len(t)==total_formula(h,F%4),(F,len(t),total_formula(h,F%4))
        targets=[map_target(*x) for x in leaves]
        assert len(set(targets))==len(leaves),('collision',F)
        for y in targets:
            assert valid(*y) and frob(*y)==F and not real_leaf(*y),(F,y)
        assert len(t)-len(leaves)>=len(leaves)
        leaves_checked+=len(leaves)
    print('VERIFY_OK', 'F_range=3..299', 'leaf_checks='+str(leaves_checked))
if __name__=='__main__': main()
