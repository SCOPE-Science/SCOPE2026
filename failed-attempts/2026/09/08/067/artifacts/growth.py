#!/usr/bin/env python3
"""Step 3: certified word-metric growth balls for three infinite candidates.

G1 = <a,b | a^2, b^3> ~= Z2 * Z3 (PSL(2,Z)); G2 = <a,b | a^2, b^4> ~= Z2*Z4;
G3 = <a,b | a^3, b^3> ~= Z3*Z3. Each maps onto the stated free product (drop no
relations), hence infiniteness is certified by the normal-form argument, and
the group word metric dominates the free-product word metric. We compute exact
word-metric balls in the FREE PRODUCT (lower bounds for the group balls) by BFS
over normal forms, with exact counts and an exponential lower bound fit.

Note: BFS over normal forms in generators {a,A,b,B} with reductions a^2=1 etc.
gives exact free-product balls. Since G_i surjects onto the free product by
removing... actually G_i EQUALS the free product here (these two-relator
presentations are exactly the free-product presentations), so the balls are exact
for G_i itself, not just lower bounds. Normal forms: alternating syllables from
C_m \\ {1} and C_n \\ {1}.

Output: output/artifacts/growth_{g1,g2,g3}.json
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))

def free_product_ball(m, n, R):
    """BFS on normal forms of C_m * C_n. State: tuple of syllables.
    Syllable: ('a', k) with 1<=k<m, or ('b', k) with 1<=k<n.
    Generators act by multiplying the exposed syllable."""
    # identity = ()
    from collections import deque
    seen = {(): 0}
    q = deque([()])
    dist_count = {}
    while q:
        s = q.popleft()
        d = seen[s]
        dist_count[d] = dist_count.get(d, 0) + 1
        if d == R:
            continue
        for gen in (('a', 1), ('a', m - 1), ('b', 1), ('b', n - 1)):
            ns = mult(s, gen, m, n)
            if ns not in seen:
                seen[ns] = d + 1
                q.append(ns)
    balls = []
    c = 0
    for d in range(R + 1):
        c += dist_count.get(d, 0)
        balls.append(c)
    return dist_count, balls

def mult(s, gen, m, n):
    g, k = gen
    if not s:
        return ((g, k % (m if g == 'a' else n)),)
    lg, lk = s[-1]
    if lg == g:
        mod = m if g == 'a' else n
        nk = (lk + k) % mod
        if nk == 0:
            return s[:-1]
        return s[:-1] + ((g, nk),)
    return s + ((g, k),)

def exp_fit(balls):
    """Find largest integer c>=2 and offset d with balls[n] >= c^n - d... simpler:
    report ratios and certify balls[n] >= 2^n + 1 statement check."""
    return {n: b for n, b in enumerate(balls)}

CASES = {'g1': (2, 3, 'AA', 'BBB'), 'g2': (2, 4, 'AA', 'BBBB'), 'g3': (3, 3, 'AAA', 'BBB')}
R = 12

for name, (m, n, w1, w2) in CASES.items():
    dist, balls = free_product_ball(m, n, R)
    # Certified per-case exponential lower bounds (checked against exact balls):
    #  g3 = Z3*Z3: spheres double from radius 2 -> |B_n| >= 2^n + 5 (1<=n<=12).
    #  g1 = Z2*Z3: spheres satisfy s_{2k}=2^{k+1}, s_{2k+1}=3*2^k -> |B_n| >= (3/2)^n + 1.
    #  g2 = Z2*Z4: spheres are Fibonacci-like (s_{n}+s_{n+1} growth, ratio->phi) -> |B_n| >= phi^n.
    import math
    if name == 'g3':
        lb = [2 ** k + 1 for k in range(R + 1)]
        claim = '|B_n| >= 2^n+1 for 2<=n<=12 (and |B_1|=5)'
    elif name == 'g1':
        lb = [math.floor(1.5 ** k) + 1 for k in range(R + 1)]
        claim = '|B_n| >= floor((3/2)^n)+1 for 1<=n<=12'
    else:
        phi = (1 + math.sqrt(5)) / 2
        lb = [math.floor(phi ** k) + 1 for k in range(R + 1)]
        claim = '|B_n| >= floor(phi^n)+1 for 1<=n<=12'
    lb[0] = 1
    holds = all(b >= l for b, l in zip(balls, lb))
    ratios = [round(balls[k + 1] / balls[k], 4) for k in range(1, R)]
    rec = {'group': f'<a,b|{w1},{w2}>', 'free_product': f'Z{m}*Z{n}',
           'radius': R, 'sphere_sizes': [dist.get(k, 0) for k in range(R + 1)],
           'ball_sizes': balls,
           'lower_bound_claim': claim,
           'lower_bound_values': lb,
           'lower_bound_holds': holds,
           'successive_ratios': ratios,
           'method': 'exact BFS over alternating normal forms in generators a,A,b,B; '
                     'presentation equals the free product, so balls are exact group balls'}
    with open(os.path.join(HERE, f'growth_{name}.json'), 'w') as f:
        json.dump(rec, f, indent=1)
    print(name, rec['group'], 'balls:', balls, claim, holds)
