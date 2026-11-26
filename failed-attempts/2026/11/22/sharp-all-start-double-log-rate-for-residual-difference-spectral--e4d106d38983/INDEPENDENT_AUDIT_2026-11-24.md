# Independent mathematical audit

## correctness

PASS

By consistency the residual lies in range(A), where B=AA^T has two positive levels. Normalize them to kappa and 1, leaving alpha B unchanged, and let e_k be the high-to-low spectral energy ratio. The first Rayleigh step inverts e_0. Substituting the residual difference into the RD quotient gives (1+kappa² e_(k−1))/(1+kappa³ e_(k−1)) in normalized units. For mixed data both filters remain nonzero. With z_k=log(kappa²e_k), their squared ratio gives z_(k+1)=z_k−2z_(k−1) and z_0+z_1=4 log(kappa)>0. The roots are sqrt(2) times unit rotations by ±theta, with π/3<theta<π/2. Four successive phase samples have all circular gaps below π, so compactness supplies a uniform positive and negative cosine excursion, bounded away from zero, in each such block. The high- and low-mode negative log multipliers are respectively [z_(k−1)]_+ and [−z_(k−1)]_+ up to bounded errors. Summing the last four excursions bounds each negative log mode norm from below by a positive constant times 2^(k/2) and summing the geometric majorant bounds it above at that scale; O(k) errors are negligible. The fixed first-step log corrections can depend on the start, so the bound on the remainder can be written O_kappa(k)+O_kappa,e0(1). Orthogonality transfers the result, with start-dependent constants, to the residual norm. A zero residual is already solved, and either pure mode is annihilated in the first step. This is not a consecutive-step Q-rate.

## originality

FAIL

The exact claim, including the two-sided rate scale and absence of exceptions, is mathematically covered by distinct assigned record 4 with the identical residual step, same first step, same spectral levels, and same quantifiers. Its strictly positive continuous phase profile yields the two-sided norm estimate and its nonzero multipliers the never-terminate assertion. This is demonstrable coverage in the frozen set, not an inference about which same-day record preceded the other or a finding that Xu previously stated the exact law.

## value

FAIL

The exact-arithmetic rate for pure RD under a natural warm start is a meaningful mathematical question. As a separate frozen finding, however, this is exactly a short consequence of the stronger record 4 for the same starts, with no extra invariant, regime, or estimate needed by a future user. Its elementary four-phase excursion argument is useful as alternative exposition, not a distinct new scientific result under the value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
