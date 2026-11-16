# Self-review

## Correctness: PASS
The object is fully normalized, the affine action is unitary, and every allowed character is checked. The exact quotient ring \(\mathbb Z[\xi_{24}]\) is represented by its eight-term basis modulo \(X^8-X^4+1\); characteristic polynomials are recomputed from exact traces, not approximate determinants. Twelve orbit-representative Gram matrices (three affine classes times four odd characters) give the three claimed squared quartics. Exact orbit enumeration covers all \(126\) four-subsets, and independent rational sign isolations identify all sixteen relevant extrema. The antiunitary \(J^2=-I\) argument explains multiplicity two. The result has no unproved infinite-family extension.

## Originality: PASS, with residual historical-priority risk
The 2021 harmonic Grassmannian construction is not new. The most important directly overlapping public result proves that the eight-dimensional order-nine harmonic fusion planes are block-full-spark; its own scope excludes sharp smallest-positive-singular-value bounds and contains no three-quartic spectral census. The new claim is explicitly the complete four-block spectra and exact sharp numerical-stability bounds. The related real quadratic-character family over order thirteen uses a different representation and yields a different four-set classification. Generic erasure-robust frame bounds and totally symmetric EITFF constructions do not imply this nonconstant three-orbit spectrum. Searches cannot eliminate unindexed older specialist computations.

## Mathematical value: PASS
The case \(\mathbb F_9\) is the smallest odd nonprime field for this two-plane harmonic frame construction; all four odd characters are covered. At the first critical four-block size, the known rank guarantee does not quantify conditioning. The exact three-level orbit classification distinguishes sharply differing stability losses and identifies all maximally unstable masks, giving a concrete optimal adversarial-erasure bound. Its precise eigenvalue data are structurally significant for the natural root-of-unity frame, not a postselected arbitrary parameter slice.

## Limits
Finite exact theorem only. No assertion of publication priority beyond inspected sources; no general field-order stability theorem or independent validation is claimed. Reproduce with `python3 verify_f9.py`.

Self-review: passed. Independent audit: not yet performed.
