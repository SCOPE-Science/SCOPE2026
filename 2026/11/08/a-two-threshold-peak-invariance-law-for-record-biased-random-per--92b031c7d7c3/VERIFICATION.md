---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

The initial rank vector is bijective by successively inserting each new label into its prescribed position in the order of earlier labels. Its product weights give the required normalization, including the forced first record. In one-line order an ascent at i-1 is exactly R_(i-1)<R_i and a descent at i is exactly R_(i+1)<=R_i. With R_i=b<i their conditional probability is b(b-1)/[(theta+i-2)(theta+i)] since neither allowed choice reaches the earlier/new record rank; with b=i it is i/(theta+i). Summing b(b-1) gives i(i-1)(i-2)/3. In the numerator after subtracting 1/3, the i-dependent terms cancel: writing u=i-1, the product is (theta+u)^3-(theta+u); three times the summed numerator minus that product is -theta(theta-1)(theta-2). This also applies at i=2, when the nonrecord term vanishes. Positivity of the denominator gives the strict signs and two positive roots. Partial fractions of the shifted triple reciprocal telescope from theta to theta+n-3 and give the claimed expectation, with a strictly positive bracket for n>=3.

## originality

PASS

Qualified to the explicit all-bias strict peak marginal, its nonuniform equality at theta=2, and the associated expectation. The known independent-rank construction and adjacent descent theorem nearly supply the computation, but the inspected sources do not give the joint adjacent comparison needed for a peak. First-order response at theta=1 is already covered separately; it is not credited here as new. The finite two-root classification is a short new enumeration from known inputs, not the introduction of the model or independent ranks.

## value

PASS

A strict peak is a natural local refinement of the already studied descent statistic. Equality at the nonuniform bias theta=2 holds simultaneously at every interior position and finite size, with a sharp sign law on the three remaining open regimes. This is useful as an exact calibration and a distinction between a natural peak marginal and other local statistics under record bias; it is not inference about the complete distribution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
