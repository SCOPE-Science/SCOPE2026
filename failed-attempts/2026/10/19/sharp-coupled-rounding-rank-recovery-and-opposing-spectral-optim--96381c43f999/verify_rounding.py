"""Independent exact checks of coupled binary stochastic-rounding rank laws.
Requires only Python 3 standard library. Execute: python3 verify_rounding.py
"""
from fractions import Fraction as Q
from math import factorial
from itertools import product


def success_formula(n, p, q):
    a=1-2*p+q
    return 1 -2*(1-p)**n -(a+q)**n +2*a**n


def success_enumerate(n,p,q):
    a,b,c,d=1-2*p+q,p-q,p-q,q
    assert min(a,b,c,d)>=0 and a+b+c+d==1
    s=Q(0)
    for i in range(n+1):
        for j in range(n-i+1):
            for k in range(n-i-j+1):
                ell=n-i-j-k
                # counts: 00, 10, 01, 11
                if sum(x>0 for x in (j,k,ell))>=2:
                    s+=Q(factorial(n),factorial(i)*factorial(j)*factorial(k)*factorial(ell))*a**i*b**j*c**k*d**ell
    return s

checks=0
for n in range(2,9):
    for p in [Q(1,10), Q(1,4),Q(1,3),Q(1,2),Q(2,3),Q(3,4),Q(9,10)]:
        qmin=max(Q(0),2*p-1)
        for q in sorted(set([qmin,(qmin+p)/2,p,p*p])):
            assert qmin<=q<=p
            f=success_formula(n,p,q)
            exact=success_enumerate(n,p,q)
            assert f==exact, (n,p,q,f,exact)
            checks+=1
        assert success_formula(n,p,qmin)>success_formula(n,p,p*p) if qmin<p*p else True
    # overall optimizer at p=2/3
    assert success_formula(n,Q(2,3),Q(1,3)) == 1-Q(3)**(1-n)
    assert success_formula(n,Q(1,2),Q(0)) == 1-Q(2)**(1-n)
    assert success_formula(n,Q(2,3),Q(4,9)) == 1-2*Q(3)**(-n)-Q(5,9)**n+2*Q(9)**(-n)
    checks+=3
print('EXACT_COUNTS_CHECKED',checks)
print('GLOBAL_OPT_SUCCESS_n8',success_formula(8,Q(2,3),Q(1,3)))
print('INDEPENDENT_SUCCESS_n8',success_formula(8,Q(2,3),Q(4,9)))
print('MIN_SINGULAR_LIMIT_OPT', 'p=1/2,q=0, squared limit 1/2')
print('RANK_OPT_LIMIT','p=2/3,q=1/3, squared limit 1/3')
print('VERIFY_OK')
