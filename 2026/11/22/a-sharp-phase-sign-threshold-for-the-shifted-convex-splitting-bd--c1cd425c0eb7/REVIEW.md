# Review: sharp phase-sign threshold for a Cahn–Hilliard convex-splitting step

## Correctness — PASS
The two-cell Neumann antiphase mode reduces the published shifted cubic force to an exact scalar implicit recurrence with a globally positive derivative in the new endpoint. The derived discriminant gives the stated threshold, the Schur inequalities give local exponential attraction, and a uniform cubic-perturbation argument extends positive real-root trajectories to all indices, including the double-root case. Above threshold, summable nonlinear angular deviations force infinitely many signs for every sufficiently small nonzero history. The exact semidiscrete starter is stated explicitly and has the required linear ratio. The symbolic checker verifies the polynomial identities and 20 representative numerical experiments; the proof, not the experiments, establishes infinite-index conclusions.

## Originality — PASS, with residual historical uncertainty
The primary 2026 Gu–Wang paper has been inspected at the definitions of the shifted cubic force, the fully discrete method, its energy theorem, and its numerical discussions. It establishes energy stability, uniqueness and convergence, not this two-cell all-time phase-sign classification. Classical BDF2 scalar monotonicity and an already published exact delayed-sign-loss result were checked against the actual recurrence, not just by title. Neither implies the shifted nonlinear threshold with exact semidiscrete starting and critical boundary behavior. A broad specialist-history search cannot certify priority; older BDF2 oscillation analyses remain a residual risk.

## Value — PASS
This is a sharp qualitative timestep diagnostic for a newly introduced energy-dissipating method on the smallest mass-conserving mesh with a globally strictly convex antiphase free energy. It exhibits indefinite false phase reversals arbitrarily near equilibrium while the true semidiscrete flow never changes sign. The completed all-time nonlinear classification distinguishes structural energy decay from sign-faithfulness without claiming instability or global full-PDE failure.

## Closest literature and scope
Gu–Wang, arXiv:2606.04204 (2026), is the method source. Hundsdorfer–Ruuth–Spiteri's standard BDF2 monotonicity theory, the prior standard-BDF2 sign-delay record, and convex-splitting Cahn–Hilliard BDF2 literature establish context, not this exact shifted-scheme threshold. The proved statement is local in initial amplitude and is for the phase-only two-cell reduction; no independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
