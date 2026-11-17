# Self-review

## Correctness

**PASS.** The strain-weight recursion is exactly common to all strains. Subtracting the weighted initial fraction times the total-state update proves a scalar linear recurrence with multiplier \(1-hd\) *at each node*. Physical invariance follows from the step bound. The subcritical scalar bound and critical normalized stable-mode contraction are analytically sufficient; reciprocal increments then give the claimed critical amplitude. Above threshold, an ordered subsolution/supersolution squeeze and uniqueness of the positive scalar fixed point establish global attraction. The converse uses the full open box of possible strain partitions, turning one-step share invariance into a row-eigenvector identity for all interior total states; this forces rank one. The attached checker passes the exact and numerical tests described in RESULT.md.

## Originality

**PASS within the inspected evidence.** The strongest same-model source, Gracy et al. (2023), supplies the general Euler competitive SIS equations and analyses convergence and equilibria; the examined theorem and model sections do not specify the fixed weighted strain share or the rigidity converse. The 2026 aligned rank-one result covers independent recovery-adjusted strain profiles and *excludes* the proportional case. The 2021 and 2023 multi-virus literature already knows that neutral equilibrium continua can occur, so that feature alone is not novel. The contribution assessed is the model-specific exact all-time decomposition, initialized selection, universal critical profile, and if-and-only-if contact-rank characterization. Uninspected relevant manuscripts and equivalent identities not indexed under epidemic terminology remain risks.

## Value

**PASS.** In identical-strain competition, existence of a continuum of endemic states does not determine which state a heterogeneous network selects from given infection data. The theorem identifies that state from one observable weighted initial fraction without integrating the nonlinear dynamics, quantifies every node's transient departure from it, and supplies the universal per-strain extinction amplitude at threshold. The necessity theorem proves rank one is the exact structural boundary for such a fixed positive weighted invariant across all states, rather than an arbitrary convenient example. These are meaningful complete classifications of a neutral population-dynamics regime, not an arbitrary finite parameter slice or mere restatement of standard local stability.

## Closest literature and limits

Primary: Gracy–Liu–Başar–Uribe, arXiv:2310.13853v1 (full source equations and result sections examined); related: Ye–Anderson–Liu arXiv:2111.07507 and Gracy et al. arXiv:2303.16457 (abstract-level comparison); published aligned rank-one competitive-bivirus result `567a29ac68ce` (complete RESULT text examined); product-hazard SIS critical result `c0fb1830567e` (scientific statement, proof opening and comparison read). Residual risks are unindexed/disparate mathematical treatments of multiplicative cocycles or neutral strain conservation, and full-text coverage of those two related preprints. Distinguish the deterministic discrete Euler model from nonlinear infection hazards or Markov epidemic chains. No independent mathematical validation is asserted.

Self-review: passed. Independent audit: not yet performed.
