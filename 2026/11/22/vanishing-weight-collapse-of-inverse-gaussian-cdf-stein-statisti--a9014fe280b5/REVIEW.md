# Mathematical review — vanishing-weight IG CDF–Stein boundary

## Correctness (C): PASS
The source's exact CDF–Stein expression has a deterministic plateau at every threshold beyond the sample maximum. ML cancels that plateau identically, while MO leaves the explicit normalized moment mismatch. An exact four-function tail decomposition in unweighted Hilbert space, whose four squared basis norms are \(x\), \(x^3/3\), \(x/3\), and \(1/(3x)\), controls the residual uniformly over all deterministic vanishing tuning rates. The IG influence-function calculation gives precisely \(6\phi^{-3}\), hence the null limiting coefficient \(3/(2\phi)\). A checker independently reconstructs the identities and passes 50 finite exact, symbolic and numerical assertions; numerical checks are not treated as proof of the limit.

## Originality (O): PASS, qualified
The 2019 preprint and 2022 open-access journal text were read at the definitions, estimators, fixed-weight null theory, computational forms, experiments and conclusions. They cover fixed positive tuning, not the arbitrary simultaneous \(a_n\downarrow0\) regime. The 2024 generalized Stein-moment estimation study concerns estimators rather than this goodness-of-fit functional. Prior accessible mathematical claims include a separate large-tuning ML result and a Rayleigh analogue, but neither implies the small-tuning moment-likelihood separation. The finite-sample tail identity itself is an elementary consequence of a known statistic; it is not asserted to be independently new. Searches cannot certify historical uniqueness; a dispersed prior theorem remains a genuine risk.

## Value (V): PASS
For a source that recommends MO implementation and finds relative tuning insensitivity on \(\(a=0.1,1,10\)\), identifying an entire unweighted boundary and exact nonstandard null calibration explains where that empirical picture ceases to describe the statistic's scale. The MO family becomes effectively one-dimensional in the vanishing-weight regime while ML loses that component, and the sharp coefficient is needed for normalization. The result concerns statistics, not the size or power of the separately bootstrap-calibrated procedure.

## Closest literature and limits
Allison et al., arXiv:1910.14119 (2019) and Mathematics 10 (2022), 350; Nik and Weiß, Journal of Statistical Theory and Applications 23 (2024), 240–274. The proof assumes i.i.d. fixed-parameter IG observations and deterministic \(a_n>0\) tending to zero. No claim is made for data-driven tuning, drifting parameters, alternatives or bootstrap rejection probabilities. Historical priority is qualified and not independently established.

Self-review: passed. Independent audit: not yet performed.
