# Independent mathematical audit

## correctness

PASS

On signed comparisons orient the complete graph with incidence B, so divergence is Bx. Summing swaps gives the operator ρI+2BᵀB/[n(n−1)], ρ=(n−5)/(n−1). The covariance of the centered comparison vector is (I+BᵀB)/12: diagonal variances 1/4, disjoint-edge covariances zero, and signed shared-vertex covariances ±1/12 from the six ranks of three entries. On gradients BᵀB=nI and on circulations it is zero. The cycle has squared edge norm n and no gradient; the ordinary path has divergence (1,0,…,−1), hence gradient squared norm 2/n and circulation squared norm n−1−2/n. Stationarity and powers of the operator give both lag formulas, including n=3,4 with a negative mode and lag zero. The jump is at most 4/√n after normalization. Squared swap increments depend only on ranks at touched endpoints and their neighbors, so a replaced underlying uniform affects at most 3(n−1) swap terms; Efron–Stein gives the stated O(1/n) variance for the conditional squared increment of the count. Its mean is 2n/[3(n−1)] by the eigenrelation. Summing conditional variances at floor(nt) and bounding absolute deviations in expectation via stationarity gives uniform bracket convergence to (2/3)t; subtracting the squared conditional drift has o(1) expectation. The martingale FCLT has deterministic covariance and vanishing jumps. Independence from the limiting initial value can also be obtained by applying it under bounded nonnegative tilts measurable at time zero; the same bracket and Lindeberg conditions persist under normalized tilts with positive limiting mass. The initial CLT is the bounded one-dependent CLT on adjacent uniform ranks, with only one bounded wrap-around term removed. The linear drift recursion yields the OU by the integral equation with drift −4, and the two paths differ uniformly by at most 1/(2√n), giving joint J₁ convergence. Periodicity of the permutation chain does not affect this stationary argument.

## originality

PASS

Credit the stationary path-space OU theorem and the process-level argument for this descent observable. Its static covariance, spectral ingredients and the resulting projected covariance calculation are not separate evidence of broad novelty. Known one-time and expectation results do not establish the claim at path level; the available full-text coverage is limited.

## value

PASS

A fixed-size deck with a non-Markovian descent-count projection nevertheless has a stationary Markov Gaussian limit. The theorem separates the macroscopically visible mode from a smaller endpoint effect and identifies both the time scale and noise. The dynamic bracket proof goes beyond a static Gaussian approximation or a direct eigenvalue lookup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
