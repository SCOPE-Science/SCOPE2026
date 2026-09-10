# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Turán cell of the Fano-plus-tetrahedron pair: baseline, symmetrization, and order-7 optimality

## Claim (EMERGENT_FINDING; target pi = 5/9 + stability stays open)

Let `F7` be the Fano plane (7 vertices, 7 triples, each pair in exactly one
triple) and `K4^(3)` the complete 3-graph on 4 vertices. Let
`F = {F7, K4^(3)}`. We prove three structural facts that jointly fix the
Turan baseline and the symmetrization-induction half of any future
`pi(F) = 5/9` + stability proof, with exact integer-only certificates:

1. **Turan template theorem (all part sizes).** Every blow-up of the cyclic
   3-partite template with multiset edges `{012, 001, 112, 022}` is `F`-free,
   and the balanced blow-up has edge density `-> 5/9`. Hence
   `pi({F7,K4^(3)}) >= 5/9`.
2. **Cloning-preservation theorem (all host orders).** One-step Zykov cloning
   (`u -> v`: delete all edges at `u`, add `{u,x,y}` for `{x,y}` in the link
   of `v`) preserves `F`-freeness: `H` `F`-free implies the clone is `F`-free.
3. **Exact order-7 optimality.** `ex(7, F) = 23`, attained by the Turan
   `(3,2,2)` blow-up, proved optimal by branch-and-bound.

Supporting evidence: 477,965 labeled `K4`-free 3-graphs on 6 vertices out of
`2^20` (exact bitwise census); order-`<= 6` flag-SDP blindness lemma
(`F7` needs 7 vertices, so the pair-SDP equals the `K4`-alone SDP with
ceiling `0.561666 > 5/9`); seeded shape search at `n = 8, 9, 10` finding no
`F`-free graph beating Turan (36/54/75 vs 34/49/69).

## What is proved vs computed vs conjectured

- **Proved:** items 1–3 (finite exhaustive checks + structural proof steps).
- **Computed evidence (not optimality):** the `n = 8, 9, 10` simulated
  annealing search and the 13,080-step cloning spot-check.
- **Conjectured / open:** the target `pi(F) = 5/9` upper bound and the
  `o(n^3)`-stability classification; the preset `<= 0.56` flag certificate
  was attempted and is blocked in-pass (see Limitations).

## Proof sketches

**Template freeness.** A blow-up contains `F7` (resp. `K4`) iff some
part-assignment map `{0..6} -> {0,1,2}` (resp. `{0..3} -> {0,1,2}`) sends
every forbidden edge into a template multiset edge. Exhaustion of all
`3^7 = 2187` (resp. `3^4 = 81`) maps finds 0 good maps. Edge count for parts
`(n0,n1,n2)`: `n0*n1*n2 + C(n0,2)*n1 + C(n1,2)*n2 + C(n2,2)*n0`; along
`n = 3q` this is `(5q^3-3q^2)/2` over `C(3q,3) -> 5/9` exactly.

**Cloning preservation.** (M1) No edge of the clone contains both `u, v` by
construction. (M2) Every pair of `F7` vertices lies in an `F7` edge (21/21
pairs) and every pair of `K4` vertices in a `K4` edge (6/6), so a copy in the
clone holds at most one of `u, v`. (M3) If the copy holds `u` (not `v`), the
map `u |-> v` sends it to an isomorphic copy in `H` (untouched edges are
`H`-edges; added edges `uxy` come from `H`-edges `vxy`). Case split: a copy
avoiding `u` already lies in `H`; a copy through `u` transfers into `H` —
both contradict `H` `F`-free.

**Order-7 optimality.** Branch-and-bound over `2^35` with unit propagation
from 65 constraints (35 `K4`-quads + 30 Fano labelings), Turan incumbent 23:
OPTIMAL, 40.1M nodes.

## Reproduction

All checks use integer/bitwise arithmetic only (no floating point):

- `python3 t1_lower_bound.py` -> `output/artifacts/t1_certificate.json`
- `python3 t3b_preservation.py` -> `output/artifacts/t3b_preservation.json`
- `python3 t4_ex7.py` -> `output/artifacts/t4_ex7.json`
- `python3 t2a_census6.py`, `python3 t2b_scale7.py`,
  `python3 t3_symmetrization.py`, `python3 t5_shape_search.py` -> supporting
  certs (re-run at gate time OK for T1/T3b/T2a; T4 cert on disk).

## Limitations

- The asymptotic `5/9` upper bound and stability classification are NOT
  proved here.
- The preset `<= 0.56` order-`<= 7` flag PSD certificate is NOT delivered:
  order `<= 6` is provably blind and order 7 needs a full type census + SDP
  solve + rational rounding, blocked in-pass (timed recovery `~2.4e4 s`
  single-core raw checks; no scipy/cvxpy/networkx, no pip, apt denied;
  `n = 8` B&B exceeded the tool limit).
- The `n = 8, 9, 10` shape-search support is heuristic, not optimality.
