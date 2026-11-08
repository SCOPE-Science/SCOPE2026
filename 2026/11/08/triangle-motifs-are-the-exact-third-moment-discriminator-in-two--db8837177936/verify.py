"""Exact enumeration of coextinction moments for cycle-union incidence models."""
from itertools import combinations
from fractions import Fraction
from math import comb


def cycles(parts):
    edges=[]; start=0
    for length in parts:
        assert length>=3
        edges.extend(tuple(sorted((start+i,start+(i+1)%length))) for i in range(length))
        start+=length
    return start,edges


def q(n,t,s):
    return Fraction(comb(n-s,t-s),comb(n,t)) if (0<=s<=t<=n) else Fraction(0)


def formula(n,t,T):
    q2,q3,q4,q5,q6=(q(n,t,s) for s in (2,3,4,5,6))
    E1=n*q2
    E2=2*(n*q3+(comb(n,2)-n)*q4)
    E3=6*(n*q4+n*(n-4)*q5+(comb(n,3)-n*(n-3))*q6+T*(q3-3*q4+3*q5-q6))
    return E1,E2,E3


def enumerated(parts,t):
    n,edges=cycles(parts)
    m1=m2=m3=0
    pmf=[0]*(n+1)
    for sub in combinations(range(n),t):
        S=set(sub)
        k=sum(u in S and v in S for u,v in edges)
        pmf[k]+=1
        m1+=k;m2+=k*(k-1);m3+=k*(k-1)*(k-2)
    denom=comb(n,t)
    return (Fraction(m1,denom),Fraction(m2,denom),Fraction(m3,denom)),pmf


def partitions(n,lo=3):
    if n==0:
        yield ()
    else:
        for x in range(lo,n+1):
            for rest in partitions(n-x,x):
                yield (x,)+rest


def main():
    count=0
    for n in range(3,12):
        for part in partitions(n):
            T=part.count(3)
            for t in range(n+1):
                exact,pmf=enumerated(part,t)
                assert exact==formula(n,t,T),(part,t,exact,formula(n,t,T))
                if n>=6:
                    coef=q(n,t,3)-3*q(n,t,4)+3*q(n,t,5)-q(n,t,6)
                    expected=Fraction(comb(n-6,t-3),comb(n,t)) if 3<=t<=n-3 else Fraction(0)
                    assert coef==expected
                count+=1
    for part in [(6,),(3,3)]:
        exact,pmf=enumerated(part,3)
        assert exact[:2]==(Fraction(6,5),Fraction(3,5))
        assert pmf[:4]==([2,12,6,0] if part==(6,) else [0,18,0,2]),pmf
        assert exact[2]==(0 if part==(6,) else Fraction(3,5))
        print(part,'pmf numerator',pmf[:4],'moments',exact,'variance',exact[1]+exact[0]-exact[0]**2)
    print('PASS',count,'exactly enumerated (cycle partition, deletion count) cases')
if __name__=='__main__': main()
