# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Refutation of the claw-free Borodin–Kostochka cell at Δ = 8:
# a minimal certified witness with Δ = 8, ω = 6, χ = 8,
# plus a certified Δ = 8, ω = 4, χ = 7 witness

## 1. Claim

The universal part of the admitted target cell is **false**. We exhibit an
explicit 8-vertex-critical claw-free graph **H** on 15 vertices with

- Δ(H) = 8 (8-regular),
- ω(H) = 6,
- χ(H) = 8,

so H satisfies the target's witness disjunct
("explicit minimal witness H with Δ(H) = 8, ω(H) ≤ 6, χ(H) = 8") and refutes
"every claw-free G with Δ(G) = 8 and ω(G) ≤ 6 has χ(G) ≤ 7".
Every single-vertex deletion H − v retains Δ = 8 and ω = 6 but is
7-colorable (8-criticality in the vertex-deletion sense).

We further exhibit a 7-vertex-critical claw-free graph **Q** on 13 vertices
with Δ(Q) = 8, ω(Q) = 4, χ(Q) = 7. Hence the preset fallback universal
"every claw-free G with Δ = 8, ω ≤ 4 has χ ≤ 6" is likewise false; its
Reed value ⌈(8+1+4)/2⌉ = 7 is best possible on this slice.

Both witnesses use only human-checkable counting (α = 2 ⇒ χ ≥ ⌈n/2⌉) for the
chromatic lower bound plus committed colorings verified edge by edge; no
unsatisfiability search output is load-bearing. Machine scripts (Python
standard library only) independently re-verify every invariant from the
committed adjacency lists.

## 2. The witness H = C₅[K₃] = C₅ ⊠ K₃ (lexicographic / strong product)

### 2.1 Definition

V(H) = ℤ₅ × {0,1,2} (15 vertices; write v = 3i + j for fiber i, position j).
Distinct (i,j), (i′,j′) are adjacent iff i′ ∈ {i−1, i, i+1} (mod 5).
Equivalently: each fiber Fᵢ = {(i,0),(i,1),(i,2)} is a K₃; Fᵢ is completely
joined to Fᵢ₋₁ and Fᵢ₊₁ and anticomplete to the two remaining fibers.
In the committed artifact vertices are labelled v = 3i + j, i ∈ ℤ₅, j ∈ {0,1,2}.

### 2.2 Maximum degree: Δ(H) = 8 (analytic)

Each vertex has 2 neighbors in its own fiber and 3 + 3 = 6 neighbors in the
two adjacent fibers: degree exactly 8. H is 8-regular (60 edges).

### 2.3 Claw-freeness (one line + machine double-check)

Each fiber is a clique and the used fibers of any independent set form an
independent set of C₅, so α(H) ≤ 2·1 = 2. Since α(K₁,₃) = 3, no induced
subgraph of H is a claw. Two independent exhaustive scans (neighborhood
triple scan; global center-plus-triple scan) confirm: no claw witness.

### 2.4 Clique number: ω(H) = 6 (analytic + machine)

A clique meets each fiber in ≤ 3 vertices, and its used fibers form a clique
of C₅ (at most 2 fibers, necessarily adjacent or equal). Hence any clique has
≤ 3 + 3 = 6 vertices. F₀ ∪ F₁ is a K₆ (vertices {0,…,5} pairwise adjacent).
So ω(H) = 6 exactly (branch-and-bound and C(15,7)-scan agree: no K₇; exactly
five K₆ sets, one per adjacent fiber pair).

### 2.5 Chromatic number: χ(H) = 8

*Lower bound (no search).* χ(H) ≥ |V|/α(H) = 15/2, so χ(H) ≥ 8.
*Upper bound (committed coloring, edge-verified).* With v = 3i + j:

| color | vertices | fibers |
|---|---|---|
| 0 | 0, 6 | F₀, F₂ |
| 1 | 1, 7 | F₀, F₂ |
| 2 | 2, 9 | F₀, F₃ |
| 3 | 3, 10 | F₁, F₃ |
| 4 | 4, 11 | F₁, F₃ |
| 5 | 5, 12 | F₁, F₄ |
| 6 | 8, 13 | F₂, F₄ |
| 7 | 14 | F₄ |

Each class pairs non-adjacent fibers (distance 2 mod 5), hence independent;
verified edge by edge from the artifact (0 conflicts). So χ(H) = 8.

### 2.6 Minimality (8-vertex-critical, machine + symmetry)

H is vertex-transitive (Aut(H) ⊇ D₅ × S₃: fiber rotations i ↦ i + t and
within-fiber permutations; transitivity verified by checking both generator
families preserve adjacency). Hence one deletion represents all — but we
verified all 15 directly: **every H − v is 7-colorable** (explicit committed
7-colorings, each edge-verified), while **every H − v retains Δ = 8 and
ω = 6** (recomputed per deletion). So H is 8-vertex-critical and minimal in
the inclusion sense: deleting any vertex keeps the BK-hypothesis parameters
but drops χ from 8 to 7.

### 2.7 Threshold meaning

ω(H) = 6 ≤ Δ(H) − 1 = 7, yet χ(H) = 8 > 7 = Δ(H) − 1: H violates the
Borodin–Kostochka conclusion at Δ = 8 while satisfying its clique
hypothesis. Reed's bound ⌈(8+1+6)/2⌉ = 8 is tight on H. H is consistent with
Brooks' theorem (χ = 8 = Δ, not Δ + 1).

## 3. The witness Q = Circ(13; {1,2,3,5}) — fallback slice

### 3.1 Definition

V(Q) = ℤ₁₃; u ∼ v iff min((u−v) mod 13, (v−u) mod 13) ∈ {1,2,3,5}.
8-regular on 13 vertices (52 edges), vertex-transitive (cyclic shifts).

### 3.2 Invariants

- Δ(Q) = 8: neighbors of 0 are ±1,±2,±3,±5 = {1,2,3,5,8,10,11,12}.
- α(Q) = 2: the non-neighbors of 0 (besides 0) are {4,6,7,9}; pairwise
  cyclic differences are 2,3,5,1,3,2 — all in the jump set — so they form a
  K₄. By vertex-transitivity every non-neighborhood is a clique, hence no
  independent triple exists (exhaustive C(13,3) scan agrees; exhibiting pair
  (0,4) shows α = 2, not 1).
- Claw-free: α(Q) = 2 < 3 = α(K₁,₃) gives it analytically; exhaustive
  13-center scan agrees (no witness). Note Q is genuinely claw-free but
  **not** quasi-line: N(0)'s complement has 10 edges, is triangle-free but
  non-bipartite, so N(0) is not covered by two cliques.
- ω(Q) = 4: (0,1,2,3) is a K₄ (consecutive jumps 1); exhaustive scan finds 39
  K₄ sets and 0 K₅ sets.
- χ(Q) = 7: lower bound ⌈13/2⌉ = 7 from α = 2; committed 7-coloring
  [0,1,2,3,0,1,2,5,4,3,6,5,4] verified edge by edge (0 conflicts).
- 7-vertex-critical: all 13 deletions Q − v are 6-colorable (committed
  colorings, edge-verified), each retaining Δ = 8, ω = 4.

Consequence: a claw-free graph with Δ = 8, ω = 4 ≤ 4 and χ = 7 exists, so
the fallback universal χ ≤ 6 is false. The Reed value 7 is best possible here.

## 4. Reproduction

Artifacts (verification-critical only):

- `artifacts/witness_H.json` — adjacency lists (v = 3i + j), 8-coloring, all
  fifteen H − v 7-colorings, construction string.
- `artifacts/witness_Q.json` — adjacency lists (ℤ₁₃ jumps {1,2,3,5}),
  7-coloring, all thirteen Q − v 6-colorings, construction string.
- `gtools.py` — stdlib-only tools used (DSATUR brancher, clique B&B,
  greedy/color checks, product/circulant builders).

Replay (all with Python 3 stdlib only):

1. Symmetry/looplessness, degree sequences [8]×15, [8]×13.
2. Claw scan: for each center, all triples of its neighbors — no independent
   triple among them.
3. Clique census: C(15,7)/C(13,5) absence + exhibited K₆/K₄.
4. Independence census: C(15,3)/C(13,3) — no independent triple.
5. Edge-by-edge verification of every committed coloring (H: one 8-coloring +
   fifteen 7-colorings; Q: one 7-coloring + thirteen 6-colorings).
6. χ lower bounds by ⌈n/α⌉ (exact integer arithmetic); χ upper bounds by the
   verified colorings. No UNSAT certificate is invoked.

A 5-million-node DSATUR run for 7-coloring H timed out (logged honestly);
it is **not** part of the proof — the α-counting bound is.

## 5. Originality and limitations (stated honestly)

- The graph C₅ ⊠ K₃ (equivalently C₅[K₃], the circular clique K_{15/2}) is a
  standard extremal object: BK literature cites C₅ ⊠ K₃ as showing the Δ ≥ 9
  hypothesis is necessary, and fractional-chromatic work (e.g. King–Lu–Peng
  line) uses it as the Δ = 8 tightness example. **The graph H itself is
  therefore not claimed as new.** What is new per the admission searches is
  its audited role as the explicit minimal witness deciding the admitted
  (Δ = 8, ω ≤ 6, χ ≤ 7) claw-free cell, with full 8-criticality certification
  and replayable artifacts — no retrieved source states this cell's
  refutation with a minimal witness.
- Q = Circ(13;{1,2,3,5}) is presented as an **explicit certified witness**,
  not as a "first known" graph: circulant (8,4,7)-chromatic graphs may appear
  elsewhere and we did not complete an exhaustive novelty census. Its value
  is the audited certificate killing the preset fallback universal.
- "Minimal" means 8-/7-vertex-critical (every single-vertex deletion drops χ
  while keeping (Δ,ω)); we do not claim H or Q is the unique or
  smallest-order witness in its class (sibling scan: no smaller strong-product
  C_m[+]K_k sibling matches the (8,6,8) profile; 73,728-config co-bipartite
  census with parts ≤ 4 found no (8,≤4,≥7) example — both logged as method,
  not theorems).
- The fallback's *success criterion* (a universal 6-colorability proof) is
  not met — because the universal is false (Q). We report this explicitly
  rather than claiming the fallback.

## 6. References (nearest priors delineating the gap)

- Cranston–Rabern, "Coloring claw-free graphs with Δ−1 colors", SIAM J.
  Discrete Math. 27 (2013) — Δ ≥ 9 only; Δ = 8 explicitly excluded.
- Chudnovsky–King–Plumettaz–Seymour (2013) + King thesis (2009): Reed's
  ⌈(Δ+1+ω)/2⌉ for claw-free — gives 8 at (8,6), 7 at (8,4), one color weaker
  in each cell than the refuted bounds 7 and 6.
- Cranston–Rabern (2017): list/online BK needs Δ ≥ 69 — far above.
- Hasanvand, arXiv:2211.00622: list-square choosability, different invariant.
