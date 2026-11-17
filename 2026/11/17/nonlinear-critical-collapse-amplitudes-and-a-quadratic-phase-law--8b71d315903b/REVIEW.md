# Scientific review

## Correctness (C): PASS

The exact log-odds conjugacy reduces the critical map to \((a,b)\mapsto (|a-\kappa(b)|,|b-\kappa(a)|)\). Strict-order preservation and convergence to the origin hold for all ordered initial pairs, and the gap argument proves finite entry into the forward-invariant smooth sector \(b\le\kappa(a)\). The squared sector map has the precise Taylor expansion \(T^2(z)=3z/4+Q(z)+O(\|z\|^3)\). Radial product bounds exclude a zero normalized amplitude, and a convergent telescoping series proves both the asymptotic vector and the quadratic correction. An analogous scalar argument proves the diagonal case. The pure-Python checker verifies the rational coefficients and tests finite trajectories; those tests are not used as infinite proofs. Domain restrictions and lack of uniformity near the diagonal are explicit.

## Originality (O): PASS, with historical-priority risk

Satur, arXiv:2611.13318v1, Section 5.2, computes the \(3/4\) factor only for the piecewise-linear approximation, explicitly calling rigorous control of the second-order terms an outstanding step. The current theorem resolves precisely that step globally and proves a nonzero phase vector with a universal quadratic correction. Satur's Theorem 2 establishes convergence, not exact nonlinear asymptotic amplitudes. Simpson, arXiv:1612.02932v1, proves general stability criteria on switching manifolds but does not give this model-specific two-step expansion. published-finding corpus similarity searches were run for the model, critical border collision, phase amplitudes, and equivalent nonlinear rates; their nearest entries concern different models. Results of semantic search do not certify global novelty. An unindexed earlier equivalent asymptotic expansion and a general linearization theorem specialized to this model remain residual risks.

## Mathematical value (V): PASS

The motivating paper identifies the critical collapse but leaves its nonlinear rate open, supported by numerical experiments. An exact all-initial-condition rate and the first nontrivial correction are needed to distinguish a genuine universal physical decay law from a linearization artefact. The surviving two-phase direction records how initial asymmetry affects transients despite universal decay speed; the diagonal/off-diagonal rate distinction is sharp. This is a structural asymptotic classification at a natural border-collision point, not a randomly selected finite calculation.

## Closest literature and limitations

The leading-order involution and \(3/4\) factor belong to Satur (2026), Section 5.2, and are not claimed as new. General nonsmooth exponential stability context belongs to Simpson (2016). The theorem is limited to \(\alpha=2\), the continuous reduced maxima map, and pointwise asymptotics with initial-state-dependent constants. Independent mathematical validation and exhaustive historical-priority adjudication have not been performed.

Self-review: passed. Independent audit: not yet performed.
