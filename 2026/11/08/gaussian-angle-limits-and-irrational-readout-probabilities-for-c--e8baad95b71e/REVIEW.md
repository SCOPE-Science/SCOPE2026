# Scientific review

**Correctness: PASS.** The proof gives the exact multinomial edge-category law and the exact linear transformation from local type counts to two independent Gaussian coordinates. It treats noncritical drift, identically zero contrasts, Gaussian boundary-nullity, and realization of every permitted rational direction. The irrational example follows from the bivariate normal quadrant identity plus an algebraic-integer proof. Exact finite enumerations and independent coefficient checks in `checker.py` returned `ALL_CHECKS_OK`.

**Originality: PASS on examined statements, with a material residual priority risk.** The 2026 Benedikt–Lu–Perry–Tan work is about decidability of local/global Presburger satisfiability rather than probability spectra; the earlier Kopczyński–Tan *spectrum* concerns finite-model sizes, not limiting probabilities. Random bounded-degree graph first-order limit-law papers use a strictly weaker observational logic. A standard multinomial CLT is broader as a probability method and directly supplies an ingredient; what is not identified in the checked sources is the exact logical angular-spectrum classification, its irrational witness, and the expressivity contrast. Closely related unindexed work and general Gaussian decision-region results may reduce historical priority.

**Value: PASS.** The classification completely describes a natural nontrivial readout fragment motivated by a new decidable counting logic; it reveals a qualitative change from three limiting values to a countable dense set with explicit irrational probability after just one bounded local observation. The precise invariant and the expressivity contrast, not novelty of the CLT, motivate the result.

**Limitations.** Only a fixed linear-readout fragment is classified. Full nesting, congruence counting, biased or dependent colors, and general graph models are not treated. Independent mathematical and historical-priority audits have not been performed.

Self-review: passed. Independent audit: not yet performed.
