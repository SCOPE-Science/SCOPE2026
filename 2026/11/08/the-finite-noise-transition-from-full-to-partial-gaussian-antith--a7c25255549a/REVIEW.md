# Review: finite-noise Gaussian antithetic correlation

## Correctness — PASS

The theorem quantifies over every \(K\ge2\), \(a\in\mathbb R\), \(b\ne0\), and positive-semidefinite Gaussian correlation matrix with diagonal one. Isserlis' covariance identities give an affine plus strictly convex squared-Frobenius objective in the correlation matrix; permutation symmetrization, feasible equicorrelation eigenvalues, and the resulting exact quadratic minimization prove a **unique** global optimizer. The cross-validation expansion is checked directly from the score in arXiv:2608.08089, Equation (3). Its joint-Gaussian covariance objective is identical with new exact positive coefficients \(P,Q\). The derivative of its threshold function has strictly negative numerator for all stated parameters, proving a unique phase boundary. Exact rational values are verified for the two-replica example. The bundled standard-library checker independently tests 136,111 finite identities, inequality comparisons, randomly constructed feasible nonexchangeable covariance matrices and simulations; those checks supplement the analytic proof.

## Originality — PASS, qualified

The 2024 antithetic cross-validation work establishes bounded variance for maximally negative equicorrelation **in the small-noise limit**; the 2026 follow-up establishes that this extreme correlation is necessary for bounded variance **as noise tends to zero** and proves a minimax statement **within zero-sum couplings**. Neither result optimizes finite-positive-noise correlations throughout the feasible Gaussian covariance class, and neither implies that full antithetics are strictly worse than partial correlation in the concrete finite-noise example. The numerical random-walk coupling paper arXiv:2610.01120 optimizes different indicator-based pairings, not quadratic Gaussian response averages. Published-record searches for the full formula, synonymous mixed-Hermite Gaussian antithetic methods and fixed-perturbation risk optimization found no directly covering statement. The underlying fourth-moment and symmetrization tools are explicitly classical and not claimed new. Unindexed historical work on Gaussian quadratic Monte Carlo coupling might imply the general component; the precise finite-noise cross-validation specialization is the novel claimed endpoint, with this residual historical-priority risk clearly disclosed.

## Value — PASS

The source literature highlights both the necessity of zero-sum antithetics when bias-perturbation vanishes and the unresolved choice of joint randomization at finite noise. The exact result supplies an implementable-in-principle phase boundary within the jointly Gaussian class, and an explicit case in which fully antithetic sampling has expected conditional variance \(8\), versus the optimal \(5167/1024\) and independent sampling's \(41/8\). This is a genuine design reversal, not a marginal parameter improvement, and clarifies when a familiar asymptotically optimal variance-reduction design ceases to be optimal at finite perturbation. The coupling choice does not change the estimator's bias. It is a sharp special-case benchmark, not a general nonlinear or non-Gaussian implementation guarantee.

## Closest primary literature and scope

1. Liu, Panigrahi, Soloff, *Cross-Validation with Antithetic Gaussian Randomization*, arXiv:2412.14423, sections 2–3. General zero-sum construction and small-perturbation bounds. No optimization over finite positive perturbation and arbitrary Gaussian correlations.
2. Chattopadhyay, Liu, Panigrahi, *On the Optimality of Antithetic Randomization for Cross-Validation*, arXiv:2608.08089, sections 2–4, Appendix A.1–A.3. Necessity and sufficiency for bounded variance as perturbation vanishes, and minimax comparison within the zero-sum family; its statements do not cover the displayed finite-perturbation optimum.
3. Abkin, Daripa, *Sign-switched antithetic coupling in gradient random-walk methods for convection–diffusion equations*, arXiv:2610.01120, sections 2–4. Sharp sign-selected Gaussian particle couplings for threshold indicators, not linear-plus-quadratic Gaussian observables or cross-validation.

The restriction to jointly Gaussian couplings is essential. Non-Gaussian couplings with fixed Gaussian marginals are not covered. No empirical claim about deployed predictors is made. A numerical-only finite check would not prove the theorem; the proof stands on exact moments and convex geometry.

Self-review: passed. Independent audit: not yet performed.
