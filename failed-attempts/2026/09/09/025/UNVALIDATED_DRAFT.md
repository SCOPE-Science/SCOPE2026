# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Jones span, adequacy, and Khovanov width on the twisted-weaving 3-braid ray

## Objects
K_k = closure of (s1 s2^{-1})^{6k+1} s1^2, k = 0, 1, 2, ...
3-braid words; closure permutation (123), so each K_k is a knot.
Crossings n(K_k) = 12k+4; writhe w(K_k) = +2 for all k.

## Results (all recomputed from the braid words; no database lookup)

### 1. K_0 is the right-handed trefoil
- Jones V(K_0) = t + t^3 - t^4 (span 3), det = 3, writhe 2.
- det 3 classifies K_0 as 3_1 (mirror excluded by Jones/writhe sign).
- Integral Khovanov (SNF-certified, every block):
  free: Z at (0,1), (0,3), (2,5), (3,9); torsion: Z_2 at (3,7), nothing else.
- Width 2 (diagonals delta = 2i-j in {-3,-1}); thin; Z_2-only torsion.

### 2. K_k for k >= 1: adequate alternating diagrams, span = crossings
- Verified (single-flip criterion, every crossing, k = 1..8):
  A- and B-adequate, sA = 6k+2, sB = 6k+4, Turaev genus gT = 0.
- Hence each such diagram is alternating; K_k is an alternating knot.
- Jones spans (two independent methods agree: 2^n state cube for k<=1,
  TL_3 transfer matrix calibrated against cube for all k):
  k=1: span 16 (range -6..10); k=2: 28; k=3: 40; ... span(K_k) = 12k+4 = n.
- Full Jones polynomials for k<=8 in output/artifacts/jones_ray.json
  (V(1)=1 and sum e*c_e=0 checked for every row).
- By Lee (alternating => thin), Khovanov width(K_k) = 2 for all k>=1,
  supported on diagonals delta in {sigma..sigma+2} with torsion Z_2-only
  on the lower diagonal (alternating-link structure theorem).

### 3. The admitted target claim is REFUTED as stated
- Target: span(K_k) = 2(6k+1)+c with one constant c; fixing c=1 from K_0
  predicts span(K_1) = 15; actual span(K_1) = 16 (two-method agreement).
- Corrected law: span(K_0) = 3 (non-alternating 4-crossing diagram of 3_1);
  span(K_k) = 12k+4 for k>=1 (adequate, alternating).
- No odd torsion appears (K_0 certified Z_2-only; K_k alternating => thin,
  Z_2-only by the alternating structure theorem, citing Lee/Shumakovitch).
  The Sazdanovic-Przytycki Z_2-only expectation is SUPPORTED (not refuted)
  on this ray; the "odd-torsion witness" branch is empty here.

### 4. Fallback table (admission fallback_claim: satisfied and exceeded)
- Exact Jones + spans for K_0..K_8 (committed range was k=0,1; delivered more).
- Integral SNF Khovanov table for K_0 (all 19 bigradings).
- F_2/F_3/F_5 Betti tables for K_0 (UCT-consistent with SNF).
- Adequacy/Turaev-genus certificates k=1..8; per-state Euler replay for K_1
  (65536 states; graded Euler == (q+q^-1)V(q^2)).

## Methods / replay
- output/artifacts/cube.py: braid-closure Kauffman cube (calibrated: unknot,
  kink, Hopf, both trefoils, figure-8, RII-dimension check).
- output/artifacts/tl.py: TL_3 transfer-matrix bracket + Jones (== cube on
  all shared tests after strand-support correction, documented in file).
- output/artifacts/kh.py, khdiff.py: Khovanov complex + F_p homology
  (d^2=0 verified; Euler-vs-Jones verified; fixed two real bugs en route:
  loop-sign, rank-elimination single-pass, merge/split misclassification).
- output/artifacts/snfc.py: integral SNF homology (sympy smith_normal_form).
- output/artifacts/jones.py: K_0/K_1 driver; jones_ray.json, jones_K0K1.json,
  adequacy.json: data.

## Limitations (honest)
- K_1 (16X) full integral SNF Khovanov NOT computed (1.7M-dim complex over Z;
  out of the remaining budget). Width/torsion claims for k>=1 rest on the
  computed adequacy + the CITED Lee thinness theorem, not on a computed cube.
- Alternating identification of K_k (k>=1) is via the computed adequate
  diagrams + Turaev gT=0 (which implies alternating); crossing-number
  minimality uses span == n (adequate => span = n is itself a check).
- K_0 = trefoil uses det-3 classification (classical) plus matching Jones.
- No infinite-k PROOF in the formal sense: the span pattern k=1..8 is computed
  evidence + the adequacy mechanism (sA/sB linear counts), not a written
  induction. Stated as computed law with mechanism, not as theorem.
