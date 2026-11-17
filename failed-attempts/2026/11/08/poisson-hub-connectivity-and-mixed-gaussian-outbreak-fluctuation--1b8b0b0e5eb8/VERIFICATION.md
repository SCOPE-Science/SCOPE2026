---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

PASS: For fixed r and activities, exact singleton incidence probabilities a_i/sqrt(n)+O(n^-1), pair incidence probabilities a_i a_j/n+O(n^-3/2), and total probability of degree >=3 O(n^-1/2) give joint independent Gaussian singleton fluctuations and independent Poisson bridges by a multinomial triangular-array MGF. The hub component is a measurable function of the bridge counts, and the O_P(1) pair contribution to ordinary component size vanishes after n^1/4 scaling. Rare-cell Poisson coupling plus triple-event probability establishes O(n^-1/2) projected-graph TV. Rebuilt a three-hub finite incidence calculation conceptually and inspected verify.py; these regressions do not prove the limit.

## originality

FAIL

FAIL: The fully inspected published finite-core Fortuin-Kasteleyn theorem covers this exact claim at cluster weight q=1, arbitrary heterogeneous a_i and fixed r, including the same n^1/4 mixed Gaussian limit and independent effective pair graph. Its product-tilting proof explicitly supplies the same rare-cell derivation. The added routine rate bound from rare-cell coupling does not create a distinct original theorem. Both records are dated November 8, 2026, and within-day precedence is not claimed; implication coverage is decisive.

## value

FAIL

FAIL: This is a correct and naturally motivated outbreak statement, but its central joint law, heterogeneity and two scales are a q=1 specialization of an already published strictly broader theorem. The elementary O(n^-1/2) TV inequality follows from standard Poisson rare-cell estimates and is not a sufficiently motivated independent advance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
