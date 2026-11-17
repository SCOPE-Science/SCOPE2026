# Scientific review: exceptional initial-seed sensitivity under resetting

## Correctness (C): PASS

The fixed-history response differentiates every return to the original seed correctly, giving exactly the published renewal formula. The logistic–doubling conjugacy yields the exact derivative identity with no typical-orbit approximation. The subcritical upper bound, almost-sure lower bound (Borel–Cantelli), and sparse prescribed-digit lower-growth subsequences prove the quantified claims. Crucially, the prefix-sparse construction fixes an `010` escape pattern after every long zero block, forcing the maximal upper exponential rate, while mid-block intervals suppress the renewal-weighted sum. The dimension calculation counts *all* free digits, including those between widely separated blocks; its exact value is \(1/(1+\alpha)\). The countable union has full dimension and remains null. The standalone `CHECK.py` passed 72 exact-identity, finite-history, and finite-block consistency checks. Its finite tests are explicitly not offered as proofs of infinite statements.

## Originality (O): PASS within inspected literature

The 2024 Aron–Kulkarni manuscript and its 2026 revised version contain the crucial renewal identity and propose the uniform chaotic resetting exponent; they do not state the full-dimension, seed-uniform exceptional construction. Their derivation assumes a well-defined seed-independent bare exponent. The 2025 follow-up studies resetting Lyapunov spectra and wavefronts, not failure of the one-dimensional fixed-seed annealed limit. Gelfert–Rams and Barreira–Schmeling develop non-typical ordinary Lyapunov/Birkhoff sets; even if such a set is known, it need not be irregular after the *positive renewal sum* takes a logarithmic asymptotic. Targeted published-record searches and the accessible historical claims yielded no source proving this renewal-specific statement. A general nonadditive irregular-spectrum theorem specialized to renewal sums remains a priority risk; abstract-level comparison to the 2000 paper does not settle that risk.

## Mathematical value (V): PASS

The motivating literature treats a critical reset probability as a seed-independent dynamical transition; precisely specifying the domain of that statement is mathematically important. A generic isolated pathological seed would be substantially weaker. Here the exceptional dependence occurs on a dense, Hausdorff-dimension-one null set **shared across all subcritical reset probabilities**, while almost-everywhere universality is independently proved, and the high-reset regime is uniformly seed-regular in the interior. This is a sharp measure-versus-dimension distinction for a directly defined dynamical sensitivity observable. There is no claim to resolve a broader multivariate or general random-map classification.

## Closest literature and residual limitations

Aron–Kulkarni, arXiv:2412.21043v1 (2024-12-30), equation (8) and logistic-map discussion; arXiv:2510.07394 (2025-10-08), resetting spectra; Gelfert–Rams, arXiv:0709.2832, ordinary Lyapunov irregular sets; Barreira–Schmeling, DOI 10.1007/BF02773211, non-typical multifractal sets. Only the resetting papers' relevant full-text sections and Gelfert–Rams' relevant original passages were inspected; Barreira–Schmeling was compared at the abstract and bibliographic level. No whole-literature uniqueness is certified.

The claim is restricted to fixed-seed Bernoulli resets of the parameter-four logistic interval map and expected absolute seed derivatives; it does not concern pathwise derivatives, endpoint seeds, or arbitrarily distributed resets. The review is a same-model reconstruction, not independent mathematical validation.

Self-review: passed. Independent audit: not yet performed.
