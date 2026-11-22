# Scientific review

## Correctness — PASS

The stated exact step criterion is reconstructed from the explicit three-by-three upper-triangular RK2 polynomial and the exact factorization of \(\det(I-T^{\mathsf T}T)\). The positive first factor and the unique strictly increasing largest singular value as a function of nonnegative shear prove necessity and sufficiency, rather than relying on determinant positivity alone. The derivative of the rational threshold has precisely one interior sign switch, proved by a cubic with positive derivative. The endpoints, nilpotent cubic term, exact rational witness, physical logarithmic norm, and square-root fold are included in the analytic proof. The standalone standard-library verifier reproduced the determinant factorization using a sufficient exact-rational polynomial interpolation grid, the rational derivative identity, root brackets, and supplementary singular-norm checks. The numerical tests alone are not offered as the infinite proof.

## Originality — PASS, with historical uncertainty

The closest inspected primary sources are Sun and Shu, arXiv:1811.10680v1; Ranocha and Ketcheson, arXiv:1909.13215v1; Sun, Wei and Wu, arXiv:2201.06501v1; and Achleitner, Arnold and Jüngel, arXiv:2308.05689v1. Their general strong-stability and energy arguments do not contain the displayed exact rational level-set classification of the RK2 three-state nilpotent Jordan chain. The closest published special families inspected address RK2 on a damped planar oscillator and RK4 on a planar Jordan shear, neither of which implies the different nilpotency-index-three RK2 frontier. No equivalent result was found in the checked historical claims or targeted mathematical searches. This is a claim-level, not title-only comparison and is not a declaration that no other specialized literature exists; priority remains provisional.

## Value — PASS

The result is a complete structural classification for a minimal higher-index defective linear test system: even though all eigenvalues remain fixed at \(-1\), the physical and numerical contraction regions differ, a detached misleading numerical window appears strictly above the exact physical threshold \(\sqrt2\), and every positive safe step disappears at a finite explicit algebraic shear ceiling. The contrast with the infinite-shear RK4 planar false window isolates an order-and-index-dependent barrier that is relevant when interpreting energy-based timestep selection for nonnormal systems. The exact threshold is not merely a grid sample, scalar stability restatement, or renaming of another result. The theorem does not imply method accuracy or a corresponding criterion for larger Jordan blocks.

## Limits and closest literature

The determinant factorization, monotonic singular-value crossing, and rational frontier are proved for the fixed real three-dimensional Jordan family only. Numerical root approximations and finite checks supplement, not replace, those proofs. General strong-stability impossibility theorems over a whole matrix class neither prove nor disprove the explicit single-family boundary. Independent mathematical and historical-priority validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
