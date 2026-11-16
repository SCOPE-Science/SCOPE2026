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

The analytical proof is contained in RESULT.md. Run `python3 CHECK.py` using the standard library. The checker passed 1,197 finite assertions on the prepared package. It compares explicit rational Zak series with direct finite sums, validates the determinant identity, checks the three-tap null vector's vanishing outside the four-erasure mask and the quadratic frame-bound obstruction for a three-row mask, and exhaustively tests bounded-degree integer Laurent polynomials for the minimum-support lemma.

A finite checker is not an infinite-dimensional proof. The proof uses fiberwise Laurent-polynomial divisibility, coprime filters, and a minimum-support argument. Independent mathematical validation has not been performed.
