#!/usr/bin/env python3
"""Independent small-carrier verification of an S5 bounded-morphism retraction census.
Uses only the Python standard library. Invoke: python3 checker.py
"""
from itertools import product
from math import comb, factorial

def parts(n):
    if n==0:
        yield []
    else:
        for ps in parts(n-1):
            for i in range(len(ps)):
                q=[x[:] for x in ps];q[i].append(n-1);yield q
            yield [x[:] for x in ps]+[[n-1]]

def onto(n,k):
    return sum((-1)**j*comb(k,j)*(k-j)**n for j in range(k+1))

def formula(sizes):
    k=len(sizes); ans=0
    for mask in range(1,1<<k):
        val=1
        for i,ni in enumerate(sizes):
            if mask>>i&1:continue
            val*=sum(onto(ni,nj) for j,nj in enumerate(sizes) if (mask>>j&1) and nj<=ni)
        ans+=val
    return ans

def direct(ps):
    n=sum(map(len,ps));cls=[None]*n
    for i,b in enumerate(ps):
        for x in b:cls[x]=i
    target=[set(b) for b in ps];found=0;images=set()
    for f in product(range(n),repeat=n):
        if any(f[f[x]]!=f[x] for x in range(n)):continue
        if any({f[x] for x in b} not in target for b in ps): continue
        # Relation forth/back independent check, no use of formula/characterization
        if any(((cls[x]==cls[y])!=(False)) and cls[f[x]]!=cls[f[y]] for x in range(n) for y in range(n) if cls[x]==cls[y]): continue
        if any(any(cls[f[x]]==cls[z] and all(f[y]!=z for y in ps[cls[x]]) for z in range(n)) for x in range(n)): continue
        found+=1;images.add(tuple(sorted(set(f))))
    return found,len(images)

if __name__=='__main__':
    tests=0
    for n in range(1,6):
        for ps in parts(n):
            exact,imgs=direct(ps)
            sizes=[len(b) for b in ps]
            expected=formula(sizes)
            mins=sum(x==min(sizes) for x in sizes)
            predicted_images=2**len(sizes)-2**(len(sizes)-mins)
            assert (exact,imgs)==(expected,predicted_images), (ps,exact,imgs,expected,predicted_images)
            tests+=1
        print(f'n={n}: all {tests} cumulative partitions checked')
    for s in range(1,5):
        for k in range(1,8):
            sizes=[s]*k
            expected=sum(comb(k,r)*(r*factorial(s))**(k-r) for r in range(1,k+1))
            assert formula(sizes)==expected
    print('ALL_CHECKS_OK')

# Independent formal-power-series verification of the labelled assembly formula.
from fractions import Fraction

def mul(a,b,N):
    return [sum((a[j]*b[i-j] for j in range(i+1)),Fraction()) for i in range(N+1)]

def exp_series(a,N):
    assert a[0]==0
    b=[Fraction(1)]+[Fraction()]*N
    for i in range(1,N+1):
        b[i]=sum((j*a[j]*b[i-j] for j in range(1,i+1)),Fraction())/i
    return b

def census_series(N):
    # u=exp(z)-1; B=sum_t z^t/t! exp(u^t); A=exp(B).
    u=[Fraction(0)]+[Fraction(1,factorial(i)) for i in range(1,N+1)]
    power=[Fraction(1)]+[Fraction()]*N
    B=[Fraction()]*(N+1)
    for t in range(1,N+1):
        power=mul(power,u,N)
        e=exp_series(power,N)
        for i in range(t,N+1):B[i]+=e[i-t]/factorial(t)
    A=exp_series(B,N)
    return [int(A[i]*factorial(i)) for i in range(N+1)]

if __name__=='__main__':
    vals=census_series(7)
    expected=[1]+[sum(formula([len(x) for x in p]) for p in parts(n)) for n in range(1,8)]
    assert vals==expected,(vals,expected)
    print('LABELED_CENSUS',vals,'ALL_SERIES_CHECKS_OK')
