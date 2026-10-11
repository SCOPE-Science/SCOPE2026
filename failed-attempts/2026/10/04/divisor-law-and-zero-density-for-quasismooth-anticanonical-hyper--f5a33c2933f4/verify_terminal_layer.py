#!/usr/bin/env python3
from itertools import combinations
from math import gcd, isqrt, log


def divisors_count(n:int)->int:
    c=0
    for d in range(1,isqrt(n)+1):
        if n%d==0:
            c += 1 if d*d==n else 2
    return c


def representable(n:int, weights)->bool:
    if n<0:
        return False
    if n==0:
        return True
    ws=sorted(set(weights))
    if 1 in ws:
        return True
    ok=[False]*(n+1)
    ok[0]=True
    for m in range(n+1):
        if not ok[m]:
            continue
        for w in ws:
            if m+w<=n:
                ok[m+w]=True
    return ok[n]


def fletcher_general(weights, degree:int)->bool:
    # Fletcher's hypersurface criterion, for the non-linear-cone case degree>all weights.
    N=len(weights)
    if degree in weights:
        return True
    for k in range(1,N+1):
        for I in combinations(range(N),k):
            Iset=set(I)
            iw=[weights[i] for i in I]
            if representable(degree, iw):
                continue
            good_out=0
            for e,w in enumerate(weights):
                if e in Iset:
                    continue
                if representable(degree-w, iw):
                    good_out+=1
            if good_out<k:
                return False
    return True


def terminal_layer_formula(r:int,a:int)->bool:
    return (r%a==0) or ((2*r-2)%a==0) or ((2*r-1)%a==0)


def fletcher_layer_reduced(r:int,a:int)->bool:
    b=a+r-1
    D=r+a+b
    # only subsets of the two heavy variables can matter; keep all three reduced checks explicit
    y = (D%a==0) or ((D-1)%a==0) or ((D-b)%a==0)
    z = (D%b==0) or ((D-1)%b==0) or ((D-a)%b==0)
    yz = representable(D,(a,b)) or representable(D-1,(a,b))
    return y and z and yz


def ages_terminal(r:int,a:int)->bool:
    b=a+r-1
    # a-chart: 1/a(1^r,b)
    if a>1:
        for k in range(1,a):
            age_num = r*k + ((b*k)%a)
            if age_num <= a:
                return False
    # b-chart: 1/b(1^r,a)
    if b>1:
        for k in range(1,b):
            age_num = r*k + ((a*k)%b)
            if age_num <= b:
                return False
    return True


def N_formula(r:int)->int:
    return (divisors_count(r)+divisors_count(2*r-2)+divisors_count(2*r-1)
            -divisors_count(gcd(r,2))-2)


def Dsum(n:int)->int:
    # divisor summatory function by hyperbola identity
    if n<=0:
        return 0
    m=isqrt(n)
    return 2*sum(n//k for k in range(1,m+1))-m*m


def cumulative_closed(R:int)->int:
    if R<2:
        return 0
    # Sum tau(r), r=2..R
    A=Dsum(R)-1
    # Sum tau(2(r-1)), r=2..R, using tau(2n)=2 tau(n)-1_{2|n}tau(n/2)
    N=R-1
    B=2*Dsum(N)-Dsum(N//2)
    # Sum tau(2r-1), r=2..R = odd tau sum up to 2R-1, minus tau(1)
    X=2*R-1
    C=Dsum(X)-2*Dsum(X//2)+Dsum(X//4)-1
    # Sum tau(gcd(r,2)) = 1 for odd r, 2 for even r
    G=(R-1)+(R//2)
    return A+B+C-G-2*(R-1)


def main():
    # Full Fletcher-subset replay for small dimensions, no reduced-criterion assumptions.
    for r in range(2,9):
        for a in range(1,2*r-1):
            b=a+r-1
            D=r+a+b
            weights=[1]*r+[a,b]
            assert D>max(weights)
            qfull=fletcher_general(weights,D)
            qred=fletcher_layer_reduced(r,a)
            qform=terminal_layer_formula(r,a)
            assert qfull==qred==qform, (r,a,qfull,qred,qform)
            assert ages_terminal(r,a), (r,a,'nonterminal')

    # Large exact arithmetic sweep using the reduced three-stratum criterion.
    for r in range(2,401):
        got=[]
        for a in range(1,2*r-1):
            assert ages_terminal(r,a), (r,a,'nonterminal')
            q=fletcher_layer_reduced(r,a)
            f=terminal_layer_formula(r,a)
            assert q==f, (r,a,q,f)
            if q:
                got.append(a)
        assert len(got)==N_formula(r), (r,len(got),N_formula(r))

    # Exact summatory identity against direct counts.
    running=0
    for R in range(2,5001):
        running += N_formula(R)
        assert running==cumulative_closed(R), (R,running,cumulative_closed(R))

    # The proven asymptotic has this main term; report a large finite residual as a regression number.
    gamma=0.577215664901532860606512090082402431
    C=6*gamma+2*log(2)-13/2
    R=5000
    exact=cumulative_closed(R)
    mainterm=3*R*log(R)+C*R
    residual=exact-mainterm
    print('VERIFY_OK')
    print('checked_full_fletcher_r<=8')
    print('checked_reduced_and_terminal_r<=400')
    print('checked_summatory_R<=5000')
    print(f'N(5000)_cumulative={exact}')
    print(f'asymptotic_residual_at_5000={residual:.12f}')

if __name__=='__main__':
    main()
