# Scientific review

## Correctness — PASS
The exact \(J_s\) convolution yields a nonnegative-square expansion; prime-power factors of \(f_{r,s}*\mu\) give the uniform mean and the positive Euler factor \(C_sR_s(r)\). Weighted partial summation, quotient-block truncation and explicit balancing prove the stated \(\theta_s\) in each range. A second application of the positive mean gives \(A_{q,s}\ge0\); absolute convergence and the \(q=1\) term give \(c_s>0\). The large-\(s\) formula follows from uniform geometric tail bounds. `verify.py` checks \(105\) exact-rational finite cases and \(12\) additional numerical comparisons, without substituting finite computation for an infinite proof.

## Originality — PASS, qualified
Azimifard's arXiv:2611.00525v1 proves \(s=2\) only; here the genuinely variable real power changes the normalization, local factors and error regimes. Aistleitner--Berkes--Seip--Weber, arXiv:1407.5403v2, prove eigenvalue results for a differently normalized kernel; Ehm, arXiv:2405.06349v2, treats Nyman--Beurling Gram kernels. A related indexed theorem concerns unimodular completely multiplicative coefficients, which exclude the Möbius function. No covering real-power Möbius theorem appeared in the recorded targeted searches. An unindexed equivalent remains possible.

## Value — PASS
The power-GCD kernel parameter is intrinsic, and the theorem gives the whole noncritical range \(s>1\) with a positive computable constant, power-saving rate, changed scaling exponent, and high-power limit. This is a structural interpolation of arithmetic quadratic forms rather than an isolated extra case or numerical table; it does not assert sharpness of the error rates.

## Limits and relationship
No theorem at \(s\le1\), no uniform near-endpoint error, no proof of optimality of \(\theta_s\). The known \(s=2\) theorem and Jordan identity are credited rather than claimed as new. An undiscovered general parameter theorem would overturn originality.

Self-review: passed. Independent audit: not yet performed.
