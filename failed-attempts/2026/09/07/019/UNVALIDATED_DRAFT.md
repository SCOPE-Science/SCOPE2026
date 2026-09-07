# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Seeded dot-product census at order 26: hypohamiltonian status and extremal symmetry among Blanusa × Petersen descendants — DRAFT

**Lane 23. Status: CLAIMED (partial census + explicit extremal witness). All computations replayable in seconds–minutes per graph from `output/artifacts/`.**

## 1. Claim

**Theorem (computational census, provenance-restricted).**
Let `P10` be the Petersen graph, `B18_1, B18_2` the two 18-vertex Blanusa snarks as fixed below (obtained as the two `P.P` dot-product types), and `J5` the Isaacs flower snark of order 20. Let F be the set of cubic bridgeless graphs of order 26 obtainable as a single Isaacs dot product `B18_i . P10` in either orientation (edge-factor / vertex-factor), over Aut-orbit representatives of independent edge-pairs × adjacent vertex-pairs × all 8 wirings. Then:

- (a) There are 1280 orbit-representative candidates (1040 `B.P` + 240 `P.B`), all bridgeless, falling into **109 non-isomorphic types**.
- (b) All 109 are snarks (bridgeless + chromatic index 4, i.e. not 3-edge-colourable), all have **girth 5**, `|Aut|` distribution `1^65 2^32 4^10 8^2`.
- (c) All 109 are non-Hamiltonian and traceable (have a Hamiltonian path); **87 are hypohamiltonian** (G non-Hamiltonian + all 26 `G−v` Hamiltonian), 22 are not (each with a named non-Hamiltonian `G−v`).
- (d) **Extremal witness.** There exists an explicit order-26 cubic hypohamiltonian snark `W26` in F with within-family minimal symmetry `|Aut|=1` and girth 5, distinguishing it from seeds `(|Aut|(P10),|Aut|(B18_1),|Aut|(B18_2),|Aut|(J5)) = (120,4,8,20)`. Example `W26` = rep 8 (`B18_1 . P10`, see §3) with full certificates below. Maximal-symmetry hypohamiltonian members have `|Aut|=8` (reps 1032, 1272, order 26 vs seed order 18).

No claim is made beyond this seeded subfamily; in particular no claim of a girth ≥7 graph and no claim of completeness for all cubics of order 26.

## 2. Definitions and seeds (explicit, no assumed invariants)

- **Petersen `P10`** (0–9): outer `0-1-2-3-4-0`, spokes `i-(i+5)`, inner star `5-7-9-6-8-5`. Edge list:
  `[(0,1),(0,4),(0,5),(1,2),(1,6),(2,3),(2,7),(3,4),(3,8),(4,9),(5,7),(5,8),(6,8),(6,9),(7,9)]`.
- **Flower `J5`** (`k=2`, 20 vertices, `A(i)=4i,B(i)=4i+1,C(i)=4i+2,D(i)=4i+3`, mod 5): edges `B(i)-A(i),B(i)-C(i),B(i)-D(i),A(i)-A(i+1),C(i)-D(i+1),D(i)-C(i+1)`. Computed girth 5, `|Aut|=20`, non-3-edge-colourable, non-Hamiltonian, `J−v` Hamiltonian for tested `v` (comparison only).
- **Dot product** (Goedgebeur–Zamfirescu / Isaacs, arXiv:1608.07164 §2): `G' = G−{ab,cd}` (independent edges), `H' = H−{x,y}` (adjacent cubic vertices), `N_H(x)\{y}={x1,x2}`, `N_H(y)\{x}={y1,y2}`, add `{a-x1,b-x2,c-y1,d-y2}` up to the 8 bijections (block swap + within-block swaps). Output order `n1+n2−2`. Both orientations enumerated.
- **Blanusa seeds via `P.P`:** `P` has 75 independent edge-pairs in 2 Aut-orbits (`((0,1),(2,3))`, `((0,1),(3,8))`) and 1 vertex-pair orbit (`(0,1)`). The 16 orbit×wiring `P.P` products collapse to **exactly 2 non-isomorphic types**, both cubic bridgeless girth-5 non-3-edge-colourable:
  - `B18_1` (|Aut|=4): `[(0,4),(0,5),(0,12),(1,2),(1,6),(1,13),(2,7),(2,10),(3,4),(3,8),(3,14),(4,9),(5,7),(5,8),(6,8),(6,9),(7,9),(10,11),(10,15),(11,12),(11,16),(12,17),(13,15),(13,16),(14,16),(14,17),(15,17)]`
  - `B18_2` (|Aut|=8): `[(0,4),(0,5),(0,12),(1,2),(1,6),(1,13),(2,3),(2,7),(3,4),(3,10),(4,9),(5,7),(5,8),(6,8),(6,9),(7,9),(8,14),(10,11),(10,15),(11,12),(11,16),(12,17),(13,15),(13,16),(14,16),(14,17),(15,17)]`
  Both verified hypohamiltonian by both solvers (G non-Hamiltonian + all 18 `G−v` Hamiltonian with verified cycles) and verified snarks. This matches the published fact that both Blanusa snarks are `P.P` dot products; we fix these edge lists as seeds. `|Aut|` computed by `GraphMatcher` enumeration (120/4/8/20 for P/B1/B2/J5).

## 3. Primary witness `W26` (rep 8, minimal symmetry)

Provenance: edge-factor `B18_1` with `ab=[0,4], cd=[1,6]`, vertex-factor `P10` with `x=0,y=1`, wiring 0, orientation `B.P`. Group size 18 (18 of 1280 candidates isomorphic to it).

Adjacency (0–25, cubic, 39 edges):
```
0: [5,12,20]; 1: [2,13,18]; 2: [1,7,10]; 3: [4,8,14]; 4: [3,9,21]; 5: [0,7,8];
6: [8,9,22]; 7: [2,5,9]; 8: [3,5,6]; 9: [4,6,7]; 10: [2,11,15]; 11: [10,12,16];
12: [0,11,17]; 13: [1,15,16]; 14: [3,16,17]; 15: [10,13,17]; 16: [11,13,14];
17: [12,14,15]; 18: [1,19,23]; 19: [18,20,24]; 20: [0,19,25]; 21: [4,23,24];
22: [6,24,25]; 23: [18,21,25]; 24: [19,21,22]; 25: [20,22,23]
```
Edge list (sorted): `[[0,5],[0,12],[0,20],[1,2],[1,13],[1,18],[2,7],[2,10],[3,4],[3,8],[3,14],[4,9],[4,21],[5,7],[5,8],[6,8],[6,9],[6,22],[7,9],[10,11],[10,15],[11,12],[11,16],[12,17],[13,15],[13,16],[14,16],[14,17],[15,17],[18,19],[18,23],[19,20],[19,24],[20,25],[21,23],[21,24],[22,24],[22,25],[23,25]]`.

Certificates:
- Order 26, cubic, bridgeless (no bridges via `networkx.bridges`), girth 5 (BFS), `|Aut|=1` (exhaustive `GraphMatcher` enumeration, 0.03 s), not 3-edge-colourable (exhaustive backtracking with symmetry-breaking, 0.01 s) ⇒ snark.
- `G` non-Hamiltonian: three independent DFS paths agree — Solver A (start 0, fail-first + degree/connectivity pruning), Solver B (start 25, reversed order + component-boundary pruning), naive DFS without pruning (102 206 nodes, 0.017 s). No Hamiltonian cycle exists.
- All 26 `G−v` Hamiltonian: both solvers return a verified cycle per `v` (each checked edge-by-edge). Cycles below are in `G−v` reindexed labels (`delete_vertex` mapping: new=old for old<v, new=old−1 for old>v; add 1 to every label ≥v to recover original labels; `v` absent):
```
G-0: [0,1,9,10,11,16,14,12,15,13,2,3,8,6,4,7,5,21,23,20,22,24,19,18,17,0]
G-1: [0,4,6,1,9,10,11,16,14,12,15,13,2,7,5,8,3,20,22,17,18,23,21,24,19,0]
G-2: [0,4,6,8,3,2,7,5,21,23,20,22,24,19,18,17,1,12,14,9,10,15,13,16,11,0]
G-3: [0,11,10,9,14,16,13,15,12,1,2,6,4,7,5,8,3,20,22,17,18,23,21,24,19,0]
G-4: [0,4,7,3,13,15,10,9,2,6,8,5,21,23,20,22,24,19,18,17,1,12,14,16,11,0]
G-5: [0,11,10,9,14,16,13,15,12,1,2,6,8,5,7,3,4,20,22,17,18,23,21,24,19,0]
G-6: [0,11,10,15,12,1,2,9,14,16,13,3,7,5,6,8,4,20,22,17,18,23,21,24,19,0]
G-7: [0,5,7,3,13,15,12,14,16,11,10,9,2,1,17,18,23,21,6,8,4,20,22,24,19,0]
G-8: [0,5,7,2,9,10,15,13,3,4,8,6,21,23,20,22,24,19,18,17,1,12,14,16,11,0]
G-9: [0,11,10,15,12,1,17,18,23,21,6,8,5,7,2,9,14,16,13,3,4,20,22,24,19,0]
G-10: [0,5,7,2,1,12,14,16,11,10,15,13,3,8,6,9,4,20,22,17,18,23,21,24,19,0]
G-11: [0,11,16,13,15,12,14,10,2,1,17,18,19,24,22,20,23,21,6,8,3,4,9,7,5,0]
G-12: [0,5,7,2,1,12,15,11,10,14,16,13,3,8,6,9,4,20,22,17,18,23,21,24,19,0]
G-13: [0,5,7,9,4,3,8,6,21,23,20,22,24,19,18,17,1,2,10,14,16,13,15,11,12,0]
G-14: [0,5,7,9,4,3,8,6,21,23,20,22,24,19,18,17,1,2,10,11,15,13,14,16,12,0]
G-15: [0,5,8,6,21,23,20,22,24,19,18,17,1,13,15,11,10,2,7,9,4,3,14,16,12,0]
G-16: [0,5,7,2,1,13,15,10,11,12,16,14,3,8,6,9,4,20,22,17,18,23,21,24,19,0]
G-17: [0,12,11,10,15,13,16,14,3,4,9,7,2,1,17,18,19,24,22,20,23,21,6,8,5,0]
G-18: [0,5,7,9,4,20,22,24,19,18,23,21,6,8,3,14,16,11,10,2,1,13,15,17,12,0]
G-19: [0,19,24,22,18,1,2,10,11,12,17,15,13,16,14,3,8,6,21,23,20,4,9,7,5,0]
G-20: [0,5,7,2,10,11,16,14,3,8,6,9,4,20,22,24,21,23,19,18,1,13,15,17,12,0]
G-21: [0,12,11,10,15,17,14,16,13,1,2,7,5,8,3,4,9,6,21,23,19,18,22,24,20,0]
G-22: [0,5,7,2,10,11,16,14,3,8,6,9,4,21,23,19,20,24,22,18,1,13,15,17,12,0]
G-23: [0,5,7,2,10,11,16,14,3,8,6,9,4,21,23,22,24,20,19,18,1,13,15,17,12,0]
G-24: [0,5,7,9,4,21,23,18,19,20,24,22,6,8,3,14,16,11,10,2,1,13,15,17,12,0]
G-25: [0,20,19,18,23,21,24,22,6,8,5,7,9,4,3,14,16,11,10,2,1,13,15,17,12,0]
```
- Hashes: WL `b499c8dddc6eb308067d5237b8d492d3` (networkx 3.6.1; WL collides on cubics — not used for dedup), invariant key `(girth, #5-cycles, #6-cycles, diameter) = (5,11,7,6)`, `sha256(sorted edgelist) = 13dd1ecf…163e39277`.
- Hypotraceability screen: `G` has a Hamiltonian path (True), consistent with hypohamiltonian ⇒ traceable.

## 4. Full subfamily table (summary; full machine-readable data in artifacts)

- Candidates 1280 → bridgeless 1280 → 46 invariant buckets (largest 108) → 109 isomorphism types (explicit `GraphMatcher` within buckets + cross-bucket verification, 26.6 s + 2.2 s).
- Invariant buckets e.g. `(5,11,8,6):108, (5,10,10,6):78, …` (see `enumerate.py` log).
- All 109: girth 5; `|Aut|`: 1×65, 2×32, 4×10, 8×2; all non-3-edge-colourable ⇒ snarks; all `G` non-Hamiltonian (A/B agree, no timeouts), all `G` traceable.
- 87 hypohamiltonian reps: `[0,8,32,48,56,64,72,88,96,104,112,120,128,136,144,152,160,168,264,272,280,288,296,304,312,320,352,360,376,384,400,424,464,488,496,504,536,544,552,560,568,576,584,592,600,608,616,624,632,648,656,664,672,712,768,776,784,792,800,808,816,824,832,840,864,888,896,904,912,928,936,944,952,960,968,976,984,992,1000,1008,1016,1024,1032,1128,1240,1264,1272]` (rep indices into 1280; `B.P`:83, `P.B`:4).
- 22 non-witnesses with first non-Hamiltonian `G−v` (all `B.P`): `16:v0,24:v0,40:v0,80:v0,176:v9,184:v3,192:v0,208:v3,216:v0,224:v3,232:v9,248:v0,256:v3,328:v1,336:v1,344:v0,392:v0,408:v9,696:v0,736:v0,848:v0,880:v0`. Each `G` non-Hamiltonian (logged) so obstruction is either `G` itself plus this `v`.
- `P.B` orientation collapses to 4 types (reps 1128,1240,1264,1272), all hypohamiltonian.

## 5. Methods, replay, and limitations (honest)

- No nauty available. Dedup used WL hash (observed to collide on all 9000 `P.P` products, so not relied upon) + custom invariant `(girth,5-/6-cycle counts,diameter)` for bucketing + exhaustive `GraphMatcher.is_isomorphic` within buckets + pairwise re-check. Two hash paths (WL + invariant) + explicit isomorphism satisfy the audit's "canonical-hash + fallback + explicit test" intent with different tooling; we do **not** claim nauty hashes.
- Hamiltonicity via two independently coded DFS solvers (different starts/orders/pruning) agreeing on all 2943 decisions (`G` + `G−v` where needed) plus a third naive DFS spot-check (witness `G`: 102k nodes; obstructions agree). Cycles machine-verified edge-by-edge. Non-Hamiltonicity "logs" are solver node/time statistics + replayable code, not full exponential transcripts — full transcripts are infeasible to publish.
- 3-edge-colouring via single backtracker with symmetry-breaking (verified on cube/dodecahedron/K4 positives); no second colourer. `|Aut|` via `GraphMatcher` enumeration (fast here: ≤0.1 s/graph; worst-case exponential in general).
- Seeds: Blanusa lists are defined as the two `P.P` types (theorem-backed) with computed `|Aut| 4/8`; we did not import external LCF tables. If literature labels `B1/B2` swapped, the pair as a set is still the Blanusa pair (exactly two 18-vertex snarks). `J5` from the published `J_{2k+1}` formula.
- Scope is strictly the seeded `B×P` order-26 dot-product subfamily, not all order-26 cubics/snarks. Originality claim is only the provenance-restricted table + extremal tuple, not general existence (order-26 hypohamiltonian snarks were known to exist).

## 6. Replay

```
python3 output/artifacts/enumerate.py   # 30 s: seeds → 1280 cands → 109 reps (seeds.json, reps.json)
python3 output/artifacts/census.py      # ~15 s: 109 reps → census.json (girth/|Aut|/colour/hypo + cycles)
python3 output/artifacts/certify_witness.py  # witness detail
```
Libs: `pipeline_lib.py` (seeds, dot product, solvers A/B/path/colouring), `orbits_lib.py` (Aut orbits, dedup), `gen_cands.py` (invariants). Requires `networkx` only.

## References

- Goedgebeur–Zamfirescu, On hypohamiltonian snarks and a theorem of Fiorini, arXiv:1608.07164 (definitions, dot-product, flower-snark formula, Blanusa = P.P, hypohamiltonian-snark existence).
- Goedgebeur–Zamfirescu, Improved bounds for hypohamiltonian graphs, arXiv:1602.07171 (orders 18/19 counts, girth-6 smallest order 25).
- Brinkmann–Goedgebeur–Hägglund–Markström, Generation and properties of snarks (counts to 36).
