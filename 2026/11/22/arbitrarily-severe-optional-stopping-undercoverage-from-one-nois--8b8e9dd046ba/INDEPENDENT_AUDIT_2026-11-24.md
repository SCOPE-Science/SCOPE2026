# Independent mathematical audit

## correctness

PASS

The normalized vector c is the first row of the symmetric Householder reflection taking e₁ to c. A has eigenvalues q^(−2i)>0, and ωB has eigenvalues t_i=q^(−4(i−1))/2 in (0,1/2]. For x†=Bw, ||w||≤1, the bias bound is the maximum of 2q^(−4)t(1−t)^k over [0,1/2], bounded by the stated b_k for each positive k. The Gaussian quantile plus this absolute bias bound gives the marginal guarantee over the whole source class. Solving the modal recursion, at the null the coefficient of ξ_i=(Vᵀε)_i in iterate k_j is q^i[1−(1−t_i)^{k_j}]/C_q. Because k_j t_j=1, its diagonal filter is at least 1−e^(−1); older modes relative to this coefficient are bounded by q^(−(j−i))/(1−e^(−1)), and later ones by q^(−3(i−j))/(1−e^(−1)) using 1−(1−t)^k≤kt. Each standardized row thus tends to e_j and b_{k_j}/sd_{k_j}→0. Coupling all q with the same standard normal vector gives convergence of the interval intersection indicator off null-probability boundaries. The selected interval covers zero exactly when all candidates cover zero, including the fallback; hence for fixed r coverage tends to (1−α)^r and for each positive target one can first choose r and then finite q to go below it. One observation means one r-dimensional noisy vector; different iterations need not be independent at finite q. Read VERIFICATION.md and check_landweber.py as text; the Monte Carlo is diagnostic, not the proof.

## originality

PASS

Neither marginal intervals nor the danger of selecting among them is new. The warranted distinction is an explicit family of Landweber operators and deterministic times that makes standardized noise at a single common coordinate from a common observation asymptotically independent while retaining fixed-index source-class guarantees. The examined spectral and coverage results do not supply that construction or imply the limit under the stated reuse and coordinate restrictions.

## value

PASS

Quantifies the extent to which exact fixed-index uncertainty quantification can fail under first exclusion even without changing the coordinate or collecting new data. The useful mathematical witness is that ordered, increasingly saturated Landweber spectral filters can behave like independent standardized tests when viewed on widely spaced time scales. The example deliberately varies dimension and conditioning; it does not impugn observation-independent stopping or every adaptive rule.

The dated certificate retains the supplied scientific assessment, sources and limitations.
