"""Reproducible finite checks for commuting partial identities in the symmetric inverse monoid.
No external dependencies; scientific content is finite checks and asymptotic diagnostics.
"""
from itertools import combinations, permutations
from math import comb, factorial, sqrt, pi, exp, log
from collections import Counter


def rook_number(n):
    return sum(comb(n,j)**2*factorial(j) for j in range(n+1))

def laguerre_integer_coeff(n):
    # n! L_n(-1): independent recurrence from Laguerre polynomial recurrence.
    r0,r1=1,2
    if n==0:return r0
    if n==1:return r1
    for k in range(1,n):
        r0,r1=r1, 2*(k+1)*r1-k*k*r0
    return r1

def partials(n):
    values=range(n)
    for k in range(n+1):
        for dom in combinations(values,k):
            for ims in permutations(values,k):
                yield dict(zip(dom,ims))

def compose(f,g):
    # (f then g)
    return {a:g[b] for a,b in f.items() if b in g}

def finite_check(n):
    seq=list(partials(n))
    assert len(seq)==rook_number(n)==laguerre_integer_coeff(n)
    by_k=Counter()
    for supp in [set(c) for k in range(n+1) for c in combinations(range(n),k)]:
        e={a:a for a in supp}
        for f in seq:
            if compose(e,f)==compose(f,e):
                by_k[len(supp)]+=1
    prediction={k: comb(n,k)*rook_number(k)*rook_number(n-k) for k in range(n+1)}
    assert dict(by_k)==prediction,(n,by_k,prediction)
    total=sum(by_k.values())
    assert total==sum(comb(n,k)*rook_number(k)*rook_number(n-k) for k in range(n+1))
    return {'n':n,'rook_size':len(seq),'commuting_pairs':total,'by_idempotent_rank':[by_k[k] for k in range(n+1)],'sample_space':(2**n)*len(seq)}

def loglag(n):
    # Stable positive Laguerre recurrence (x=-1, alpha=0); store logs via ratios.
    if n==0:return 0.0
    l0,l1=1.,2.
    scale=0.
    for k in range(1,n):
        l2=((2*k+2)*l1-k*l0)/(k+1)
        l0,l1=l1,l2
        if l1>1e120:
            l0/=1e100;l1/=1e100;scale+=100*log(10)
    return log(l1)+scale

def gaussian_check(n):
    # Conditional centered variance and predicted asymptotic counting probability.
    logs=[loglag(k)+loglag(n-k) for k in range(n+1)]
    max_log=max(logs)
    vals=[exp(x-max_log) for x in logs]
    z=sum(vals)
    variance=sum((k-n/2)**2*v for k,v in enumerate(vals))/z
    logP=log(z)+max_log - n*log(2)-loglag(n)
    approx= (-n*log(2)+2*(sqrt(2)-1)*sqrt(n)+0.5*log(n)-0.5-0.75*log(2))
    return {'n':n,'variance_over_n_to_3_2':round(variance/n**1.5,8),
            'limit_variance':round(2**-1.5,8),'probability_over_asymptotic':round(exp(logP-approx),8)}

if __name__=='__main__':
    print('Exact independent brute-force tests:')
    for n in range(0,5):print(finite_check(n))
    print('Asymptotic diagnostic only (not a proof):')
    for n in [100,400,1600,6400]:print(gaussian_check(n))
    print('ALL FINITE TESTS PASSED')
