import pulp, itertools
from petersen_core import BASE, EDGES, NBR, all_minimal_covers
covers = all_minimal_covers()
Cmat = [[(m >> v) & 1 for v in range(10)] for m in covers]
E = EDGES
def in_ordinary(a, r):
    prob = pulp.LpProblem("ord", pulp.LpMaximize)
    zs = [pulp.LpVariable(f"z{e}", lowBound=0, cat='Integer') for e in range(len(E))]
    prob += 0
    prob += pulp.lpSum(zs) == r
    for v in range(10):
        prob += pulp.lpSum(zs[e] for e in range(len(E)) if v in E[e]) <= a[v]
    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    return pulp.LpStatus[prob.status] == 'Optimal'

# (a) walk vector: girth 5 means NO triangle/square monomial check needed; odd 5-walk monomial has degree 6.
# classical non-containment for non-bipartite: product over closed odd walk of length 2r+1 lies in I^{(r+1)} but not I^{r+1}? test 5-cycle monomial (deg 5) lies in which symbolic powers?
cyc = (1, 2, 4, 6, 9)
# edges of the cycle in order? find order
S = set(cyc)
# order the cycle
order = [cyc[0]]
prev = None
cur = cyc[0]
for _ in range(4):
    nxt = [w for w in NBR[cur] if w in S and w != prev][0]
    order.append(nxt); prev, cur = cur, nxt
print("cycle order:", order, "closing edge?", order[-1] in NBR[order[0]])
a = [0]*10
for v in order: a[v] = 1
print("cover sums of C5 monomial:", sorted(sum(Cmat[c][v]*a[v] for v in range(10)) for c in range(15)))
# So C5 monomial is in I^{(2)}? min is 2? Let's see exact min
print("min cover sum:", min(sum(Cmat[c][v]*a[v] for v in range(10)) for c in range(15)))
for r in (1, 2):
    print("in I^%d?" % r, in_ordinary(a, r))

# (b) clique-sum / star upper bounds for rho of edge ideals: known bounds: rho <= 2 - 2/omega? For graphs, rho(I(G)) <= 2-2/chi_f? Let's recall:
# For squarefree monomial ideals, rho <= ... ; for edge ideals: rho <= 2 - 2/(omega+1)? Hmm.
# Direct computational search for failures m/r with small m: scan minimal feasible vectors s<=8 for non-membership in I^r with LP check.
def alpha_sym_vec(s):
    prob = pulp.LpProblem("a", pulp.LpMinimize)
    xs = [pulp.LpVariable(f"x{v}", lowBound=0, cat='Integer') for v in range(10)]
    prob += pulp.lpSum(xs)
    for row in Cmat:
        prob += pulp.lpSum(row[v]*xs[v] for v in range(10)) >= s
    prob.solve(pulp.PULP_CBC_CMD(msg=0))
    return int(round(pulp.value(prob.objective))), [int(round(x.value())) for x in xs]

# General containment test I^{(m)} subset I^r: suffices to check minimal elements of symbolic polyhedron box? ord(I^r) monsters have max coordinate 2r.
# For each (m, r) pair of interest, enumerate minimal feasible vectors within box {0..2r}^10 and test membership.
def contains(m, r, verbose=True):
    import itertools
    bad = []
    nmin = 0
    B = 2*r  # truncation bound claim: any feasible a with some a_v > 2r descends by 2e_v staying feasible... but e_v-decent needs care; we use minimal elements which satisfy a_v <= 2r? PROVE: minimal => a_v <= 2r? Suppose a_v >= 2r+1... hmm need edge argument.
    # For now, brute box only valid if we can certify completeness; collect minimals in box.
    for a in itertools.product(range(B+1), repeat=10):
        if not all(sum(Cmat[c][v]*a[v] for v in range(10)) >= m for c in range(15)):
            continue
        # minimality
        mins = True
        for v in range(10):
            if a[v] == 0: continue
            if all(sum(Cmat[c][w]*a[w] for w in range(10)) - Cmat[c][v] >= m for c in range(15)):
                mins = False; break
        if not mins: continue
        nmin += 1
        if not in_ordinary(list(a), r):
            bad.append(a)
    if verbose:
        print(f"I^({m}) vs I^{r}: box B={B}, minimals={nmin}, failures={len(bad)}")
        for b in bad[:8]:
            print("   fail:", b, "deg", sum(b))
    return bad

for (m, r) in [(2,1),(3,2),(4,2),(4,3),(5,3),(5,4),(6,4),(6,5),(3,1),(4,1),(5,2),(6,3),(8,5)]:
    contains(m, r)
