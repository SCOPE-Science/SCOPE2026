# Scientific review: exact finite-capacity logistic stationary-mode boundary

## Correctness — PASS

For the finite irreducible birth–death chain, detailed balance gives the exact adjacent stationary-mass ratios. Their successive differences have a numerator strictly decreasing in the occupancy index, giving the two-modal-component ceiling and reducing occurrence of a separated occupied mode to a strict threshold crossing. The threshold is the minimum of finitely many explicitly derived rational functions, not a numerical fit. The continuous minimizer, closed envelope, and exact lattice correction follow from a positive quadratic double-root identity. The \(N^{-1/2}\), \(N^{-1}\), and error orders follow from expansion and bounded integer rounding. The exact example at \(N=10\) has \(B=639/400\), below \(b=8/5\). The standalone checker reproduced the relevant ratios, finite minimizers, lattice identity, and sample asymptotics. General correctness is supported by the analytic proof, not inferred from the finite tests.

## Originality — PASS, with documented priority risk

The model of Brugevin and Zanette (arXiv:2605.27100, 2026) establishes the setting and discusses active/vacant intervals and an approximate active-time bimodality criterion. The present result instead establishes the exact positive-immigration stationary **count**-mode phase boundary, its integer correction, and its weak-immigration asymptotics. This is not the paper's approximate active-time criterion. Chuang Xu (arXiv:1605.06084) establishes stationary bimodality in a distinct mate-limited, strong-Allee model; that mechanism does not imply the displayed threshold for a logistic contact-birth process without mate limitation. The known stationary birth–death product recursion is credited rather than claimed as novel. Earlier mass-limit results for the same logistic chain concern exponentially weak immigration or logarithmic count scaling; neither establishes the finite modal threshold. A 2004 immigration-logistic study by Matis and Kiffe was available in abstract only and may contain closer unpublished-in-abstract finite-mode information. Thus the priority claim is bounded by accessible literature, not a claim of globally proved uniqueness.

## Value — PASS

The exact joint birth-immigration threshold distinguishes a stationary zero-density peak plus an occupied peak from a monotone stationary population law. This naturally addresses the interpretation of population intermittency in the source model, while keeping stationary count modality distinct from the distribution of active-period lengths. The finite-integer correction supplies an exact boundary and the weak-immigration expansion gives a \(1/\sqrt N\) scale inaccessible to mean-field growth alone. The result characterizes an entire parameter region and its discrete-size effects, not an arbitrary parameter sample.

## Limitations and independent checking

Local modes are not necessarily comparable in total probability mass; the theorem does not compute active/vacant dwell times, fixation, network effects, or finite-time extinction. The asymptotic expansion is not uniform as the normalized immigration \(\eta\) approaches one. There remains a limited historical-priority risk from older population studies not inspected in full. All computational checks use finite inputs; no formal proof-assistant or external certification is asserted.

Self-review: passed. Independent audit: not yet performed.
