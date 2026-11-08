# Scientific review — finite-size antipodal stability for a higher-order phase model

## Correctness — PASS

The theorem concerns the explicitly normalized complete-graph model with *ordered, distinct* triads, positive pairwise and triadic gains, and all integers \(n\ge3\). Every antisynchronous binary state is an equilibrium. Differentiating each triadic term yields two appearances of any off-diagonal derivative, giving the essential factor \(2\). The Jacobian's three invariant transverse spaces have dimensions \(p-1\), \(q-1\), and \(1\); together with the global rotation they exhaust all \(n\) eigen-directions. Their eigenvalues are explicit and verified by an independent exact-rational ordered-triple sum. The inequalities reduce to \(S^2>n\), a lower triadic threshold and, in an exceptional strip, a finite upper threshold. The exact count for seven vertices is computed over every nontrivial minority size. The argument treats the zero eigenvalues at parameter boundaries as unclassified nonlinear cases, not as hyperbolic attractors.

`verify.py` was executed successfully. It confirmed the complete eigenvector decomposition and window signs for \(504\) finite rational parameter examples, both seven-node endpoints, the orbit counts and the nonlinear vector-field derivatives in three numerical cases. These are checks, not an infinite proof.

## Originality — PASS under inspected evidence

The most closely related exact model is Wang et al., arXiv:2603.14950, where Section II defines ordered distinct triads and Section V studies spectra of *twisted* states rather than antipodal two-population configurations. Zhang et al., arXiv:2309.16581, report two-cluster and other non-twisted attractors in higher-order Kuramoto systems, but do not provide this complete finite-size antipodal spectrum, strict population-imbalance cutoff, re-entrant upper boundary or exact count of stable labelled clusters. Carballosa et al., arXiv:2308.05406, treat an all-to-all mixed mean-field model but study distributions of natural frequencies and cluster transitions instead of these exact finite-node normalized distinct-triad stability windows. Pure-triad and continuum-limit cluster mechanisms are older and are not claimed as new. Kovalenko et al. (Phys. Rev. Lett. 127, 258301, 2021) establish an earlier strong cluster mechanism with unrestricted index sums and negative pairwise coupling; their full published article was inspected and does not contain the present finite distinct-triad Jacobian theorem.

The finite-size sign classification is not obtained by simply identifying a model name: one must account for the ordered-triad normalization, decompose three different transverse modes, and compare their crossing parameters. Nevertheless, all-to-all cluster eigenspace reductions are standard, and previously unindexed finite-size calculations remain a historical-priority risk. Absence of a search match does not independently establish novelty.

## Mathematical value — PASS

The specific question is motivated by the established observation that higher-order interactions create two-cluster memory-like attractors but that stronger triadic gain can profoundly rearrange the attractor landscape. The result provides an exact answer for every labelled antipodal partition on a complete graph. The universal imbalance cutoff \(S^2>n\) explains which configurations are even eligible, while the separate upper bound identifies infinitely many genuinely *re-entrant* stable windows. On seven vertices, exactly \(21\) locally attracting antipodal circles disappear between two concrete coupling values even though complete synchrony remains stable. The count is a directly useful benchmark for finite-size basin studies and is not a selected arbitrary numerical slice.

The result is deliberately restricted to antipodal equilibria, not the full global attractor landscape. It does not assert global basins, finite-noise lifetimes, nonlinear behavior at the thresholds, or dynamical classification for more general hypergraphs.

Self-review: passed. Independent audit: not yet performed.
