# Scientific review

## Correctness — PASS

The ratio-feedback derivative is reconstructed from equation (4) and the published gradient step; strict convex-combination updates keep every gain strictly interior, so the feedback is defined at each finite time. Independent fresh samples give a contractive random affine recursion and exact stationary first/second moments. The prospective multiplier is computed from an independent test curvature and is **not** substituted for the growth rate of actual squared state. A quartic sign analysis gives the unique gain-window threshold. The almost-sure state bound follows from uniformly coupled stationary and nonstationary gain paths, Lipschitz truncated logarithms, the ergodic theorem and Jensen's inequality. Exact rational regression checks are in the standalone artifact. The proof does not assert mean-square divergence of the actual state.

## Originality — PASS, subject to historical-priority risk

The closely related 2026 source defines stochastic out-of-sample ratio feedback and analyzes large-batch convergence. A previous result on stochastic OSGM gives its **population** gain target and a **fixed** target mean-square stability classification, not the actual stochastic online-gain stationary fluctuations, the sharp gain-induced prospective risk crossing, or the simultaneous all-gain almost-sure contraction bound. General stochastic-approximation literature covers random affine tools, but the current source-specific joint classification requires the feedback reduction, invariant law and pathwise Jensen argument. Published mathematical-record searches for stochastic OSGM stationary gains, curvature thresholds and prospective-versus-pathwise separation did not identify stronger coverage. General stationary-recursion literature is broad and not exhaustively excluded.

## Value — PASS

The gain learns a correct population mean but its persistent variance can cause fresh-test mean-square amplification on a specific exact curvature/gain phase, even as the actual coupled optimizer converges almost surely. This separates three operationally distinct diagnostics—feedback-target quality, fresh-test squared progress and actual typical-path convergence—and quantifies the sharp boundary at which the first two disagree. The exact criterion can inform the interpretation and tuning of noisy online preconditioning, without claiming a general convergence theorem.

## Closest comparisons and limitations

The 2026 source has full accessible equation (4), Algorithm 2 and appendix; the previous published source-specific record was inspected as a full `RESULT.md`. Generic constant-step stochastic-approximation research and deterministic online-scaling theory are acknowledged and do not themselves provide the identified source-specific transition. Complete historical priority cannot be established by search. The result is restricted to scalar equal-probability two-curvature interpolation and a prospective factor, not actual state mean-square divergence.

Self-review: passed. Independent audit: not yet performed.
