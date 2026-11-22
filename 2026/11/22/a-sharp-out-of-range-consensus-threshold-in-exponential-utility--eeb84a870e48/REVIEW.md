# Scientific review

## Correctness — PASS

The two-agent normalized simultaneous update directly yields the signed-gap multiplier \(1-2\mu\) and the nonnegative mean drift \(\mu d_t\tanh(\kappa d_t/2)\). Summation proves the limit. For \(\mu>1/2\), all terms in the threshold series are increasing in \(r=2\mu-1\), and its sum tends to infinity as \(r\uparrow1\). The crossing therefore exists once and only once. Bounds on \(\tanh\) give the weak-bias asymptotic, and the tail beyond the zeroth summand gives the strong-bias asymptotic. Monotone Riemann-sum comparison proves the high-rate coefficient. Direct-update and series computations matched in 50 cases. No finite experiment is treated as proof.

## Originality — PASS (qualified by incomplete historical coverage)

The 2026 source states the utility-weighted update and disagreement contraction but does not derive the deterministic two-agent sharp out-of-initial-range threshold for exponential utility or the inverse-learning-gap divergence. A closely related indexed result, *The finite-population Gibbs exponent for noisy utility-weighted opinion averaging*, handles the stochastic finite-population weak-noise Gibbs exponent instead, not this singular deterministic consensus boundary. Other inspected records concerned confirmation bias, stochastic influence or delayed consensus. No inspected statement implies the combined threshold and asymptotic claim; this is not a proof of worldwide historical priority. Unread or inaccessible closely related literature remains a residual risk.

## Value — PASS

The exact boundary identifies when a natural utility-weighted compromise mechanism ceases to preserve the initial opinion interval even though its disagreement strictly contracts. The singular amplification at near-unit learning rate exposes a concrete interpretability problem for the high-response regime. It resolves an exact parameter-range question intrinsic to the original model rather than an arbitrarily chosen numerical slice.

## Scope and limitations

Only two agents, strictly positive exponential utility, noiseless simultaneous updates, an always-active confidence link and real-valued unprojected opinions are covered. Higher-population networks, noisy dynamics and clipped bounded opinion scales are not proved. The nearest original source was inspected in its mathematical development; historical-priority review beyond checked sources remains open.

Self-review: passed. Independent audit: not yet performed.
