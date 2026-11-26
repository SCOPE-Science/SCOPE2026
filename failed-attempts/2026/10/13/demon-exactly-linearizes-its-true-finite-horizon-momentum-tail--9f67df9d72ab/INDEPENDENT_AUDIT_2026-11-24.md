# Independent mathematical audit

## correctness

PASS

For the defined dimensionless velocity-state multiplier, splitting off its first factor gives E_t=β_t(1+E_{t+1}) and E_T=0. With C=T(1−b)+b, substituting the proposed next tail gives 1+E_{t+1}=(T−bt)/C; cancellation proves the formula down to t=0, including T=1. The proxy satisfies P_t=b(T−t)/[T(1−b)], so the constant ratio and the discrepancy normalized by P_t are correct for t<T; the ratio of two zero tails is not taken at t=T. In the source Algorithm 1, t runs through T inclusive and β_T=0, so omitting that zero-term product is correct. A gradient at t first enters v_{t+1}; its future dimensionless momentum multiplier is E_{t+1}, not E_t. In the source velocity convention its actual signed coefficient in accumulated future parameter increments is −ηE_{t+1} (the immediate gradient contributes −η); the coefficient in the finding is interpreted in its stated normalized-memory sense.

## originality

FAIL

No exact DEMON-labelled expression was found in the inspected optimizer texts, and the application is a useful reading of the source motivation. But the exact mathematical assertion is directly covered by Chu–Vandermonde on inserting the already-published DEMON coefficients. The remaining proxy and indexing claims are direct algebra of that same sum and the published recurrence.

## value

FAIL

Knowing that the true momentum-only tail preserves the intended shape can clarify the original heuristic. As a narrow research finding, however, the shape and scale are mechanically implied by the exact prior summation with the source schedule. No further nonroutine conclusion about the optimizer, a distinct weighting, or another motivated invariant survives; the explanation is useful as an expository observation, not a distinct research result under this standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
