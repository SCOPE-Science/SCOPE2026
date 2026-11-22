# Scientific assessment

**Correctness: PASS.** The difference variables obey the displayed cooperative affine system by direct subtraction of the source's normalized equations. Its positive fundamental matrix has row-sum comparison bounds independent of the Fermi feedback. Variation of constants yields a quantitative uniform lower bound, and the explicitly defined time makes both gaps strictly positive. `checker.py` symbolically verifies the difference equations and numerically stress-tests the bound. The infinite-time statement follows from the proof, not finite simulation.

**Originality: PASS within the inspected primary literature.** The originating 2026 paper supplies the mean-field equations but does not derive a uniform payoff-independent sorting time and gap across arbitrary initial edge-state distributions. The authors' 2024 community-edge model uses different environment coordinates; general cooperative systems give mathematical tools but no recorded same-model environmental sorting statement was found. A broader comparison theorem may subsume the proof technique, and historical priority is not independently established.

**Value: PASS.** This gives a structural restriction on all solutions, including the paper's oscillatory regimes: conditional depleted environments necessarily become and remain ranked by strategy-pair type, no matter how strongly selection distorts the strategy trajectory. The payoff-independent finite horizon and nonzero gap turn a qualitative intuition into an explicit transient bound, useful for testing numerical approximations and interpreting conditional edge measurements. It is not a generic equilibrium-only monotonicity calculation.

Limitations: the bound is not sharp; finite stochastic networks and sparse-graph pair closure are not covered.

Self-review: passed. Independent audit: not yet performed.
