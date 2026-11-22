# Mathematical review

## Correctness — PASS
The piecewise-bridge conditional expectation, independent Gaussian quadratic-form variance identity, and direct double-integral value \(\operatorname{Var}(Q)=1/45\) prove the risk formula. The two-variable domain is exhausted analytically by the convex-in-center-shift regime and the strictly decreasing-in-separation regime. The unique radical optimizer, exact minimum and equality cases follow without relying on finite sampling. `verify.py` reproducibly checks the algebra and 325 exact-rational instances; 5151 finite-grid tests are supplementary, not a proof.

## Originality — PASS, with publication-priority caveats
Foster–Lyons–Oberhauser, arXiv:1904.06998v1 (2019-04-15), treat quadratic Wiener-path integrals conditioned on an endpoint and a time-integral observable, not optimized point observations of the pinned bridge. The full published result on iid two-node Brownian-bridge kernel quadrature instead estimates a linear integral and optimizes a sampling probability distribution. The Purdue path-design dissertation abstract concerns integrated error for linear path reconstruction. Tang–Xiao (2018/2019) address KL-based approximation, but a full-text comparison was unavailable. Search and source inspections do not establish absolute historical priority, and a hidden equivalent older optimum remains possible.

## Value — PASS
The Cramér–von Mises-type quadratic energy is not a linear quadrature target. Determining where exactly two noiseless samples should be taken to minimize the irreducible mean-square error of its best nonlinear predictor is a natural finite information-design question. The answer supplies the complete optimal site pair and sharp risk, excluding endpoints and replication, and distinguishes the nonlinear target from the standard linear-integral trisection design. It does not imply a general numerical SDE method or computational speedup.

## Limitations
Only fixed two-point, noise-free, Gaussian pinned-bridge energy estimation is solved. Adaptive/noisy settings and historical equivalence remain outside the claim. Formal independent mathematical and publication-priority validation have not been performed.

Self-review: passed. Independent audit: not yet performed.
