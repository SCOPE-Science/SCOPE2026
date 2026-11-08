# Scientific review

## Correctness — PASS

The fixed-data problem is reduced exactly to two coordinates. Haar projector idempotence and conditional spherical invariance give independent \(\operatorname{Beta}(a,b)\) and \(\operatorname{Beta}(\delta,\delta(n-2))\) variables. A separate gamma-sum split proves the independent contraction, including the degenerate \(\ell=1\) case; ordinary Gaussian conditioning proves the beta-prime reference. Gamma integration and the positive beta-prime density establish all quantifiers, moments and tail constants. Direct independent Haar-QR and Gaussian simulations in `verify.py` passed 610 diagnostics, which are not substituted for proof.

## Originality — PASS (qualified)

Epperly and Webber, arXiv:2605.19096, Theorem 2.1 and Sections 5.3–5.5, derive expected-error formulas and minimax mean-square optimality. They do not state a joint independent-beta contraction or the resulting full stochastic order, critical-moment spectrum and exact heavy-tail coefficient. Ahfock et al. (2020) and Browne–Andrews (2023/2024) establish the Gaussian sketch marginal distribution; that contribution is credited and not reclaimed. Eaton–Muirhead's Haar conditional sphere decomposition and scalar beta–gamma algebra are also standard ingredients. No directly covering theorem was identified in searched published-record abstracts, full primary sections or accessible related claims. A historically unindexed equivalent scalar-Haar formula remains possible; full historical priority is not certified.

## Value — PASS

An expected-squared-residual bound does not imply quantile or higher-moment dominance. The independent coupling proves simultaneous improvement for every nondecreasing error criterion for which expectations exist, yet it shows precisely when higher-order reliability diagnostics diverge: e.g. finite mean and infinite variance of excess squared residual for real sketch dimensions three and four. Tail constants quantify the improvement left after heavy-tail exponents remain unchanged. This is a useful finite-dimensional benchmark for randomized least-squares solver reliability, even without a general-rank extension.

## Boundaries and residual risks

The theorem is for deterministic fixed inconsistent scalar regression and exact real/complex Haar or Gaussian sketches, not arbitrary embeddings, covariate rank or floating-point implementations. Inaccessible or unindexed distributional work could affect priority. No independent external mathematical validation has occurred.

Self-review: passed. Independent audit: not yet performed.
