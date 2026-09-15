"""Psi-floor counts F_{d,k}: computational model matching DRAFT Sections 4-5.

Rules (documented in DRAFT):
- Underlying classical floor diagram D (degree d): floors 0..d-1, bounded
  elevators (multiset), divergence u_v = 1+out-in >= 0, tree, mu = prod w^2.
- Classical poset P(D): floors chain + bounded bead per elevator + u_v
  unbounded beads per floor. |P| = 3d-1. Beads distinguishable in code;
  Aut(D) = prod_v u_v! * prod_{pair,w} m_e!  (parallel-edge multiplicity).
- n = 3d-1-k free points. Marking factor Inj_n(D) = # order-preserving
  injections of an n-chain into P(D) (distinguishable beads), divided by Aut.
  k=0 -> bijections = classical marking number. (Empirically integral.)
- Distinguished floor v*: det-factor delta = 1 per floor (tropical Bezout:
  each degree-1 floor meets L once); psi-germ factor
  c(val(v*),k) = C(val(v*)+k-1, k) (stars-bars attachments of k
  indistinguishable psi-germs to val incident half-edges),
  val(v) = (#incident bounded elevators, counted with multiplicity 1 per
  edge) + u_v + 2 (two floor ends).
- F_{d,k} = sum_D mu(D)/Aut(D) * Inj_n(D) * [sum_{v*} c(val(v*),k)].
  Hence F_{d,0} = d * N_d exactly (sum over d floors, c=1).
"""
import math
from itertools import permutations
from floor_enum import enumerate_diagrams, count_markings  # reuse poset builder logic


def build_poset(d, edges, u):
    E = len(edges)
    n = d + E + sum(u)
    pred = [set() for _ in range(n)]
    for v in range(1, d):
        pred[v].add(v - 1)
    bid = d
    for (i, j), w in edges:
        pred[bid].add(i)
        pred[j].add(bid)
        bid += 1
    for v in range(d):
        for _ in range(u[v]):
            pred[v].add(bid)
            bid += 1
    assert bid == n
    # transitive closure not needed: direct preds suffice for DP if we use
    # "available" propagation with full ancestor masks:
    # compute ancestor masks by Floyd over DAG (edges pred->node)
    anc = [set() for _ in range(n)]
    order = list(range(n))
    changed = True
    # simple closure: iterate
    for _ in range(n):
        for e in range(n):
            for p in list(pred[e]):
                anc[e].add(p)
                anc[e] |= anc[p]
    predmask = [0] * n
    for e in range(n):
        m = 0
        for p in anc[e]:
            m |= 1 << p
        predmask[e] = m
    return n, predmask


def count_injections(nP, predmask, n):
    """# order-preserving injections f: chain[n] -> P (distinguishable)."""
    from functools import lru_cache
    if n == 0:
        return 1
    if n > nP:
        return 0

    @lru_cache(maxsize=None)
    def dp(mask, j):
        # mask = image set used; j = #placed (next rank j).
        # count completions. Available e not in mask with anc(e) subset of mask?
        # NO: order-preserving injection only needs: if e in image at rank j',
        # all anc(e) in P that are also in image have rank < j'. Ancestors may
        # be skipped (not in image). So availability = any unused e, but future
        # feasibility requires we never place e before... actually any unused e
        # can be placed next ONLY IF all image-predecessors already placed?
        # Since skipped ancestors are allowed, every unused e is eligible next
        # provided that placing it keeps extendability: the only restriction is
        # that if a<b in P and both chosen, a comes first. Equivalent to:
        # sequences of distinct elements (e_0,...,e_{n-1}) with no "inversion"
        # (never e_j > e_i in P-order for j<i, i.e. anc(e_i) intersect image
        # must be subset of {e_0..e_{i-1}}).
        if j == n:
            return 1
        t = 0
        for e in range(nP):
            if not (mask >> e) & 1:
                if (predmask[e] & mask) == (predmask[e] & full_image_constraint(mask, e)):
                    # condition: every ancestor of e that is already used is fine
                    # (always true); the real constraint: no unused... none.
                    # Actually any e is allowed next? No! If some unused a is an
                    # ancestor of e and a is LATER chosen, we'd have inversion
                    # (a must precede e but placed after). To avoid overcounting
                    # we allow it: the sequence (e before a) with a ancestor of e
                    # is INVALID and must be excluded. Exclusion rule: e allowed
                    # iff no ancestor of e is "still to be chosen and placed
                    # later" — but we don't know future. Standard fix: count
                    # linear extensions of induced subposets summed over subsets:
                    # e allowed next iff all its ancestors ALREADY in mask OR
                    # will be skipped. Since skipping is allowed, e always allowed?!
                    # Then validity must be checked at the end (sequence has no
                    # inversion). We enforce incrementally: e allowed iff none of
                    # its ancestors is unused-but... can't decide. Fall through to
                    # explicit sequence check below (we pass full sequence).
                    pass
                t += dp(mask | (1 << e), j + 1) if _seq_ok(mask, e, j) else 0
        return t

    # We need sequence memory, not just mask: different orders give same mask.
    # So dp over mask undercounts (merges orders). Instead enumerate sequences
    # directly with pruning (sizes here are tiny: |P|<=8, n<=8).
    seq = []

    def seq_ok(e):
        # e may be placed next iff no already-placed element is a strict
        # successor of e... i.e. for all placed q: e not < q in P (else e should
        # have come before q). Ancestor relation: e<q iff e in anc(q).
        for q in seq:
            if (predmask[q] >> e) & 1:
                return False
        return True

    def _seq_ok(mask, e, j):
        return seq_ok(e)

    count = [0]

    def rec(mask):
        if len(seq) == n:
            count[0] += 1
            return
        for e in range(nP):
            if not (mask >> e) & 1 and seq_ok(e):
                seq.append(e)
                rec(mask | (1 << e))
                seq.pop()

    rec(0)
    return count[0]


def aut_order(d, edges, u):
    a = 1
    for v in range(d):
        a *= math.factorial(u[v])
    seen = {}
    for key in edges:
        seen[key] = seen.get(key, 0) + 1
    for c in seen.values():
        a *= math.factorial(c)
    return a


def valency(d, edges, u, v):
    inc = sum(1 for (i, j), w in edges if i == v or j == v)
    return inc + u[v] + 2


def F_table(d):
    diags = enumerate_diagrams(d)
    rows = {}
    for k in range(0, 3 * d - 1 + 1):
        n = 3 * d - 1 - k
        tot = 0
        detail = []
        ok = True
        for Dd in diags:
            edges, u, mu = Dd["edges"], Dd["u"], Dd["mu"]
            nP, pm = build_poset(d, edges, u)
            assert nP == 3 * d - 1
            inj = count_injections(nP, pm, n)
            aut = aut_order(d, edges, u)
            csum = sum(math.comb(valency(d, edges, u, v) + k - 1, k) for v in range(d))
            num = mu * inj * csum
            if num % aut != 0:
                ok = False
                detail.append((edges, u, mu, inj, aut, csum, num, "NON-INT"))
            else:
                tot += num // aut
        rows[k] = (n, tot, ok)
    return rows


def main():
    for d in [1, 2, 3]:
        print(f"=== degree {d} (N_d={[None, 1, 1, 12][d]})")
        rows = F_table(d)
        for k, (n, tot, ok) in rows.items():
            flag = "" if ok else "  [NON-INTEGRAL!]"
            extra = ""
            if k == 0:
                extra = f"  (expect d*N_d = {d * [None, 1, 1, 12][d]})"
            print(f"  k={k} n={n}: F={tot}{extra}{flag}")
        print()


if __name__ == "__main__":
    main()
