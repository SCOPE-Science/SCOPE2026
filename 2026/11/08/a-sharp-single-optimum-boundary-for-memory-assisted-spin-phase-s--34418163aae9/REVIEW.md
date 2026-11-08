# Review of the sharp switching-optimum boundary

## Correctness

**PASS.** The scope is a nonmagnetic incoherent linear threshold with zero spin-only and direct-phase coupling. The OU increment variance gives the displayed positive phase kernel; the two independent linear-response channels reproduce the established coupling threshold. The new lemma is proved without assuming an external reliability theorem: strict log-concavity of the exponentially tilted kernel makes its hazard strictly increasing, its survival function strictly submultiplicative, and its variance strictly below its squared mean. This gives \(M_0M_2<2M_1^2\), forces the optimizer equation to have at most one root, and supplies both quantitative asymptotics. The numerical verifier independently checks the formulas for multiple parameter sets but is not used as an infinite proof.

## Originality

**PASS, with publication-priority qualification.** The source Hayashi (arXiv:2609.35838v1, Sections II.2–II.3 and Appendix A) establishes the exact critical coupling and an **existence-only sufficient condition** for a finite switching optimum. Its stated example values and plots do not supply a proof of uniqueness, a necessary-and-sufficient response boundary for all positive parameters, or the linear-onset and strong-response asymptotic laws. The new argument uses a strict moment inequality arising from the OU kernel's log-concavity to establish those claims. Published-result searches and relevant primary literature did not reveal a matching or stronger theorem. Related colored-noise Kuramoto and externally switched network models have different spin-response terms; their full documents were not completely examined, so a residual indirect-coverage risk remains. The hazard-rate lemma is classical and is not itself claimed as novel. No independent priority adjudication is implied.

## Value

**PASS.** The source's finite-rate optimum was supported through a sufficient criterion and examples; the unique-optimum theorem closes a natural question about the rate landscape, excludes multiple competing local operating points, and gives the exact parameter boundary for when optimizing an interior rate is worthwhile. The linear onset slope and asymptotic strong-response scaling provide interpretable quantitative predictions for the model, rather than an arbitrary parameter slice. The result does not claim new experimentally verified synchronization behavior.

## Closest prior work and scientific limits

- R. Hayashi, *Memory-induced optimal switching in a dynamic Ising–Kuramoto model*, arXiv:2609.35838v1 (2026-09-24), https://arxiv.org/html/2609.35838 . Provides the model, susceptibility, finite-rate sufficient condition, and example optima. Its exact threshold formula is an essential premise for this refinement.
- R. Tönjes, *Synchronization Transition in the Kuramoto Model with Colored Noise*, arXiv:1003.1549 (2010), https://arxiv.org/abs/1003.1549 . Considers colored-noise phase oscillators without the internal Glauber response.
- Y. Zhang and S. H. Strogatz, *Designing temporal networks that synchronize under resource constraints* (2021), https://doi.org/10.1038/s41467-021-23446-9 . Optimizes externally varied network structures, not this endogenous switching rate.

The theorem is restricted to the first-harmonic linear threshold in the nonmagnetic background and positive finite OU memory time; no nonlinear phase diagram, finite-population convergence, or external scientific audit is asserted.

Self-review: passed. Independent audit: not yet performed.
