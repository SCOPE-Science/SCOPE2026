# Scientific review: backward blow-up amplitude echo in star-node flows

## Correctness — PASS

For \(\dot z=\lambda z+Q(z)\) with strictly negative radial homogeneous coefficient \(f\) and positive angular coefficient \(g\), exact polar differentiation gives \(w'=2p(\lambda+fw)/g\) in the positive radial power \(w=r^{2p}\). The strictly decreasing integrating factor \(\rho\) produces a unique periodic positive graph and an exact decomposition \(w=w_*+C\rho\). Its quotient has strictly positive derivative, proving the full backward trichotomy. For \(C>0\), direct integration of actual physical time shows finite backward blow-up, and a uniform first-order expansion establishes \((t-t_-)r^{2p}=w_*(\theta)/(2p\lambda)+O(t-t_-)\). The logarithmic phase change is a global diffeomorphism, yielding an exact periodic profile and the universal accumulation interval. No numerical extrapolation substitutes for these proofs. The accompanying symbolic/numerical checker passes an explicit anisotropic cubic instance; it verifies only its finite tests.

## Originality — PASS within inspected sources

The closely relevant 2013 Bendjeddou–Llibre–Salhi author preprint contains the linear radial-power angular equation and periodic-orbit criteria, so neither that reduction nor existence is new. The 2023 Alarcón–Castro–Labouriau full-text treatment gives forward invariant-circle attraction and global topological phase portraits, including infinity, but not finite original-time backward escape or the precise logarithmically periodic amplitude profile. The published exact-angular-return record establishes forward-time period and Floquet rigidity but expressly excludes backward completeness from its scope. The related general planar oscillatory-blow-up record proves a conditional spectral criterion, not the present global partition of all initial conditions or an explicit formula identifying the blow-up amplitude with the forward attracting radial graph. The primary mathematical distinction is implication: none of the inspected statements yields the phase-resolved physical-time formula or its nonconstant-profile criterion without additional analytic work.

The underlying angular equation is long established, so the possibility that equivalent consequences occur in less readily indexed sources is a genuine residual novelty risk. No claim of priority beyond the inspected evidence is made.

## Mathematical value — PASS

Qualitative phase portraits identify which orbits tend to infinity backwards but lose the physical-time information: finite-time versus infinite-time escape, exact divergence exponent, time-dependent angular oscillations, and the extent of universality across all exterior initial conditions. These are natural dynamical invariants. The nonconstant logarithmically periodic amplitude is not a cosmetic restatement of forward attraction: it describes the actual asymptotic blow-up clock and shows how one forward attracting cycle controls an entire backward blow-up basin. The polynomial witness proves that the oscillation is real, not an artifact of coordinate definitions. The result does not require a conjectural downstream theorem to motivate the exact classification.

## Scope and residual risks

The angular drift must remain nonzero; the polycycle case is excluded. The result is not robustly extended to nonhomogeneous perturbations. The checker does not prove arbitrary-degree assertions. The guaranteed log-period need not be minimal. Literature coverage cannot exclude unindexed equivalent results, and no independent mathematical audit has been carried out.

Self-review: passed. Independent audit: not yet performed.
