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

# Verification

The checker performs exact integer cellular-incidence checks on the actual finite polytopal facets; no floating-point approximation is used. It constructs the same orientation-sign convention as the mathematical proof. For each tested parameter it verifies that all codimension-one boundary coefficients cancel and that adjacent transpositions in the vertex permutation group act by \(-1\). When \(p=q\), it also verifies the degree \(-1\) of particle interchange.

Nine parameter pairs were run successfully: \((1,1),(1,2),(1,3),(2,2),(2,3),(3,3),(1,4),(4,1),(2,4)\). Execute `python3 orientation_checker.py` from the extracted directory. The checker is finite corroboration only; the general proof in `RESULT.md` separately verifies all quantifiers and follows from explicit incidence cancellation plus the published PL manifold theorem.

Limits: no independent external audit, no integral ring computation, no connected-sum homotopy proof, no claim about larger particle count. The full scientific result is the single orientation-and-character theorem in `RESULT.md`.
