#!/usr/bin/env python3
"""Finite exact audit of conditional sample-scatter/sign-imbalance identities.

The theorem for all sample sizes follows from the paper proof; this checker
exhaustively enumerates the declared finite probability models only.
"""
from fractions import Fraction as F
from itertools import product

CHECKS = 0

def check(assertion, why):
    global CHECKS
    CHECKS += 1
    if not assertion:
        raise AssertionError(why)

def example(n, atoms):
    # atoms = (positive magnitude, probability), with independent fair signs.
    a = sum((p*y for y,p in atoms), F())
    b = sum((p*y**2 for y,p in atoms), F())
    c = sum((p*y**3 for y,p in atoms), F())
    f = sum((p*y**4 for y,p in atoms), F())
    B = 4*a/F(n*n) * ((n-2)*(c-2*a*b+a**3) + c-a*b)
    varq = F(n-1,n) * ((n-1)*f-(n-3)*b*b)
    expvar = 2*a**4*F(n-1,n)
    assert sum(p for _,p in atoms) == 1
    grouping = {k:[F(),F(),F()] for k in range(n+1)}
    signs = [((1,y),p/2) for y,p in atoms] + [((-1,y),p/2) for y,p in atoms]
    for choices in product(signs,repeat=n):
        prob=F(1)
        values=[]
        for ((sg,y),p) in choices:
            prob *= p
            values.append(sg*y)
        k=sum(x>0 for x in values)
        q=sum(x*x for x in values)-sum(values)**2/F(n)
        g=grouping[k]
        g[0] += prob
        g[1] += prob*q
        g[2] += prob*q*q
    p_tot=F(); q_tot=F(); q2_tot=F(); projected_var=F()
    for k,(pk,pq,pq2) in grouping.items():
        t=2*k-n
        check(pk==F(__import__('math').comb(n,k),2**n), f'binomial n={n} k={k}')
        cm=pq/pk
        cv=pq2/pk-cm**2
        em=(n-1)*b+a*a*F(n-t*t,n)
        ev=varq-expvar+B*(n-t*t)
        check(cm==em, f'conditional mean n={n} k={k}: {cm}!={em}')
        check(cv==ev, f'conditional variance n={n} k={k}: {cv}!={ev}')
        check(cv>=0, f'nonnegative variance n={n} k={k}')
        p_tot+=pk
        q_tot+=pq
        q2_tot+=pq2
        projected_var+=pk*(cm-(n-1)*b)**2
    check(p_tot==1, f'probabilities sum n={n}')
    check(q_tot==(n-1)*b, f'unconditional mean n={n}')
    check(q2_tot-q_tot*q_tot==varq, f'unconditional variance n={n}')
    check(projected_var==expvar, f'explained variance n={n}')
    eta=expvar/varq
    check(eta==2*a**4/((n-1)*f-(n-3)*b*b), f'eta n={n}')
    if len(atoms)>1:
        check(B>0, f'strict conditional variance slope n={n}')
    else:
        check(B==0, f'constant magnitude zero variance slope n={n}')
    return len(grouping)

def main():
    for n in range(2,9):
        example(n, [(F(1),F(1,2)),(F(2),F(1,2))])
        example(n, [(F(3),F(1))])
    for n in range(2,6):
        example(n, [(F(1),F(1,2)),(F(2),F(1,3)),(F(4),F(1,6))])
    print('PASS:',CHECKS,'exact rational assertions; independent enumeration of',
          'the 2-, 4-, and 6-outcome iid symmetric models. Max n=8,5 respectively.')

if __name__=='__main__':main()
