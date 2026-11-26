# Independent mathematical audit

## correctness

PASS

Each nonfixed update decreases the integer sum, so T_n is at most 2n and a fixed state is absorbing. The cited one-site densities give the exact drop (t+15)/(81·3^t); a cone with 2t+3 distinct sites transfers this drop to the ring, giving the claimed Markov bound for T_n>t. The two zero endpoints of 0·2^a·1^b·0 are permanent. For a−1 updates the two descending boundaries move together, and for b−1 more updates the ones erode, forcing a change into time a+b−2. There are t−1 splits. At n≥2(t+4), interior overlaps are incompatible, only the two shared-endpoint offsets can add covariance, and disjoint windows are independent. This gives Var Z≤EZ+2n(t−1)^2·3^(−2(t+4)+1) and the stated lower tail. The two tails at the logarithmic center are geometric; above the valid cone range use the deterministic horizon, and below half log_3 n use monotonicity. Summing gives bounded absolute mean deviation, not just tightness. Independent bounded replay: checks/replay_certificates.py (fixation); finite checks supplement the literature input and analytic proof.

## originality

PASS

The inspected prior work provides the lifted rule and its one-site degeneration, not the finite-ring maximum or a lower tail sufficient to prove the clock. The closest exact indexed result is the identical record; the nearby distinct extreme-value records concern genuinely different dynamics and stopping times.

## value

PASS

For a previously studied natural local rule, the global relaxation clock is a different and useful observable. The exact dependence mechanism in protected two-run words yields the matching lower tail and a genuine diverging second-order correction to log_3 n. The bounded mean error is not inferred solely from a density curve or a numerical fit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
