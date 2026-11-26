# Scientific review

**Claim reviewed.** For the asymmetric endemic equilibrium of the four-compartment opinion–SIS model, under \(\alpha=0\), \(\delta=1\), \(0<z<1\), and \(u>0\), the simplex Jacobian is Hurwitz precisely when the explicit quadratic \(P_z(u)>0\); it has an eigenvalue with positive real part when \(P_z(u)<0\). At \(z=3/8\) this gives two exact, transversal spectral crossings separating stable, unstable and stable open intervals as both positive parameters change on the specified curve.

## Correctness: PASS

Eliminating the fourth compartment gives a genuine three-dimensional local chart on the population simplex. The endemic equilibrium is characterized exactly by \(R=1+z+u\), \(p=R^2u/[z(1+z)]\), and all four positive proportions; direct substitution verifies the original field. The displayed Jacobian, its trace, determinant and two-minor sum give the exact third cubic Hurwitz determinant \(uP_z(u)/[z^2(z+1)^3]\). Since the trace and determinant of the Jacobian are negative for every stated parameter, positivity of the Hurwitz determinant is necessary and sufficient for all eigenvalues to have strictly negative real parts. The strict positive sign implies local exponential stability; the strict negative sign gives an eigenvalue with positive real part and implies instability. The quadratic sign/root conditions prove two positive crossings and the fixed-ratio rational example. At a crossing, the cubic factors as a stable real factor times an imaginary quadratic; differentiating the polynomial proves a transverse spectral crossing at each simple root. The bundled checker recomputes exact symbolic identities and tests three rational cases. A finite test is not substituted for the proof.

**Boundaries and risks:** The result only treats the asymmetric endemic branch and local spectrum. The derivation neither establishes a nonzero first Lyapunov coefficient nor infers actual periodic orbits. On the crossing locus linearization is nonhyperbolic, so no asymptotic-stability verdict is asserted there.

## Originality: PASS (literature-bounded)

The starting paper (Götz, Krüger, Niedzielewski, Schneider and Pabjan, arXiv:2512.10612v1, Section 3, Figure 2; journal Appendix A.3, DOI 10.1038/s41598-026-66686-9) derives the model and asymmetric endemic branch and explicitly does not simplify the remaining Routh–Hurwitz condition, preferring numerical stability illustrations. It is the closest and most relevant source: the new content is the exact quadratic factorization on a physically admissible fixed-ratio family, the necessary-and-sufficient two-positive-crossing criterion for all such ratios, and two algebraic transverse thresholds. Its numerical figures may anticipate regions of stability; no novelty is claimed for generic oscillatory behavior. The classical Routh–Hurwitz theorem supplies machinery but not the model-specific factorization. Achterberg–Sensi's adaptive SIS and Samadi et al.'s higher-order SIS–opinion model involve different feedback equations and do not imply this factorization. Additional publicly indexed records on two-stage information delay, epidemic-logit coupling and triadic SIS–opinion oscillations likewise study different equations. Unread historical sources and undiscovered preprints remain residual priority risks. In particular, full independent historical-priority verification has not occurred.

## Value: PASS

The originating paper explicitly leaves a nonlinear characteristic inequality untreated. Exact stability classification for a native positive endemic branch is a substantive missing mathematical question: it gives a closed sign test in place of a numerical heatmap, distinguishes a finite instability window from monotone destabilization, and identifies both rigorously transversal boundaries with exact radicals. It is not a mere reparameterization of a previously proved threshold, nor a routine fixed-parameter arithmetic check. The fixed-ratio curve is biologically feasible but requires co-variation of two model parameters, limiting claims about single-control experiments.

## Closest literature and scientific limits

Primary source: https://arxiv.org/abs/2512.10612, https://doi.org/10.1038/s41598-026-66686-9. Additional context: https://doi.org/10.1007/s11071-023-08498-4 and https://arxiv.org/abs/2608.31032. The proof is analytical and deterministic; it does not establish global attraction, stochastic behavior, Hopf criticality or periodic solutions.

Self-review: passed. Independent audit: not yet performed.
