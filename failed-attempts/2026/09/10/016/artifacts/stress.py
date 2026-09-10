"""Random + structured stress test of reg <= 2*nu on claw-free graphs (n=7..14)."""
import sys, random, itertools, time
sys.path.insert(0, 'output/artifacts')
from clawreg import adj_from_edges, has_claw, induced_matching_number, reg_SI_modp


def rand_line_graph(nH, p, rng):
    # random graph H on nH vertices, m edges -> line graph G with m vertices
    pairs = [(a, b) for a in range(nH) for b in range(a + 1, nH)]
    Hed = [e for e in pairs if rng.random() < p]
    m = len(Hed)
    adj = [0] * m
    Ge = []
    for i in range(m):
        for j in range(i + 1, m):
            if len(set(Hed[i]) & set(Hed[j])) > 0:
                adj[i] |= (1 << j)
                adj[j] |= (1 << i)
                Ge.append((i, j))
    return m, adj, Ge


def rand_clawfree_deletion(n, p, rng):
    pairs = [(a, b) for a in range(n) for b in range(a + 1, n)]
    edges = [e for e in pairs if rng.random() < p]
    adj = adj_from_edges(n, edges)
    # greedy delete edges to kill claws
    while has_claw(n, adj):
        # find a claw, delete one of its edges
        found = None
        for v in range(n):
            N = [u for u in range(n) if (adj[v] >> u) & 1]
            L = len(N)
            for i in range(L):
                for j in range(i + 1, L):
                    if (adj[N[i]] >> N[j]) & 1:
                        continue
                    for k in range(j + 1, L):
                        if ((adj[N[i]] >> N[k]) & 1) == 0 and ((adj[N[j]] >> N[k]) & 1) == 0:
                            found = (v, N[i], N[j], N[k])
                            break
                    if found:
                        break
                if found:
                    break
            if found:
                break
        v, a, b, c = found
        # delete edge v-a (arbitrary)
        adj[v] &= ~(1 << a)
        adj[a] &= ~(1 << v)
    return adj


def stats(n, adj):
    if has_claw(n, adj):
        return None
    nu = induced_matching_number(n, adj)
    reg = reg_SI_modp(n, adj)
    return nu, reg


if __name__ == "__main__":
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
    rng = random.Random(seed)
    t0 = time.time()
    nviol = 0
    ntest = 0
    worst = (0, None, None, None)  # reg-2nu, n, nu, reg
    trial = 0
    budget = float(sys.argv[2]) if len(sys.argv) > 2 else 240
    while time.time() - t0 < budget:
        trial += 1
        kind = trial % 3
        if kind == 0:
            nH = rng.randint(4, 7)
            m, adj, Ge = rand_line_graph(nH, rng.choice([0.3, 0.5, 0.7]), rng)
            if m < 4 or m > 11:
                continue
            n = m
        elif kind == 1:
            n = rng.randint(7, 10)
            adj = rand_clawfree_deletion(n, rng.choice([0.25, 0.4, 0.55]), rng)
        else:
            # circulants / structured
            n = rng.randint(7, 11)
            S = set()
            for d in rng.choice([[{1, 2}], [{1, 3}], [{1, 2, 3}], [{2, 3}]]):
                S = d
            edges = []
            for a in range(n):
                for d in S:
                    b = (a + d) % n
                    if a < b:
                        edges.append((a, b))
                    elif b < a and (b, a) not in edges:
                        edges.append((min(a, b), max(a, b)))
            edges = sorted(set(edges))
            adj = adj_from_edges(n, edges)
            if has_claw(n, adj):
                continue
        r = stats(n, adj)
        if r is None:
            continue
        nu, reg = r
        ntest += 1
        gap = reg - 2 * nu
        if gap > worst[0]:
            worst = (gap, n, nu, reg)
            el = [(a, b) for a in range(n) for b in range(a + 1, n) if (adj[a] >> b) & 1]
            print("NEW WORST gap=%d n=%d nu=%d reg=%d edges=%s" % (gap, n, nu, reg, el), flush=True)
        if gap > 0:
            nviol += 1
            el = [(a, b) for a in range(n) for b in range(a + 1, n) if (adj[a] >> b) & 1]
            print("VIOLATION n=%d nu=%d reg=%d edges=%s" % (n, nu, reg, el), flush=True)
    print("done trials=%d tested=%d viol=%d worst=%s elapsed=%.1f" % (trial, ntest, nviol, worst[:4], time.time() - t0))
