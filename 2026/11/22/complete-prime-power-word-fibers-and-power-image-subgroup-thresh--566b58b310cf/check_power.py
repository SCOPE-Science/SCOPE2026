#!/usr/bin/env python3
"""Direct finite-group power checker for the power-image theorem.
Uses actual semidirect-product multiplication, not polynomial ranks.
No external dependencies.
"""
from collections import Counter, defaultdict
from itertools import product

def add(a,b,p,f):
    if f == 1: return (a+b)%p
    out,place=0,1
    for _ in range(f):
        out+=((a%p+b%p)%p)*place
        a//=p;b//=p;place*=p
    return out

def mul(x,y,n,p,f):
    a,i=x;b,j=y
    return tuple(add(a[t],b[(t-i)%n],p,f) for t in range(n)),(i+j)%n

def group_power(x,k,n,p,f):
    out=((0,)*n,0)
    for _ in range(k):out=mul(out,x,n,p,f)
    return out

def n_transform(v,m,n,p,f):
    # (T-I)^m, where T v has component r equal to v_(r-1)
    for _ in range(m):
        v=tuple(add(v[(t-1)%n],(-v[t])%p if f==1 else negate(v[t],p,f),p,f) for t in range(n))
    return v

def negate(a,p,f):
    if f==1:return -a%p
    out,place=0,1
    for _ in range(f):out+=(-a%p)*place;a//=p;place*=p
    return out

def image_N(m,n,p,f):
    q=p**f
    return {n_transform(v,m,n,p,f) for v in product(range(q),repeat=n)}

def formula(p,f,a,b):
    n=p**a;q=p**f;k=p**b
    if b>a:return {(0,)*n: {(0,): 0}} # unused
    d=defaultdict(dict)
    for j in range(n):
        if j and j%k:continue
        if j:
            s=0;t=j
            while t%p==0:s+=1;t//=p
            m=p**(s-b)*(k-1)
        else:m=n-p**(a-b)
        d[j]=(m, image_N(m,n,p,f))
    return d

def test(p,f,a,bs):
    n=p**a;q=p**f
    bases=list(product(range(q),repeat=n))
    elements=[(v,i) for v in bases for i in range(n)]
    for b in bs:
        k=p**b
        actual=Counter(group_power(x,k,n,p,f) for x in elements)
        expect={}
        if b>a:
            expect[((0,)*n,0)]=len(elements)
        else:
            for j,(m,im) in formula(p,f,a,b).items():
                for w in im:
                    if j:
                        cnt=p**b*q**m
                    elif w!=(0,)*n:
                        cnt=(p**b-p**(b-1))*q**m
                    else:
                        cnt=(p**b-p**(b-1))*q**m+p**(b-1)*q**n
                    expect[(w,j)]=cnt
        assert actual==expect,(p,f,a,b,len(actual),len(expect),[(x,actual[x],expect.get(x)) for x in actual if actual[x]!=expect.get(x)][:4])
        if b<=a:
            predicted=q**(p**(a-b))+sum((p-1)*p**(a-s-1)*q**(n-p**(s-b)*(p**b-1)) for s in range(b,a))
            assert len(actual)==predicted,(p,f,a,b,len(actual),predicted)
        print('PASS',p,f,a,'b',b,'group',len(elements),'image',len(actual),'root sum',sum(actual.values()))

if __name__=='__main__':
    test(2,1,1,[1,2,3])
    test(2,1,2,[1,2,3])
    test(2,1,3,[1,2,3,4])
    test(2,2,1,[1,2])
    test(2,2,2,[1,2,3])
    test(3,1,1,[1,2,3])
    test(3,2,1,[1,2])
    test(5,1,1,[1,2])
    print('ALL_DIRECT_CHECKS_PASS')
