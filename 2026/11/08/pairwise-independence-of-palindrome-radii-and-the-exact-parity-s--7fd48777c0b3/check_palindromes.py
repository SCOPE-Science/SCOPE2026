#!/usr/bin/env python3
"""Exact finite checks of palindrome-radius independence and count covariances."""
from itertools import product
from fractions import Fraction as Q


def palindromic_radii(word):
    n=len(word)
    out=[]
    for c2 in range(2*n-1):
        l=(c2-1)//2
        r=(c2+2)//2
        k=0
        while l>=0 and r<n and word[l]==word[r]:
            k+=1
            l-=1
            r+=1
        out.append(k)
    return tuple(out)


def max_radius(n,c2):
    k=0
    l=(c2-1)//2
    r=(c2+2)//2
    while l>=0 and r<n:
        k+=1
        l-=1
        r+=1
    return k


def moments(n,q):
    words=product(range(q),repeat=n)
    sums=[0]*(n+1)
    cross=[[0]*(n+1) for _ in range(n+1)]
    radii_cums=[[0]*(max_radius(n,c)+1) for c in range(2*n-1)]
    pair_success={}
    T_sum=T2_sum=0
    total=q**n
    for w in words:
        rs=palindromic_radii(w)
        counts=[0]*(n+1)
        counts[1]=n
        for c2,radius in enumerate(rs):
            for r in range(1,radius+1):
                counts[2*r+(c2%2==0)]+=1
            for a in range(1,radius+1):
                radii_cums[c2][a]+=1
        T=sum(counts)
        T_sum+=T
        T2_sum+=T*T
        for a in range(1,n+1):
            sums[a]+=counts[a]
            for b in range(1,n+1):
                cross[a][b]+=counts[a]*counts[b]
        for c in range(2*n-1):
            for d in range(c+1,2*n-1):
                for a in range(1,rs[c]+1):
                    for b in range(1,rs[d]+1):
                        key=(c,d,a,b)
                        pair_success[key]=pair_success.get(key,0)+1
    assert T_sum==sum(sums)
    t=Q(1,q)
    expect_T=Q(n)+sum(Q(2*n-4*r+1)*t**r for r in range(1,n//2+1))
    assert Q(T_sum,total)==expect_T,(n,q)
    expected_var=sum(sum((2*r-1)*t**r for r in range(1,max_radius(n,c)+1)) -
                     sum(t**r for r in range(1,max_radius(n,c)+1))**2 for c in range(2*n-1))
    assert Q(T2_sum,total)-Q(T_sum,total)**2==expected_var,(n,q)
    checks=2
    for c in range(2*n-1):
        for a in range(1,max_radius(n,c)+1):
            assert Q(radii_cums[c][a],total)==t**a,(n,q,c,a)
            checks+=1
            for d in range(c+1,2*n-1):
                for b in range(1,max_radius(n,d)+1):
                    assert Q(pair_success.get((c,d,a,b),0),total)==t**(a+b),(n,q,c,d,a,b)
                    checks+=1
    for a in range(2,n+1):
        for b in range(2,n+1):
            cov=Q(cross[a][b],total)-Q(sums[a]*sums[b],total*total)
            if a%2 != b%2: target=Q(0)
            else:
                ra=a//2; rb=b//2
                length=2*max(ra,rb)+(a%2)
                common=max(0,n-length+1)
                target=common*(t**max(ra,rb)-t**(ra+rb))
            assert cov==target,(n,q,a,b,cov,target)
            checks+=1
    return checks,expect_T,expected_var


def check_forest(n,c,d,a,b):
    parent=list(range(n))
    def root(v):
        while parent[v]!=v:
            v=parent[v]
        return v
    pairs=[]
    for j,rad in ((c,a),(d,b)):
        l=(j-1)//2
        r=(j+2)//2
        for k in range(rad):
            pairs.append((l-k,r+k))
    for u,v in pairs:
        ru,rv=root(u),root(v)
        if ru==rv:return False
        parent[ru]=rv
    return True


def main():
    checks=0
    for n in range(2,15):
        for c in range(2*n-1):
            for d in range(c+1,2*n-1):
                for a in range(1,max_radius(n,c)+1):
                    for b in range(1,max_radius(n,d)+1):
                        assert check_forest(n,c,d,a,b)
                        checks+=1
    for q,upper in [(2,8),(3,6)]:
        for n in range(2,upper+1):
            c,e,v=moments(n,q)
            checks+=c
            print(f'q={q},n={n}: E={e}, Var={v}, exact_checks={c}')
    # Exact nonuniform obstruction for p=(4/5,1/5) at n=3:
    p=[Q(4,5),Q(1,5)]
    alpha=sum(x*x for x in p)
    beta=sum(x*x*x for x in p)
    assert beta-alpha**2==Q(36,625)
    checks+=1
    # Three event indicators at separate centers are pairwise, not jointly, independent.
    for q in (2,3,4):
        words=list(product(range(q),repeat=3))
        A=sum(w[0]==w[1] for w in words)
        B=sum(w[0]==w[2] for w in words)
        C=sum(w[1]==w[2] for w in words)
        AB=sum(w[0]==w[1] and w[0]==w[2] for w in words)
        ABC=sum(w[0]==w[1]==w[2] for w in words)
        total=q**3
        assert Q(A,total)==Q(B,total)==Q(C,total)==Q(1,q)
        assert Q(AB,total)==Q(ABC,total)==Q(1,q*q)!=Q(1,q**3)
        checks+=2
    print('PASS:',checks,'independently computed exact checks')

if __name__=='__main__':main()
