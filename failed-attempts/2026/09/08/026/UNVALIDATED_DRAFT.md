# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Certified Hamiltonicity–girth–expansion census of connected cubic bipartite graphs, n ≤ 16

## 1. Result

**Theorem.** Up to isomorphism, the numbers of connected cubic bipartite simple
graphs on $n$ vertices are exactly

| $n$ | 6 | 8 | 10 | 12 | 14 | 16 |
|---|---|---|---|---|---|---|
| #classes | 1 | 1 | 2 | 5 | 13 | 38 |

and **every one of these 60 graphs is Hamiltonian**. Each class carries a
machine-checkable certificate: explicit edge list, explicit Hamiltonian cycle,
girth with witness cycle, exact combinatorial 6-cycle count, full adjacency
spectrum (two-routine cross-check + trace identities), algebraic connectivity
$\lambda_2$ (= adjacency gap $3-\lambda_{\max-1}$ for cubic regular), and a
bridgelessness proof (every edge lies on a cycle). The class list is proved
pairwise non-isomorphic and complete by two independent enumeration routes
whose transversals agree (13/13 at $n=14$, both directions). Hamiltonicity is
decided twice: DFS backtracker (stored cycle) and Held–Karp DP (independent
replay, all 60 agree). The counts 1,1,2,5,13,38 agree with the published
sequence A060851 prefix, an external sanity check.

**High-girth witnesses (verified Hamiltonian).**
- $n=14$: unique girth-6 class, $c_4=0$, $\operatorname{tr}(A^6)=1554$,
  $\lambda_2 = 2-\sqrt2 \approx 1.585786$ (maximal $\lambda_2$ at $n=14$),
  edges `[[0,7],[0,8],[0,12],[1,8],[1,9],[1,13],[2,9],[2,10],[2,7],[3,10],[3,11],[3,8],[4,11],[4,12],[4,9],[5,12],[5,13],[5,10],[6,13],[6,7],[6,11]]`
  (bipartition $\{0..6\}$ vs $\{7..13\}$),
  girth witness $[9,2,7,0,8,1]$, Hamiltonian cycle
  $[0,7,2,9,1,8,3,10,5,13,6,11,4,12]$.
- $n=16$: unique girth-6 class, $c_4=0$, $\operatorname{tr}(A^6)=1680$,
  $\lambda_2 \approx 1.267949$ (maximal at $n=16$),
  Hamiltonian cycle $[0,8,2,10,7,11,3,12,4,15,6,14,5,13,1,9]$ (edges in artifact).

**Corollary (no small non-Hamiltonian example).** There is no non-Hamiltonian
connected cubic bipartite graph on $n \le 16$ vertices; in particular the
target-plan's "minimal-order non-Hamiltonian witness" does not exist in this
range — every graph is bridgeless (verified edge-by-edge), so bridge
obstructions never occur, and no 2-cut obstruction occurs either. This is
consistent with the literature placing the smallest 3-connected
non-Hamiltonian cubic bipartite graph at 50 vertices (Georges–Kelmans):
small non-Hamiltonicity would have to come from cuts, and the census shows
even cut-obstructed examples are absent at $n \le 16$.

## 2. Method (reproducible, stdlib + numpy only)

Every cubic bipartite simple graph is 3-edge-colourable (Kőnig), hence a union
of three perfect matchings. Fix $M_1 = \mathrm{id}$ by relabelling; $M_2$ is a
derangement $\sigma$ taken over integer-partition cycle types; $M_3$ is a
derangement $\tau$ avoiding $\sigma$, taken over $C_{S_m}(\sigma)$-orbit
lex-min representatives. Completeness: any such graph has a perfect matching
$ M_1$ (Hall, regular bipartite) and $G - M_1$ is 2-regular bipartite, hence
two further perfect matchings. Cross-dedup by invariant bucketing
(girth, $c_4$, $\operatorname{tr}(A^6)$, rounded spectrum) plus exact
bipartite isomorphism backtracking. Raw connected preimages:
$n=14$: 217 (4 discarded disconnected); $n=16$: 1837 (17 discarded).

## 3. Verification (all in `output/artifacts/`)

- `pipeline.py` — enumeration + invariants + backtracking Hamiltonicity.
- `verify.py` — independent replay: cubic/connected/bipartite/balanced checks,
  girth recomputation with witness-edge validation, exact combinatorial
  6-cycle count, two-routine spectrum + $\operatorname{tr}(A^2)=3n$,
  $\operatorname{tr}(A)=0$ checks, exact Hamiltonian-cycle edge validation,
  per-edge bridgelessness (BFS avoiding each edge), all-pairs
  non-isomorphism with an independent backtracker. Result: all 60 classes pass.
- `transversal_check.py` — completeness cross-check with a *different*
  transversal (random conjugate $\sigma$ per type + Schreier-BFS
  first-seen $\tau$ rule + independent WL-refined iso code): raw 217,
  13 classes, 13/13 cross-match both directions; Held–Karp DP replays
  Hamiltonicity for all 13 ($n=14$) and all 38 ($n=16$).
- `census_verified.json` — the 60 certified classes (edges, cycles, spectra).
- `verify_rows.json`, `transversal_check.json` — replay logs.
- `backup/` — original per-order census files preserved.

## 4. Scope, limits, honesty

- Claimed range is $n \le 16$ (complete, certified), **not** 14–26: $n=18$
  enumeration was started but did not finish in the available time
  (expected 152 classes per A060851; next term 449 at $n=20$), so orders
  18–26 are explicitly **not claimed**. The fallback "14–22 + partial 24–26"
  was likewise out of reach; we claim the smaller complete theorem instead.
- "New" does not mean the counts were unknown (they match A060851); the
  contribution is the *joint certified dataset*: every representative with
  Hamiltonian cycle + girth witness + spectrum/expansion + bridgelessness,
  replayable in seconds with stdlib + numpy.
- Originality vs cited literature: Georges–Kelmans minimality (50 vertices,
  3-connected), Barnette sufficiency theorems, and asymptotic spectral-gap
  work are all disjoint from this small-order joint census; see topic file.

## 5. How to replay

```
python3 output/artifacts/verify.py            # full independent replay (~1 min)
python3 output/artifacts/transversal_check.py # completeness + Held-Karp (~2 min)
python3 output/artifacts/pipeline.py 14       # re-enumerate n=14 (~1 s)
```
