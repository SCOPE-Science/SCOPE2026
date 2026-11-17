---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

The positive-part Jensen gap identity gives Delta_n=-(sigma/(2 sqrt n)) (|V|-|sqrt(n)Y/sigma+W|)_+, with independent W,V~N(0,1/2). Polar integration of the Gaussian wedge gives sigma^2/(2 pi n) F(n tau^2/sigma^2), and the p*delta_0 Gaussian mixture averages the tau=0 and tau>0 cases. Taylor expansion gives n^-1 if p>0 and n^-3/2 if p=0, with stated constants. The single-term debiaser is integrable by telescoping and convexity. Cauchy–Schwarz on the level second-moment and cost sums proves necessity and a geometric q_l with 1<r<3/2 suffices at p=0. Independent Gaussian-wedge polar quadrature in four parameter cases confirmed the formula, but not the infinite asymptotics.

## originality

FAIL

FAIL: the earlier November 1, 2026 published full Gaussian positive-part antithetic correction law is algebraically identical to the entire p=0 finite-n second moment (with its total n_total=2*n here). In that result t=sigma^2/(2n), w=tau^2+t, theta=arctan(sqrt(t/w)); its second moment [(tau^2+2t)theta-sqrt(t(tau^2+t))]/(2pi) equals sigma^2 F(n tau^2/sigma^2)/(2 pi n). The p>0 mixture is the immediate linear combination of this formula and its continuous tau down-to-zero limit F(0), which yields all stated rates without a new Gaussian calculation. Standard one-term debiasing Cauchy–Schwarz plus those exponents gives the cost/variance frontier. The new claim is covered mathematically even though the older statement explicitly restricted tau>0 and did not phrase an atomic mixture.

## value

FAIL

FAIL: A decision-tie mass is a motivated stochastic boundary, but for this submitted exact Gaussian mixture it only linearly mixes a fully published exact finite-sample law with its elementary tau=0 endpoint. The remaining if-and-only-if criterion is a routine geometric-level summability/Cauchy–Schwarz consequence of those already-determined exponents. No independently unknown, nonmechanical invariant or structural lemma survives as submitted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
