# Scientific review

## Correctness

**PASS.** The result concerns all generalized paperfolding instruction sequences and every length divisible by four and at least eight. The proof derives a unique modulo-four starting phase from the nonalternating other track, proves compatibility with cyclic rotation, constructs a well-defined interleaving lift, excludes odd-position identifications, and exhausts even- and odd-start target factors. The factor-size identity follows from distinct representatives and their distinct one-position rotations. A standalone verifier checked 216 nontrivial length pairs with 18 instruction sequences, two independent word constructions, wordwise lifts, class maps and exact factor-count saturation. The universal conclusion is from the proof, not the finite tests.

## Originality

**PASS, with historical-priority qualification.** Cassaigne et al., Section 5.2 Proposition 20 (https://arxiv.org/abs/1402.5843), prove full rotation classes at lengths of the form \(4\cdot2^{j+1}\) for paperfolding words. This does not imply the all-multiple-of-four size-distribution lifting, for instance at length \(12\), where the classes are not full orbits. Allouche's factor count (https://doi.org/10.1017/S0004972700011655) fixes the sum of class sizes, not the class partition. The 1994 canonical-position work (https://doi.org/10.1016/0304-3975(94)90028-0) is a plausible additional historical source; its accessible description concerns positions of factors, and its complete text was not inspected. Unindexed or unpublished equivalent statements remain possible.

## Value

**PASS.** The theorem gives an exact all-class transfer between successive dyadic lengths for an uncountable family of generalized paperfolding sequences. It resolves the full restricted orbit-size distribution at length \(2n\) from the distribution at length \(n\) of the shifted instruction word, for infinitely many lengths beyond the previously established pure-power cases. It is a structural renormalization principle, not an isolated table entry or a rephrasing of ordinary factor complexity.

## Limitations

The length condition is essential to the marker-rotation argument; the regular word already violates count stabilization from length \(4\) to length \(8\). Same-word stabilization requires an instruction sequence fixed by the shift. The 1994 canonical-position article has only been compared at abstract level; complete historical-priority verification remains outstanding. The Python program is finite corroboration rather than an infinite proof.

Self-review: passed. Independent audit: not yet performed.
