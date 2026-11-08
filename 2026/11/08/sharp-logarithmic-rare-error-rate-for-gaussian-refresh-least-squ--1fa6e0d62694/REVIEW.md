# Review of sharp logarithmic rare-error rate

## Correctness

**PASS, self-review.** The stationary-series construction is valid because the Gaussian update coefficient has negative mean log magnitude for each fixed \(0<a<2/3\). The backward Gaussian-refresh process decomposes into iid geometric runs. The logarithmic block-increment tail rate is \(-\log\rho\), with matching upper/lower estimates from Gaussian marks and long geometric runs. The product maximum is controlled by a negative-drift random walk and Veraverbeke's theorem, applied to an explicitly dominating subexponential law. A square-integrable discounted additive envelope controls the remaining SGD noise; one long Gaussian-mark run with Gaussian anti-cancellation proves the matching stationary error lower bound. All quantifiers concern fixed \(a,\rho,\sigma\) and \(x\to\infty\). Standalone finite checks: `python3 verify.py`.

## Originality

**PASS, qualified.** Li--Wu (arXiv:2610.05599v1), Section 3 and Appendix G, supply the same refresh design, moment-divergence theorem, and a non-sharp one-sided lower tail. The sharp two-sided logarithmic coefficient is not given there. Zachary (arXiv:1410.8551) proves the general random-walk maximum theorem used in the proof, but a nontrivial SGD product reduction and matching conditional-Gaussian lower bound are still required. Li--Lei--Wei--Wu (arXiv:2610.23750v1) instead assume regularly varying, infinite-variance innovations; this theorem has Gaussian innovations and persistent multiplicative dependence. Targeted comparisons of published mathematical claims did not uncover a directly covering result; an equivalent unindexed regenerative perpetuity specialization remains a concrete historical-priority risk.

## Value

**PASS.** The exact coefficient provides a sharp reliability scale for stationary stochastic optimization with temporally persistent Gaussian designs, where Gaussian central approximations coexist with infinite stationary moments. It separates the leading effects of persistence from the fixed stepsize and noise scale. This is a meaningful missing numerical-optimization error diagnostic, rather than a routine restatement of the moment-divergence theorem.

## Limits and sources

The claim is scalar, stationary, fixed-stepsize, and Gaussian; it does not address finite horizons, independent covariates, or matching multiplicative prefactors. The principal source is arXiv:2610.05599v1; the random-walk ingredient is arXiv:1410.8551; the distinct contemporary innovation-tail comparison is arXiv:2610.23750v1. Independent review is not claimed.

Self-review: passed. Independent audit: not yet performed.
