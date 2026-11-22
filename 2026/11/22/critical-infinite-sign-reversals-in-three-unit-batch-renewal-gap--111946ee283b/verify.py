"""Independent finite arithmetic diagnostics for the 1-or-3 batch-renewal formulas.

The analytic arguments establish the infinite-index assertions; this program
checks finite identities and boundary signs only.
"""
from fractions import Fraction
from itertools import product
from math import sqrt, cos, sin, acos

checks = 0

def check(condition, description):
    global checks
    assert condition, description
    checks += 1

def renewal(q, nmax):
    u = [Fraction(1)]
    for n in range(1, nmax + 1):
        u.append(q * (u[n-1] if n >= 1 else 0) +
                 (1-q) * (u[n-3] if n >= 3 else 0))
    return u

def brute_renewal(q, target):
    # Sum the weights of all compositions of target with parts 1 or 3.
    total = Fraction(0)
    for k in range(target + 1):
        for seq in product((1, 3), repeat=k):
            if sum(seq) == target:
                total += q ** seq.count(1) * (1-q) ** seq.count(3)
    return total

def brute_joint(q, n):
    # Sum complete paths to the first passage of integer level n.
    result = Fraction(0)
    stack = [(0, Fraction(1), frozenset((0,)))]
    while stack:
        partial, mass, seen = stack.pop()
        if partial >= n:
            if n-1 in seen and n in seen:
                result += mass
            continue
        stack.append((partial+1, mass*q, seen | {partial+1}))
        stack.append((partial+3, mass*(1-q), seen | {partial+3}))
    return result

for q in (Fraction(1,5), Fraction(1,4), Fraction(1,2),
          Fraction(3,4), Fraction(9,10)):
    nmax = 65
    u = renewal(q, nmax)
    a = 1-q
    m = 3-2*q
    v = [Fraction(2), 2*q-1]
    for n in range(2, nmax+1):
        v.append(-a*(v[n-1]+v[n-2]))
    for n in range(nmax+1):
        check(u[n] == 1/m + a/m*v[n], f'partial fraction at {q}, {n}')
    for n in range(2, 11):
        check(brute_joint(q,n) == u[n-1]*q,
              f'joint gaps via direct path enumeration at {q}, {n}')
    for n in range(0, 13):
        check(brute_renewal(q,n) == u[n],
              f'renewal mass via compositions at {q}, {n}')
    for n in range(0, 50):
        check(u[n] >= 0 and u[n] <= 1, 'renewal mass range')
    theta = acos(-sqrt(float(a))/2)
    kappa = float(q)/sqrt(float(a)*(4-float(a)))
    for n in range(0, 50):
        approximation = 1/float(m)+(2*float(a)/float(m))*float(a)**(n/2)*(
            cos(n*theta)+kappa*sin(n*theta))
        check(abs(float(u[n])-approximation)<1e-12,
              f'complex root formula at {q}, {n}')

u = renewal(Fraction(1,2), 250)
signs = [1 if u[n] < Fraction(1,2) else -1 if u[n] > Fraction(1,2) else 0
         for n in range(2, 250)]
check(signs.count(1)>40 and signs.count(-1)>40,
      'finite sample shows both signs (not an infinite proof)')
for q in (Fraction(1,3), Fraction(1,2), Fraction(2,3)):
    u=[Fraction(1)]
    for n in range(1,125):
        u.append(q*u[n-1]+(1-q)*(u[n-2] if n>=2 else 0))
    for n in range(2,125):
        check(u[n] > q, f'1-or-2 strict sign at q={q}, n={n}')

print(f'PASS {checks} exact and numerical finite checks')
