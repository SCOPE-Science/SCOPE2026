# Self-review

## Correctness — PASS

For the stated strictly positive rates and \(m\geq1/h\), the negative nonlinear correction and strong cooperativity are directly visible from the ODE. A scalar total-population comparison bounds all solutions. The symmetric Metzler Jacobian has principal spectral sign determined exactly by \(\delta(e-s)-es\). Positive sub- and supersolutions, strict sublinearity and order comparison prove the globally attracting unique positive equilibrium. A Perron-weighted linear comparison proves exponential extinction on the stable side. At the critical rate, the positive weighted mass has derivative at most \(-sv^2\), yielding global extinction; orthogonal projection then supplies the explicit quadratic center coefficient \(k>0\), and hence the reciprocal-time vector profile for all nonzero nonnegative initial states. Lyapunov--Schmidt expansion derives the equilibrium amplitude. The executable verifies each critical polynomial identity in exact arithmetic, plus representative trajectories; the proof does not promote finite experiments to an infinite-time theorem. Main remaining technical risk is that the comparison and smooth local reduction have not undergone external independent examination.

## Originality — PASS on checked literature, with residual priority risk

The identical linear-migration equations are equation (2.11) of Xia et al., 2023 (preprint https://arxiv.org/abs/2310.10558, DOI 10.3934/mbe.2023876). Its relevant Section 2.3 and Theorems 2.9--2.10 were read: Theorem 2.9 already gives high-migration global extinction and is excluded from novelty claims. Theorem 2.10 proves coexistence only for \(\delta\leq s\), and global attraction under a narrower inequality; the source explicitly leaves complete qualitative analysis open. Our missing-range global attraction, exact neutral-threshold law and first-order branch slope are not implied by the stated source theorems. The related 2019 source--sink paper of Wu et al. (DOI 10.1016/j.tpb.2019.11.004) claims a broad dispersal-dependent classification; only its abstract was accessible, so qualitative overlap with general source--sink theory remains unresolved at full-text level, although no exact Allee--logistic critical coefficient is identified there. The additive-Allee 2022 paper (DOI 10.3934/math.2022034) uses a different model and cannot imply the model-specific coefficients. The nonlinear-migration variant is not interchanged with the linear variant. General positive-systems theory may cover portions of the qualitative phase classification, and unindexed equivalent models remain a publication-priority risk.

## Value — PASS

The strict high-Allee restriction creates a natural source--sink rescue problem: one habitat is incapable of persistence in isolation, while diffusion couples it to a logistic habitat. The threshold answers the complete rescue question for every positive migration rate and distinguishes global extinction from global coexistence. The neutral case, omitted by strict-threshold theorems, changes extinction from exponential to reciprocal-time, with a universal habitat ratio and exact amplitude. The equilibrium branch formula quantifies loss of abundance immediately before rescue fails. These are model-motivated rather than arbitrary parameter slices.

## Scientific scope and risks

The result is restricted to a deterministic two-patch ODE with equal bidirectional migration and \(m\geq1/h\). It does not assert spatial or stochastic extensions, detailed error rates, or novelty of the source's original high-dispersal theorem. Published priority cannot be proven from finite search coverage.

Self-review: passed. Independent audit: not yet performed.
