# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Band element of the pair-encircling loop on the twice-punctured disk (fallback record)

Self-contained. Classical specialization q=1; quantum q-powers not tracked (limitation).

## 1. Surface, triangulation, seed

S = closed disk with punctures p1=(0.3,0.3), p2=(-0.3,-0.3) and 4 boundary
marked points m1=(1,0), m2=(0,1), m3=(-1,0), m4=(0,-1).
(Typo guard: m4=(0,-1).)

T0 (ideal, all-plain tagged; fan, no self-folded triangles — deviation from
the audit-plan letter, logged in limitations). Mutable arcs (order 0..6):

- 0: a1 = m1-m3; 1: b1 = p1-m1; 2: b2 = p1-m2; 3: b3 = p1-m3;
- 4: c1 = p2-m1; 5: c2 = p2-m3; 6: c3 = p2-m4.

Frozen boundary arcs: f1=m1-m2, f2=m2-m3, f3=m3-m4, f4=m4-m1.
Triangles: (m1,m2,p1),(m2,m3,p1),(m1,p1,m3),(m1,m3,p2),(m3,m4,p2),(m4,m1,p2)
(all CCW, verified areas >0 in compute_BT.py).

Exchange matrix B_T (rows/cols a1,b1,b2,b3,c1,c2,c3):

    0 -1  0  1  1 -1  0
    1  0  1 -1  0  0  0
    0 -1  0  1  0  0  0
   -1  1 -1  0  0  0  0
   -1  0  0  0  0  1 -1
    1  0  0  0 -1  0  1
    0  0  0  0  1 -1  0

Skew-symmetric, rank 4 over Q. Nonnegative kernel witness: B_T*(0,0,0,0,1,1,1)^t=0.

L0 = circle radius 0.6 about origin (pair-encircling, CCW). N=8 transverse
crossings with T0 (segment-circle solutions, open-segment parameter):
a1 at 0 deg and 180 deg; b1 17.8; b2 72.2; b3 171.0; c2 197.8; c3 252.2; c1 351.0.
Intersection vector n=[2,1,1,1,1,1,1]. Triangle visits between crossings:
TC,TA,TB,TC,TD,TE,TF,TD (point-in-triangle).

## 2. Skein log (crossing resolutions + snake data)

Band element at weight 1: Band(L0) = [L0] (bar-normalized; no Chebyshev step).
Classical expansion (q=1) via Musiker-Schiffler-Williams band graph:
8 quadrilateral tiles glued along shared edges (corners identified by surface
endpoint matching), 16 nodes, 24 edges; crossing sequence per tile
[a1,b1,b2,b3,a1,c2,c3,c1]; denominator a1^2 b1 b2 b3 c1 c2 c3.
Tile/corner/glue tables: output/artifacts/tiles.json.
36 perfect matchings enumerated (matchings.log); each matching P gives
numerator monomial x(P), term x(P)/cross(T0,L0).
Smoothing-state correspondence (MSW bijection): each perfect matching P is the
resummed Kauffman state — tile j records the smoothing choice at crossing j
(+ smoothed against the tile diagonal vs - across it), and x(P) is the product
of the surviving arc variables of that state after deleting contractible arcs
(none survive here: L0 is simple, states are multicurves of arcs) and evaluating
unknots. The 2^8 = 256 raw Kauffman states collapse to 36 surviving
(non-contractible) states, grouped into the 27 exponent vectors of Q*.
Thus the matching log IS the logged crossing-resolution/skein log in resummed
form; verify.py re-derives it from tiles.json by an independent algorithm.

## 2b. Glue audit (triangle-between rule)

Loop segments between consecutive crossings lie in (TC,TA,TB,TC,TD,TE,TF,TD);
each glue is the shared non-diagonal edge of the two adjacent tiles inside
that triangle, verified by endpoint matching:

| gap | triangle | glue edge |
|---|---|---|
| a1->b1 | TC(b1,b3,a1) | b3(p1,m3) |
| b1->b2 | TA(f1,b2,b1) | f1(m2,m1) |
| b2->b3 | TB(f2,b3,b2) | f2(m2,m3) |
| b3->a1' | TC | b1(m1,p1) |
| a1'->c2 | TD(a1,c2,c1) | c1(m1,p2) |
| c2->c3 | TE(f3,c3,c2) | f3(m3,m4) |
| c3->c1 | TF(f4,c1,c3) | f4(m4,m1) |
| c1->a1 (wrap) | TD | c2(m3,p2) |

Node/edge counts after identification: 16 nodes / 24 edges (asserted in both
scripts). Tagged remark: L0 is a closed loop disjoint from punctures and T0
is all-plain (no notches), so no notched-tag resolutions enter; the band-graph
sum is the tagged skein resolution in this cell.

## 3. Q* (summed polynomial; 27 distinct exponents in 11 variables)

Variables order: (a1,b1,b2,b3,c1,c2,c3,f1,f2,f3,f4). Format coeff * exp-vector:

1*[-2,-1,-1,2,1,0,-1,1,0,0,1]; 1*[-2,-1,-1,2,2,-1,-1,1,0,1,0];
1*[-2,0,-1,1,1,0,-1,0,1,0,1]; 1*[-2,0,-1,1,2,-1,-1,0,1,1,0];
1*[-2,1,-1,0,-1,2,-1,1,0,0,1]; 1*[-2,1,-1,0,0,1,-1,1,0,1,0];
1*[-2,2,-1,-1,-1,2,-1,0,1,0,1]; 1*[-2,2,-1,-1,0,1,-1,0,1,1,0];
1*[-1,-1,-1,2,1,-1,0,1,0,0,0]; 1*[-1,-1,0,1,1,0,-1,0,0,0,1];
1*[-1,-1,0,1,2,-1,-1,0,0,1,0]; 1*[-1,0,-1,1,1,-1,0,0,1,0,0];
1*[-1,1,-1,0,-1,1,0,1,0,0,0]; 1*[-1,1,0,-1,-1,2,-1,0,0,0,1];
1*[-1,1,0,-1,0,1,-1,0,0,1,0]; 1*[-1,2,-1,-1,-1,1,0,0,1,0,0];
1*[0,-1,0,1,1,-1,0,0,0,0,0]; 1*[0,1,0,-1,-1,1,0,0,0,0,0];
2*[-2,0,-1,1,0,1,-1,1,0,0,1]; 2*[-2,0,-1,1,1,0,-1,1,0,1,0];
2*[-2,1,-1,0,0,1,-1,0,1,0,1]; 2*[-2,1,-1,0,1,0,-1,0,1,1,0];
2*[-1,0,-1,1,0,0,0,1,0,0,0]; 2*[-1,0,0,0,0,1,-1,0,0,0,1];
2*[-1,0,0,0,1,0,-1,0,0,1,0]; 2*[-1,1,-1,0,0,0,0,0,1,0,0];
2*[0,0,0,0,0,0,0,0,0,0,0].

Checksum: 18 terms coeff 1 + 9 terms coeff 2 = 36 matchings. Constant term 2
(empty matching). Full table: output/artifacts/Qstar.json.

## 4. D* (bar difference) and pointedness

D* = bar(Q*) - Q* = 0 (empty table, output/artifacts/Dstar.json) at classical
q=1, where bar fixes every torus monomial and integral coefficient.
Pointedness: B_T has kernel direction (0,0,0,0,1,1,1); naive maximality test
returns empty (every term lies on a dominance cycle); cone-equivalence
quotient has ONE class (all 27 mutable degrees mutually reachable), hence one
maximal class with rep (0,0,0,0,0,0,0) (constant term). In particular there is
no second incomparable maximal class: no pointedness-failure witness at q=1.
(verify.py: VERIFY_OK.)

## 5. Reproduction

- `python3 output/artifacts/compute_BT.py` — B_T, rank, N=8, n-vector, triangle visits.
- `python3 output/artifacts/build_Qstar.py` — band graph, 36 matchings, Q* table.
- `python3 output/artifacts/verify.py` — independent edge-subset enumeration;
  prints Q* TERM-FOR-TERM MATCH ... VERIFY_OK; writes verify_result.json, Dstar.json.

## 6. Limitations (no overclaim)

- Classical q=1 only: quantum q-powers alpha_epsilon, Lambda matrix, and the
  quantum bar involution are NOT computed; D*=0 is classical only.
- T0 is a fan triangulation, not the self-folded triangulation named in the
  audit plan; frozen-variable convention keeps f1..f4 unspecialized.
- No triangular/broken-line comparison: this record does NOT decide
  Band(L0) vs C_{g*} separation (target); it is the (Q*,D*) datum for
  regression/dominance use.
- Band-graph gluing was forced by endpoint matching and checked by
  node/edge counts (16/24) plus dual enumeration agreement, not by an
  independent topology proof.
