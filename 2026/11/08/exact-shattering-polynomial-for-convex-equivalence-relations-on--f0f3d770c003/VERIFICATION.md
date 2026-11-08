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

# Reproducible checks

Run `python checker.py` with the included standard-library-only file. A successful run prints `CONVEX_EQUIVALENCE_INTERVAL_SHATTERING_PASS`. It independently evaluates all \(2^N\) cut sets for every query subset on \(N=0,1,2,3,4,5\) cut sites. For each support it compares the direct all-label realizability result with the private-site condition. It separately compares transfer polynomials and the coefficient formula for \(N\le30\), including the boundary and top-degree coefficients.

The proof is a general theorem, so these finite computations only check special instances. The independent external audit status is `not_performed`. The known OEIS total sequence and the residual historical-coverage risk are stated in the result.
