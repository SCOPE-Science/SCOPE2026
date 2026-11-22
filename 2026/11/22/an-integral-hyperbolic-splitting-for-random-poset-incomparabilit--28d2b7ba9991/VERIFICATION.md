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

# Verification and reproduction

The theorem is proved for every finite parameter poset by an explicit unimodular basis, not by finite extrapolation. The independent finite checks in `verify.py` enumerate natural-linear-extension posets through four points and fourteen five-point patterns; compare the proposed incomparable-realization predicate with a direct finite-poset transitivity test for two distinct new points; and verify all entries of the transformed Gram matrix, the zero-block basis and the zeta-matrix triangularity. Run `python verify.py` with Python 3 (standard library only). The bundled `verification_output.txt` records `FINITE_EXTENSION_AND_CONGRUENCE_OK`, 90 input patterns and 45,913 checked entries.

Separate exact integral Smith reductions on the named antichain of three points, three-point fork, four-point two-level complete order, four-point diamond and two disjoint two-point chains gave only invariant factors equal to one, with nullities respectively 0, 3, 9, 7 and 2. Those additional reductions were inspection checks, not a required dependency and not an all-size proof.

Scope: nonalgebraic one-point types in the homogeneous generic partial order, finite individually named parameter posets, and existential incomparability of two *distinct* realizations. The theorem does not determine counts of all ordered pair types or ordinary eigenvalue values. Historical novelty has not been independently certified.
