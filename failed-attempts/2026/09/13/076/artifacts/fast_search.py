#!/usr/bin/env python3
"""Bounded adversarial test: fast OPT<=1.6 decider + trap families.
Goal: find explicit two-valued instance, config-LP feasible at T=1, OPT>8/5
(= complete TARGET disproof), or gain confidence for proof route."""
import sys; sys.path.insert(0,'output/artifacts')
from search_gap import all_configs, config_lp_feasible
import random, time

CAP = 1.6

def opt_leq_cap(p, cap=CAP):
    """Decide if integral assignment with max load<=cap exists. DFS + pruning.
    p[i][j] = size or None. Returns True/False."""
    m = len(p); n = len(p[0])
    elig = [[i for i in range(m) if p[i][j] is not None] for j in range(n)]
    for j in range(n):
        if not elig[j]:
            return False
    order = sorted(range(n), key=lambda j: (len(elig[j]),
                 -max(p[i][j] for i in elig[j])))
    loads = [0.0]*m
    minsize = [min(p[i][j] for i in elig[j]) for j in range(n)]
    # suffix sums of minsize in order
    suf = [0.0]*(n+1)
    for k in range(n-1, -1, -1):
        suf[k] = suf[k+1] + minsize[order[k]]
    room = [cap]*m
    found = [False]
    # candidate machine order cache per job: prefer tight fit
    def dfs(k, used):
        if found[0]:
            return True
        if k == n:
            found[0] = True
            return True
        # capacity prune: remaining min need vs total room
        totroom = 0.0
        for i in range(m):
            totroom += cap - loads[i]
        if suf[k] > totroom + 1e-9:
            return False
        j = order[k]
        # forward check: some machine fits this job
        cands = []
        for i in elig[j]:
            nl = loads[i] + p[i][j]
            if nl <= cap + 1e-9:
                cands.append(i)
        if not cands:
            return False
        # try best-fit first (least remaining room after), dedup by resulting load
        cands.sort(key=lambda i: (loads[i] + p[i][j]))  # smallest resulting load first
        # symmetry: skip machines with identical (load, size-for-j) tried;
        # note loads differ across branches so key on size classes only when safe:
        # group candidates by size value for this job; order groups by size, and
        # within group by current load.
        from collections import defaultdict
        bysize = defaultdict(list)
        for i in cands:
            bysize[p[i][j]].append(i)
        order2 = []
        for s in sorted(bysize):
            bysize[s].sort(key=lambda i: loads[i])
            order2.extend(bysize[s])
        for i in order2:
            loads[i] += p[i][j]
            if dfs(k+1, used + p[i][j]):
                return True
            loads[i] -= p[i][j]
        return False
    return dfs(0, 0.0)

def eval_inst(p):
    m = len(p); n = len(p[0])
    elig = [[(j, p[i][j]) for j in range(n) if p[i][j] is not None] for i in range(m)]
    cfgs = [all_configs(es) for es in elig]
    feas, tv, _ = config_lp_feasible(cfgs, n)
    if not feas:
        return (False, None, None)
    return (True, tv, opt_leq_cap(p))

def gen_trap(rng, fam):
    """Generate trap instance. Returns (p, a, b)."""
    if fam == 'pigeon':
        m = rng.choice([3,4,5,6]); b = rng.choice([0.7,0.8,0.9,1.0])
        a = rng.choice([0.2,0.25,0.3,0.35,0.4])
        S = rng.sample(range(m), k=rng.choice([2,3]))
        nb = len(S)
        ns = rng.choice([5,6,7,8])
        jobs = []
        for i in S:
            jobs.append(({i}, {i: b}))
        for _ in range(ns):
            E = set(S)
            jobs.append((E, {i: a for i in E}))
        # fillers: jobs eligible outside to occupy others? none
    elif fam == 'twochoice':
        m = rng.choice([4,5,6,7,8]); b = rng.choice([0.65,0.7,0.75,0.8,0.85,0.9])
        a = rng.choice([0.2,0.25,0.3,0.35,0.4,0.45])
        n = rng.choice([8,9,10,11,12])
        jobs = []
        for _ in range(n):
            E = set(rng.sample(range(m), 2))
            il = list(E)
            style = rng.random()
            if style < 0.5:
                sz = {il[0]: b, il[1]: a}
            elif style < 0.8:
                sz = {il[0]: a, il[1]: b}
            else:
                v = rng.choice([a,b]); sz = {il[0]: v, il[1]: v}
            jobs.append((E, sz))
    elif fam == 'cycle':
        m = rng.choice([3,4,5,6]); b = rng.choice([0.7,0.8,0.9])
        a = rng.choice([0.2,0.3,0.4])
        n = rng.choice([6,7,8,9,10])
        jobs = []
        for _ in range(n):
            i = rng.randrange(m)
            E = {i, (i+1) % m}
            if rng.random() < 0.5:
                sz = {i: b, (i+1) % m: a}
            else:
                sz = {i: a, (i+1) % m: b}
            jobs.append((E, sz))
    elif fam == 'triple':
        m = rng.choice([4,5,6]); b = rng.choice([0.7,0.75,0.8,0.85,0.9])
        a = rng.choice([0.25,0.3,0.35,0.4])
        n = rng.choice([8,9,10,11,12])
        jobs = []
        for _ in range(n):
            E = set(rng.sample(range(m), 3))
            il = list(E)
            sz = {}
            for i in il:
                sz[i] = b if rng.random() < 0.45 else a
            jobs.append((E, sz))
    elif fam == 'asym':
        m = rng.choice([3,4,5]); b = rng.choice([0.8,0.9,1.0])
        a = rng.choice([0.2,0.3,0.4])
        n = rng.choice([6,7,8,9])
        jobs = []
        for _ in range(n):
            k = rng.choice([1,2,2,3])
            E = set(rng.sample(range(m), min(k, m)))
            il = list(E)
            sz = {i: (b if rng.random() < 0.5 else a) for i in il}
            # force at least one small so LP feasible-ish
            if all(v == b for v in sz.values()) and rng.random() < 0.7:
                sz[rng.choice(il)] = a
            jobs.append((E, sz))
    n = len(jobs)
    m2 = max(max(E) for E, s in jobs) + 1
    p = [[None]*n for _ in range(m2)]
    for j, (E, sz) in enumerate(jobs):
        for i in E:
            p[i][j] = sz[i]
    return p, a, b

def main():
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    ntrials = int(sys.argv[2]) if len(sys.argv) > 2 else 15000
    rng = random.Random(seed)
    fams = ['pigeon', 'twochoice', 'cycle', 'triple', 'asym']
    t0 = time.time(); checked = 0; feas = 0; hard = 0
    worst = None
    for t in range(ntrials):
        fam = fams[t % len(fams)]
        p, a, b = gen_trap(rng, fam)
        m = len(p); n = len(p[0])
        ok, tv, fits = eval_inst(p)
        checked += 1
        if not ok:
            continue
        feas += 1
        if not fits:
            print(f"[{t}] COUNTEREXAMPLE? fam={fam} ({a},{b}) m={m} n={n} t={tv:.3f}", flush=True)
            print("p=", p, flush=True)
            return
        hard += 1
    print(f"done seed={seed} checked={checked} feas={feas} time={time.time()-t0:.1f}s NO counterexample", flush=True)

if __name__ == '__main__':
    main()
