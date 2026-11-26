---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For a single recoloring a→b the change in energy is J(N_a−N_b); at a degree-three vertex strict stability is equivalent to N_a≥2. On a mixed rung this forces both respective row neighbors to agree, propagating the same ordered pair around the cycle. Otherwise the monochromatic rungs form a cyclic word without singleton runs. In the latter case the r run boundaries are nonadjacent edges and there are (n/r) binom(n−r−1,r−1) placements for r≥2; the run-color factor is (q−1)^r+(q−1)(−1)^r, including the two-run case. The cyclic matching recurrence gives the two Lucas terms, and the exceptional q(q−1) states have H/J=n and W=0. At u=1 the dominant root λ is separated in modulus from λ−1, roots of modulus 1 and the constant term. Analytic continuation gives a uniform exponential error near u=1. If λ(t)(λ(t)−1)=(q−1)e^t, then (log λ)'=(λ−1)/(2λ−1) and (log λ)''=λ(λ−1)/(2λ−1)^3. The expansion at t/√n establishes the fixed-q CLT; the exceptional states have exponentially small probability, so the energy limits follow. This covers the n=3 simple cycle, labeled states, and strictly positive recoloring cost, not neutral moves or dynamical sampling. Inspected RESULT.md, VERIFICATION.md and verify_potts_ladder.py; the finite census (2,123,582 configurations) and transfer checks are source-reported, not rerun or used to prove generality.

## originality

FAIL

A distinct Resultary record gives the same classification, unweighted count, and exact count refined by the number of runs. A nonconstant monochromatic-rung word with r runs has exactly W=r and H/J=2r. The refined polynomial is a direct relabeling of the prior coefficients, including the known exceptional and consensus counts. The prior generating-function proof also yields the marked roots by the single substitution w(z)→u w(z). Its isolated dominant quadratic root yields the quoted LLN, entropy, and Gaussian constants by routine analytic moment expansion; the asymptotes are not claimed to have been explicitly printed in the earlier record. The overlap is mathematical and does not depend on a publication-priority inference.

## value

FAIL

Strict stability and energy statistics are natural observables, but the only additions beyond the known useful ladder classification and run census are an exact change of weight and the standard quadratic dominant-root moment expansion. No independently useful nonmechanical result remains to repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
