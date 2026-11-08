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

# Verification of the Clebsch line-complement spectrum

Two standalone exact-arithmetic checks accompany the proof.

The program `verify_incidence.py` enumerates all fifteen diagonal lines as rational two-dimensional subspaces of the five-dimensional ambient vector space. It verifies their line-intersection graph, its strongly regular parameters, and the rank-six intersection matrix. Its observed terminal output was `VERIFY_CLEBSCH_INCIDENCE_OK lines=15 graph_edges=45 picard_span=6`.

The independently structured `verify_finite.py` enumerates every rational point and every rational line on the Clebsch model in each of the prime fields of sizes \(7,11,13,17,19,23\), compares the actual multiplicities on rational lines to the formula, and verifies the predicted point counts. Its observed terminal output was `VERIFY_CLEBSCH_FINITE_OK fields=6`. In the nonsplit cases, nonrational lines have no rational points by the skew-Frobenius-pair argument in the proof.

These finite checks are exhaustive for the six tested base fields but cannot on their own certify infinitely many finite fields or extension degrees. The general conclusion follows from the separate geometric and Frobenius argument in `RESULT.md`. No proof assistant or independent formal audit was used.
