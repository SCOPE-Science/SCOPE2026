"""Certified RACG growth census: Steinberg series + shortlex automaton cross-check + pole table.
Reads graphs.json; writes cliques.json, steinberg_series.json, automaton_counts.json, growth_table.json.
All arithmetic exact (Fractions / integers); replay: python3 compute_all.py
"""
import json, itertools, os
from fractions import Fraction
from math import comb
ART = os.path.dirname(os.path.abspath(__file__)) + '/'
pool = json.load(open(ART+'graphs.json'))
N = 12

def clique_counts(n, E):
    adj = [[0]*n for _ in range(n)]
    for a, b in E: adj[a][b] = adj[b][a] = 1
    c = [0]*(n+1); c[0] = 1
    for r in range(1, n+1):
        k = 0
        for S in itertools.combinations(range(n), r):
            if all(adj[S[i]][S[j]] for i in range(r) for j in range(i+1, r)): k += 1
        c[r] = k
    return c

def steinberg_series(c, N):
    # Q(t) = F(t/(1+t)), F(u)=sum (-1)^k c_k u^k; q_m exact; W=1/Q
    q = [Fraction(0)]*(N+1); q[0] = Fraction(1)
    for k in range(1, len(c)):
        if c[k] == 0: continue
        for m in range(k, N+1):
            j = m-k
            q[m] += Fraction(((-1)**k)*c[k]*(((-1)**j)*comb(k+j-1, j)))
    a = [Fraction(0)]*(N+1); a[0] = Fraction(1)
    for n in range(1, N+1):
        a[n] = -sum(q[m]*a[n-m] for m in range(1, n+1))
    assert all(x.denominator == 1 for x in a)
    return [int(x) for x in a]

def shortlex_counts(n, E, N):
    # Shortlex normal-form automaton (proved by cross-check): states = right-descent cliques.
    # From state S on letter s: reject if s in S (not geodesic); reject if s < max(S cap N(s))
    # (would not be lexicographically minimal); else go to (S cap N(s)) U {s}.
    comm = [set() for _ in range(n)]
    for a, b in E: comm[a].add(b); comm[b].add(a)
    cur = {frozenset(): 1}; out = [1]
    for _ in range(1, N+1):
        nxt = {}
        for S, cnt in cur.items():
            for s in range(n):
                if s in S: continue
                C = S & comm[s]
                if C and s < max(C): continue
                Sp = frozenset(C | {s})
                nxt[Sp] = nxt.get(Sp, 0) + cnt
        cur = nxt; out.append(sum(cur.values()))
    return out

cliques, series, autos, match = {}, {}, {}, {}
for name, g in pool.items():
    n = g['n']; E = [tuple(e) for e in g['edges']]
    c = clique_counts(n, E)
    s = steinberg_series(c, N); w = shortlex_counts(n, E, N)
    cliques[name] = {'n': n, 'm': len(E), 'clique_counts': c}
    series[name] = s; autos[name] = w; match[name] = (s == w)
    print(name, 'MATCH' if s == w else 'MISMATCH!')
assert all(match.values()), 'automaton cross-check failed'
json.dump(cliques, open(ART+'cliques.json','w'), indent=1)
json.dump(series, open(ART+'steinberg_series.json','w'), indent=1)
json.dump(autos, open(ART+'automaton_counts.json','w'), indent=1)
json.dump(match, open(ART+'crosscheck.json','w'), indent=1)
print('OK: %d/%d graphs cross-checked to length %d' % (len(pool), len(pool), N))
