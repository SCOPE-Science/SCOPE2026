"""Finite falsification checks for marked Ferrers-chain adjacency types.

Usage: python3 check_chain_traces.py
Only Python 3 standard library is needed.
"""
from itertools import combinations, permutations
from collections import defaultdict
from math import comb


def subsets(n):
    return [sum(1 << i for i in c) for k in range(n + 1) for c in combinations(range(n), k)]


def is_chain(rows, v):
    return all(not ((x & ~y) and (y & ~x)) for x in rows for y in rows)


def trace_count(rows, u, v, marked_u, marked_v):
    # Left vertices see marked right vertices; right vertices see marked left vertices.
    left = {row & marked_v for row in rows}
    right = set()
    for j in range(v):
        bits = sum((1 << i) for i in range(u) if rows[i] & (1 << j))
        right.add((bits & marked_u) << v)
    return len(left | right)


def is_connected(rows, u, v):
    if u + v <= 1:
        return True
    seen={0}
    stack=[0]
    while stack:
        x=stack.pop()
        nxt=([(u+j) for j in range(v) if rows[x]>>j&1] if x<u
             else [i for i in range(u) if rows[i]>>(x-u)&1])
        for y in nxt:
            if y not in seen:
                seen.add(y)
                stack.append(y)
    return len(seen)==u+v


def canonical(rows, u, v, mu, mv):
    # Normalize separately within the four colour/mark blocks.
    a1 = [i for i in range(u) if mu >> i & 1]
    a0 = [i for i in range(u) if not (mu >> i & 1)]
    b1 = [j for j in range(v) if mv >> j & 1]
    b0 = [j for j in range(v) if not (mv >> j & 1)]
    best = None
    for ps in permutations(a1):
      for qs in permutations(a0):
        rr = ps + qs
        for pt in permutations(b1):
          for qt in permutations(b0):
            cc = pt + qt
            encoding = tuple(sum((1 << j) for j, k in enumerate(cc) if rows[i] >> k & 1) for i in rr)
            if best is None or encoding < best:
                best = encoding
    return best


def check_all(max_n=7):
    # Visit every side-labelled binary adjacency matrix and every marked subset.
    count_graphs = count_marked = 0
    extremizers = defaultdict(set)
    connected_extremizers = defaultdict(set)
    best = defaultdict(int)
    min_size = {}
    for n in range(1, max_n + 1):
      for u in range(n + 1):
        v = n - u
        for code in range(1 << (u * v)):
          rows = tuple((code >> (i * v)) & ((1 << v)-1) for i in range(u))
          if not is_chain(rows, v):
              continue
          count_graphs += 1
          for mu in subsets(u):
            for mv in subsets(v):
              a, b = mu.bit_count(), mv.bit_count()
              m = a+b
              if m == 0:
                  continue
              t = trace_count(rows, u, v, mu, mv)
              count_marked += 1
              assert t <= m+1, (u,v,rows,mu,mv,t)
              best[(a,b)] = max(t, best[(a,b)])
              if t == m+1:
                  bound = max(2*max(a,b),m+1)
                  assert n >= bound, (a,b,n,bound)
                  if n == bound:
                    key = (a,b)
                    extremizers[key].add((u,v,canonical(rows,u,v,mu,mv)))
                  connected_bound=bound+(1 if a==b else 0)
                  if is_connected(rows,u,v):
                    assert n>=connected_bound,(a,b,n,connected_bound)
                    if n==connected_bound:
                        connected_extremizers[(a,b)].add((u,v,canonical(rows,u,v,mu,mv)))
          
      print('order',n,'graphs',count_graphs,'marked_tests',count_marked,flush=True)
    for (a,b),types in sorted(extremizers.items()):
        predicted = 2 if a==b else comb(max(a,b)-1,min(a,b))
        assert len(types)==predicted, (a,b,len(types),predicted,types)
        assert best[a,b] == a+b+1
    for (a,b),types in sorted(connected_extremizers.items()):
        assert len(types) > 0
    print('CONNECTED_MINIMAL_TYPE_CHECKS_OK',len(connected_extremizers),
          'balanced_sample_counts',[(k,len(connected_extremizers[k,k])) for k in (1,2)])
    print('ALL_EXHAUSTIVE_CHECKS_OK','graphs',count_graphs,'marked_tests',count_marked,'extremal_parameter_pairs',len(extremizers))


def constructed(a,b,connected=False):
    assert a+b > 0
    if a == b:
        k=a
        # Half graph plus either an isolated vertex or a two-sided connector.
        left = k+1
        right = k+(1 if connected else 0)
        rows = tuple(sum(1 << j for j in range(i, k)) for i in range(k)) + (((1 << right)-1) if connected else 0,)
        mu = (1 << k)-1
        mv = (1 << k)-1
        return rows,left,right,mu,mv
    if a > b:
        left=right=a
        # right column j has the first j+1 marked left neighbours
        rows=tuple(sum((1<<j) for j in range(i,a)) for i in range(a))
        mu=(1<<a)-1
        mv=(1<<b)-1
        return rows,left,right,mu,mv
    # b > a, transpose the previous construction
    t,uu,vv,tmu,tmv = constructed(b,a)
    rows=tuple(sum((1<<i) for i in range(uu) if t[i]>>j & 1) for j in range(vv))
    return rows,vv,uu,tmv,tmu


def check_constructions(max_a=60):
    cases=0
    for a in range(max_a+1):
      for b in range(max_a+1):
        if not a+b:continue
        rows,u,v,mu,mv=constructed(a,b)
        assert is_chain(rows,v)
        assert mu.bit_count()==a and mv.bit_count()==b
        assert trace_count(rows,u,v,mu,mv)==a+b+1, (a,b)
        assert u+v==max(2*max(a,b),a+b+1), (a,b)
        crows,cu,cv,cmu,cmv=constructed(a,b,connected=True)
        assert is_chain(crows,cv)
        assert is_connected(crows,cu,cv)
        assert trace_count(crows,cu,cv,cmu,cmv)==a+b+1
        assert cu+cv==max(2*max(a,b),a+b+1)+(1 if a==b else 0)
        cases+=1
    print('CONSTRUCTION_CHECKS_OK',cases)

if __name__ == '__main__':
    check_all(7)
    check_constructions(40)
    print('ALL_CHECKS_OK')
