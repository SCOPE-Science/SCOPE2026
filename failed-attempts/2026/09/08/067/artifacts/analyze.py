#!/usr/bin/env python3
"""Step 2: analyze each canonical presentation.

- Abelianization via 2x2 exponent-sum matrix (det != 0 => finite abelianization;
  det == 0 => certified infinite via tuberculosis-free map onto Z).
- Bounded Todd-Coxeter (HLT-style, fixed cap) from the trivial subgroup for the
  rest; closed tables are logged with claimed orders.
- Free-product-of-cyclics pairs (pure powers in distinct generators) with both
  orders >= 2 are certified infinite by normal-form argument.
- Output: output/artifacts/results.csv + output/artifacts/coset_tables/<id>.json
"""
import csv, json, math, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
PRES = os.path.join(HERE, "presentations.csv")
RES = os.path.join(HERE, "results.csv")
CTAB = os.path.join(HERE, "coset_tables")
os.makedirs(CTAB, exist_ok=True)

GENS = ['a', 'A', 'b', 'B']
G2I = {'a': 0, 'A': 1, 'b': 2, 'B': 3}
INV = [1, 0, 3, 2]
MAXN = 200          # max cosets per presentation
TIME_BUDGET = 1.5   # seconds per presentation

def exp_sums(w):
    ea = sum(1 if g in 'a' else (-1 if g in 'A' else 0) for g in w)
    eb = sum(1 if g in 'b' else (-1 if g in 'B' else 0) for g in w)
    return ea, eb

def is_pure_power(w):
    s = set(g.lower() for g in w)
    return len(s) == 1

class Overflow(Exception):
    pass

class TC:
    def __init__(self, rels, maxn=MAXN, t0=None, budget=TIME_BUDGET):
        self.rels = rels
        self.maxn = maxn
        self.t0 = t0 or time.time()
        self.budget = budget
        self.n = 1
        self.parent = [0, 1]
        self.alive = [False, True]
        self.tab = [[-1] * 4 for _ in range(maxn + 1)]
        self.ndefs = 0

    def find(self, x):
        p = self.parent
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x

    def tick(self):
        if time.time() - self.t0 > self.budget:
            raise Overflow()

    def new_coset(self):
        if self.n >= self.maxn:
            raise Overflow()
        self.n += 1
        self.parent.append(self.n)
        self.alive.append(True)
        return self.n

    def set_link(self, p, g, q):
        """Set p*g=q (and q*inv[g]=p); queue coincidences via return list."""
        p = self.find(p); q = self.find(q)
        if p == q and self.tab[p][g] != -1:
            return [((self.find(self.tab[p][g])), q)] if self.find(self.tab[p][g]) != q else []
        e = self.tab[p][g]
        if e != -1 and self.find(e) != q:
            return [(self.find(e), q)]
        rev = self.tab[q][INV[g]]
        if rev != -1 and self.find(rev) != p:
            return [(p, self.find(rev))]
        self.tab[p][g] = q
        self.tab[q][INV[g]] = p
        return []

    def coincidence(self, a, b):
        a = self.find(a); b = self.find(b)
        if a == b:
            return
        # union by small index wins (keep 1 alive)
        if a > b:
            a, b = b, a
        self.parent[b] = a
        self.alive[b] = False
        # merge rows: adopt b's defined entries into a
        pending = []
        for g in range(4):
            ea, eb = self.tab[a][g], self.tab[b][g]
            if ea != -1 and eb != -1:
                if self.find(ea) != self.find(eb):
                    pending.append((self.find(ea), self.find(eb)))
            elif ea == -1 and eb != -1:
                self.tab[a][g] = self.find(eb)
            if eb != -1:
                self.tab[b][g] = -1
        # redirect all pointers to b toward a
        for i in range(1, self.n + 1):
            if not self.alive[i]:
                continue
            for g in range(4):
                if self.tab[i][g] == b:
                    self.tab[i][g] = a
        for x, y in pending:
            self.coincidence(x, y)

    def scan_one(self, w, c):
        """Scan relator w (list of ints) at coset c. Returns 'ok'|'deduced'|'defined'."""
        self.tick()
        c = self.find(c)
        # forward
        f = [c]; i = 0
        while i < len(w):
            e = self.tab[f[-1]][w[i]]
            if e == -1:
                break
            f.append(self.find(e)); i += 1
        # backward
        b = [c]; j = len(w) - 1
        while j >= i:
            e = self.tab[b[-1]][INV[w[j]]]
            if e == -1:
                break
            b.append(self.find(e)); j -= 1
        if i > j:
            if self.find(f[-1]) != self.find(b[-1]):
                self.coincidence(f[-1], b[-1])
                return 'deduced'
            return 'ok'
        if i == j:
            for pair in self.set_link(f[-1], w[i], b[-1]):
                self.coincidence(*pair)
            return 'deduced'
        # gap: define new coset from the front
        d = self.new_coset()
        self.ndefs += 1
        for pair in self.set_link(f[-1], w[i], d):
            self.coincidence(*pair)
        return 'defined'

    def run(self):
        # initial: scan relators at 1 until stable-ish, then sweep all cosets
        ptr = 1
        passes_without_change = 0
        while True:
            self.tick()
            changed = False
            for c in range(1, self.n + 1):
                if not self.alive[c]:
                    continue
                c = self.find(c)
                if not self.alive[c]:
                    continue
                for w in self.rels:
                    r = self.scan_one(w, c)
                    if r != 'ok':
                        changed = True
            if not changed:
                break
            passes_without_change += 1
            if passes_without_change > 400:
                raise Overflow()
        # closed?
        for c in range(1, self.n + 1):
            if not self.alive[c]:
                continue
            for g in range(4):
                if self.tab[self.find(c)][g] == -1:
                    return None
        reps = sorted({self.find(c) for c in range(1, self.n + 1) if self.alive[c]})
        return reps

def tc_relators_trivial(reps, tab, rels):
    for w in rels:
        for c in reps:
            x = c
            for g in w:
                x = tab[x][g]
            if x != c:
                return False
    return True

def main():
    rows = list(csv.DictReader(open(PRES)))
    out = []
    n_fin = n_inf_ab = n_inf_fp = n_unres = 0
    for r in rows:
        pid, w1, w2 = int(r['id']), r['w1'], r['w2']
        e1, e2 = exp_sums(w1), exp_sums(w2)
        det = e1[0] * e2[1] - e1[1] * e2[0]
        ab_order = abs(det) if det != 0 else 0
        status, order, detail = None, '', ''
        if det == 0:
            status = 'infinite_abelianization'
            detail = f'Z^2-row-lattice det=0; maps onto Z (exp rows {e1},{e2})'
            n_inf_ab += 1
        elif is_pure_power(w1) and is_pure_power(w2) and \
                {next(iter(set(g.lower() for g in w1))), next(iter(set(g.lower() for g in w2)))} == {'a', 'b'}:
            m, n = len(w1), len(w2)
            if m == 1 or n == 1:
                pass  # cyclic; fall through to TC
            else:
                status = 'infinite_free_product'
                detail = f'Z_{m}*Z_{n} free product, m,n>=2, contains F2/inf-dihedral'
                n_inf_fp += 1
        if status is None:
            rels = [[G2I[g] for g in w1], [G2I[g] for g in w2]]
            t0 = time.time()
            try:
                tc = TC(rels, t0=t0)
                reps = tc.run()
                if reps is None:
                    status = 'unresolved_open_table'
                    detail = f'table not closed within cap {MAXN}'
                    n_unres += 1
                else:
                    # compress table to reps
                    idx = {c: k + 1 for k, c in enumerate(reps)}
                    comp = {}
                    ok = True
                    for c in reps:
                        row = [tc.find(tc.tab[c][g]) for g in range(4)]
                        if any(v not in idx for v in row):
                            ok = False
                            break
                        comp[str(idx[c])] = [idx[v] for v in row]
                    if not ok or not tc_relators_trivial(
                            [idx[c] for c in reps],
                            {int(k): v for k, v in comp.items()}, rels):
                        status = 'unresolved_incoherent'
                        detail = 'closed scan but replay failed'
                        n_unres += 1
                    else:
                        status = 'finite_closed_table'
                        order = len(reps)
                        detail = f'closed TC table, {tc.ndefs} definitions'
                        n_fin += 1
                        with open(os.path.join(CTAB, f'{pid}.json'), 'w') as f:
                            json.dump({'id': pid, 'w1': w1, 'w2': w2, 'order': order,
                                       'table': comp, 'defs': tc.ndefs,
                                       'ab_order': ab_order}, f)
            except Overflow:
                status = 'unresolved_overflow'
                detail = f'exceeded cap {MAXN} cosets or time budget'
                n_unres += 1
        out.append({'id': pid, 'w1': w1, 'w2': w2, 'ltot': r['ltot'],
                    'ab_det': det, 'ab_order': ab_order,
                    'status': status, 'order': order, 'detail': detail})
    with open(RES, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        w.writeheader(); w.writerows(out)
    print(f"finite={n_fin} inf_ab={n_inf_ab} inf_fp={n_inf_fp} unresolved={n_unres} total={len(out)}")

if __name__ == '__main__':
    main()
