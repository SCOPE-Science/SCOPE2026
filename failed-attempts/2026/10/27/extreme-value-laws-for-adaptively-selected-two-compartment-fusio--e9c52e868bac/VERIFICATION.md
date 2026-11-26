---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A positive increment needs opposite signs, and their two largest magnitudes are attained at distinct compartments when both are positive. Thus the adaptive increment is min(M_+,M_−). The Skellam series follows by summing the Poisson difference probabilities, and independent compartments and disjoint positive/negative categories give the exact tail by inclusion–exclusion for every k≥1. The probability of A=k,B=0 and the upper tail of A give log p_k=−k log k+O_λ(k), so thresholds (1±ε)log C/log log C have Cp_k tending to infinity or zero respectively. For the expectation, the lower threshold gives the lower bound, and the Poisson mass ratio bounds the sum of upper tails past the upper threshold by a geometric series with first term tending to zero after multiplying by C. The centered Skellam mgf rescaled by sqrt(2λ) converges to the normal mgf, and the optimizer is continuous, which gives the stated fixed-C limit in law including its atom at zero. With standard normal norming, C(1−Φ(u_C+x/a_C))→exp(−x), and substituting this into the same inclusion–exclusion formula gives the displayed minimum-of-two-Gumbels CDF. The proof needs no uploaded computations; the reported finite checks were not independently replayed. Neither a joint limit nor growth at fixed total inventory is asserted.

## originality

FAIL

The adaptive wording was not found verbatim, but the frozen contribution is mechanically obtained by optimizing the prior pair-capacity identity on the prior iid Skellam model, then applying standard extrema in the two separately ordered regimes. In particular, the classical fixed-mean Poisson maximum scale transfers unchanged by constant-probability thinning. The review does not claim prior verbatim publication of the three formulas together.

## value

FAIL

The adaptive objective is natural and the formulas are useful as a worked application. The finite law, however, is an elementary consequence of the known capacity formula, and the asymptotics are routine transfers of Poisson and normal maxima. No nontrivial joint-loading transition, sharper discrete adaptive fluctuation law, or other independently useful unknown invariant is established in the frozen claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
