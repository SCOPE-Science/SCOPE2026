# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Ramsey–Turán interval for n=30, K4-free, α≤5: 180 ≤ RT(30,K4,6) ≤ 255, with circulant optimality

## 1. Definition

For integers n,k and graph H, let

  RT(n,H,k) = max{ e(G) : |V(G)|=n, H ⊄ G, α(G) < k }.

We study H=K4, n=30, k=6:

  RT(30,K4,6) = max{ e(G) : |V(G)|=30, K4 ⊄ G, α(G) ≤ 5 }.

Feasibility is non-vacuous because R(4,6) ≥ 36 (open interval [36,41] in the
literature), so K4-free α≤5 graphs exist on 30 vertices. Trivial bounds from
Turán's theorem are 75 ≤ RT ≤ 300 (see §4). We improve both sides rigorously
to 180 ≤ RT ≤ 255, with an explicit symmetric witness and a one-lemma Ramsey
degree bound. We additionally prove the witness is optimal among all
circulants. We do **not** claim the exact value, **not** claim DRAT/SAT
certificates, and **not** claim full extremal enumeration.

## 2. Results

**Theorem 1 (certified interval).**
  180 ≤ RT(30,K4,6) ≤ 255.

**Theorem 2 (circulant optimality).**
  Among all circulant graphs on 30 vertices, the maximum number of edges of a
  K4-free graph with α ≤ 5 is 180, attained for example by the 12-regular
  circulant with jump set J={4,5,6,8,10,13}. No circulant on 30 vertices with
  more than 180 edges is K4-free with α ≤ 5.

Theorem 1's lower bound is by explicit construction (§3) verified by
exhaustive enumeration of all C(30,4)=27405 quadruples and all
C(30,6)=593775 6-sets. Theorem 1's upper bound is by Lemma 1 plus counting.
Theorem 2 is by exhaustive enumeration over circulant jump sets combined with
the same verifiers plus the degree bound for high-degree cases.

## 3. Lower bound: 180-edge witness

### 3.1 Construction

Label vertices Z30 = {0,…,29}. Fix jump set J = {4,5,6,8,10,13} ⊂ {1,…,14}.
Join i to i±d (mod 30) for each d ∈ J. Since J ∩ (−J mod 30) = ∅ and 15 ∉ J,
the graph G0 is simple, vertex-transitive, 12-regular, hence e(G0)=30·12/2=180.
Explicit adjacency: N(i) = {i±4,i±5,i±6,i±8,i±10,i±13 mod 30}.
The 30×30 0/1 matrix is archived as `artifacts/best_adj.txt` (space-separated,
12 ones per row, symmetric, zero diagonal) and is deterministically
reproducible from J by the rule above.

Eleven further 12-regular feasible circulants were found; see
`artifacts/circulant_catalog.txt` (12 jump sets total). Any one suffices for
Theorem 1; we fix the above J as primary.

### 3.2 Verification (brute force, replayable)

Standalone verifier `artifacts/verify.py` (stdlib only):
- checks symmetry, zero diagonal, counts edges and degrees;
- enumerates all 27405 4-sets; fails if all 6 pairs present (K4);
- enumerates all 593775 6-sets; fails if all 15 pairs absent (independent 6-set).
On `best_adj.txt` it prints:
  edges=180 maxdeg=12 mindeg=12,
  K4 check passed (27405 quadruples),
  alpha<=5 check passed (593775 6-sets),
  VERIFIED.
Runtime is seconds in CPython. No SAT solver, no heuristics, no sampling:
both properties are decided by complete enumeration. Re-run:
  python3 output/artifacts/verify.py output/artifacts/best_adj.txt.

Hence a K4-free α≤5 graph with 180 edges exists, so RT(30,K4,6) ≥ 180.

## 4. Upper bound: RT ≤ 255

We use the known Ramsey number R(3,6)=18 (Greenwood–Gleason 1955; standard
table: any graph on 18 vertices contains a triangle or an independent 6-set).
Only the upper bound R(3,6) ≤ 18 is needed; we cite it as an external
dependency (see Limitations).

**Lemma 1 (codegree remark, not needed for U but recorded).**
If uv ∈ E(G) and G is K4-free, then N(u)∩N(v) is independent: two adjacent
common neighbours x,y together with u,v would form a K4.

**Lemma 2 (max degree).**
If G is K4-free with α(G) ≤ 5 then Δ(G) ≤ 17.

*Proof.* Suppose d(v) ≥ 18. Then G[N(v)] has ≥18 vertices and is
triangle-free: a triangle in N(v) plus v would be a K4. By R(3,6)=18 it
contains an independent 6-set, which is independent in G, contradicting
α(G) ≤ 5. ∎

**Corollary (U=255).** Any feasible G on 30 vertices has
e(G) ≤ n·Δ/2 ≤ 30·17/2 = 255. Hence RT(30,K4,6) ≤ 255.

*Remarks.* Trivial Turán T(30,3) gives e ≤ 300 (partitions 10,10,10). Lemma 2
shaves 45 edges. Complement Turán gives the trivial lower bound e ≥ 75 for any
feasible graph (complement K6-free ⇒ e(comp) ≤ Turán(30,5)=360 ⇒ e(G) ≥ 75);
our 180 improves it by 105. The heuristic expectation n²/8≈112 is exceeded by
the construction, showing the constant-α regime is denser than the o(n)
Ramsey–Turán asymptotics.

## 5. Circulant optimality (Theorem 2)

A circulant C30(J0) with J0 ⊂ {1,…,14} plus optional 15 has degree 2|J0|
(+1 if 15 included) and edges 30·deg/2. Exhaustion:
- deg 12 (k=6, 3003 graphs): exactly 12 feasible (all 180 edges), listed in
  catalog; each passed both exact checks.
- deg 14 (k=7, 3432 graphs): 170 K4-free, all contain an exhibited I6
  (randomized greedy finds one; no exact alpha check needed to reject).
  0 feasible.
- deg 16 (k=8): 49 K4-free, 0 feasible. deg 18 (k=9): 10 K4-free, 0 feasible.
- deg 20 (k=10): 1 K4-free (degree ≥18 forces I6 by Lemma 2 in any case).
- Odd deg 13 (k=6+15, 195 edges): 64 K4-free, 0 feasible.
- Odd deg 15 (k=7+15, 225 edges): 8 K4-free, 0 feasible.
- Odd deg 17 (k=8+15): 0 K4-free.
- k ≥ 9 even / k ≥ 9 odd have degree ≥18, so Lemma 2 alone forces α ≥ 6;
  no computation needed. k ≤ 5 even / k ≤ 5 odd have <180 edges and cannot
  beat the witness.
Method per graph: exact K4 enumeration (early exit on first K4 for speed);
if K4-free, 80–150 randomized greedy independent-set trials (finding an I6
certifies α ≥ 6 and rejects); only if greedy finds none, exact 593775-set
alpha check. All graphs with >180 edges were rejected at the greedy stage
except a handful checked exactly. Script: `artifacts/circulant_enum.py`;
helpers in `artifacts/search.py`. Total runtime < 1 min.

Thus no circulant beats 180, proving Theorem 2. This does **not** imply global
optimality: non-circulant feasible graphs with >180 edges may exist (upper
bound allows up to 255).

## 6. What was not done (honesty)

- No SAT encoding was solved; no CaDiCaL/Kissat/DRAT artifact is claimed.
  The 593775 α-clause CNF for m=181 was not built or proven UNSAT.
- No exact value m* is claimed; gap is 75 (180 vs 255), not ≤8.
- No enumeration of all extremals up to isomorphism (bliss/nauty) is claimed;
  only 12 circulant witnesses cataloged.
- Upper bound depends on cited R(3,6)=18; we did not re-prove it from scratch.
- Originality: Lemma 2 is folklore (immediate from R(3,6)); novelty is only the
  explicit 180-edge circulant interval and the reusable verified
  circulant-optimum benchmark for the R(4,6)-gap regime.

## 7. Reproduction

1. Rebuild witness matrix from J (see §3.1) or use archived matrix.
2. `python3 output/artifacts/verify.py output/artifacts/best_adj.txt`
   must report 180 edges, K4-free, α≤5.
3. (Optional) `python3 output/artifacts/circulant_enum.py --quick` re-checks
   k=6/k=7 even cases; full run without flag reproduces §5 counts.
4. Upper bound: inspect Lemma 2 proof; external fact R(3,6)=18 e.g.
   Greenwood–Gleason, Quart. J. Math. 1955, and standard Ramsey tables.

## Appendix: jump sets (12 feasible, degree 12)

[1,2,4,5,10,12], [1,2,4,9,10,14], [2,3,4,5,10,14], [2,3,4,8,10,13],
[2,3,7,8,10,14], [2,4,5,8,9,10], [2,5,6,7,10,14], [2,5,8,9,10,14],
[3,4,5,8,10,14], [4,5,6,8,10,13] (primary), [4,8,9,10,11,14],
[5,8,10,11,12,14].
