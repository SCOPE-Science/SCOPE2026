# Scientific assessment

## Correctness — PASS

The model specifies the order of events, both seasonal matrices, mortality and endpoint policies. Direct matrix multiplication gives the period-two square factorization; the Perron root yields the exact growth factor. Its exact second derivative is positive throughout the closed policy interval, hence interior policies are strictly inferior to an endpoint. Endpoint evaluation and one-sided derivatives establish both cutoff thresholds and the local-versus-global trap. The concrete rescue example follows from an exact quadratic and a proved unique crossing. `verify.py` corroborates the identities using rational matrices; computation is not substituted for an infinite proof.

## Originality — PASS (best-knowledge, provisional)

The closest inspected work is Schreiber and Li (arXiv:1007.5267), particularly its model assumptions, Theorem 2, application, and discussion of migrant-cost extensions. That theorem assumes lossless movement and analyzes evolutionary invasibility, not the exact intrinsic-growth optimum with migration mortality. Kirkland, Li and Schreiber (DOI:10.1137/050628933), especially their Theorem 4.4, allow mortality but cover a single temporally constant patch-growth matrix; this does not imply a reversed two-season matrix-product comparison. McPeek and Holt (DOI:10.1086/285453) discuss density-regulated selection, including low/high dispersal types, without the present linear multiplier cutoff. This distinguishes objects and implications; similarity-search nonhits alone do not establish originality. Residual risk remains from specialized spectral-radius and historical dispersal-cost literature and requires independent priority verification.

## Value — PASS

Mortality during dispersal is a direct ecological mechanism. This precise model resolves the full intervention design space rather than just giving a small perturbation or numerical example. Its counterintuitive nonempty interval where sedentary behavior locally maximizes growth but complete movement globally dominates makes an explicit limitation of marginal-policy reasoning. The open parameter set in which migration rescues two individually declining patches gives a concrete ecological interpretation without claiming a field-validated policy.

## Limits

The result concerns linear rare-population growth with perfectly alternating patch quality and symmetric migration; it makes no evolutionary-stability, nonlinear-carrying-capacity or stochastic-extinction claim. Related work on periodic dispersal and static costs makes historical priority provisional.

Self-review: passed. Independent audit: not yet performed.
