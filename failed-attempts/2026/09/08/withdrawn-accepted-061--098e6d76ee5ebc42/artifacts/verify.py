"""Independent verifier: recompute e(P) for any row from the childform string alone.

Usage: python3 verify.py [csv ...] [--pairs N] [--limit K]
Recomputes e(P) via a fresh ideal-DP implementation (different code path from
census.py: upset-based recursion), checks hook formula on forests, and rechecks a
sample of sorting probabilities by direct augmented-poset DP.
"""
import ast, csv, sys, math
from fractions import Fraction

def parse(s):
    return ast.literal_eval(s.replace('{', '[').replace('}', ']'))

def preds(covers0):
    n = len(covers0)
    pred = [0]*n
    for k, lst in enumerate(covers0):
        for j in lst:
            pred[k] |= (1 << (j-1))
    for m in range(n):
        for k in range(n):
            if (pred[k] >> m) & 1:
                pred[k] |= pred[m]
    return pred

def count_lin_ext(pred):
    n = len(pred); full = (1 << n) - 1
    from functools import lru_cache
    @lru_cache(maxsize=None)
    def rec(placed):
        if placed == full: return 1
        tot = 0
        for k in range(n):
            if (placed >> k) & 1: continue
            if pred[k] & ~placed == 0:
                tot += rec(placed | (1 << k))
        return tot
    return rec(0)

def main(args):
    files = [a for a in args if not a.startswith('--') and not a.isdigit()]
    limit = int(args[args.index('--limit')+1]) if '--limit' in args else None
    npair = int(args[args.index('--pairs')+1]) if '--pairs' in args else 0
    nchecked = 0; nforest = 0
    for f in files:
        for r in csv.DictReader(open(f)):
            if limit is not None and nchecked >= limit: break
            cov = parse(r['childform']); p = preds(cov)
            e = count_lin_ext(p)
            assert e == int(r['e']), (r['n'], r['id'], e, r['e'])
            n = len(cov)
            # forest recheck
            cc = [0]*n
            for k, lst in enumerate(cov):
                for j in lst: cc[j-1] += 1
            if all(c <= 1 for c in cc):
                nforest += 1
                parent = [-1]*n
                for k, lst in enumerate(cov):
                    for j in lst: parent[j-1] = k
                ch = [[] for _ in range(n)]
                for j, pa in enumerate(parent):
                    if pa >= 0: ch[pa].append(j)
                def sz(k):
                    return 1 + sum(sz(c) for c in ch[k])
                h = math.factorial(n)
                for k in range(n): h //= sz(k)
                assert h == e
            nchecked += 1
    print(f'VERIFY_OK rows={nchecked} forests_rechecked={nforest}')
    # targeted pair recheck for headline witnesses
    targets = [('{{},{},{1},{2,3},{4},{4},{5},{6,7}}', 9, (0,1,6,3)),
               ('{{},{},{},{},{1},{1},{1},{2,3,4}}', 2520, (0,7,2484,36))]
    for cf, ee, (x,y,ex,ey) in targets:
        cov = parse(cf); p = preds(cov)
        assert count_lin_ext(p) == ee, cf
        for (a,b,want) in ((x,y,ex),(y,x,ey)):
            q = list(p)
            q[b] |= (q[a] | (1 << a))
            chg = True
            while chg:
                chg = False
                for m in range(len(q)):
                    for k in range(len(q)):
                        if (q[k] >> m) & 1 and (q[k] | q[m]) != q[k]:
                            q[k] |= q[m]; chg = True
            assert count_lin_ext(q) == want, (cf,a,b)
        print(f'WITNESS_OK cf={cf} e={ee} pair({x+1},{y+1})={ex}/{ee} vs {ey}/{ee}')
    # random pair sample
    import random
    random.seed(7)
    if npair:
        checked = 0
        for f in files:
            for r in csv.DictReader(open(f)):
                if checked >= npair: break
                cov = parse(r['childform']); p = preds(cov); n = len(cov); e = int(r['e'])
                full_le = [[(p[b] >> a) & 1 == 1 for b in range(n)] for a in range(n)]
                incomp = [(a,b) for a in range(n) for b in range(a+1,n)
                          if not full_le[a][b] and not full_le[b][a]]
                if not incomp: continue
                a,b = random.choice(incomp)
                tot = 0
                for (u,v) in ((a,b),(b,a)):
                    q = list(p)
                    q[v] |= (q[u] | (1 << u))
                    chg = True
                    while chg:
                        chg = False
                        for m in range(n):
                            for k in range(n):
                                if (q[k] >> m) & 1 and (q[k] | q[m]) != q[k]:
                                    q[k] |= q[m]; chg = True
                    tot += count_lin_ext(q)
                assert tot == e, (r, a, b)
                checked += 1
        print(f'PAIR_SAMPLE_OK pairs={checked}')

if __name__ == '__main__':
    main(sys.argv[1:])
