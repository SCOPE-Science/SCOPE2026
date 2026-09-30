# Certified census of class-number-125 imaginary quadratic fields through |d| ≤ 2×10⁷

## Context

Let d < 0 be a negative fundamental discriminant and H(d) the ideal class group
of the imaginary quadratic field Q(√d), of order h(d). The admitted target asked
for an unconditional proof that no H(d) is isomorphic to (Z/5Z)³, the elementary
abelian 5-group of rank 3 (order 125, exponent 5). The effective
Goldfeld–Gross–Zagier–Oesterlé bound forcing h(d) > 125 lies astronomically
beyond any enumerable range, so the infinitary half of the target is untouched.
What completed is the target's finite-check machinery at scale: a certified
exact census of every class-number-125 field through |d| ≤ 2×10⁷ with full
group-structure determination, which unconditionally excludes (Z/5Z)³ in that
window. This bears directly on the recognized missing-group problem for
(Z/pZ)³ (cf. Holmin–Jones–Kurlberg–McLeman–Petersen, Conjecture 1.10).

## Definitions

- Fundamental discriminant: d = −m with m squarefree and m ≡ 3 (mod 4), or
  d = −4m with m squarefree and m ≡ 1, 2 (mod 4).
- h(d): number of reduced binary quadratic forms (a,b,c) with b²−4ac = d,
  counted with weights (1 if |b| ∈ {0,a} or a = c, else 2).
- The three abelian groups of order 125 are distinguished by n_ord5, the number
  of non-identity classes of order dividing 5: C₁₂₅ → 4, C₂₅×C₅ → 24,
  (Z/5Z)³ → 124.

## Result (headline theorem)

There are exactly 290 negative fundamental discriminants d with
|d| ≤ 20,000,000 and h(d) = 125. Of the corresponding class groups, 279 are
cyclic C₁₂₅ and 11 are C₂₅×C₅, occurring at |d| = 258563, 320659, 394987,
548059, 569323, 669763, 1082083, 1103923, 1289803, 1295947, 1656883.
In particular, no imaginary quadratic field with |d| ≤ 2×10⁷ has class group
(Z/5Z)³.

## Proof / evidence

1. Census sieve (`artifacts/sieve.c`): enumerates (a,|b|,c) triples with
   D = 4ac−b² ≤ 2×10⁷, tests fundamentality by squarefree sieving, and
   accumulates weights. Output `hits20M.txt` (290 hits) and `sieve20M.log`
   (6079277 fundamentals, calibration h(−3)=h(−4)=h(−7)=h(−8)=h(−11)=h(−19)=1,
   h(−15)=h(−20)=h(−24)=2, h(−23)=h(−31)=3, h(−39)=4, h(−47)=5, h(−163)=1).
   All arithmetic is exact 64-bit integer arithmetic. An independent re-run at
   B = 2×10⁶ agreed 282/282 on the overlap; the auditor recompiled and
   re-ran the sieve at B = 5×10⁵ (131/131 match) and in the 2.0–3.5M window
   (8/8 match), plus an independent Python reduced-form check of samples.
2. Exact structure verifier (`artifacts/hnf.c`): for each candidate, enumerates
   all reduced forms (count cross-checks the sieve), composes classes by ideal
   multiplication in the maximal-order integral basis with exact HNF reduction
   and content division for imprimitive products, checks identity presence
   (hasid = 1), and computes f⁵ for every class. Logs `scan.log`/`scan2.log`
   classify all 290 fields: 279 with n_ord5 = 4, 11 with n_ord5 = 24, zero
   with 124. The auditor recompiled the verifier and reproduced h and n_ord5
   on calibration and sample discriminants.
3. The union of the two logs covers exactly the 290 census hits with no
   missing or extra entries.

## Limitations

Finite certified census only, not the unconditional theorem F((Z/5Z)³) = 0 over
all discriminants; absence beyond 2×10⁷ is not certified. Correctness rests on
the sieve weights and the HNF/content-division composition, validated by
calibration, identity checks, and independent re-execution but not externally
cross-checked against PARI/GP or Sage.

## Reproducibility

gcc -O2 -fopenmp -o sieve sieve.c -lm && ./sieve 20000000
gcc -O2 -o hnf hnf.c -lm && ./hnf <|d| list>

## References

- M. Watkins, Class numbers of imaginary quadratic fields, Math. Comp. 73 (2004).
- S. Holmin et al., Missing class groups and class number statistics, Exp. Math. (2017).
- A.-S. Elsenhans, J. Klüners, F. Nicolae, Imaginary quadratic fields with small exponent (2018).
- LMFDB, Class groups of quadratic imaginary fields dataset documentation.
