# Exact maximum M_3(2,7) = 15 for complete (k,3)-arcs in PG(2,7), with line spectra and NMDS certificates; record (15,3)-arc in PG(2,8) with interval k ≤ 19

## Context

In PG(2,q) (N = q²+q+1 points and lines, q+1 points per line), a (k,3)-arc is a
k-set with at most 3 points on any line (no 4-secant). It is complete if
maximal under inclusion: every point outside it lies on a line already
carrying 3 of its points (a 3-secant). Small complete (k,n)-arcs with few
characters and k near the plane order are a recognized hard problem with
finite-geometry and coding-theory applications (Korchmáros–Nagy–Szőnyi 2023);
the only exact (n,3)-arc packing in the literature is at q=16 (max 28, min 15;
Bartoli–Marcugini–Pambianco 2012). No source tables M_3(2,7), M_3(2,8), their
spectra, or UNSAT bounds. The (k,2)-arc minima/FOP tables (no 3 collinear)
do not imply (k,3) maxima.

## Definitions

- Line spectrum (n_0,n_1,n_2,n_3): number of lines meeting K in exactly i
  points. Satisfies Σ n_i = N and Σ i·n_i = k(q+1).
- Dimension-3 code reading: homogeneous coordinates of K as columns of a
  3×k matrix give a q-ary [k,3] code with weight distribution
  A_{k-i} = n_i·(q−1) (i=0..3), A_0=1, summing to q³; minimum distance k−3
  iff n_3 > 0.
- M_3(2,q): maximum k of a complete (k,3)-arc in PG(2,q).

## Result

**Theorem A (exact maximum at q=7).** M_3(2,7) = 15.

Witness K_7 (15 points over F_7, homogeneous coordinates):

    (1,0,0),(1,0,5),(1,0,6),(1,3,2),(1,3,3),(1,3,4),(1,4,0),(1,4,4),
    (1,4,5),(1,5,2),(1,5,3),(1,5,6),(1,6,2),(1,6,3),(1,6,5)

K_7 is a complete (15,3)-arc with spectrum (n_0,n_1,n_2,n_3) = (12,0,15,30),
and no (k,3)-arc in PG(2,7) has k ≥ 16.

**Theorem B (record + certified interval at q=8).** With GF(8)=GF(2)[x]/(x³+x+1)
(elements 0..7, x=2), the set K_8:

    (0,1,5),(0,1,6),(1,0,0),(1,0,2),(1,0,5),(1,1,0),(1,1,1),(1,2,6),
    (1,3,5),(1,4,2),(1,5,1),(1,6,2),(1,7,0),(1,7,1),(1,7,5)

is a complete (15,3)-arc in PG(2,8), maximal under inclusion, with spectrum
(12,18,12,31). Every (k,3)-arc in PG(2,8) satisfies k ≤ 19. Global optimality
at q=8 is not claimed; the maximum lies in {15,...,19}.

## Proof / evidence

Witness verification (both planes, `artifacts/verify.py` from coordinates only):
rebuild PG(2,q) incidence from scratch; check max line occupancy 3 (no
4-secant); spectrum sums: (12,0,15,30)→57 with 2·15+3·30=120=15·8, and
(12,18,12,31)→73 with 18+24+93=135=15·9; every outside point lies on a
3-secant (0 uncovered of 42 resp. 58); 0 addable points (single-point
maximality); NMDS identity gives q=7 {0:1,12:180,13:90,14:0,15:72} summing to
343=7³ and q=8 {0:1,12:217,13:84,14:126,15:84} summing to 512=8³, distance 12.

Upper bounds (`artifacts/bound.py`): fix P in K; the q+1 lines through P each
carry at most 2 further points of K, so k−1 ≤ 2(q+1), i.e. k ≤ 2q+3
(k ≤ 17 at q=7, k ≤ 19 at q=8). Refinement: writing t,s,u for lines through P
with 2,1,0 further points, t+s+u=q+1 and 2t+s=k−1. At q=7, k=16 forces unique
(t,s)=(7,1) and k=17 forces (8,0); then every point of K lies on exactly t
3-secants and double counting gives 3·t_3=k·t, so 3 | k·t — but
16·7=112 and 17·8=136 are both 1 mod 3, impossible. Hence k ≤ 15 at q=7, and
the 15-witness closes M_3(2,7)=15 (no search needed). At q=8, k=18 forces
(8,1) with 144=3·48 and k=19 forces (9,0) with 171=3·57, both consistent, so
only k ≤ 19 is certified. Stochastic q=8 searches plateauing at 15 are
reported as conjecture/evidence only.

## Limitations

Exact closure only at q=7. At q=8 the gap 16–19 remains open (conjectured
{15,16}); no exhaustive UNSAT is claimed there. No q=9 witness pursued.

## Reproducibility

Stdlib-only:

    python3 artifacts/verify.py artifacts/wit7.json artifacts/wit8.json
    python3 artifacts/bound.py

`verify.py` prints VERIFY_OK lines with spectra and NMDS distributions;
`bound.py` asserts the divisibility UNSAT and writes the per-(q,k) table to
`unsat_log.json`.

## References

- G. Korchmáros, G. P. Nagy, T. Szőnyi, Algebraic approach to the completeness
  problem for (k,n)-arcs in planes over finite fields, arXiv:2302.10162 (2023).
- D. Bartoli, S. Marcugini, F. Pambianco, The maximum and the minimum size of
  complete (n,3)-arcs in PG(2,16), arXiv:1201.2260 (2012).
- S. Marcugini, A. Milani, F. Pambianco, Minimal complete arcs in PG(2,q),
  q ≤ 32, arXiv:1005.3412 (2010).
- D. Bartoli et al., Tables, bounds and graphics of sizes of complete arcs
  ... (FOP), arXiv:1404.0469 (2014/2018).
