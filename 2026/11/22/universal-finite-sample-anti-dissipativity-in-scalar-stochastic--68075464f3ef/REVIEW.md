# Self-review

## Correctness — PASS
The scope explicitly requires an invariant conservative generator, a bounded observable bounded away from zero, strict population dissipation and nonzero generator action. The zero-mean generator action must occupy a positive-measure positive set. A positive-measure subset with a fixed lower bound supplies an event of probability \(p^m\), a strictly positive fitted eigenvalue and exponential expected growth. The contractive true semigroup makes the triangle-inequality lower bound rigorous. In the explicit circle diffusion, integration yields population eigenvalue \(-1/9\); the negative-cosine arc has probability \(1/3\) and gives exact fitted-eigenvalue floor \(1/3\). Every displayed quantifier and boundary, including \(k=0\) and \(0<h<18\), follows from these steps. The reproducibility program checks the corresponding rational identities and finite grids but is not used as an infinite proof.

## Originality — PASS, qualified
The 2026 Richardson-SDMD source proves fixed-horizon error bounds, including perturbation constants depending on the horizon, not a universal positive-growth event for each fixed finite sample size or an explicit true-forecast risk lower bound. Its generator-invariant-dictionary identity excludes rather than subsumes this non-invariant example. The 2025 SDMD and 2024/2026 gEDMD convergence papers concern large-data and other limits, not the stated order-of-limits impossibility. A 2026 multi-step EDMD paper treats prediction bias and variance generally; only its abstract was accessible, so a stronger general result could overlap. Database and accessible related records were compared by claimed implications, with no direct covering claim found. Failed discovery is not a proof of global novelty.

## Value — PASS
Long-time predictions are a primary use of finite-data Koopman models. The theorem proves that neither making the extrapolated time step arbitrarily small nor increasing the dataset to any fixed finite size ensures expected long-time stability without structural dissipation constraints. It provides an exact, smooth stochastic-diffusion benchmark, a universal positivity mechanism beyond an isolated example, and an explicit exponential lower bound quantifying the failure while the population discretization contracts. The result does not claim to invalidate fixed-horizon convergence or existing stabilization mechanisms.

## Closest literature and residual risks
See the structured originality analysis. The residual novelty risk is a general EDMD spectral-pollution or multi-step-prediction theorem with a stronger consequence not found among accessible indexed statements. The comparison against Schurig et al. is limited to available abstract text, not a full-document noncoverage certification.

Self-review: passed. Independent audit: not yet performed.
