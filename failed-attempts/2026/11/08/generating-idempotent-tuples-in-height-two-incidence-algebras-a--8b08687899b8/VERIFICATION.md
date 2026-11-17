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

For height-at-most-two incidence algebras the strict radical has square zero. Idempotent diagonal entries must be binary, and for each cover edge the off-diagonal coordinate is free precisely at positions where endpoint binary words differ; the algebra-generation criterion is injective diagonal labeling and an off-diagonal k-vector outside the one-dimensional span of the diagonal difference, yielding exactly q^{h}-q valid choices. Multiplying over independent edges proves the Hamming sum and specializing root-to-r-distinct-leaf difference words yields the star coefficient polynomial. For fixed r>=2, edge-failure probability is (1+q(2^k-1))/(q+1)^k and each leaf collision has probability ((q²+1)/(q+1)²)^k, giving the q=2 vs q>=3 leading asymptotics. The exact formula and its proof are also proved for every finite poset, not merely height two, by the earlier Nov2 public result. Independently checked 36 weighted star coefficient cases over q=2,3,4,5 and small r,k; this is finite corroboration.

## originality

FAIL

FAIL for the original final claim. A complete November 2 2026 published theorem counts ordered idempotent generating tuples in EVERY finite poset by a Hamming-cover polynomial; when the poset has height <=2 its noncover exponent vanishes, recovering the submitted formula exactly. An earlier October 18 2026 radical-square-zero quiver theorem already gives the same single-arrow idempotent generation law: for m=1 the factor q*R_q(h-1,1)=q^h-q. The star coefficient is immediate from the all-poset formula by fixing root codeword and choosing labelled leaf words. The asymptotic field crossover is a short inclusion-exclusion comparison of two explicit failure probabilities already fully encoded by that exact enumeration, not an independently original theorem rescuing the covered main claim.

## value

FAIL

FAIL for the combined submitted contribution after accounting for published stronger results. The all-height-two count and star exact polynomial are direct specializations of published all-poset and all-quiver counts. The remaining fixed-r field-crossover is a routine leading-term comparison of single-edge and paired-leaf collision probabilities determined explicitly by the stronger exact enumeration; without a substantively new mechanism or inference it does not constitute an independent mathematical result of value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
