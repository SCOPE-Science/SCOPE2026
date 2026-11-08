#!/usr/bin/env python3
"""Finite independent tests for leaf-count asymptotics in polynomial aggregation trees.

The accompanying mathematical proof, not finite testing, establishes the limit theorem.
Uses only the Python standard library.
"""
from fractions import Fraction as F
import itertools
import math

CHECKS = 0

def check(cond, message):
    global CHECKS
    CHECKS += 1
    if not cond:
        raise AssertionError(message)

def distribution_via_leaf_chain(n, beta):
    weights = {1:F(1)}
    for j in range(1,n):
        q=F(j,n)**beta
        nxt={}
        for leaves,prob in weights.items():
            p=q*(1-F(leaves,j))
            nxt[leaves]=nxt.get(leaves,F(0))+prob*(1-p)
            nxt[leaves+1]=nxt.get(leaves+1,F(0))+prob*p
        weights=nxt
    return {k:v for k,v in weights.items() if v}

def distribution_via_parent_choices(n,beta):
    # Enumerate every rooted increasing labelled parent-list, independent of leaf chain.
    outcome={}
    for parents in itertools.product(*(range(1,j+1) for j in range(1,n))):
        probability=F(1)
        children=[0]*(n+1)
        for j,parent in enumerate(parents,start=1):
            q=F(j,n)**beta
            chance=q/j + (1-q if parent==j else 0)
            probability*=chance
            children[parent]+=1
        leaves=sum(k==0 for k in children[1:])
        outcome[leaves]=outcome.get(leaves,F(0))+probability
    return {k:v for k,v in outcome.items() if v}

def moments_exact(n,beta):
    mean=F(1);sq=F(1)
    for j in range(1,n):
        q=F(j,n)**beta
        new_sq=(1-2*q/j)*sq+q*((2-F(1,j))*mean+1)
        mean=(1-q/j)*mean+q
        sq=new_sq
    return mean,sq-mean*mean

def limiting(beta,mesh=20000):
    h=1/mesh;integral=0.;x=[0.]
    last=0.
    for k in range(1,mesh+1):
        t=k*h
        now=t**beta*math.exp(t**beta/beta)
        integral+=(now+last)*h/2
        x.append(math.exp(-t**beta/beta)*integral)
        last=now
    prev=0.;variance=0.
    for k in range(1,mesh+1):
        t=k*h
        p=t**beta*(1-x[k]/t)
        g=math.exp(-2*(1-t**beta)/beta)*p*(1-p)
        variance+=h*(prev+g)/2
        prev=g
    return x[-1],variance

for beta in (0,1,2):
    for n in range(2,8):
        d=distribution_via_leaf_chain(n,beta)
        e=distribution_via_parent_choices(n,beta)
        check(d==e, f'parent enumeration vs leaf recursion: n={n}, beta={beta}')
        check(sum(d.values())==1, f'normalization: n={n}, beta={beta}')
        m,v=moments_exact(n,beta)
        check(m==sum(F(k)*p for k,p in d.items()),'mean mismatch')
        check(v==sum(F(k*k)*p for k,p in d.items())-m*m,'variance mismatch')

# At the beta=1 benchmark, compare the complete leaf law with
# independent Prüfer-word enumeration of uniform labelled trees.
for n in range(3,7):
    histogram={}
    for word in itertools.product(range(1,n+1),repeat=n-2):
        leaves=sum(k not in word for k in range(2,n+1))
        histogram[leaves]=histogram.get(leaves,0)+1
    cayley={k:F(v,n**(n-2)) for k,v in histogram.items()}
    check(distribution_via_leaf_chain(n,1)==cayley, 'Cayley distribution from Prüfer words')

for n in range(3,65):
    m,v=moments_exact(n,0)
    check(m==F(n,2),'recursive-tree mean')
    check(v==F(n,12),'recursive-tree variance')
    m1,v1=moments_exact(n,1)
    a=F(n-1,n)**(n-2)
    b=F(n-2,n)**(n-2)
    em=(n-1)*a
    ev=(n-1)*a*(1-a)+(n-1)*(n-2)*(b-a*a)
    check(m1==em,'Cayley mean from absent Prüfer labels')
    check(v1==ev,'Cayley variance from absent Prüfer labels')

for beta in (0.5,1.0,2.0,3.0):
    mlim,vlim=limiting(beta)
    for n in (1000,5000):
        m,v=(None,None)
        if m is None:
            # Independent floating recurrence for half-integer beta.
            m=1.; s=1.
            for j in range(1,n):
                q=(j/n)**beta
                s=(1-2*q/j)*s+q*((2-1/j)*m+1)
                m=(1-q/j)*m+q
            v=s-m*m
        check(abs(float(m)/n-mlim)<0.002,'finite-to-limit mean')
        check(abs(float(v)/n-vlim)<0.002,'finite-to-limit variance')

m,v=limiting(1.0)
check(abs(m-1/math.e)<2e-8,'closed form beta=1 mean')
check(abs(v-(math.e-2)/math.e**2)<2e-8,'closed form beta=1 variance')
check(v>1/12,'nonmonotone fluctuation benchmark')
print('PASS:',CHECKS,'independent exact and numerical assertions')
