# Scientific review

## Correctness

**PASS.** The deterministic equations match the cited compartmental balance law under a concrete equal-patch specialization. The demographic dynamics form a stable, triangular two-dimensional subsystem, so all equilibria have unit total patch populations; reducing to four infection coordinates is exact. The quadratic mean/difference equations and critical antisymmetric eigenvalue are derived algebraically. Nondegeneracy follows from the exact negative Lyapunov–Schmidt cubic coefficient. An implicit-function argument establishes the local branch count and orientation, and the noncentral spectral gap establishes the claimed Morse indices. `verify.py` rechecks the nonstandard algebraic identities and strict coefficient sign symbolically. Risk: no global equilibrium count or nonlinear global basin statement is proved; finite numerical root solves are not used as proofs of existence.

## Originality

**PASS on available literature, with priority uncertainty.** Calvo et al. (2019), arXiv:1907.08887, Section 3.3 and Example 4.7, already demonstrate by computation multiple feasible two-patch equilibria, including stable equilibria; those phenomena are not claimed as new. Calvo et al. (2024), arXiv:2405.10998, Section 2, reproduce the deterministic system and study stochastic approximations and source–sink regimes, not the exact synchronized lower-endemic pitchfork coefficient. Knipl, Pilarczyk, and Röst (2015) discuss rich bifurcation structure in a *vaccination* model with different reaction terms, so general qualitative pitchfork possibility is not equivalent to the present model-specific threshold, sign and instability count. Direct searches for model names, symmetry breaking, pitchfork, antisymmetric eigenvalues and cubic migration bifurcation identified no covering theorem. Residual risk: inaccessible or unindexed work may already contain an equivalent specialization; exhaustive priority certification is not asserted.

## Value

**PASS.** The initiating epidemiological literature makes migration-dependent endemic multiplicity and sensitivity to population movement central, but its reported multiple equilibria are largely numerical. A sharp local analytical threshold for the disappearance of two asymmetric **saddle** states distinguishes the topology of the low-prevalence basin boundary from the existence of stable endemic states. The exact square-root imbalance, subcritical orientation and change in unstable dimension supply structurally interpretable information unavailable from simply counting numerical fixed points. This is a mathematically motivated local classification, not a generic exercise in diagonalizing a two-patch matrix: the cubic sign requires the explicit nonlinear reinfection reaction and slaved mean equation.

## Literature and limitations

Closest sources: Calvo et al. (2019), arXiv:1907.08887; Calvo et al. (2024), arXiv:2405.10998; Knipl, Pilarczyk and Röst (2015), *Rich bifurcation structure in a two-patch vaccination model*. The proof addresses the explicit symmetric rational-parameter specialization only. No claim about global counts, stochastic systems, stable asymmetric endemic attractors, or model calibration is made. Independent external verification is outstanding.

Self-review: passed. Independent audit: not yet performed.
