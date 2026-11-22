---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Mathematical verification

The fixed-size Gaussian ensemble and mutant-versus-resident payoff formula are stated explicitly in `RESULT.md`. The theorem's critical analytic checks are: (i) conditioning on each resident's diagonal produces independent Gaussian invader fitnesses; (ii) the strict-mean derivative follows from Gaussian integration by parts; (iii) two resident ESS constraints form a shrinking interval in an independent Gaussian antisymmetric contrast, with width controlled by a \(\mathcal N(0,4)\) positive part; and (iv) three distinct resident ESS events require two independent pair contrasts in intervals of length \(O(\mu^{-1})\).

The analytic remainder is \(O_N(\mu^{-2})\), not a numerically guessed exponent. For each fixed \(N\), bounded derivatives of the Gaussian CDF and finite Gaussian moments justify expansion under expectation. Triple intersections admit a uniform \(O_N(\mu^{-2})\) bound. The exact zero-ratio binomial law follows from independent row maxima, not numerical extrapolation.

The included `check_pure_ess.py` was executed with Python, NumPy and SciPy. It completed 12 deterministic simulation/quadrature scenarios (\(N=2,3,4\) and \(\mu=0,2,10,40\)), checking the Gaussian-integral expectation against sampled ESS counts, the exact two-state bivariate-normal orthant probability, and the leading large-ratio coefficient. All programmed checks passed. Examples: for \(N=3\), \(\mu=40\), the observed zero/one/multiple frequencies were approximately \((0.25490,0.74086,0.00425)\) and the exact expected count was \(0.75014548\); for \(N=4\), \(\mu=40\), the observed frequencies were approximately \((0.49956,0.49824,0.00221)\) and the exact expected count was \(0.50029096\). Sampling confirms only finite-instance consistency, not an infinite proof or independent audit.

Limitations: no mixed-support ESS assertions, no uniform estimates as the number of strains increases, no claims beyond the iid Gaussian interaction law, and no inference about observed epidemiological persistence.
