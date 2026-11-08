#!/usr/bin/env python3
"""Recompute finite Ewens fixed-point/descent covariances by exact permutation enumeration.
No external packages or network resources are required.
"""
from fractions import Fraction as Q
from itertools import permutations
from math import prod

ASSERTIONS = 0

def check(a,b,tag):
    global ASSERTIONS
    ASSERTIONS += 1
    if a != b:
        raise AssertionError((tag,a,b))

def p(n,t):
    return Q((n-1)*(n+2*t-2),2*(t+n-1)*(t+n-2))

def cov(n,t,i,j):
    # one-indexed fixed-point i and descent at j
    q=Q(t,t+n-1)
    if i==j:
        return q*(Q(i-1,t+n-2)-p(n,t))
    if i==j+1:
        return q*(Q(n-i,t+n-2)-p(n,t))
    return -Q(t*t*(t-1),(n+t-3)*(n+t-2)*(n+t-1)**2)

def total_cov(n,t):
    return -Q(t*t*(n-1)*(n*n+2*n*t-4*n-2*t+2),
              (n+t-3)*(n+t-2)*(n+t-1)**2)

def cycles(perm):
    count=0;seen=set()
    for i in range(len(perm)):
        if i not in seen:
            count+=1;k=i
            while k not in seen:
                seen.add(k);k=perm[k]
    return count

def main():
    for n in range(3,8):
        stats=[]
        for perm in permutations(range(n)):
            fix=tuple(int(perm[i]==i) for i in range(n))
            des=tuple(int(perm[i]>perm[i+1]) for i in range(n-1))
            stats.append((cycles(perm),fix,des))
        for t in [1,2,3,4,5,6]:
            # t integer biases permit wholly integer weighted enumeration
            sumw=sum(t**c for c,f,d in stats)
            ef=[sum((t**c)*f[i] for c,f,d in stats) for i in range(n)]
            ed=[sum((t**c)*d[j] for c,f,d in stats) for j in range(n-1)]
            check(Q(sumw), Q(prod(t+k for k in range(n))),('normalizer',n,t))
            for j in range(n-1):
                check(Q(ed[j],sumw), p(n,t),('desc-marginal',n,t,j))
                for i in range(n):
                    efd=sum(t**c*f[i]*d[j] for c,f,d in stats)
                    observed=Q(efd,sumw)-Q(ef[i]*ed[j],sumw*sumw)
                    check(observed,cov(n,t,i+1,j+1),('mixed',n,t,i,j))
            global_total=sum(sum((t**c)*sum(f)*sum(d) for c,f,d in stats) for _ in [0])
            ef_total=sum(ef);ed_total=sum(ed)
            check(Q(global_total,sumw)-Q(ef_total*ed_total,sumw*sumw),total_cov(n,t),('total',n,t))
            if n>=4:
                check(total_cov(n,t)<0,True,('negative',n,t))
        # small-n theta rational cases, direct exact enumerations
        for t in [Q(1,4),Q(1,2),Q(3,2),Q(5,4)]:
            sw=sum(t**c for c,f,d in stats)
            for j in range(n-1):
                for i in range(n):
                    efd=sum(t**c*f[i]*d[j] for c,f,d in stats)
                    ef=sum(t**c*f[i] for c,f,d in stats)
                    ed=sum(t**c*d[j] for c,f,d in stats)
                    check(efd/sw-ef*ed/sw**2,cov(n,t,i+1,j+1),('rational',n,t,i,j))
    for n in range(3,40):
        for t in [Q(1,10),Q(1,4),Q(2,3),Q(1),Q(2),Q(15)]:
            for j in range(1,n):
                check(sum((cov(n,t,i,j) for i in range(1,n+1)),Q(0))*(n-1)==total_cov(n,t),True,('summing',n,t,j))
                for i in range(1,n+1):
                    if i!=j and i!=j+1:
                        check((cov(n,t,i,j)==0)==(t==1),True,('remote iff uniform',n,t,i,j))
                        check((cov(n,t,i,j)>0)==(t<1),True,('remote sign',n,t,i,j))
            expected=(n==3 and t<Q(1,4))
            check((total_cov(n,t)>0)==expected,True,('aggregate positive',n,t))
    print(f'VERIFY_OK {ASSERTIONS} exact assertions')
if __name__=='__main__':main()
