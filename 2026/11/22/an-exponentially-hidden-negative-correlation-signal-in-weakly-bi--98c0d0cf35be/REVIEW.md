# Scientific review

## Correctness — PASS
The claim concerns a precisely normalized, irreducible three-state column generator. The proof derives its stationary distribution and two nonzero eigenvalues, reconstructs the stationary occupancy autocovariance from its initial value and derivative, and computes its first zero and exact global negative minimum. The weak-bias logarithmic limit follows from an exact positive expression, with no replacement of an infinite limit by finite sampling. Exact symbolic identities and direct matrix-exponential spot checks have been replayed successfully from `check.py`.

## Originality — PASS, with residual priority risk
Generic damped oscillation and two-mode spectral decomposition for three-state Markov processes were already established by Amann, Schmiedl and Seifert (2010), and general three-state correlation formulae are discussed by Chen (2007). Those ingredients are expressly treated as prior. Fiusa et al. (2026) give the double-dot generator and stationary populations but not the frequency-optimal weak-bias first-negative-time and sharp global-negative-amplitude laws. Comparison against relevant indexed research statements found no exact match for this combined physical tuning and essential-suppression asymptotic. Chen's complete 2007 article was not available for comparison, creating an important risk that a general formula already implicitly yields the specific result without substantial work; no priority certification is claimed.

## Value — PASS
A negative time-lagged occupancy covariance is a recognized diagnostic of irreversible three-state dynamics. The finding quantifies why even an oscillation-frequency-maximizing operating point can conceal such a diagnostic as the reservoirs approach equilibrium: detection lag diverges inversely with contrast while the strongest negative signal is exponentially small. The exact singular rate is a natural parameter-dependent boundary and provides a reproducible benchmark for finite-bandwidth or finite-sample transport diagnostics, rather than an arbitrary finite-state numeric example.

## Scope and limitations
Only incoherent classical three-state dynamics with infinite Coulomb blockade, equal reservoir couplings and the specified hopping tuning are proved. Noise, finite observation statistics and coherent dynamics are not covered. The generic oscillation criterion is not new, no optimality over all control strategies is claimed, and independent priority and proof validation remain outstanding.

Self-review: passed. Independent audit: not yet performed.
