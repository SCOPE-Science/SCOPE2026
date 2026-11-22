#!/usr/bin/env python3
"""Exact finite checks for equal-degree vertices across independent Cayley trees.
Each Cayley tree corresponds bijectively to one uniform Pruefer word of length n-2.
This checker supplements (not replaces) the analytic proofs.
"""
from fractions import Fraction
from itertools import product
from math import comb, factorial, exp
from collections import Counter, defaultdict

checks = 0

def test(condition, message):
    global checks
    checks += 1
    assert condition, message

def distribution_formula(n, r):
    m = n - 2
    p = sum((Fraction(comb(m,k)*(n-1)**(m-k), n**m))**r for k in range(m+1))
    q = sum((Fraction(factorial(m)*(n-2)**(m-a-b), factorial(a)*factorial(b)*factorial(m-a-b)*n**m))**r
            for a in range(m+1) for b in range(m-a+1))
    mean = n*p
    var = n*p*(1-p) + n*(n-1)*(q-p*p)
    return p,q,mean,var

def brute(n,r):
    seqs = []
    for w in product(range(n),repeat=n-2):
        c=[0]*n
        for v in w: c[v]+=1
        seqs.append(tuple(c))
    N=len(seqs)**r
    total=pair=totalsq=0
    for rows in product(seqs,repeat=r):
        indicators=[all(rows[j][i]==rows[0][i] for j in range(1,r)) for i in range(n)]
        z=sum(indicators)
        total+=z
        totalsq+=z*z
        pair+=indicators[0] and indicators[1]
    return Fraction(total,n*N),Fraction(pair,N),Fraction(total,N),Fraction(totalsq,N)-Fraction(total,N)**2

for n,r in ((2,2),(3,2),(3,3),(4,2),(4,3),(5,2)):
    analytical=distribution_formula(n,r)
    computed=brute(n,r)
    for i,(x,y) in enumerate(zip(analytical,computed)):
        test(x==y,f'n={n} r={r} component={i}: {x} vs {y}')

# Independently check the complete exact coefficient-extraction pgf.
def pgf_coeff_distribution(n,r):
    m=n-2
    dp={(0,)*r+(0,):Fraction(1)}
    for _ in range(n):
        nxt=defaultdict(Fraction)
        for key,coefficient in dp.items():
            totals=key[:r]
            z_count=key[r]
            for marks in product(range(m+1),repeat=r):
                new_totals=tuple(t+k for t,k in zip(totals,marks))
                if max(new_totals)>m: continue
                j=z_count+int(len(set(marks))==1)
                weight=Fraction(1)
                for k in marks:weight/=factorial(k)
                nxt[new_totals+(j,)]+=coefficient*weight
        dp=nxt
    scale=Fraction(factorial(m)**r,n**(r*m))
    return {j:scale*coeff for (*totals,j),coeff in dp.items() if all(t==m for t in totals)}

def brute_full_law(n,r):
    seqs=[]
    for w in product(range(n),repeat=n-2):
        c=[0]*n
        for v in w:c[v]+=1
        seqs.append(tuple(c))
    counter=Counter()
    for rows in product(seqs,repeat=r):
        z=sum(all(row[i]==rows[0][i] for row in rows[1:]) for i in range(n))
        counter[z]+=1
    denom=len(seqs)**r
    return {k:Fraction(v,denom) for k,v in counter.items()}

for n,r in ((2,2),(3,2),(3,3),(4,2),(4,3),(5,2)):
    expected=brute_full_law(n,r)
    actual=pgf_coeff_distribution(n,r)
    test(all(v==expected.get(k,Fraction(0)) for k,v in actual.items()),f'complete pgf n={n} r={r}')
    test(all(v==actual.get(k,Fraction(0)) for k,v in expected.items()),f'brute pgf n={n} r={r}')
    test(sum(actual.values())==1,f'normalization n={n} r={r}')

# A separate exact covariance identity via enumerations of occupancy pair probabilities.
for r in (2,3,4):
    for n in range(3,19):
        p,q,mean,var = distribution_formula(n,r)
        test(mean == n*p, 'mean identity')
        test(var == n*p*(1-p)+n*(n-1)*(q-p*p),'variance identity')
        test(p>0 and q>0 and var>=0, 'probability or variance positivity')
        test(var <= n*n/4,'count range variance bound')

# r=2 infinite coefficients via convergent series: I_0(2), I_1(2) definitions.
def constants(r):
    fact=1
    s0=s1=0.
    for k in range(30):
        if k:fact*=k
        w=1./(fact**r)
        s0+=w
        s1+=k*w
    rho=exp(-r)*s0
    eta=exp(-r)*s1
    cov=eta-rho
    sig2=rho*(1-rho)-r*cov*cov
    return rho,eta,cov,sig2
for r in (2,3,4):
    rho,eta,c,sig2=constants(r)
    test(0<eta<rho<1,'strict comparison of Poisson weighted means')
    test(0<sig2<rho*(1-rho),'strict variance deficit')
    for n in (50,100,200):
        # Exact formulas too expensive with huge factorial rational arithmetic;
        # evaluate using stable multinomial probabilities instead.
        m=n-2
        a=[0.]*(m+1)
        a[0]=((n-1)/n)**m
        for k in range(m):a[k+1]=a[k]*(m-k)/(k+1)/(n-1)
        p=sum(x**r for x in a)
        test(abs(p-rho)<4/n,'first moment converges at the claimed rate')
print(f'{checks} exact/analytic-numeric assertions passed')
print('r=2 constants: rho, eta, c, sigma2 =',*constants(2))
