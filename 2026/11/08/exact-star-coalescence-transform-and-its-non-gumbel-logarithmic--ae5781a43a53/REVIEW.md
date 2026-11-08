# Review of the star full-coalescence law

## Correctness
**PASS.** The process uses independent rate-one particle clocks and mergers at shared vertices. All states reduce exactly to hub occupancy and the number of occupied leaves. The first-step system treats the one-leaf absorbing boundary separately; this is essential. Its rational resolvent yields the explicit finite transform, and independent exact-rational generator calculations reproduce the transform and mean for the tested sizes. Gamma factorization is an algebraic re-expression of the finite product. Uniform near-origin gamma-ratio asymptotics and two-sided exponential moment bounds justify the non-Gumbel limiting law. The exact mean and limiting variance were derived analytically. Finite tests are supplementary, not proofs of the asymptotic theorem.

## Originality
**PASS, with historical-priority risk.** Kanade, Mallmann-Trenn and Sauerwald, Appendix C.7 (arXiv:1611.02460), establish only the order of the star coalescence time for a *synchronous* discrete-time model. Ben-Ari, Panzo, Speegle and VandenBerg (arXiv:2004.10187), especially Sections 4 and 5, study discrete-time quasi-stationary voter distributions and dual coalescence, not the full asynchronous star hitting-time transform. Pickering and Lim (arXiv:1408.2130), Section V, address the two-opinion voter model and use approximate spectral methods for complete bipartite graphs. Kátai-Urbán, Pongrácz and Szabó (2024) study discordant voting protocols with different transition mechanisms. None of these inspected statements implies the exact finite transform and logarithmically centered limit in this result. The overlap search is evidence of noncoverage among inspected work, not proof of global novelty; specialized earlier unpublished derivations cannot be ruled out.

## Value
**PASS.** Full coalescence from all occupied sites is a natural interacting-particle observable and a distinct-opinion consensus time. Existing logarithmic-scale estimates do not describe its order-one fluctuations. The new formula gives an exact computable law for each finite star and a non-Gumbel centered limit with a variance sharply different from the classical extreme-value benchmark. The phenomenon is driven by revisits to the high-degree center, making the exact fluctuation law mathematically motivated.

## Limits
The theorem does not cover synchronous jumps, binary initial opinion consensus, edge-clock updates, or multiple hub vertices. The local moment-transform interval is sufficient, not optimal. No independent mathematical audit has occurred.

Self-review: passed. Independent audit: not yet performed.
