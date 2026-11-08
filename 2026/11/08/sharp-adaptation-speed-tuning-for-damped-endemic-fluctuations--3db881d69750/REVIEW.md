# Scientific review: sharp adaptation-speed tuning for damped endemic fluctuations

## Correctness — PASS

The fixed point is derived by eliminating the link density from both equilibrium equations. The actual two-variable vector field yields trace \(-A-B\xi\) and determinant \((\tau-1)\xi\), with a strict positive off-diagonal coupling when \(\omega>0\). The characteristic discriminant has two explicitly positive, distinct roots. Its sign determines node versus focus and the smaller real decay root gives a differentiable spectral exponent away from the boundary. The derivative sign proves the unique optimal speed; the fast-limit ratio follows without asymptotic approximations. A polar-coordinate perturbation argument proves infinitely many damped prevalence-level crossings in a sufficiently small neighborhood of each focus. The parameter restrictions and spectral, rather than finite-time, meaning of optimality are explicit. Symbolic algebra, the exact defective example and 180 exact-rational comparisons were run from `verify.py`.

## Originality — PASS, with priority risks

The closest initiating article is Achterberg and Sensi, *A minimal model for adaptive SIS epidemics* (arXiv:2209.01224, first publicly posted 2022-09-02; journal 2023), especially equations (12), the Jacobian displayed in Section 4.2, and slow-network Section 5. The fully accessible primary text analyzes stable endemicity and shows a spiral example, but does not state or imply a uniquely fastest common response speed, its sharp node–focus interval, or the fast-limit quantitative penalty without additional new optimization. The full accessible multigroup extension arXiv:2407.17639 discusses equilibria and two-community cycles rather than the single-community spectral optimum. The earlier 2020 generalized adaptive SIS article addresses link-update classes and epidemic thresholds; its full text was not accessible in this review. Targeted literature and mathematical-record comparisons found no exact covering statement. Priority uncertainty remains for inaccessible or unindexed treatments, and novelty is not inferred from keyword nonmatches alone.

## Value — PASS

Holding the ratio of contact-breaking and contact-creation responses fixed keeps the endemic state unchanged, isolating the practically meaningful question of **how quickly** the contact network should react. The precise answer is not “as fast as possible”: a uniquely optimal finite speed has an exact decay-rate advantage over the infinite-speed limit, up to a factor approaching two. The theorem simultaneously identifies a nonempty interval of damped endemic fluctuations at every positive risk-response intensity, despite the absence of cycles. These are sharp, continuous-parameter phenomena useful for comparing response timescales and interpreting numerical transients, not isolated numeric table entries or a relabeling of existing equilibrium formulas.

## Closest literature and limitations

The initiating paper already proves stability and provides the equilibrium and Jacobian; these are not presented as new. The multigroup model considers a larger dynamical system but does not supply a result dominating the fixed-ratio single-group optimization. Neither linearized spectral speed nor its optimum directly controls peak prevalence or finite-time recovery. The optimal Jacobian has a defective double eigenvalue, with potential polynomial transient prefactors. No assertion is made about stochastic finite-population models, sustained periodic epidemic waves, or independent validation. Full-text priority review of the restricted-access 2020 model was not possible; only its public abstract was used.

Self-review: passed. Independent audit: not yet performed.
