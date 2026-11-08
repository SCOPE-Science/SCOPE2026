"""Independent finite-state and asymptotic checks for stationary Bell-pair matching laws.

Usage: python verify.py
Standard library only. No reliance on external data or simulation randomness.
"""
from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import comb, factorial, exp, lgamma, log, sqrt

checks=0

def check(condition, note):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(note)

def all_matchings(vertices):
    if not vertices:
        yield ()
        return
    x=vertices[0]
    yield from all_matchings(vertices[1:])
    for pos,y in enumerate(vertices[1:]):
        remain=vertices[1:pos+1]+vertices[pos+2:]
        for m in all_matchings(remain):
            yield tuple(sorted(((x,y),)+m))

def update(m,x,y=None):
    partner={}
    for a,b in m:
        partner[a]=b
        partner[b]=a
    edges=set(m)
    if y is None:
        if x in partner:
            edges.remove(tuple(sorted((x,partner[x]))))
    else:
        if partner.get(x)==y:
            return m
        ax=partner.get(x)
        by=partner.get(y)
        if ax is not None:
            edges.remove(tuple(sorted((x,ax))))
        if by is not None:
            edges.remove(tuple(sorted((y,by))))
        edges.add(tuple(sorted((x,y))))
        if ax is not None and by is not None:
            edges.add(tuple(sorted((ax,by))))
    return tuple(sorted(edges))

def Z(n,w):
    return sum(Fraction(factorial(n),factorial(n-2*k)*2**k*factorial(k))*w**k
               for k in range(n//2+1))

def falling(x,j):
    y=1
    for v in range(j):
        y *= x-v
    return y

for n in range(4,9):
    states=list(all_matchings(tuple(range(n))))
    check(len(states)==sum(factorial(n)//(factorial(n-2*k)*2**k*factorial(k))
                            for k in range(n//2+1)), 'matching count')
    for p in (Fraction(1,5),Fraction(2,5),Fraction(4,5)):
        w=(1-p)/(p*(n-1))
        zn=Z(n,w)
        pi={m:w**len(m)/zn for m in states}
        check(sum(pi.values())==1,'Gibbs normalization')
        kernel={m:defaultdict(Fraction) for m in states}
        for m in states:
            for x in range(n):
                kernel[m][update(m,x)]+=p/n
            for x,y in combinations(range(n),2):
                kernel[m][update(m,x,y)]+=(1-p)/comb(n,2)
            check(sum(kernel[m].values())==1,'transition normalization')
        for m in states:
            for m2,rate in kernel[m].items():
                check(pi[m]*rate==pi[m2]*kernel[m2][m], 'detailed balance')
        for a in range(1,n):
            b=n-a
            mass=defaultdict(Fraction)
            for m in states:
                crossing=sum((x<a)!=(y<a) for x,y in m)
                mass[crossing]+=pi[m]
            check(sum(mass.values())==1,'cut probability normalization')
            for j in range(min(a,b)+1):
                moment=sum(falling(s,j)*prob for s,prob in mass.items())
                theory=falling(a,j)*falling(b,j)*w**j*Z(n-2*j,w)/zn
                check(moment==theory, 'all factorial moments')
            for t in (Fraction(0),Fraction(1,3),Fraction(4,3)):
                direct=sum(prob*t**s for s,prob in mass.items())
                formula=sum(Fraction(falling(a,j)*falling(b,j),factorial(j))*
                            (w*(t-1))**j*Z(n-2*j,w)/zn for j in range(min(a,b)+1))
                check(direct==formula,'full PGF')

# Independent large-N summation over total pair counts (no finite-state enumeration).
def moments(n,p,theta):
    c=(1-p)/p
    w=c/(n-1)
    a=round(theta*n); b=n-a
    logs=[lgamma(n+1)-lgamma(n-2*k+1)-lgamma(k+1)-k*log(2)+k*log(w)
          for k in range(n//2+1)]
    mx=max(logs)
    terms=[exp(v-mx) for v in logs]
    norm=sum(terms)
    ek=sum(k*terms[k] for k in range(len(terms)))/norm
    vk=sum((k-ek)**2*terms[k] for k in range(len(terms)))/norm
    q=2*a*b/(n*(n-1))
    rr=4*a*(a-1)*b*(b-1)/(n*(n-1)*(n-2)*(n-3))
    return q*ek,(q-rr)*ek+(rr-q*q)*ek**2+rr*vk

for p in (.1,.4,.8):
    c=(1-p)/p
    u=2/(1+sqrt(1+4*c))
    rho=1-u
    for theta in (.25,.5):
        h=theta*(1-theta)
        expected_mean=rho*h
        expected_var=h*rho/(2-u)*(u+2*theta*rho)*(u+2*(1-theta)*rho)
        for n in (1000,3000,6000):
            mn,vr=moments(n,p,theta)
            check(abs(mn/n-expected_mean)<.0005,'asymptotic mean')
            check(abs(vr/n-expected_var)<.0006,'asymptotic variance')
        check(abs(expected_var/expected_mean-(u+4*h*rho**2/(2-u)))<1e-12,'Fano simplification')
        check(0<expected_var/expected_mean<1,'strict sub-Poisson coefficient')

print('PASS:',checks,'deterministic detailed-balance, PGF, moment and asymptotic assertions')
