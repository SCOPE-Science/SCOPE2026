---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

PASS: In stationary common Poisson resetting, the last reset age T~Exp(r) gives conditional variance theta(1-e^{-2muT}), so Q_N/theta=V*(chi2_N/N) with V~Beta(1,b), b=r/(2mu). The exact survival integral over w=1-V with density b*w^(b-1) yields, under w=s/sqrt N and chi-square CLT with exponential Chernoff domination, the edge N^{-b/2} Gaussian-tail integral and threshold gamma constant. For fixed t>1 the gamma survival equivalent exp[-NI(t)]/((t-1)sqrt(pi N)) combined with endpoint rate derivative (t-1)/2 yields 2^b*Gamma(b+1)/(sqrt(pi)(t-1)^(b+1))*N^{-b-1/2} exp[-NI(t)]. Independently numerically evaluated the exact mixture with scipy gammaincc at N=100..1600, b=0.5,1,2 and fixed supercritical t=1.4: ratios approach both stated prefactors. These finite calculations corroborate rather than prove asymptotic uniformity.

## originality

PASS

PASS best-of-knowledge: De Mauro–Majumdar–Schehr supplies the exact common-reset Gaussian mixture and Biroli et al generic conditional-iid bulk sum law. Neither inspected primary section gives the sharp critical N^{-1/2} crossover or exact reset-dependent supercritical energy prefactor. Related published SCOPE results concern macroscopic beta energy and maximum-extreme fluctuations; these differ from finite-N sum-square tails.

## value

PASS

PASS: The explicit crossover law and sharp rate/prefactor separate reset-rate-independent chi-square large-deviation action from reset-rate-dependent polynomial finite-N energy fluctuations. These are natural observable-specific tail invariants, beyond an elementary restatement of the known beta mixture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
