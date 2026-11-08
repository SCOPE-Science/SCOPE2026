"""Exact integer-arithmetic tests for a lattice-excursion covariance identity.

Run: python verify.py
No third-party dependencies. Tests are finite corroboration, not a proof of
claims for arbitrary length.
"""
from collections import defaultdict
from fractions import Fraction
from math import comb


def catalan(n):
    return comb(2*n, n)//(n+1)


def formulas(n):
    c=catalan(n)
    q=Fraction(4**n,c)
    ea=q-(2*n+1)
    er=Fraction(3*n,n+2)
    ear=3*q-10*n+3-Fraction(12,n+2)
    cov=Fraction(6*q-4*n*n-14*n-6,n+2)
    assert cov==ear-ea*er
    return ea,er,ear,cov


def dynamic_moments(n):
    # State = current height; tuple: (number, sum A, sum R, sum A*R)
    old={0:(1,0,0,0)}
    for t in range(2*n):
        new=defaultdict(lambda:[0,0,0,0])
        for h,(count,sa,sr,sar) in old.items():
            for step in (-1,1):
                hh=h+step
                if hh<0 or hh>2*n-(t+1):
                    continue
                r=int(hh==0)
                # New A is A+h, new R is R+r.
                box=new[hh]
                box[0]+=count
                box[1]+=sa+h*count
                box[2]+=sr+r*count
                box[3]+=sar+h*sr+r*sa+h*r*count
        old={k:tuple(v) for k,v in new.items()}
    return old.get(0,(0,0,0,0))


def exhaustive_paths(n):
    sums=[0,0,0,0]
    def visit(t,h,a,r):
        if t==2*n:
            if h==0:
                sums[0]+=1
                sums[1]+=a
                sums[2]+=r
                sums[3]+=a*r
            return
        if h+1<=2*n-(t+1):
            visit(t+1,h+1,a+h,r)
        if h>0:
            visit(t+1,h-1,a+h,r+int(h==1))
    visit(0,0,0,0)
    return tuple(sums)


def compare(n, sums):
    c,sa,sr,sar=sums
    assert c==catalan(n)
    results=tuple(Fraction(x,c) for x in (sa,sr,sar))
    ea,er,ear,cov=formulas(n)
    assert results==(ea,er,ear),(n,results,(ea,er,ear))
    assert Fraction(sar,c)-Fraction(sa*sr,c*c)==cov
    assert (cov==0 if n==1 else cov<0)


def sign_cert(nmax):
    # P_n=(2n^2+7n+3)/3 is the explicit strict super-solution.
    for n in range(1,nmax+1):
        q=Fraction(4**n,catalan(n))
        p=Fraction(2*n*n+7*n+3,3)
        assert (q==p if n==1 else q<p)
        assert Fraction(4**(n+1),catalan(n+1))==q*Fraction(2*(n+2),2*n+1)
        assert Fraction(2*(n+1)**2+7*(n+1)+3,3)-p*Fraction(2*(n+2),2*n+1)==Fraction(n,3)


def main():
    count=0
    for n in range(1,10):
        compare(n,exhaustive_paths(n));count+=1
    for n in range(1,81):
        compare(n,dynamic_moments(n));count+=1
    sign_cert(300);count+=300
    print(f"PASS: {count} independent length/certificate cases; exact enumeration n<=9, DP n<=80, sign inequalities n<=300")

if __name__=='__main__':
    main()

# Additional independent check of the two-class conditional-area gap.
def conditional_area_by_returns(n):
    states={(0,0):(1,0)}
    for t in range(2*n):
        nxt=defaultdict(lambda:[0,0])
        for (h,r),(cnt,sa) in states.items():
            for step in (-1,1):
                hh=h+step
                if hh<0 or hh>2*n-t-1: continue
                rr=r+int(hh==0)
                box=nxt[hh,rr]
                box[0]+=cnt
                box[1]+=sa+h*cnt
        states={k:tuple(v) for k,v in nxt.items()}
    return {r:Fraction(sa,c) for (h,r),(c,sa) in states.items() if h==0}

if __name__=='__main__':
    for n in range(2,51):
        cr=conditional_area_by_returns(n)
        assert cr[1]-cr[2]==n, (n, cr)
    print('PASS: conditional mean area gap n for 2<=n<=50 (exact DP)')
