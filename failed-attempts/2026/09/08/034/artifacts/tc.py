"""From-scratch Todd-Coxeter coset enumeration (HLT strategy) over trivial subgroup.
No external group-theory libraries. Generators: 0=a, 1=A=a^-1, 2=b, 3=B=b^-1.
"""
INV = [1, 0, 3, 2]

def pow_word(g, e):
    return [g] * e

def comm_word(k):
    return [0, 2, 1, 3] * k

def invert_word(w):
    return [INV[g] for g in reversed(w)]

class Enumeration:
    def __init__(self, relators):
        # relators: list of words (each a list of gen ints); inverses added automatically
        Rs = []
        for w in relators:
            Rs.append(list(w))
            Rs.append(invert_word(w))
        self.relators = Rs
        self.rows = [[-1] * 4]  # row per coset; coset i <-> index i
        self.parent = [0]
        self.alive = [True]
        self.ndefs = 1
        self.nded = 0
        self.ncoin = 0

    def find(self, x):
        p = self.parent
        while p[x] != x:
            p[x] = p[p[x]]
            x = p[x]
        return x

    def new_coset(self):
        i = len(self.rows)
        self.rows.append([-1] * 4)
        self.parent.append(i)
        self.alive.append(True)
        self.ndefs += 1
        return i

    def set_edge(self, i, g, j, queue):
        """Set i.g = j (and j.inv[g] = i), enqueueing coincidences on conflict."""
        i = self.find(i); j = self.find(j)
        if i == j:
            # self-loop: still record the table entry
            if self.rows[i][g] == -1:
                self.rows[i][g] = i
                b = self.rows[i][INV[g]]
                if b == -1:
                    self.rows[i][INV[g]] = i
                elif self.find(b) != i:
                    queue.append((b, i))
            elif self.find(self.rows[i][g]) != i:
                queue.append((self.rows[i][g], i))
            return
        ri, rj = self.rows[i], self.rows[j]
        e = ri[g]
        if e != -1:
            queue.append((e, j))
        else:
            ri[g] = j
            rj2 = self.rows[j]
            f = rj2[INV[g]]
            if f != -1:
                if self.find(f) != self.find(i):
                    queue.append((f, i))
            else:
                rj2[INV[g]] = i

    def process_queue(self, queue):
        while queue:
            x, y = queue.pop()
            x = self.find(x); y = self.find(y)
            if x == y:
                continue
            self.ncoin += 1
            # keep smaller index alive
            if x > y:
                x, y = y, x
            # merge y into x
            rx, ry = self.rows[x], self.rows[y]
            for g in range(4):
                t = ry[g]
                if t != -1:
                    t = self.find(t)
                    s = rx[g]
                    if s != -1:
                        s = self.find(s)
                        if s != t:
                            queue.append((s, t))
                    else:
                        rx[g] = t
                        # fix back-pointer
                        rt = self.rows[t]
                        b = rt[INV[g]]
                        if b != -1:
                            if self.find(b) != x:
                                queue.append((b, x))
                        else:
                            rt[INV[g]] = x
            # redirect all refs to y
            for i, r in enumerate(self.rows):
                if not self.alive[i]:
                    continue
                for g in range(4):
                    if r[g] != -1 and self.find(r[g]) == x:
                        r[g] = x
            self.parent[y] = x
            self.alive[y] = False

    def trace(self, start, word):
        """Follow word from start; return (ok_full, end_or_None, gap_pos, gap_coset)."""
        c = self.find(start)
        for j, g in enumerate(word):
            nxt = self.rows[c][g]
            if nxt == -1:
                return (False, None, j, c)
            c = self.find(nxt)
        return (True, c, -1, -1)

    def scan_once(self, queue):
        changed = False
        cosets = [i for i in range(len(self.rows)) if self.alive[i] and self.find(i) == i]
        for c in cosets:
            if not self.alive[c] or self.find(c) != c:
                continue
            for R in self.relators:
                # forward scan
                pos = self.find(c); j = 0
                L = len(R)
                while j < L:
                    nxt = self.rows[pos][R[j]]
                    if nxt == -1:
                        break
                    pos = self.find(nxt); j += 1
                if j == L:
                    if pos != self.find(c):
                        queue.append((pos, self.find(c)))
                        self.process_queue(queue)
                        changed = True
                    continue
                # backward scan from end
                pos2 = self.find(c); j2 = L
                while j2 > j:
                    nxt = self.rows[pos2][INV[R[j2 - 1]]]
                    if nxt == -1:
                        break
                    pos2 = self.find(nxt); j2 -= 1
                if j2 == j + 1:
                    # deduction
                    e = self.rows[pos][R[j]]
                    if e != -1:
                        if self.find(e) != pos2:
                            queue.append((self.find(e), pos2))
                            self.process_queue(queue)
                            changed = True
                    else:
                        self.set_edge(pos, R[j], pos2, queue)
                        self.process_queue(queue)
                        self.nded += 1
                        changed = True
                # else: gap too big here; HLT definition happens in define pass
        return changed

    def define_pass(self, queue, max_cosets):
        alive_n = sum(1 for i in range(len(self.rows)) if self.alive[i] and self.find(i) == i)
        if alive_n >= max_cosets:
            return False
        cosets = [i for i in range(len(self.rows)) if self.alive[i] and self.find(i) == i]
        for c in cosets:
            for R in self.relators:
                pos = self.find(c); j = 0
                L = len(R)
                while j < L:
                    nxt = self.rows[pos][R[j]]
                    if nxt == -1:
                        break
                    pos = self.find(nxt); j += 1
                if j < L:
                    # define new coset along this gap edge (HLT)
                    nc = self.new_coset()
                    self.set_edge(pos, R[j], nc, queue)
                    self.process_queue(queue)
                    return True
        return False

    def run(self, max_cosets=2000, max_passes=20000):
        queue = []
        passes = 0
        while passes < max_passes:
            passes += 1
            ch = self.scan_once(queue)
            if self.ndefs > max_cosets:
                return ('OVERFLOW', passes)
            if not ch:
                made = self.define_pass(queue, max_cosets)
                if self.ndefs > max_cosets:
                    return ('OVERFLOW', passes)
                if not made:
                    break
        return ('DONE' if passes < max_passes else 'PASSLIMIT', passes)

    def live_cosets(self):
        return [i for i in range(len(self.rows)) if self.alive[i] and self.find(i) == i]

    def compact_table(self):
        """Remap live cosets to 0..N-1 with coset 0 = subgroup. Return (N, pa, pb) or None."""
        live = self.live_cosets()
        root = self.find(0)
        # put trivial coset first
        live_sorted = [root] + [c for c in live if c != root]
        idx = {c: k for k, c in enumerate(live_sorted)}
        N = len(live_sorted)
        pa, pb = [0]*N, [0]*N
        for c in live_sorted:
            r = self.rows[c]
            for g in range(4):
                t = r[g]
                if t == -1:
                    return None
                t = idx[self.find(t)]
                if g == 0: pa[idx[c]] = t
                elif g == 2: pb[idx[c]] = t
        return (N, pa, pb)

    def is_closed(self):
        return self.compact_table() is not None


def apply_perm(p, start, word, pa, pb, N):
    perms = [pa, None, pb, None]
    # build inverses
    pai = [0]*N; pbi = [0]*N
    for i in range(N):
        pai[pa[i]] = i; pbi[pb[i]] = i
    perms[1] = pai; perms[3] = pbi
    c = start
    for g in word:
        c = perms[g][c]
    return c

def check_certificate(N, pa, pb, relators):
    """Independent check: perms, relator closure at every point, transitivity."""
    if len(pa) != N or len(pb) != N: return False, "length"
    if sorted(pa) != list(range(N)) or sorted(pb) != list(range(N)):
        return False, "not permutations"
    for R in relators:
        for s in range(N):
            if apply_perm(None, s, R, pa, pb, N) != s:
                return False, f"relator {R} fails at {s}"
    # transitivity from 0
    seen = {0}; stack = [0]
    pai = [0]*N; pbi = [0]*N
    for i in range(N):
        pai[pa[i]] = i; pbi[pb[i]] = i
    while stack:
        c = stack.pop()
        for q in (pa[c], pai[c], pb[c], pbi[c]):
            if q not in seen:
                seen.add(q); stack.append(q)
    if len(seen) != N:
        return False, "not transitive"
    return True, "ok"

def perm_order(p):
    N = len(p); vis = [False]*N; from math import gcd
    l = 1
    for i in range(N):
        if not vis[i]:
            c = i; k = 0
            while not vis[c]:
                vis[c] = True; c = p[c]; k += 1
            l = l * k // gcd(l, k)
    return l

def compose(p, q):
    return [p[q[i]] for i in range(len(p))]

def perm_image_order(pa, pb, limit=2000000):
    """BFS order of <pa,pb> in S_N (ok for small images)."""
    N = len(pa)
    ident = tuple(range(N))
    seen = {ident}; stack = [ident]
    gens = [tuple(pa), tuple(pb)]
    while stack:
        cur = stack.pop()
        for g in gens:
            for h in (g,):
                nxt = tuple(cur[g[i]] if False else g[cur[i]] for i in range(N))
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
                    if len(seen) > limit:
                        return None
    return len(seen)
