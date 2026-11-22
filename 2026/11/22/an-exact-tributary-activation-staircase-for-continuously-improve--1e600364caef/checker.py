"""Supplementary finite numerical checks for the stated continuous-access theorem.
The symbolic proof, not this finite test, establishes the global assertion.
Run: python3 checker.py
Dependencies: Python 3 standard library only.
"""
import math
import random


def cutoffs(weights):
    assert all(a>b>0 for a,b in zip(weights, weights[1:])), weights
    out=[]
    for j in range(2,len(weights)+1):
        tail=weights[j-1]
        T=math.log(sum(weights[:j-1])/tail-(j-2))
        T+=sum(math.log(v/tail) for v in weights[:j-1])
        out.append(T)
    return out


def solve(weights,budget):
    m=len(weights)
    cuts=cutoffs(weights)
    k=1+sum(budget>t for t in cuts)
    W=sum(weights[:k])
    lower=0.0; upper=budget+2.0
    def Bofx(root):
        tau=W/(math.exp(root)+k-1)
        return root+sum(math.log(v/tau) for v in weights[:k])
    for _ in range(90):
        mid=(lower+upper)/2
        if Bofx(mid)>budget: upper=mid
        else: lower=mid
    root=(lower+upper)/2
    tau=W/(math.exp(root)+k-1)
    return (root,)+tuple(max(0.0,math.log(v/tau)) for v in weights),k,tau


def goal(x,weights):
    return -math.expm1(-x[0])*sum(v*(-math.expm1(-a)) for v,a in zip(weights,x[1:]))


def main():
    rng=random.Random(20261119)
    assertions=0
    for m in range(1,8):
        for run in range(35):
            vals=sorted([math.exp(rng.uniform(-1.7,1.7)) for _ in range(m)],reverse=True)
            for B in (0.03,0.2,1.,3.,8.,20.):
                x,k,tau=solve(vals,B)
                assert abs(sum(x)-B)<2e-10
                assertions+=1
                assert min(x)>-1e-12
                assertions+=1
                if k==1:
                    assert abs(x[0]-x[1])<1e-10
                else:
                    assert x[0]>max(x[1:])+1e-12
                assertions+=1
                assert all(x[j]>0 for j in range(1,k+1))
                assert all(x[j]<1e-12 for j in range(k+1,m+1))
                assertions+=2
                for _ in range(22):
                    v=[rng.expovariate(1) for _ in range(m+1)]
                    s=sum(v)
                    v=[B*y/s for y in v]
                    assert goal(x,vals)>=goal(v,vals)-2e-10
                    assertions+=1
    assert abs(cutoffs([9.,3.,1.])[0]-math.log(9.))<1e-12
    assert abs(cutoffs([9.,3.,1.])[1]-math.log(297.))<1e-12
    assertions+=2
    for q in (0.3,0.5,0.8):
        n=70; w=[q**j for j in range(n)]
        C=cutoffs(w)
        assert all(a<b for a,b in zip(C,C[1:]))
        assertions+=1
        for k in (3,7,15,30,55):
            L=-math.log(q)
            exact=L*(k-1)*(k+2)/2-math.log(1-q)+math.log(1-q**(k-1)*(1+(k-2)*(1-q)))
            assert abs(C[k-2]-exact)<2e-10
            assertions+=1
    print('PASS', assertions, 'supplementary checks')

if __name__=='__main__':main()
