# Independent mathematical audit — SCOPE-20260912-010

Outcome: **FAILED**.

## Correctness

**PASS** — The unit ideal in the coefficient embedding is Z^1024 and self-dual. At width 0.85 s_B, the 2048 norm-one dual vectors alone give tail at least 2048 exp(-(289/400)L), with L=ln(2048(1+2^128)); the exact interval calculation yields tail >=2^-90>2^-128. I independently recomputed the rational inequalities and 38-bit margin.

## Originality

**FAIL** — Published 2025 work on smoothing-parameter bounds gives the exact product relation eta_epsilon(Z^n)=eta_{(1+epsilon)^(1/n)-1}(Z) and a first-shell lower bound eta_delta(Z)>sqrt(ln(2/delta)/pi). Applied to n=1024 and epsilon=2^-128, this already supplies the integer-lattice obstruction underlying the claimed uniform constant-factor improvement failure. The record's 0.85 numerical specialization is therefore mechanically implied by stronger published Z^n smoothing results.

Equivalent formulations: The claimed counterexample is exactly a lower bound on eta_epsilon(Z^1024) from the norm-one shell, compared with a generic shortest-vector smoothing upper bound.

Broader coverage: Guo et al. 2025 give a stronger general Z^n smoothing relation plus lower bound that implies this fixed 1024-dimensional specialization.

Database/table comparison: Not a table claim; decisive coverage is theorem-level via the published Z and Z^n smoothing formulas.

Claim-vs-prior implication: Published 2025 work on smoothing-parameter bounds gives the exact product relation eta_epsilon(Z^n)=eta_{(1+epsilon)^(1/n)-1}(Z) and a first-shell lower bound eta_delta(Z)>sqrt(ln(2/delta)/pi). Applied to n=1024 and epsilon=2^-128, this already supplies the integer-lattice obstruction underlying the claimed uniform constant-factor improvement failure. The record's 0.85 numerical specialization is therefore mechanically implied by stronger published Z^n smoothing results.

## Value

**FAIL** — The counterexample is correct, but after the stronger published integer-lattice smoothing relation and lower bound are taken into account, the 15% threshold is a direct numerical specialization of known theory rather than a new motivated boundary. Recomputing the same first-shell obstruction at N=1024 does not add sufficient mathematical value.

## Source inspections

- **Guo et al., New bounds of the smoothing parameter for lattices, PLOS One 20 (2025), DOI 10.1371/journal.pone.0328688** — Material read: full open-access HTML, especially Lemma 7, Corollary 12 and Section 3.2. Finding: gives the Z first-shell lower bound and exact reduction of eta_epsilon(Z^n) to eta_epsilon'(Z), which mechanically yields the obstruction used here.
- **Chung-Dadush-Liu-Peikert, On the Lattice Smoothing Parameter Problem, arXiv:1412.7979** — Material read: abstract/full-text landing page. Finding: establishes smoothing-parameter context and near-tight discrete-Gaussian characterizations, but the 2025 Z^n result is the decisive coverage.
- **Zheng-Liu-Lu-Tian, Cyclic Lattices, Ideal Lattices and Bounds for the Smoothing Parameter, arXiv:2112.13185** — Material read: abstract/full-text landing page. Finding: confirms ideal lattices as cyclic integer lattices and develops smoothing bounds; not needed for decisive coverage.

## Residual risks

- The coefficient/canonical embedding normalization must be scaled consistently; the first-shell obstruction is invariant under the corresponding common scale.
- Scientific rejection is for prior coverage/value, not correctness.
