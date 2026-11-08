# Self-review

## Correctness — PASS

The decomposition of binary quasinecklaces into an initial longest zero run and bounded trailing zero runs gives the exact count. Fixed-window rare-pattern inclusion–exclusion produces the Poisson factor, and a separate second-moment block bound controls all discarded initial-run lengths uniformly. Burnside normalization and a Mellin/Fourier integral complete the all-length proof. Direct enumeration of every binary word through length 16 agrees with two counting implementations, and exact counts through length 4096 support the phase law numerically. These finite checks do not substitute for the proof. The critical error to exclude is unjustified interchange of the logarithmic-run window with the whole sum; the uniform two-tail argument supplies that step.

## Originality — PASS with historical priority risk

Gabrić and Sawada's 2026 original paper supplies an exact finite recurrence and a uniform constant-factor bound, but its inspected main enumerative sections do not establish the explicit log-periodic ratio limit or nonzero Fourier harmonics. The 2017 pseudonecklace paper treats a different auxiliary superset. Accessible fixed-content exact identities describe sparse regimes and permit finite sums but do not establish the uniform dense-composition limit or imply its phase law without additional analysis. The classical 1978 run-distribution paper was only accessible at abstract level and is a residual risk; no definitive priority certification is claimed. The exact source comparisons, queries, and limitations are recorded in AUDIT.json.

## Mathematical value — PASS

The candidate count per necklace is the natural central quantitative cost in colex quasinecklace-based enumeration. Replacing the unspecified multiplicative bound with an explicit positive analytic one-periodic function, and proving its nonconstancy and complete Fourier coefficients, reveals a previously unquantified digital phase effect. This is an infinite-family theorem about the full unrestricted binary enumerator, not an arbitrary finite sample.

## Boundaries

The result is restricted to binary quasinecklaces and is about candidate counts, not specific machine-time instruction counts. A sharp rate for the o(1) term is not established. Priority against unread classical full texts and independent validation remain open.

Self-review: passed. Independent audit: not yet performed.
