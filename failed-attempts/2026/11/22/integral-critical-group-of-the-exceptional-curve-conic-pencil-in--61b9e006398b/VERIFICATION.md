---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The 16 exceptional curves and 10 conic classes of the blow-up of five general points are the stated classical lists. Pairing with F_i=L−E_i gives a vertical index set of size zero on Q (the empty set), size two on L_ab (indices a,b), and size four on E_a (all indices except a). Pairing with G_i=−K−F_i gives the complementary indicator since (−K)·C=1. These are exactly the even-weight five-bit strings. Vertical exceptional curves belong to reducible fibers; a fiber cannot consist solely of a multiple of an exceptional curve, since its square would be negative. The independent parity reconstruction and exact integer Smith and determinant calculations give 1^15,5,20^4,80,320^4 at both a curve sink and a pencil sink. The determinant is 2^36 * 5^10 = 671088640000000000, nonzero, and the degrees 5 and 8 give 80 edges. The exponent is 320. The submitted Euclidean code uses integral unimodular operations, with tracked transformations and exact determinant checks; the independent computation did not use it.

## originality

FAIL

The exact group is mechanically implied by the classical parity incidence, the complete-multipartite critical-group formula of Jacobson–Niedermaier–Reiner (2003), and routine local Schur complements and eigenspace splitting. This is a demonstrated implication, not a claim that their paper directly names or tabulates the 26-vertex graph.

## value

FAIL

The configuration and its critical group are natural, and the correct values could be useful as reference data. But the entire proposed new exact invariant comes from a standard local block calculation, a direct substitution into the existing complete-multipartite formula, and the elementary 5-primary splitting. The frozen result adds no substantive integral theorem or independent mathematical gap beyond that specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
