"""Independent verifier: replays everything from committed edge lists only."""
import json, sys
from fractions import Fraction
from itertools import combinations

ART = '/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-258/output/artifacts'
R = json.load(open(ART + '/results.json'))
S = json.load(open(ART + '/sturm.json'))
ok = []


def check(name, cond):
  assert cond, 'FAIL ' + name
  ok.append(name)


def padd(a, b):
  c = dict(a)
  for k, v in b.items():
    c[k] = c.get(k, 0) + v
  return {k: v for k, v in c.items() if v != 0}


def psub(a, b):
  c = dict(a)
  for k, v in b.items():
    c[k] = c.get(k, 0) - v
  return {k: v for k, v in c.items() if v != 0}


def pmul(a, b):
  c = {}
  for k1, v1 in a.items():
    for k2, v2 in b.items():
      c[k1 + k2] = c.get(k1 + k2, 0) + v1 * v2
  return {k: v for k, v in c.items() if v != 0}


def peval(p, x):
  return sum(Fraction(v) * (x ** k) for k, v in p.items())


def chrom(n, edges):
  memo = {}
  def rec(vs, es):
    k = (tuple(sorted(vs)), tuple(sorted(es)))
    if k in memo:
      return memo[k]
    for (a, b) in es:
      if a == b:
        memo[k] = {}
        return memo[k]
    seen = set(); ues = []
    for e in es:
      e2 = tuple(sorted(e))
      if e2 not in seen:
        seen.add(e2); ues.append(e2)
    es = ues
    if not es:
      memo[k] = {len(vs): 1}
      return memo[k]
    adj = {v: set() for v in vs}
    for a, b in es:
      adj[a].add(b); adj[b].add(a)
    st = vs[0]; stack = [st]; vis = {st}
    while stack:
      x = stack.pop()
      for y in adj[x]:
        if y not in vis:
          vis.add(y); stack.append(y)
    if len(vis) < len(vs):
      s1 = set(v for v in vs if v in vis)
      r = pmul(rec(tuple(v for v in vs if v in vis), tuple(e for e in es if e[0] in s1)),
               rec(tuple(v for v in vs if v not in vis), tuple(e for e in es if e[0] not in s1)))
      memo[k] = r
      return r
    e0 = es[0]; a, b = e0
    r1 = rec(tuple(vs), tuple(e for e in es if e != e0))
    nvs = tuple(v for v in vs if v != b)
    nes = tuple((a if x == b else x, a if y == b else y) for (x, y) in es if (x, y) != e0)
    r = psub(r1, rec(nvs, nes))
    memo[k] = r
    return r
  return rec(tuple(range(n)), tuple(tuple(sorted(e)) for e in edges))


def bareiss(M):
  N = len(M)
  if N == 0:
    return 1
  A = [row[:] for row in M]
  prev = 1
  for k in range(N - 1):
    if A[k][k] == 0:
      s = next((i for i in range(k + 1, N) if A[i][k] != 0), None)
      if s is None:
        return 0
      A[k], A[s] = A[s], A[k]
    for i in range(k + 1, N):
      for j in range(k + 1, N):
        A[i][j] = (A[i][j] * A[k][k] - A[i][k] * A[k][j]) // prev
    prev = A[k][k]
  return A[N - 1][N - 1]


def trees(n, edges):
  L = [[0] * n for _ in range(n)]
  for a, b in edges:
    L[a][a] += 1; L[b][b] += 1; L[a][b] -= 1; L[b][a] -= 1
  return bareiss([r[:n - 1] for r in L[:n - 1]])


def ao_bf(n, edges):
  m = len(edges)
  U = [e[0] for e in edges]; V = [e[1] for e in edges]
  c = 0
  for mask in range(1 << m):
    out = [[] for _ in range(n)]; ind = [0] * n
    for i in range(m):
      a, b = (U[i], V[i]) if (mask >> i) & 1 else (V[i], U[i])
      out[a].append(b); ind[b] += 1
    st = [v for v in range(n) if ind[v] == 0]; seen = 0
    while st:
      x = st.pop(); seen += 1
      for y in out[x]:
        ind[y] -= 1
        if ind[y] == 0:
          st.append(y)
    if seen == n:
      c += 1
  return c


def trees_bf(n, edges):
  c = 0
  for combo in combinations(range(len(edges)), n - 1):
    par = list(range(n))
    def f(x):
      while par[x] != x:
        par[x] = par[par[x]]
        x = par[x]
      return x
    good = True
    for i in combo:
      a, b = edges[i]
      ra, rb = f(a), f(b)
      if ra == rb:
        good = False; break
      par[ra] = rb
    if good and all(f(v) == f(0) for v in range(n)):
      c += 1
  return c


for name, d in R['graphs'].items():
  n = d['n']
  edges = [tuple(e) for e in d['edges']]
  p = chrom(n, edges)
  cc = {int(k): v for k, v in d['chrom_coeffs'].items()}
  check(name + ':DC-replay', p == cc)
  check(name + ':monic-deg', max(p.keys()) == n and p[n] == 1)
  check(name + ':P3', int(peval(p, Fraction(3))) == d['P3'])
  check(name + ':ao-formula', ((-1) ** n) * int(peval(p, Fraction(-1))) == d['T20_ao'])
  check(name + ':matrix-tree', trees(n, edges) == d['T11_trees'])
  check(name + ':trees-bf', trees_bf(n, edges) == d['T11_trees'])
  check(name + ':ao-bf', ao_bf(n, edges) == d['T20_ao'])
  check(name + ':tree-DC', d['T11_del'] + d['T11_con'] == d['T11_trees'])
  check(name + ':ao-DC', d['T20_del'] + d['T20_con'] == d['T20_ao'])
  # independent 3-connectivity
  adj = {v: set() for v in range(n)}
  for a, b in edges:
    adj[a].add(b); adj[b].add(a)
  good = True
  for u in range(n):
    for v in range(u + 1, n):
      skip = {u, v}
      st = next(w for w in range(n) if w not in skip)
      stack = [st]; vis = {st}
      while stack:
        x = stack.pop()
        for y in adj[x]:
          if y not in skip and y not in vis:
            vis.add(y); stack.append(y)
      if len(vis) != n - 2:
        good = False
  check(name + ':3conn', good)

# Sturm replay for cube + antiprism
def pdivmod_f(A, B):
  A = [Fraction(x) for x in A]; B = [Fraction(x) for x in B]
  if len(A) < len(B):
    return [Fraction(0)], A
  Q = [Fraction(0)] * (len(A) - len(B) + 1)
  Rm = list(A)
  for i in range(len(Q)):
    c = Rm[i] / B[0]
    Q[i] = c
    for j in range(len(B)):
      Rm[i + j] -= c * B[j]
  k = 0
  while k < len(Rm) - 1 and Rm[k] == 0:
    k += 1
  return Q, Rm[k:]

def sturm(cd):
  P = [Fraction(x) for x in cd]
  n = len(P) - 1
  dP = [c * (n - i) for i, c in enumerate(P[:-1])]
  sq = [P, dP]
  while True:
    _, r = pdivmod_f(sq[-2], sq[-1])
    if all(x == 0 for x in r):
      break
    sq.append([-x for x in r])
    if len(sq[-1]) == 1:
      break
  return sq

def pv(desc, x):
  s = Fraction(0)
  for c in desc:
    s = s * x + c
  return s

def vc(sq, x):
  vs = []
  for P in sq:
    v = pv(P, x)
    if v != 0:
      vs.append(-1 if v < 0 else 1)
  return sum(1 for i in range(1, len(vs)) if vs[i] != vs[i - 1])

def desc_of(c):
  d = max(c.keys())
  return [Fraction(c.get(k, 0)) for k in range(d, -1, -1)]

pc = desc_of({int(k): v for k, v in R['graphs']['G1_cube']['chrom_coeffs'].items()})
Sq = sturm(pc)
check('cube:Sturm-zeroin(2,3]', vc(Sq, Fraction(2)) - vc(Sq, Fraction(3)) == 0)
check('cube:P2,P3-nonzero', pv(pc, Fraction(2)) != 0 and pv(pc, Fraction(3)) != 0)
pa = desc_of({int(k): v for k, v in R['graphs']['G4_sqantiprism']['chrom_coeffs'].items()})
Sa = sturm(pa)
for lo, hi, key in [('643/256', '645/256', 'r1'), ('871/256', '873/256', 'r2')]:
  def F(s):
    a, b = s.split('/')
    return Fraction(int(a), int(b))
  a, b = F(lo), F(hi)
  check('anti:%s-signchange' % key, pv(pa, a) * pv(pa, b) < 0)
  check('anti:%s-sturm1' % key, vc(Sa, a) - vc(Sa, b) == 1)

print('ALL %d CHECKS PASSED' % len(ok))
