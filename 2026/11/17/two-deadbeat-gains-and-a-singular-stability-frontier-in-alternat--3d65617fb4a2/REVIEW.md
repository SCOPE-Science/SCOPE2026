# Scientific review: alternating sampled-feedback stability

## Correctness (C): PASS

The initial-value equation is well posed on every cell because the self-consistency denominator is strictly positive. Exact integration gives the one-cell factors, and their product is the full physical two-cell Floquet multiplier. The completed-square inequality proves the strict universal lower bound; an upward quadratic with a negative constant term has exactly one positive stability crossing. An exact derivative with respect to the sample location proves strict growth of the stability budget. The numerator factorization gives precisely two distinct deadbeat gains for interior phases. A singular expansion proves the endpoint coefficient, and exact rational arithmetic checks the stated witness. The standalone numerical checker corroborates the algebra but is not substituted for proof.

## Originality (O): PASS within inspected evidence

The most directly relevant 2012 Song–Liu paper already treats the endpoint-alternating equation, so that case is explicitly excluded as a novelty claim. The 2026 Torres Naranjo–Castillo Apolonio paper admits generalized interior sampling and develops sufficient estimates, but its inspected theorem and examples do not give the sharp two-period gain frontier, two distinct finite-time-extinction gains, or the reciprocal endpoint law. Published single-phase gain-stability studies cover constant sampling phases rather than an alternating two-step product. The joint interior-phase structure, not the elementary single-cell formula, is the novelty claim. Historical priority for other mixed-argument scalar equations cannot be absolutely excluded.

## Mathematical value (V): PASS

The result solves a natural design question left open by sufficient-condition approaches: how sharp closed-loop stability and exact finite-time cancellation change when one sample in an alternating inhibitory feedback schedule moves continuously from delayed to advanced observation. Two physically distinct deadbeat gains exist for every genuine interior advanced phase and merge at the retarded endpoint, while the stable gain budget diverges at the advanced endpoint with an exact coefficient. This sharp instability-versus-cancellation classification is useful for assessing periodic sampling protocols and is not a mere normalization or single isolated parameter check.

## Closest literature and scope

The 2012 exact endpoint-alternating model limits novelty to interior phases. The 2026 generalized piecewise-argument source provides the motivation and ambient class. Single-phase gain-independent sampling thresholds are related but insufficient to determine the two-step product. The model is linear, scalar, and nonimpulsive; broader networks and nonlinearities are unproved.

Self-review: passed. Independent audit: not yet performed.
