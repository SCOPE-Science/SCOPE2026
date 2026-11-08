# Assessment of the thirteen-point one-flex Hermitian-relative quartics

## Correctness

**PASS (self-review).** Smoothness and genus follow from the displayed partial derivatives. The rational-inflexion criterion follows from the exact characteristic-three tangent substitution. The standalone program exhausts the eight coefficients over \(\mathbb F_9\) and the three distinguished coefficients over \(\mathbb F_{81}\) and \(\mathbb F_{729}\), verifying all field structures and every affine pair. The Weil functional equation and Newton identities uniquely reconstruct degree-six numerator polynomials from the three counts. Rational irreducibility of the quartic Frobenius factor is proved directly and establishes the simple-surface isogeny factor; all normalized eigenvalues are roots of unity. A code execution is reproducible, but mathematical verification remains a self-review.

## Originality

**PASS, qualified.** Homma–Kim 2026 classify only \((N_9,I_9)\)-types and parameter counts (Theorem 46); here the new invariant is the *complete* two-class zeta/isogeny decomposition within their single \((13,1)\) stratum. Homma–Kim 2024 imply geometrical supersingularity and Frobenius-root-of-unity restrictions but not the explicit arithmetic factorization. Meagher–Top's classic twist tables explicitly exclude characteristic three, so their similar-sounding result does not imply the present finite-field classification. The closely related one-rational-point Hermitian-relative quartic calculations have a different base-field point count and the cube numerator \((1-3T+9T^2)^3\), and neither they nor their family-wide formulas cover this thirteen-point stratum. Targeted external and research-database searches found no exact numerical or implication coverage. A comprehensive specialist survey of characteristic-three unitary twists could yet uncover an implicit equivalent classification.

## Mathematical value

**PASS.** This is a complete classification of arithmetic isogeny decomposition in the smallest smooth nonelliptic case (degree-four Hermitian relatives) of a natural published rational-point/flex stratum. The boundary changes not just a point count but the dimension of simple factors in the Jacobian: an elliptic cube versus an elliptic curve times a simple abelian surface. These are intrinsic arithmetic-geometric invariants relevant to Jacobian arithmetic, Prym-type decompositions, and finite-field twist classification; the precise field and parameter slice are motivated by the source's three-member type, not selected after an arbitrary census.

## Closest literature and limitations

Sources: Homma–Kim, arXiv:2610.09672v1, main classification and full Section 4; Homma–Kim, arXiv:2402.14192, Sections 1–3; Meagher–Top (2010), particularly Sections 3, 7–8. The result does not assert pairwise nonisomorphism of the two \(c=1\pm\iota\) curves, full Jacobian group structure, or a classification beyond the displayed normal form. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
