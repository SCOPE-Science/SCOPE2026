# Review status

Fresh independent audit outcome: **failed**.

- Correctness: **PASS** — The unit ideal in the coefficient embedding is Z^1024 and self-dual. At width 0.85 s_B, the 2048 norm-one dual vectors alone give tail at least 2048 exp(-(289/400)L), with L=ln(2048(1+2^128)); the exact interval calculation yields tail >=2^-90>2^-128. I independently recomputed the rational inequalities and 38-bit margin.
- Originality: **FAIL** — Published 2025 work on smoothing-parameter bounds gives the exact product relation eta_epsilon(Z^n)=eta_{(1+epsilon)^(1/n)-1}(Z) and a first-shell lower bound eta_delta(Z)>sqrt(ln(2/delta)/pi). Applied to n=1024 and epsilon=2^-128, this already supplies the integer-lattice obstruction underlying the claimed uniform constant-factor improvement failure. The record's 0.85 numerical specialization is therefore mechanically implied by stronger published Z^n smoothing results.
- Value: **FAIL** — The counterexample is correct, but after the stronger published integer-lattice smoothing relation and lower bound are taken into account, the 15% threshold is a direct numerical specialization of known theory rather than a new motivated boundary. Recomputing the same first-shell obstruction at N=1024 does not add sufficient mathematical value.
