# Review of the global inverse-geometry theorem

**Correctness — PASS.** The map, domain, coefficient matrix, sigmoid and both free parameters agree with the published equations. The determinant identity
\[
\det DF=(1-T+17Td_1/10)(1-T+17Td_2/10)+T^2d_1d_2,
\qquad d_j=\alpha\operatorname{sech}^2(\alpha z_j)
\]
is exact. At the unit step the image is an explicit affine parallelogram. For nonunit steps, the map differs from \((1-T)I\) by a bounded term; the homotopy is proper, with degree \(+1\). Below the strict loss boundary, all finite determinants are positive; degree gives global diffeomorphism. Above it, a negative determinant region exists and proper degree forces at least two compensating positive inverse branches at nearby regular targets. The borderline derivative tends to a singular matrix only at infinity. The exact rational negative-Jacobian witness and all 1,105 checker diagnostics passed. The checker is not the infinite proof; proper-degree arguments supply the necessary quantifiers.

**Originality — PASS within inspected coverage.** The originating paper [1] was read at its governing equations, Jacobian, numerical bifurcation analysis, conclusions and appendices; its focus is forward spiking dynamics and local equilibrium stability. Two full publicly accessible findings for the identical model were compared at their actual theorem/proof text: one classifies compact-global-attractor existence and another excludes/constructs primitive two-cycles. Neither claims global injectivity, a gain-step reentry boundary, or the open three-inverse-fiber phase. Related inverse-sheet theorems for Huygens and risk-sensitive maps concern different equations, and the general theory of noninvertible planar maps supplies tools but not the specific sharp threshold. Residual risk: unindexed or differently named equivalent results for this exact sigmoid-rotation Euler map may exist; absence from a ranked index cannot prove global uniqueness.

**Value — PASS.** The paper's observed regimes motivate whether the state update supports unique backward reconstruction. The theorem supplies a sharp complete parameter classification, including the exceptional bounded-image step, recovery of global invertibility as the step grows for small gain, a nonsingular yet nonuniform inverse boundary, and persistent three-preimage output regions in the moderate-step phase. It also proves that every nonunit-step regular target has an odd number of inverse states. These are structural, all-parameter facts, not a routine numerical fit or a single arbitrary output count. The result does not classify forward physical attractors, noise robustness, or exact maximum inverse multiplicity.

**Most relevant primary source:** A. Buscarino, C. Famoso, L. Fortuna, *Bifurcations in a new two-cell spiking map: a numerical and experimental study*, Nonlinear Dynamics 111 (2023), DOI: https://doi.org/10.1007/s11071-023-08897-7 (first public 2023-09-27).

**Closest complementary published claims:** *A sharp global-attractor threshold for the two-cell sigmoid spiking map*; *Sharp prime-two exclusion and a saturated repelling cycle in a two-cell spiking map* (public 2026 notes). Their conclusions concern global forward attraction and periodic recurrence, not one-step inverse-state multiplicities.

Self-review: passed. Independent audit: not yet performed.
