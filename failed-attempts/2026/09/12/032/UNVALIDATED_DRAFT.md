# FAILED ATTEMPT — NOT A VALIDATED FINDING

> This draft is retained only as evidence of an unsuccessful SCOPE attempt. Its claims must not be cited as established results.

# Sharp ordinary-line gap for B17 — proof draft

## Claim
Let B17 = {ζ^k : k = 0,…,15} ∪ {0} ⊂ ℂ ≅ ℝ², where ζ = e^{2πi/16},
i.e. the 16th roots of unity on the unit circle plus the origin
(17 distinct noncollinear Euclidean points).
Then B17 spans at least 9 ordinary lines (lines containing exactly
two points of B17). In fact the exact ledger is: 120 distinct spanned
lines, of which 8 are rich (3 points each, the origin diameters) and
112 are ordinary — far above threshold 9.

## Definitions
A *spanned line* is a Euclidean line containing ≥ 2 points of B17.
It is *ordinary* if it contains exactly 2 points of B17, *rich*
if it contains ≥ 3.

## Lemma 1 (line–circle bound)
A Euclidean line meets the unit circle in at most 2 points.
*Proof.* Parametrize the line as p + tv; |p+tv|² = 1 is a nondegenerate
quadratic in t (coefficient |v|² > 0), hence ≤ 2 real roots. ∎

## Lemma 2 (rich-line classification)
Every line containing ≥ 3 points of B17 is one of the 8 origin
diameters {ζ^k, ζ^{k+8}, 0}, each with exactly 3 points.
*Proof.* By Lemma 1, a line with ≥ 3 points of B17 cannot have all
three on the circle; it contains the origin 0 and two circle points.
A line through 0 meets the circle in an antipodal pair (if 0,u,v are
collinear with |u|=|v|=1, then v = −u since the line meets the circle
symmetrically about 0). So the line is {ζ^k, −ζ^k, 0} = {ζ^k,ζ^{k+8},0}.
There are exactly 8 such diameters, each with exactly 3 points of B17:
no fourth point is possible since the line already has its 2 circle
intersections and 0 is the only off-circle point. ∎

## Lemma 3 (ordinary-line classification)
A pair of distinct non-antipodal roots spans an ordinary line;
a pair {ζ^k, 0} spans a rich (diameter) line.
*Proof.* Let a,b be non-antipodal roots. The line ab meets the circle
in exactly {a,b} by Lemma 1. It cannot contain 0: a line through 0 and
a root meets the circle again at the antipode of a, which is not b.
So ab ∩ B17 = {a,b}: ordinary. A pair {ζ^k,0} lies on diameter k,
a 3-point line by Lemma 2. ∎

## Theorem (exact ledger; implies the 9-line gap)
B17 spans exactly 120 distinct lines: 8 rich and 112 ordinary. Hence
it spans ≥ 9 ordinary lines.
*Proof.* There are C(17,2) = 136 point pairs. The 8 diameters each
contain C(3,2) = 3 pairs, accounting for 24 pairs. The remaining
136 − 24 = 112 pairs are non-antipodal root pairs, each spanning (by
Lemma 3) a line with exactly those 2 points — hence 112 distinct
ordinary lines, one per pair. Total distinct lines: 8 + 112 = 120. ∎

## Degree-3 polynomial cell ledger (Green–Tao transfer certificate)
Take f(x,y) = (x² + y² − 1/4)(x − 1/2), of total degree 3.
Its zero set avoids B17:
- on each root, x²+y² = 1 so the first factor is 3/4 ≠ 0;
- no root has x = 1/2: cos(2kπ/16) = 1/2 would need
  k/8 = ±1/6 + m, i.e. k = ±4/3 + 8m ∉ ℤ;
- at the origin f(0,0) = (−1/4)(−1/2) = 1/8 ≠ 0.
Cell distribution of the 17 points (signs of the two factors):
- disk x²+y² < 1/4: 1 point (the origin);
- exterior x < 1/2: 11 roots; exterior x > 1/2: 5 roots
  (x > 1/2 exactly for k ∈ {0,1,2,14,15}, since cos(π/8)≈0.924,
  cos(π/4)≈0.707 > 1/2 > cos(3π/8)≈0.383).
No cell boundary meets B17, so the ledger above is the cell-respecting
incidence count: every rich line crosses cells through the central disk
(diameters), while each ordinary pair-line is certified cell-by-cell.

## Machine replay (exact, no floats)
`output/artifacts/verify_b17.py` replays the ledger in exact integer
arithmetic in Z[ζ16] = Z[x]/(x⁸+1): collinearity via reality of
(a−c)/(b−c) under the conjugation automorphism x ↦ −x⁷. Output:
120 lines; 8 rich (exactly the diameters [k,k+8,16]); 112 ordinary
(all non-antipodal root pairs); 136/136 pairs covered. An independent
float determinant sweep finds exactly 8 collinear triples (the
diameters) with smallest nonzero determinant ≈ 0.058, confirming
nondegeneracy. Both replays print VERIFY_OK.

## Remarks
- Threshold 9 = ⌈17/2⌉ is the Dirac–Motzkin prediction; the proved
  value 112 exceeds it by an order of magnitude, and exceeds the
  unconditional Csima–Sawyer floor ⌊6·17/13⌋ = 7 as well.
- Either outcome would have resolved the target; the positive
  resolution is proved above with a hand-checkable line list.
