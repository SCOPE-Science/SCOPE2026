# Scientific review

**Correctness — PASS.** The ambient gradient and exact EMA/retraction equations yield a two-dimensional linearization \(B_t=I+t^{-1/2}A+t^{-1}C\) plus an independent decaying normal-memory mode. The characteristic polynomial has strictly positive determinant \(\theta\) and trace \(\theta(c-1)-1\). Positive-definite discrete Lyapunov estimates establish stability or instability on either strict side of the threshold. Exact symbolic and numerical Jacobian checks support the derivation. The critical equality, nonlinear global trajectories and noisy dynamics are not claimed.

**Originality — PASS, with historical-priority risk.** The primary full-text source gives the RGR-EMA update, sufficient convergence estimates and a tangent-space REMA comparator, but does not provide this same-objective ambient-extension stability classification. Nearby published-finding corpus records concern Stiefel equivariance or other optimizer spectral thresholds and do not imply this precise result. Earlier Riemannian momentum references emphasize tangent-space methods; their available summaries do not constitute full exclusions. A broader prior theorem about extrinsic EMA gauge dependence remains possible.

**Value — PASS.** The exact stability frontier is a model-identifiability boundary for the algorithm: the constrained problem and its Hessian are fixed, while a derivative entirely normal to the feasible set changes its local dynamics. It identifies a concrete risk of retaining unprojected historical gradients and a reason to distinguish ambient and intrinsic momentum estimators. This is not a counterexample to small-stepsize convergence guarantees.

**Closest comparison and limitations.** Yuan–Sun–Yuan (2026), Section 3.4 and Theorem 4.3; their Appendix B REMA method; Han–Gao (2021); Alimisis et al. (2021). Only late-time linearized stability of the deterministic rank-one case is decided; the boundary and global basins are left open.

Self-review: passed. Independent audit: not yet performed.
