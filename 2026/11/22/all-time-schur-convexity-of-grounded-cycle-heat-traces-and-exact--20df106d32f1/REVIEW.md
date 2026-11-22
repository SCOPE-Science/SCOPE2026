# Scientific review: all-time cyclic grounded heat-trace ordering

## Correctness — PASS

Grounded follower paths retain degree two. Their matrix exponential is \(e^{-2t}\exp(tA_\ell)\), so a rooted closed-walk span expansion with nonnegative coefficients establishes \(h_{\ell+1}-2h_\ell+h_{\ell-1}\ge2e^{-2t}t^{2\ell}/(2\ell)!>0\). Integer-gap transfers yield every optimal and maximal placement, while the rooted-gap-word count gives the exact multiplicity. Positive-time integrals transfer the ranking to inverse powers and integrated covariance. The standalone matrix/walk checker passed 18,804 finite comparisons; the infinite proof is analytical. Edge weights, principal-minor convention, strict time domain and all edge cases are specified.

## Originality — PASS, qualified

The closest full-text literature is Clark et al. (2013), which studies a different transient convergence-error bound and approximate supermodular selection; Patterson et al. (2014), whose ring dynamic programming optimizes a stationary inverse trace; the previously established screened-cycle Nyström theorem, which is **exactly equivalent** to screened inverse-first-moment balanced leader selection and already gives its optimizer count; and El Soufi–Harrell (2014), whose heat-trace obstacle theorem applies to continuous Euclidean domains. Searches also compared a published directed-ring spacing result and the existing cycle/other-graph heat work. Neither the recovered full-text theorems nor accessible indexed statements imply the new strictly ordered *all-time* discrete cycle gap theorem or its sharp transfer penalty; **the inverse-first-moment optimum count is prior work**, not claimed as original. Unindexed equivalent work and some inaccessible record full text remain explicit publication-priority risks. General ring block decomposition and the earlier stationary inverse-trace criterion are prior contributions, not independent claims here.

## Value — PASS

Perfectly grounded cycle networks are a natural homogeneous control benchmark. An exact, simultaneous minimizer for all finite horizons, all positive inverse spectral orders and all leader budgets has practical design meaning distinct from a single-time optimum. The walk-span lemma supplies a strict, quantitative structural reason for balancing; the result also verifies the known optimum count at every horizon and establishes the worst configuration. The novel pointwise all-time strict hierarchy is a natural complete classification, not merely a known-table recomputation.

## Scientific limitations

Only simple unweighted undirected cycles, uniform screening and perfect grounding are treated. The theorem concerns isotropic trace metrics rather than every possible initial condition, and no independent audit or exhaustive publication-priority check has been completed. The reproduced finite checks cannot by themselves certify the infinite theorem. The first-inverse balanced optimum and count are already known from the screened-cycle Nyström equivalence.

Self-review: passed. Independent audit: not yet performed.
