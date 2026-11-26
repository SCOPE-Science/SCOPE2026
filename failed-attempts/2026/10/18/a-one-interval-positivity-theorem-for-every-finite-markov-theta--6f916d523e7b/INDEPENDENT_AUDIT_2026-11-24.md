# Independent mathematical audit

## correctness

PASS

The exponential-time representation of R gives entrywise nonnegativity, and M=(R−(1−θ)I)/θ reduces the positivity test to its diagonal for θ>0. Discounted occupation before departure and after the first return gives R_ii(s)=[1+r_i E{s(1−exp(−T_i/s))}]⁻¹, retaining T_i=∞ rather than conditioning on return. The integrand increases strictly to T_i for both finite positive times and ∞, and is bounded by s near zero. Monotone convergence therefore gives the specified limit, including zero for a transient state; renewal reward gives the stationary mass in each closed class. Absorbing diagonals are constant one. This proves the exact crossing criterion with equality included; θ=0 is the Euler diagonal test and θ=1 is a nonnegative resolvent. Reversal preserves the diagonal and the Euler exit rates. The recorded rational tests are finite corroboration only; the frozen script was inspected, not executed.

## originality

FAIL

The 2026-10-12 Resultary stationary-mass positivity frontier already gives the full arbitrary-θ classification for irreducible generators, including nonreversible ones, using the same return formula and monotonicity. The remaining universal interval and exact roots follow mechanically by continuity and analyticity from that result; recurrence endpoints are the classical finite-chain limits, and reversal is diagonal conjugacy and transposition. This is stronger coverage than the reversible prior identified in the frozen record.

## value

FAIL

The sharp horizon has genuine use for Markov time stepping, but the structurally significant nonreversible no-reentry theorem is already covered. In the frozen extension, the new cases require only extending the same return-time argument to a defective return distribution, or a continuity argument followed by classical finite-chain limiting probabilities. The reversal observation is immediate diagonal similarity and transposition. No independently substantive surviving contribution was established.

The dated certificate retains the supplied scientific assessment, sources and limitations.
