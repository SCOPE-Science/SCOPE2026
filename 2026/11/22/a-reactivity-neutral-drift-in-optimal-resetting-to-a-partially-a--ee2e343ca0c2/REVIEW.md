# Scientific assessment: reactivity-neutral drift in partially absorbing Brownian resetting

## Correctness — PASS

The claim is restricted to the unique mean-reaction-time-optimal Poisson rate under constant drift and one delta sink. The exact mean formula is taken from the cited primary literature. Differentiating this formula yields the stationarity function \(B_\eta\), whose one-crossing geometry proves a unique, transverse global minimum for every finite reactivity. The reactivity derivative at the optimum vanishes only if the \(\eta\)-linear and constant stationarity terms vanish simultaneously, reducing to a unique one-variable root. Strict monotonicity of that root equation and continuity with independently controlled signs at zero and strong inward drift give both strict sides of the reversal. Boundary regimes, quantifiers and physical normalization were checked. The packaged standard-library checker passed 534 finite tests; those tests do not establish the global theorem in place of the analytic proof.

## Originality — PASS, qualified

The exact drifted mean, zero-drift reactivity monotonicity, finite-drift numerical behavior and all-drift unique optimizer are established by prior literature and published mathematical results; none is claimed as new. The directly inspected initiating paper (Mazzolo, arXiv:2609.22527v1, Appendix A.4–A.5) analyzes reactivity dependence only at zero drift and drift dependence at fixed reactivity, without the unique all-reactivities invariant optimum. Whitehouse–Evans–Majumdar (arXiv:1301.2489, Section 4.1) concerns zero drift; Ray–Mondal–Reuveni (arXiv:1811.08239, Section IV) concerns a perfectly absorbing target. Closely matching published drifted-point-trap notes on orientation gaps, uniqueness and strong-reactivity crossover were read by statement and implication; none of their investigated conclusions entails the globally fixed reset-rate crossing at \(\mu_c\). An implicit derivative identity or an equivalent statement in broader resetting literature remains a priority risk. Search noncoverage is not treated as uniqueness certification.

## Value — PASS

The problem is motivated directly by the known tension between drift-assisted trap encounters and incomplete reaction on each encounter. The new sharp criterion resolves whether more effective chemistry should be accompanied by more or less frequent restarting, and identifies a singular reactivity-independent design point. It is a global-in-reactivity structural boundary, not a small expansion, arbitrary parameter slice or restatement of the previously known formula. Further value could come from robustness to imperfect drift calibration, but that property is not claimed.

## Limitations and risks

The model assumes one constant-drift diffusion on the real line, one local-time point sink, a fixed reset point and a memoryless reset clock. The theorem concerns the optimizer of mean killing time only. No claim is made about multi-target interactions, noisy estimation, non-Poisson clocks or the discontinuous perfect-absorber transition. Publication priority remains subject to external expert and independent checking.

Self-review: passed. Independent audit: not yet performed.
