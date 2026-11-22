# Scientific review

## Correctness — PASS

The stated Gaussian mean-square risk is the exact Schur complement, and optimizing freely distributed independent measurement precision gives the squared-total-variation penalty by Cauchy–Schwarz. The positive Markov interpolation coefficients and inverse-positivity of the exponential kernel precision matrix establish positive optimal weights. The endpoint variation and strict point-splitting argument exclude boundary or unused sensors. At the remaining interior optimum the residual-potential ODE and derivative jumps enforce uniform quadrature weights, interior spacing and symmetric margins. The scalar design equation has a unique root for every permitted parameter. The explicit risk and budget transition follow. A separate standalone program reproduced 656 formula/design assertions and 4,788 numerical competitor comparisons; finite checks are not a continuous-space proof.

## Originality — PASS, qualified

The inspected published noiseless exponential-kernel theorem identifies symmetric margins and equal interior gaps under exact observations, which is not the present finite-noise resource-allocation problem. Pronzato–Zhigljavsky (2018) provide Gaussian kernel-energy foundations; Karvonen–Kanagawa–Särkkä (2018) address quadrature weight positivity; Cai–Lam–Scarlett (2022) address noisy convergence rates, without this joint all-sensor-count optimum. A previously recorded two-sensor exponential-kernel noisy design is covered as a special case and is not claimed as new. The related Brownian and Brownian-bridge all-n precision-budget theorems concern different covariances and boundary behavior. No accessible source inspected directly established this theorem or implied its budget threshold. Historical priority remains conditional on older unavailable integral-design material.

## Value — PASS

Freely dividing a finite sensor-precision budget while choosing all measurement locations is a natural design objective, not an arbitrary low-dimensional slice. The classification identifies a unique globally optimal rule for every finite sensor count, demonstrates that every extra sensor is strictly useful, and finds an exact budget at which all gaps become uniform independently of kernel length scale. This is a structural completion beyond the familiar noiseless and two-sensor cases.

## Closest literature and limitations

Primary references: Pronzato–Zhigljavsky, arXiv:1808.10722v1; Karvonen–Kanagawa–Särkkä, arXiv:1812.08509v1; Cai–Lam–Scarlett, arXiv:2202.10615v1; the published noiseless exponential-kernel design theorem at https://github.com/published-finding corpus/2026/tree/main/2026/11/8/SCOPE-exact-optimal-nodes-and-stratification-penalty-for-ornstein-uhle--971795799fba. The 2003 Mukherjee integral-estimation article and related older dissertation could be examined only at abstract level, leaving a specific residual priority risk. The theorem assumes known stationary exponential covariance and continuously divisible independent Gaussian measurement precision. It does not address adaptive sampling, unknown parameters, integer replicate costs or other kernels.

Self-review: passed. Independent audit: not yet performed.
