# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exact chromatic polynomials of 17 plantri-natural triangulations on 8–12 vertices, with a certified non-3-colorability witness and a real-root gap

## 1. Objects (explicit, generator-free)

Disk near-triangulations (hub + path/rim), $n=8,\dots,12$:

- Wheel $W_n$: hub $0$ joined to rim cycle $1-\cdots-(n-1)-1$ ($m=2(n-1)$).
- Fan $F_n$: hub $0$ joined to path $1-\cdots-(n-1)$ plus path edges ($m=2n-3$).

Sphere triangulations ($m=3n-6$), $n=8,\dots,12$:

- Bipyramid $D_n$: apexes $0,1$ joined to equator cycle $2-\cdots-(n-1)-2$ plus cycle edges.
- Stacked $S_9$: $K_4$ on $\{0,1,2,3\}$ with vertices $4,\dots,8$ stellated in
  greedily (each new vertex joined to one face triple).
- Icosahedron $I_{12}$: apexes $0,11$, upper ring $1$–$5$, lower ring $6$–$10$,
  edges $0U_i$, $11L_i$, ring cycles, and $U_iL_i$, $U_iL_{i-1}$ (indices mod 5).

All edge lists are stored verbatim in `output/artifacts/tables.json`
(`edges` field) and replayed by `verify.py`.

## 2. Exact polynomials (committed table)

Coefficients low$\to$high; $P_G(q)=\sum c_iq^i$.

| $G$ | $n,m$ | coefficient list |
|---|---|---|
| $W_8$ | 8,14 | 0, −126, 447, −672, 560, −280, 84, −14, 1 |
| $F_8$ | 8,13 | 0, −64, 256, −432, 400, −220, 72, −13, 1 |
| $D_8$ | 8,18 | 0, −664, 1992, −2432, 1595, −615, 141, −18, 1 |
| $W_9$ | 9,16 | (see tables.json) |
| $F_9$ | 9,15 | (see tables.json) |
| $D_9$ | 9,21 | (see tables.json) |
| $W_{10}$ | 10,18 | (see tables.json) |
| $F_{10}$ | 10,17 | (see tables.json) |
| $D_{10}$ | 10,24 | (see tables.json) |
| $W_{11}$ | 11,20 | (see tables.json) |
| $F_{11}$ | 11,19 | (see tables.json) |
| $D_{11}$ | 11,27 | (see tables.json) |
| $W_{12}$ | 12,22 | 0, −2046, 11263, −28160, 42240, −42240, 29568, −14784, 5280, −1320, 220, −22, 1 |
| $F_{12}$ | 12,21 | 0, −1024, 6144, −16640, 26880, −28800, 21504, −11424, 4320, −1140, 200, −21, 1 |
| $D_{12}$ | 12,30 | 0, −58024, 250756, −480554, 542325, −402090, 206262, −74886, 19290, −3465, 415, −30, 1 |
| $S_9$ | 9,21 | 0, 1458, −5103, 7533, −6183, 3105, −981, 191, −21, 1 |
| $I_{12}$ | 12,30 | 0, −121020, 463310, −782108, 780286, −517360, 241605, −81622, 20023, −3500, 415, −30, 1 |

(Ten middle rows are fully listed in `tables.json`; the shorthand above keeps
this draft readable. The verifier recomputes every check from that file.)

Integer evaluations (both methods agree; $P(0)=P(1)=P(2)=0$ throughout):

| $G$ | $P(3)$ | $P(4)$ |
|---|---|---|
| $W_8$ | 0 | 504 |
| $F_8,D_8,W_9,F_9$ | 6 | 768, 288, 1032, 1536 |
| $D_9$ | 0 | 504 |
| $W_{10}$ | 0 | 2040 |
| $F_{10},D_{10},W_{11},F_{11}$ | 6 | 3072, 1056, 4104, 6144 |
| $D_{11}$ | 0 | 2040 |
| $W_{12}$ | 0 | 8184 |
| $F_{12},D_{12}$ | 6 | 12288, 4128 |
| $S_9$ | 0 | 24 |
| $I_{12}$ | 0 | 240 |

**Theorem 1 (exact table).** For each of the 17 graphs above, the listed
$P_G$ equals the chromatic polynomial. *Proof.* Method A: memoized
deletion–contraction DAG with leaf reductions (edgeless $q^n$, complete
falling factorial, disjoint components, pendant/isolated vertex factors,
chordal PEO product, cycle closed form); branching $P(G)=P(G-e)-P(G/e)$
with canonical edge-set keys (node budgets: max 25 623 DAG nodes for
$I_{12}$, all others $<8\,300$). Method B (independent program path):
degeneracy-ordered backtracking color counter agrees at $q=0,1,2,3,4$
for all 17; polynomials are monic of degree $n$ with $P(1)=P(2)=0$.
The independent `verify.py` replays all of Method B plus structural
checks from the bare edge lists. ∎

## 3. Non-3-colorability witness

**Theorem 2.** $P_{W_8}(3)=0$: the 8-vertex wheel with rim $C_7$ is not
3-colorable, and it is vertex-deletion-minimal for this property.
*Proof.* Exhaustive symmetry-broken backtracking over the hub-first order
finds 0 proper 3-colorings (replayed by `verify.py`). Deleting the hub
leaves $C_7$ with $126= (3-1)^7-(3-1)$ colorings; deleting any rim vertex
leaves a 7-vertex wheel with even rim $C_6$, with exactly 6 colorings each.
Hence every one-vertex deletion is 3-colorable. ∎
(Remark: $S_9$ also has $P(3)=0$ but is not deletion-minimal — every
one-vertex deletion still has 0 colorings — so $W_8$ is the clean minimal
witness.)

## 4. Beraha-flavored real-root gap

Let $B_7 = 2+2\cos(2\pi/7) \approx 3.24698 < 10/3$.

**Theorem 3.** No graph in the 17-family has a real chromatic root in the
open interval $J=(10/3,\,4)$. *Proof.* Exact Sturm sequences over
$\mathbb{Q}$ (Fraction arithmetic in `sturm.py`, replayed in `verify.py`):
sign-variation difference at the rational endpoints is $0$ for every
family member. ∎

Exact Beraha-$B_5$ values ($B_5=(3+\sqrt5)/2$), in the form
$P(B_5)=A+B\sqrt5$ with $A,B\in\mathbb{Q}$ (exact Horner in
$\mathbb{Q}(\sqrt5)$), e.g. $I_{12}$: $-4575+2046\sqrt5\approx-0.0049$;
$D_{12}$: $-1762+788\sqrt5\approx0.0216$; $S_9$: $123/2-55\sqrt5/2\approx0.0081$.
Full per-graph pairs are in `verify_report.json`. These are recorded data,
not an identity claim.

Real-root census notes (exact Sturm totals): fans have exactly 3 real
chromatic roots ($0,1,2$); $I_{12}$ has 6, including the largest real root
in the family at $\approx 3.22246\in(3,10/3)$, isolated to width $<10^{-6}$.

## 5. What is NOT claimed

- Not the full 297-class (let alone disk-class) census of the admitted
  target; only the 17 explicit plantri-natural members above.
- The gap is for real roots only (Sturm), not a complex-disc zero-free
  region; no Birkhoff–Lewis reduction log is supplied (leaf reductions
  above substitute for it).
- No Tutte golden identity is proved; $B_5$ evaluations are exact data points.
