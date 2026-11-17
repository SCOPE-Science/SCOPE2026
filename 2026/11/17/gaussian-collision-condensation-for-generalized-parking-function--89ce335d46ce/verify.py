#!/usr/bin/env python3
"""Reproducible finite checks for Euclidean normal-cone collision laws of generalized parking-function polytopes."""
import itertools
import collections
import math


def vertices(b):
    n = len(b)
    s=[]; v=0
    for a in b:
        v+=a; s.append(v)
    result=set()
    for k in range(n+1):
        original=(1,)*k+tuple(s[k:])
        result.update(itertools.permutations(original))
    return sorted(result)


def exposed_prediction(c,b):
    n=len(b)
    rank=sorted(range(n),key=lambda i:c[i])
    s=[];v=0
    for a in b:
        v+=a;s.append(v)
    k=sum(t<0 for t in c)
    if b[0]==1 and k==0: k=1
    w=[None]*n
    for rank_index,i in enumerate(rank):
        w[i]=1 if rank_index<k else s[rank_index]
    return tuple(w)


def gaussian_chambers(n):
    for p in itertools.permutations(range(1,n+1)):
        for signs in itertools.product([-1,1],repeat=n):
            yield tuple(a*s for a,s in zip(p,signs))


def check_finite(n,b):
    vv=vertices(b)
    count=collections.Counter()
    for c in gaussian_chambers(n):
        guess=exposed_prediction(c,b)
        assert guess in vv, (n,b,c,guess)
        maxdot=max(sum(a*y for a,y in zip(c,x)) for x in vv)
        assert sum(a*y for a,y in zip(c,guess))==maxdot,(n,b,c,guess,maxdot)
        assert sum(sum(a*y for a,y in zip(c,x))==maxdot for x in vv)==1,(n,b,c)
        count[guess]+=1
    assert len(count)==len(vv),(n,b,len(count),len(vv))
    size=(1<<n)*math.factorial(n)
    coll_num=sum(a*a for a in count.values())
    expected_base=sum(math.comb(n,j)/math.factorial(j) for j in range(n+1))
    # Check the combinatorial probabilities by exact integer cross multiplication.
    for vertex,ct in count.items():
        j=sum(v>1 for v in vertex)
        if b[0]==1 and j==n-1:
            assert ct*math.factorial(n)==size*(n+1)//(1<<n),(n,b,ct,j)
        else:
            assert ct*math.factorial(j)==math.factorial(n),(n,b,ct,j)
    # For b1>=2, n!*2^n chambers count at vertex j is n!/j!;
    # when b1=1, the merged top orbit (j=n-1) has (n+1) chambers.
    if b[0]>=2:
        predicted_num=sum((math.factorial(n)//math.factorial(n-j))*(math.factorial(n)//math.factorial(j))**2 for j in range(n+1))
        assert coll_num==predicted_num, (n,b,coll_num,predicted_num)
    else:
        pred=0
        for j in range(n-1):
            multiplicity=math.factorial(n)//math.factorial(n-j)
            pred+=multiplicity*(math.factorial(n)//math.factorial(j))**2
        pred+=math.factorial(n)*(n+1)**2
        assert pred==coll_num,(n,b,coll_num,pred)
    for r in (2, 3, 4):
        observed=sum(t**r for t in count.values())
        predicted=sum((math.factorial(n)//math.factorial(n-j))*(math.factorial(n)//math.factorial(j))**r for j in range(n+1))
        if b[0]==1:
            predicted+=((n+1)**r-n**r-1)*math.factorial(n)
        assert observed==predicted,(n,b,r,observed,predicted)
    return len(vv),len(count),size,coll_num/(size*size)


def logsumexp(vals):
    m=max(vals)
    return m+math.log(sum(math.exp(v-m) for v in vals))


def stats(n):
    # Stable exact-sum log weights w_j = binom(n,j)/j!.
    logw=[math.lgamma(n+1)-math.lgamma(n-j+1)-2*math.lgamma(j+1) for j in range(n+1)]
    s=logsumexp(logw)
    weights=[math.exp(w-s) for w in logw]
    mean=sum(j*p for j,p in enumerate(weights))
    var=sum((j-mean)**2*p for j,p in enumerate(weights))
    asym=2*math.sqrt(n)-0.5-math.log(2*math.sqrt(math.pi))-0.25*math.log(n)
    return mean,var,math.exp(s-asym),s


def multi_collision_ratio(n,r):
    x=n**(1/r)
    logw=[math.lgamma(n+1)-math.lgamma(n-j+1)-r*math.lgamma(j+1) for j in range(n+1)]
    s=logsumexp(logw)
    asym=r*x+(1-r)/2*math.log(2*math.pi*x)-math.log(r)/2-(0.5 if r==2 else 0)
    ww=[math.exp(v-s) for v in logw]
    mean=sum(j*v for j,v in enumerate(ww))
    var=sum((j-mean)**2*v for j,v in enumerate(ww))
    return math.exp(s-asym),mean/x,var/x


def main():
    cases=0
    for n in range(2,6):
        for b in [(1,)*n,(2,)*n,tuple(range(1,n+1))]:
            v,seen,chambers,col=check_finite(n,b)
            cases+=1
            print('FINITE_PASS',n,b,'vertices',v,'chambers',chambers,'collision',f'{col:.12g}')
    for n in (100,400,1600,6400):
        mean,var,ratio,s=stats(n)
        print('ASYMPTOTIC_CHECK',n,'mean/sqrt_n',round(mean/math.sqrt(n),8),
              'var/sqrt_n',round(var/math.sqrt(n),8),'Laguerre_ratio',round(ratio,8))
    for r in (3,4):
        for n in (100,400,1600,6400):
            ratio,mean,var=multi_collision_ratio(n,r)
            print('MULTI_COLLISION_ASYMPTOTIC_CHECK',r,n,'ratio',round(ratio,8),'mean/rank',round(mean,8),'var/rank',round(var,8))
    print('PARKING_ANGULAR_COLLISION_PASS finite_cases='+str(cases)+' exponents=2,3,4')

if __name__=='__main__':main()
