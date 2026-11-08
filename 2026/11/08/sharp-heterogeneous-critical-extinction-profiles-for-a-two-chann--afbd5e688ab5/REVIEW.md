# Scientific review

**Correctness — PASS.** The invariant cube, cooperative strong positivity, Perron pair, LaSalle extinction argument and stable spectral alignment are established in RESULT.md. The nonstandard quadratic identity uses the vanishing second derivative of the arctan kernel and is independently verified from the packaged `check.py` on 30 heterogeneous systems, as well as one exact-rational three-node certificate. Convergence of finite simulations alone is not used as proof.

**Originality — PASS with residual risk.** The complete 2026 motivating source provides local linear thresholds and regular-system equilibria, but does not state an arbitrary connected topology's explicit critical spatial \(1/t\) coefficient. Paré et al. (2021) provide global SIWS threshold theory for an analogous but different linear environment model; neither that result nor generic positive-systems principles supply the written cubic incidence formula without additional model-specific calculation. A previously unindexed normal-form calculation may nevertheless imply it, and independent confirmation remains desirable.

**Value — PASS.** A reproduction threshold predicts whether an epidemic can invade but not the size of the near-critical persistent tail. The result computes each node's and environment's late-time contamination coefficient on heterogeneous connected hypergraphs, including the exact dependence on node–environment incidence. The rate is slow and algebraic even though global extinction holds, a quantitatively motivated distinction for threshold interventions.

**Scientific limits.** Deterministic closure only; fixed connected network; positive rates; no stochastic extinction-time claim or finite-time error bound. The spectral-normalization and curvature assumptions are essential.

Self-review: passed. Independent audit: not yet performed.
