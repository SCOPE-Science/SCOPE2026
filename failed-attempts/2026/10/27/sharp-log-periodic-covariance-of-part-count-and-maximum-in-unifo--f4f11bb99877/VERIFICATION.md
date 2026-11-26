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

The fair-cut representation gives n=N−1 and (K,M)=(1+S,1+R). For k zero-run starts, compressing out the kr prescribed zeros gives the two binomial counts, with p^k or p^(k−1) according as the first start is interior or at the boundary. The Bernoulli score identity gives −(1/4)∑F′. At r=m+j the binomial terms divided by k! are dominated by an exponential series, including their scaled derivatives, and the limit of F′/m is 2x_j exp(−x_j). For the derivative tails the union of candidate windows about a pivotal site has length at most 2r−1; when r≤n/8 a disjoint length-≥n/4 segment gives an independent no-run condition, bounded using independent geometric runs and a binomial lower-tail bound. This yields summable centered tails; the omitted r>n/8 terms are exponentially small. The analogous probability tails give uniform integrability, so the phase-specific variance and the covariance normalization by sqrt(n)/2 are valid. Mellin integration over adjacent dyadic intervals gives the stated Gamma coefficients. Independent integer enumeration via aggregate cut counts (python3 /workspace/audit_evidence/composition_count_check.py) recovered −7/8 for four bits and the three finite table comparisons within 2.4e−7. Those checks are diagnostic; the all-sequence claim follows from the tail estimates.

## originality

FAIL

A distinct earlier-dated public mathematical record gives a stronger two-term result for the very same covariance, with the very same logarithmic phase and profile. Its displayed pole estimate and geometric tails also imply the exact variance phase and hence the asserted phase-resolved correlation coefficient by direct normalization. No conclusion about exact historical order beyond the records and their dates is needed for this coverage judgment.

## value

FAIL

The sharp covariance problem is worthwhile, but the frozen finding supplies no distinct scientific increment over the stronger covariance result and its direct variance-normalized consequence. The finite comparisons do not add an independent mathematical claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
