# Review of the synchronous aged-path cascade theorem

## Correctness — PASS

The entire assertion refers to one precisely defined model: the rooted path with a strict threshold \(0<\theta<1/2\), irreversible adoption and frozen synchronous rounds with independent age-based activation \(1/(s+2)\). The prefix invariant implies only the next unadopted path vertex can change, reducing the process to one Bernoulli success per round. The explicit coupling with independent Bernoulli cycle increments proves the complete finite-time distribution, including \(m=1\) and \(t=0\). Stirling-number recurrence gives the fixed-depth sharp survival tail; Borel–Cantelli and tail integration establish almost-sure completion and the exact moment cutoff. The bounded-summand central limit theorem yields the large-depth Gaussian log-time limit. The included standalone checker passed 3,887 exact finite-state or exhaustive-permutation comparisons. Finite checks supplement but do not replace proof.

## Originality — PASS, best-knowledge assessment

The initiating Abella–San Miguel–Ramasco study (arXiv:2209.05990, full paper Secs. II–V and Appendix) uses the inverse-age activation law but reports approximate/random-network dynamics under asynchronous Monte Carlo updates. The reviewed claim is explicitly restricted to an independently specified synchronous variant and asserts a full exact law unavailable by simply treating its time variable as the asynchronous study's time. Classical Feller permutation-cycle increments and their central limit theorem are credited rather than claimed new (Najnudel–Pitman, arXiv:1907.09587, plus classical permutation theory). The closest accessible older research claim studied a continuous-time globally inverse-age cascade; it establishes long-time depth-dependent tails but not this finite-round Stirling distribution or large-length Gaussian log-time limit. Specific semantic searches found no statement implying the entire new model-specific claim. Residual risks: unindexed parallel derivations; the synchronous update convention may have been studied separately; and classical probability results make the final reduction relatively short. Neither a title search nor source partition establishes uniqueness.

## Value — PASS

The result answers the motivated question of *full finite-time versus eventual adoption* for a one-dimensional threshold cascade with resistance increasing with time. Its exact finite-round probability table is useful for finite-horizon diffusion forecasts, while an infinite mean despite almost-sure completion and an exponential-in-path-depth typical delay create a structurally consequential separation between adoption certainty and timeliness. These are natural, scalable invariants of a network diffusion mechanism, not an arbitrary graph enumeration; the new scientific insight is the sharp model-specific distribution and depth-rescaled Gaussian transition, not the classical permutation theorems themselves.

## Scope, nearest literature, and residual risks

The claim assumes per-vertex independent coins at each frozen synchronous round, rather than the random asynchronous Monte Carlo convention of arXiv:2209.05990. It does not cover thresholds at or above one half, different graph topologies, or exogenous aging. Previously known continuous-time fixed-depth asymptotics and classical permutation identities remain acknowledged precedents. Independent confirmation and broader publication-priority review remain appropriate.

Self-review: passed. Independent audit: not yet performed.
