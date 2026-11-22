#!/usr/bin/env python3
"""Independent exact arithmetic checks supporting the stated finite-depth formulas.
The proof of the infinite theorem is in RESULT.md; these checks test it.
"""
from math import comb, log

checks = 0

def check(predicate, detail):
    global checks
    if not predicate:
        raise AssertionError(detail)
    checks += 1

def allowed_digit(m, p, d, carry):
    return d <= (m*d + carry) % p

def legal_digits(n, p, m):
    carry = 0
    while n:
        n, d = divmod(n, p)
        check_d = (m*d+carry) % p
        if d > check_d:
            return False
        carry = (m*d+carry)//p
    return True

def direct_lucas_nondivisibility(n, p, m):
    top = m*n
    while n:
        n, d = divmod(n, p)
        top, e = divmod(top, p)
        if d > e:
            return False
    return True

def prefix_count(p, m, s, prefix, depth):
    base = p**s
    return sum(legal_digits(prefix + base*t, p, m) for t in range(p**depth))

for p in (3, 5, 7, 11, 13, 17, 19):
    a = (p+1)//2
    for m in range(2, min(p*3+3, 44)):
        if m % p in (0, 1):
            continue
        for carry in range(m):
            dset = [d for d in range(p) if allowed_digit(m,p,d,carry)]
            check(len(dset) == a, f'local branching p={p} m={m} carry={carry}')
        for r in range(0, 3):
            count = sum(legal_digits(n,p,m) for n in range(p**r))
            check(count == a**r, f'block p={p} m={m} r={r}')

for p,m,depth in ((3,2,6),(5,3,5),(7,4,4),(11,3,3),(13,9,3)):
    a=(p+1)//2
    for n in range(p**depth):
        check(legal_digits(n,p,m)==direct_lucas_nondivisibility(n,p,m), ('Lucas',p,m,n))
    for r in range(depth+1):
        check(sum(legal_digits(n,p,m) for n in range(p**r))==a**r, ('full-depth',p,m,r))
    for s in range(1,min(depth,3)):
        for prefix in range(p**s):
            legal=legal_digits(prefix,p,m)
            if not legal:
                continue
            for r in range(0,min(3,depth-s)+1):
                check(prefix_count(p,m,s,prefix,r)==a**r,('suffix',p,m,s,prefix,r))

for p,m in ((3,2),(5,3),(7,4),(11,3)):
    for n in range(70):
        check((comb(m*n,n)%p!=0)==legal_digits(n,p,m),('binomial',p,m,n))

for p in (3,5,7,11):
    for r in range(1,4):
        check(sum(legal_digits(n,p,p) for n in range(p**r))==1,('boundary m=0',p,r))
        check(sum(legal_digits(n,p,p+1) for n in range(p))==p,('boundary m=1',p))

print(f'VERIFY_OK {checks} exact assertions')
