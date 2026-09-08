# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Exact chromatic/Tutte census for eight polyhedral graphs with a certified
root-free interval and two Beraha-proximate root enclosures

## 1. Committed graphs and certificates of class membership

All graphs are 3-connected planar (polyhedral), verified by two independent
exact checks replayed in `artifacts/verify.py`:

- 3-connectivity: removal of every vertex pair leaves a connected graph.
- planarity: committed integer straight-line embeddings with exact
  proper-segment intersection test (no crossing among disjoint-edge pairs).

| id | graph | n | m | degrees sorted | P(3) | ao = (-1)^n P(-1) | tau = T(1,1) |
|----|-------|---|---|---|---|---|---|
| G1 | cube | 8 | 12 | 3^8 | 114 | 1862 | 384 |
| G2 | wheel W8 | 8 | 14 | 3^7 7^1 (hub deg 7) | 0 | 2184 | 841 |
| G3 | wheel W9 | 9 | 16 | 3^8 8^1 (hub deg 8) | 6 | 6558 | 2205 |
| G4 | square antiprism | 8 | 16 | 4^8 | 0 | 4968 | 3528 |
| G5 | pentagonal prism | 10 | 15 | 3^10 | 180 | 14700 | 1805 |
| G6 | wheel W10 | 10 | 18 | 3^9 9^1 (hub deg 9) | 0 | 19680 | 5776 |
| G7 | hexagonal prism | 12 | 18 | 3^12 | 858 | 109334 | 8100 |
| G8 | capped pentagonal prism | 11 | 20 | 3^5 4^5 5^1 | 0 | 115560 | 30976 |

Full edge lists, embeddings, and degree sequences are in
`artifacts/results.json`.

## 2. Exact chromatic polynomials (fresh deletion-contraction)

Each polynomial below was computed by memoized deletion-contraction
`P(G) = P(G-e) - P(G/e)` with component-factor splitting, then replayed from
the committed edge lists by the independent verifier. Memo-table sizes
(number of stored states) are listed. Structural identities hold for all:
monic degree n, second coefficient -m, `P(0)=P(1)=0`, coefficient sum 0.

- G1 cube (573 states):
  `P = q^8 - 12q^7 + 66q^6 - 214q^5 + 441q^4 - 572q^3 + 423q^2 - 133q`
- G2 wheel W8 (561 states):
  `P = q^8 - 14q^7 + 84q^6 - 280q^5 + 560q^4 - 672q^3 + 447q^2 - 126q`
- G3 wheel W9 (1084 states):
  `P = q^9 - 16q^8 + 112q^7 - 448q^6 + 1120q^5 - 1792q^4 + 1792q^3 - 1023q^2 + 254q`
- G4 square antiprism (1081 states):
  `P = q^8 - 16q^7 + 112q^6 - 446q^5 + 1086q^4 - 1596q^3 + 1285q^2 - 426q`
- G5 pentagonal prism (2378 states):
  `P = q^10 - 15q^9 + 105q^8 - 450q^7 + 1303q^6 - 2651q^5 + 3795q^4 - 3670q^3 + 2146q^2 - 564q`
- G6 wheel W10 (2109 states):
  `P = q^10 - 18q^9 + 144q^8 - 672q^7 + 2016q^6 - 4032q^5 + 5376q^4 - 4608q^3 + 2303q^2 - 510q`
- G7 hexagonal prism (9148 states):
  `P = q^12 - 18q^11 + 153q^10 - 810q^9 + 2970q^8 - 7936q^7 + 15823q^6 - 23640q^5 + 26020q^4 - 20080q^3 + 9700q^2 - 2183q`
- G8 capped pentagonal prism (4454 states):
  `P = q^11 - 20q^10 + 185q^9 - 1045q^8 + 4003q^7 - 10896q^6 + 21380q^5 - 29825q^4 + 28131q^3 - 15994q^2 + 4080q`

## 3. Tutte evaluations with triple cross-checks

For each graph, with `tau` = spanning-tree count and `ao` = acyclic-orientation
count:

1. `tau` by exact Matrix-Tree (Bareiss fraction-free determinant) equals the
   brute-force `C(m, n-1)` spanning-tree enumeration.
2. `tau` satisfies a one-edge deletion-contraction identity
   `tau(G) = tau(G-e) + tau(G/e)` with both sides evaluated independently by
   Matrix-Tree (loops from contraction correctly discarded).
3. `ao = (-1)^n P(-1)` re-expanded from committed coefficients equals the
   brute-force `2^m` orientation-acyclicity enumeration (Kahn test) and an
   independent deletion-contraction `ao(G) = ao(G-e) + ao(G/e)` recursion.

Recorded splits (G-e plus G/e), brute-force tallies, and tree counts:

| id | tau | tau(G-e) | tau(G/e) | ao | ao(G-e) | ao(G/e) |
|----|-----|------|------|-----|------|------|
| G1 | 384 | 276 | 108 | 1862 | 1318 | 544 |
| G2 | 841 | 441 | 400 | 2184 | 1394 | 790 |
| G3 | 2205 | 1153 | 1052 | 6558 | 4182 | 2376 |
| G4 | 3528 | 2058 | 1470 | 4968 | 3012 | 1956 |
| G5 | 1805 | 1282 | 523 | 14700 | 10408 | 4292 |
| G6 | 5776 | 3025 | 2751 | 19680 | 12540 | 7140 |
| G7 | 8100 | 5763 | 2337 | 109334 | 77500 | 31834 |
| G8 | 30976 | 16080 | 14896 | 115560 | 61928 | 53632 |

The wheel values agree with closed forms (e.g. hub-spoke family), and the
prism values with the prism family; these agreements are noted as consistency
remarks, not used as proof steps.

## 4. Certified real-root-free interval for the cube (Theorem 1)

**Theorem 1.** The chromatic polynomial of the cube has no real zero in the
closed interval [2,3]. In particular its real zeros are exactly {0, 1}.

*Proof.* Exact Sturm sequence over Q (Fractions) for the degree-8 cube
polynomial has degrees 8,7,6,5,4,3,2,1,0. Sign-variation counts give
V(2) = V(3) = 3, so zero roots in (2,3] by Sturm's theorem; endpoint values
`P(2) = 2`, `P(3) = 114` are nonzero, closing the endpoints. A quarter-mesh
sign table (all positive: 2, 5/2, ...) is logged in `sturm.json`.
Since P(0) = P(1) = 0 and the Sturm count over (2,3] is zero with P(2),P(3)
nonzero, the closed interval [2,3] is root-free; combined with the factored
trivial zeros the cube's only real chromatic zeros are 0 and 1 (the Sturm
table counts all real roots of the full polynomial, so no hidden real root
outside [2,3] beyond 0,1 exists either — verified by the total real-root
count: V(-inf)-V(+inf) replayable from the sequence). The interval [2,3]
strictly extends the (1,2) interval known to fail universally for
3-connected graphs (Royle), so per-graph certification is genuine content. ∎

## 5. Isolated Beraha-proximate chromatic roots of the square antiprism (Theorem 2)

**Theorem 2.** The chromatic polynomial of the square antiprism (G4) has
exactly one simple real zero `r1` in `[643/256, 645/256]` = [2.5117, 2.5195]
and exactly one simple real zero `r2` in `[871/256, 873/256]` = [3.4023, 3.4102].
Both brackets have strict endpoint sign changes, Sturm count exactly 1, and
strictly positive derivative at both endpoints (simplicity). The gap bracket
`(645/256, 871/256]` contains exactly one root (the integer root q = 3), so
r1 and r2 are isolated from each other and from all other real zeros.

*Proof.* Exact rational evaluation gives endpoint values of opposite sign
(logged as exact fractions in `sturm.json`); the exact Sturm sequence
(degrees 8,7,5,4,3,2,1,0) yields variation drop exactly 1 across each
bracket and exactly 1 across the gap; derivative positivity at all four
endpoints certifies simplicity. The verifier replays all evaluations and
counts. ∎

Proximity to Beraha numbers (computed evidence, not a limit claim):
`B5 = 2.61803`; bracket r1 lies within 0.107 of B5.
`B8 = 3.41421`; bracket r2 lies within 0.012 of B8 (its upper end is 0.004
below B8's exact value region... precisely, |r2 - B8| < 0.012).
No accumulation or exact-equality claim is made.

## 6. Originality and relation to prior work

- Shrock-Xu studies Tutte-ratio asymptotics for infinite triangulation
  families, not per-graph deletion-contraction tables with certificates.
- Backman's Tutte-activity survey gives the general identities we instantiate
  (T(1,1) = trees, T(2,0) = orientations), not the numerical tables.
- Royle shows (1,2) contains chromatic roots for some 3-connected graphs, so
  our per-graph [2,3] certificate is not mechanically implied.
- Harvey-Royle B10 existence is general; our r1/r2 enclosures are for the
  committed antiprism edge list with replayable logs.
- No source tabulates these eight polynomials with recursion-state counts,
  triple cross-checks, and Sturm logs for these edge lists.

## 7. Limitations and uncertainty

- The eight graphs are classical polyhedral representatives, not an exhaustive
  census; no universality beyond them is claimed.
- Complex (nonreal) zeros are located only numerically (numpy discovery, not
  certified); the certified claims concern real zeros only.
- Beraha proximity is a numerical observation with certified enclosures, not a
  theorem about accumulation points.
- Wheel/prism closed-form agreement is a consistency remark, not a proof step.

## 8. Reproduction

Run `python3 artifacts/verify.py` (stdlib only): replays deletion-contraction
for all eight graphs from committed edge lists, Matrix-Tree plus brute-force
tree counts, brute-force orientation counts, one-edge DC identities,
3-connectivity, and all Sturm counts — 86 checks, all passing.
