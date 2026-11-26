---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Conditioning on the independent two-sided switching history gives a centered Gaussian with variance V in [H,L], H=D/b and L=D/a. A stiff interval of length tau forces the entrance gap Z=L-V of the next soft interval into [(L-H)(1-exp(-2b tau)), L-H], bounded away from zero. At soft age A the gap is Z exp(-2a A); renewing whole cycles, the unconditional probability of soft phase and age greater than t is integral_t^infty Pr(W>u) du/(mu+tau). Squeezing between the two deterministic entrance gaps gives Pr((L-V)/L<y, soft) asymptotic to K[log(1/y)/(2a)]^(1-beta), with K=c/((mu+tau)(beta-1)). A stationary stiff interval has deterministic length, so the preceding soft duration there is not length biased; small gap requires a preceding duration of order at least log(1/y)/(2a), giving only O(log(1/y)^(-beta)). To pass from this variance edge to the density, write Y=(L-V)/L and q=x^2/(2L). The density ratio is the expectation of (1-Y)^(-1/2) exp(-qY/(1-Y)). For fixed 0<eta<1 the contribution below Y=q^(-1-eta) gives a lower bound (1-o(1))Pr(Y<q^(-1-eta)); the upper bound is (1+o(1))Pr(Y<q^(-1+eta))+O(exp(-q^eta)), using V>=H. Divide by Pr(Y<1/q) and let eta decrease to zero. Thus the ratio is asymptotic to K[log q/(2a)]^(1-beta); the factor of two cancels when changing from q to displacement. This checks the unconditional density and full constant without imposing a density on W. VERIFICATION.md and CHECK.py were inspected, not executed; the two Pareto quadrature examples are diagnostics, not a proof or an attestation.

## originality

PASS

The model and Gaussian-mixture method have direct antecedents, and the inverse-logarithmic renewal-age mechanism occurs in a related indexed work. The distinct result supported by the checked sources is the normalized Gaussian-tail attenuation, with constant, for the Brownian particle with two positive stiffnesses and the specified heavy-tailed soft clock.

## value

PASS

The exact density equivalent distinguishes a truly Gaussian equilibrium from a stationary law with the same quadratic decay rate but a vanishing Gaussian density ratio. It identifies how a heavy residence-time law remains visible despite uniform confinement, including the exponent and normalization and the contrast with a released trap. The analysis uses a physically meaningful endpoint of the conditional variance distribution, not just a recomputation of Gaussian decay.

The dated certificate retains the supplied scientific assessment, sources and limitations.
