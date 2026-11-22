# Scientific review

## Correctness: PASS

The generator normalization is \(\mathcal L=D\partial_{xx}+b\partial_x\), corresponding to noise amplitude \(\sqrt{2D}\). The raw second moment solves \(\mathcal Lm_2=-2\tau\), and the variance consequently solves \(\mathcal Lv=-2D(\tau')^2\); omitting the factor of \(D\) would invalidate the formula. Elimination gives \(DW=v'\). Positive integrating-factor representations establish strict positivity of both measured derivatives, and the inverse direction verifies both ODE boundary problems with the required regularity at reflection. The fourth-order wall coefficient and strictly monotone variance in the mean-degenerate example follow from explicit integrals. The 183-check standalone verification supplements these analytical steps, rather than serving as a proof for arbitrary functions.

## Originality: PASS, with residual risk

The 2026 arXiv source solves an inverse problem from a single **mean profile**, assuming constant diffusivity and reconstructing a potential on a half-line. The 2026 moment-identification article derives scalar ABM/GBM parameter estimates from two **scalar** moments at a fixed starting point. Bal–Chou (2004) treat a full exit-time distribution and fixed-start spectral inverse measurements; their citation of the classical exit-probability-plus-mean identification employs a different second observable and two possible exit boundaries. The complete realizability condition for **mean and variance spatial profiles** with two unknown functions, plus a strict continuum mean-ambiguity example, is not implied directly by those claims. Targeted mathematical-literature and claim-level database searches found no directly dominating statement. The elimination itself uses classical backward equations, and a previously published equivalent may exist implicitly in inverse diffusion literature; this priority uncertainty remains material, not a claim of certified novelty.

## Value: PASS

Inverse first-passage design is motivated by inference of stochastic transport landscapes. If both diffusivity and drift are unknown, first-passage *mean* observations alone are insufficient—even a smooth family of physically regular diffusions has identical complete mean profiles. The additional variance profile resolves the infinite-dimensional ambiguity and has a constructive, checkable compatibility criterion involving a strict cross-derivative inequality and endpoint regularity. This is a natural complete data-realization problem, rather than a narrowly selected numerical example; the explicit ambiguity family shows why the second observable is needed. The result is limited to exact functional data and makes no statistical robustness claim.

## Closest literature and scientific limits

See `RESULT.md` references for Keidar–Reuveni–Sokolov (2026), Xiang–Zhou–Xiang (2026), Bal–Chou (2004), and Cristofol–Roques (2017). The closest conceptual overlap is the standard inverse-generator principle that enough independent solutions of backward equations determine its coefficients. The precise first-passage **variance** equation, full-profile feasibility criterion, and mean-ambiguity witness distinguish the present claim. The major remaining risks are implicit classical coverage and instability of derivative-based recovery from finite/noisy measurements.

Self-review: passed. Independent audit: not yet performed.
