# Self-review

## Correctness — PASS

The singular multipliers are exactly \(|(1-\omega^k)(1+b\omega^k)|\) under the stated Euclidean normalization. Squared modulus is a concave quadratic of the cosine, reducing **all** nonconstant Fourier modes to the extremal two cosine values for each parity. The even formula is the unique intersection of an increasing and a decreasing endpoint function; for odd orders \(n\ge5\) the smaller quadratic root occurs before the far-endpoint minimum, and the later range cannot compete. The triangle is handled separately. The endpoint \(b=1\) can introduce a second zero singular value for even orders; the definition takes the minimum over the full mean-zero subspace, so this degeneracy is correctly included rather than discarded. Large-order expansions follow from explicit root formulas. Full-matrix SVD and Fourier-grid diagnostic checks passed for \(3\le n\le100\); no finite check is substituted for proof.

## Originality — PASS (subject to independent priority assessment)

Emirov et al. (arXiv:2003.11152v1, 2020) develop polynomial graph filters of multiple shifts and distributed inversion; Chen et al. (arXiv:2205.06242v1, 2022) obtain general directed-circulant Fourier singular multipliers. The latter directly supplies the general spectral mechanism and implies the unoptimized Fourier-symbol identity, but does **not** state the explicit universal two-hop fixed-budget optimizer, the parity transition, or the complete equality-mode classification in the sections and appendix inspected. Segarra et al.'s graph-filter optimization (2017) targets approximation of a specified operator, not maximization of the least nonconstant difference gain. General trigonometric minimax and graph-weight optimization literature remain priority risks. The mathematical comparison concerns these exact implications, not mere title matching.

## Mathematical value — PASS

This solves a natural fully specified signal-stability design problem rather than exhibiting an arbitrary small computation: under a fixed outgoing-conductance budget, it identifies the unique optimal directed two-hop stencil in every cycle size, the limiting frequency obstructions, and an asymptotically twofold reduction in worst-case inverse noise amplification. The resonance of the lowest and highest discrete frequencies supplies a structural explanation for the parity-dependent formulas. Scope remains two-hop, nonnegative, fixed-budget; the finding is not promoted to arbitrary graphs or mixing-time optimization.

## Remaining scientific risks

Earlier cyclic-filter or trigonometric maximin theory might imply the closed forms without using this wording; full historical priority has not been independently checked. The result is not an independent verification of any earlier research.

Self-review: passed. Independent audit: not yet performed.
