#!/usr/bin/env python3
"""Independent exact first-hit series checks and numerical sign tests.

No external dependencies. Run `python3 checker.py`.
Finite tests corroborate, but do not establish, the universal theorem.
"""
from itertools import product
from collections import defaultdict
from fractions import Fraction
from math import isfinite


def borders(word):
    n = len(word)
    return [(j, word[:j].count('1')) for j in range(1, n + 1)
            if word[:j] == word[-j:]]


def first_hit_table(word, limit):
    n = len(word)
    transitions = []
    for state in range(n):
        row = []
        for symbol in '01':
            s = word[:state] + symbol
            row.append(max(i for i in range(n+1) if s.endswith(word[:i])))
        transitions.append(row)
    current = {(0, 0): 1}
    hits = [defaultdict(int) for _ in range(limit+1)]
    for length in range(1, limit + 1):
        following = defaultdict(int)
        for (state, ones), count in current.items():
            for digit, successor in enumerate(transitions[state]):
                if successor == n:
                    hits[length][ones+digit] += count
                else:
                    following[(successor, ones+digit)] += count
        current = following
    return hits


def formal_series_identity(word, limit):
    # Phi = x^k y^a / D(x,y), with
    # D = x^k y^a + C - x(1+y) C / 2,
    # C = sum_{b border} 2^b x^(k-b) y^(a-ones(prefix b)).
    k = len(word); a = word.count('1')
    poly = defaultdict(Fraction)
    poly[(k, a)] += 1
    for b, j in borders(word):
        term = Fraction(2**b)
        deg_x, deg_y = k-b, a-j
        poly[(deg_x, deg_y)] += term
        poly[(deg_x+1, deg_y)] -= term/2
        poly[(deg_x+1, deg_y+1)] -= term/2
    dist = first_hit_table(word, limit)
    phi = [defaultdict(Fraction) for _ in range(limit+1)]
    for i in range(1, limit+1):
        for j, count in dist[i].items():
            phi[i][j] = Fraction(count, 2**i)
    for n in range(limit+1):
        left = defaultdict(Fraction)
        for (dx,dy), coefficient in poly.items():
            if dx > n: continue
            for jy, mass in phi[n-dx].items():
                left[dy+jy] += coefficient*mass
        rhs = {a:Fraction(1)} if n==k else {}
        assert {i:v for i,v in left.items() if v} == rhs,(word,n,left,rhs)


def q_integral_simpson(word, steps=1200):
    bd=borders(word)
    def integrand(z):
        if z<=0.: return (2*bd[0][1]-1)/2 if len(word)==1 else 0.
        if z>=1.: return 0.
        X=2/z
        C=sum(X**b for b,j in bd)
        H=sum((2*j-b)*X**b for b,j in bd)
        return (1-z)*H/(z*(1+(1-z)*C)**2)
    h=1/steps
    total=integrand(0.)+integrand(1.)
    for i in range(1,steps):
        total += (4 if i%2 else 2)*integrand(i*h)
    return 0.5 + (h*total/3)/2


def q_from_first_hits(word, limit=1200):
    # Marginalized integer-state recurrence avoids enumeration of 2^n words.
    k=len(word); transitions=[]
    for state in range(k):
        row=[]
        for a in '01':
            u=word[:state]+a
            row.append(max(h for h in range(k+1) if u.endswith(word[:h])))
        transitions.append(row)
    counts=[0]*k; ones=[0]*k; counts[0]=1
    q=0.
    for n in range(1,limit+1):
        newc=[0]*k; newo=[0]*k; hit_ones=0
        for s in range(k):
            for bit,nxt in enumerate(transitions[s]):
                if nxt==k: hit_ones += ones[s]+bit*counts[s]
                else:
                    newc[nxt]+=counts[s]; newo[nxt]+=ones[s]+bit*counts[s]
        q += hit_ones/(n*(2**n))
        counts,ones=newc,newo
    residual=sum(counts)/(2**limit)
    return q,residual


def run():
    exact_cases=0
    for k in range(1,7):
        for tup in product('01',repeat=k):
            formal_series_identity(''.join(tup),13)
            exact_cases+=1
    print('Exact bivariate first-hit generating-function identities:', exact_cases,
          'patterns, lengths 0..13')
    sign_cases=0; min_margin=1.
    for k in range(1,11):
        for tup in product('01',repeat=k):
            w=''.join(tup)
            d=next((2*j-b for b,j in reversed(borders(w)) if 2*j!=b),0)
            q=q_integral_simpson(w)
            assert isfinite(q)
            if d==0: assert abs(q-.5)<1e-10,(w,q)
            else:
                assert (q>.5) == (d>0),(w,d,q)
                min_margin=min(min_margin,abs(q-.5))
            sign_cases+=1
    print('Integral sign classifications:',sign_cases,'patterns; minimum nonzero margin',min_margin)
    for word in ('0','1','00','11','01','10','010','101','0110','1001','10001'):
        q=q_integral_simpson(word, steps=4800)
        approx, residual=q_from_first_hits(word,1600)
        assert abs(q-approx) <= residual+2e-9,(word,q,approx,residual)
        print(word, 'integral',f'{q:.12f}','direct first-hit',f'{approx:.12f}', 'residual',f'{residual:.2e}')
    print('PASS')

if __name__=='__main__':run()
