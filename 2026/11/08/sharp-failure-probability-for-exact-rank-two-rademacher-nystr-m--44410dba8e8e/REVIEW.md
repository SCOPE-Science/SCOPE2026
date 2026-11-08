# Scientific review

## Correctness
**PASS.** Factoring the rank-two matrix as \(B^{\mathsf T}B\) reduces Nyström exact recovery to the planar rank of \(B\Omega\). Conditional counting bounds the zero atom by \(1/4\) and the mass of any line including zero by \(1/2\). Convex majorization under these simultaneous restrictions gives the global failure bound, and a fully enumerated three-coordinate witness realizes equality. The separate \(n=2\) computation is exact. Integer-exact verification covers 48, 624, and 6240 rank-two small-coefficient matrices in dimensions two through four plus additional tests; it supports, rather than replaces, the proof.

## Originality
**PASS, qualified by specialist publication precedence.** The closest primary theorem inspected is Saibaba--Międlar (2023), Appendix D, which offers general non-Gaussian Nyström guarantees without a sharp constant for the low-rank Rademacher exact-recovery event. Dereziński et al. (2022) give high-stable-rank approximate expected projector formulas, whose regime is inapplicable when exact rank and sketch width are both at least two. Balabanov et al. (2023) address a distinct randomized Hadamard embedding, not independent sign-column rank failure. Existing elementary anti-concentration principles are explicitly treated as prior tools. Relevant mathematical searches uncovered no matching sharp all-\(m\) rank-two formula, but specialist literature may still contain an equivalent formulation.

## Value
**PASS.** Exact recovery is a natural success event for low-rank randomized Nyström approximations, and independent Rademacher sketches can fail on exact low-rank data even though continuous Gaussian sketches do not. The sharp all-budget, all-ambient-dimension law and its explicit three-dimensional extremizer expose how a zero-projection atom worsens discrete sketching: at two probes the worst-case failure is \(5/8\), instead of \(1/2\) in ambient dimension two. It yields an exact baseline for selecting a budget against rank-loss probability, without overstating finite-precision accuracy.

## Closest literature and limitations
The result is restricted to dense independent signs, exact arithmetic, and rank two. Sharpness is only for exact rank loss; general approximation errors, conditioning and higher target ranks are not addressed. General sub-Gaussian and Hadamard embedding bounds neither state nor contradict the exact extremal probability. An independently conducted scientific audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
