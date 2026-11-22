# Scientific assessment

## Correctness — PASS

The prescribed nonnegative pair \(G_{i,h}=\alpha_{i,h}x_i\) and \(L_{i,h}=\kappa_i+\alpha_{i,h}\) cancels identically to \(-\kappa_i x_i\), for every state and offset. The rational NSFD update is exactly a positive scalar multiplier. The uniform identity for the effective rate and the log inequality bound the global shadow-flow error by \(C_i h\) without any upper bound on the offsets. Compactness and exponential injectivity give the full attainable limit cube and the necessary-and-sufficient criterion. Exact rational identity checks and finite limiting examples accompany the proof, without being presented as its substitute.

## Originality — PASS, with historical-priority limitations

The source's consistency statement assumes fixed differentiable gain and loss functions and supplies no resolution-dependent gauge classification. Its full first-public preprint was inspected, including equations (1)–(3), Proposition 1, and the proof. General nonstandard discretization surveys and a different Patankar face-flux-offset stalling result do not imply the all-resolution shadow-flow theorem for this NSFD layer. The separate two-time split-flow alias theorem concerns inverse identification of time maps, not this gain–loss representation equivalence. Search and full-text comparisons found no covering theorem, but unexamined literature may contain equivalent reformulations.

## Value — PASS

Resolution transfer is an intrinsic mathematical question when positivity-constrained gain–loss parameters are inferred independently from observations at different sampling intervals: equality of the underlying vector field does not identify the representation. A sharp and complete continuum-limit classification distinguishes correct decay, arbitrary slowed decay, and total freezing; it gives an exact uniform parameter-growth condition required for the physically correct limit. This is not merely a positivity check or an assertion that first-order methods converge; it delineates the boundary at which a fixed-model consistency theorem ceases to be uniform.

## Closest literature and limitations

Zinihi–Ehrhardt–Sidi Ammi (arXiv:2607.10858v1) is the exact source of the integrator. Related fixed-step flux-offset mPDeC stalling and split exponential–Euler alias results concern different maps and hypotheses. The present result is restricted to diagonal linear ODEs, nonnegative offsets and mesh-dependent representations. No claim is made for arbitrary neural-network training procedures, nonlinear coupled equations, or an independent mathematical audit.

Self-review: passed. Independent audit: not yet performed.
