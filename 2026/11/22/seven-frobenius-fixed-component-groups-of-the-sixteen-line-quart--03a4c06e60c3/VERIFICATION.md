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

The reproducible finite computation is `python3 verify.py`, using only Python 3's standard library. Its expected terminal line is `QUARTIC_DEL_PEZZO_SEVEN_FROBENIUS_COMPONENT_GROUPS_OK`.

**Actual calculations:** the geometric graph has 16 vertices, 40 edges and degree 5 at each vertex. The vertex-orbit matrices for each of the seven \(S_5\) cycle types are formed over the integers, with the unique conic vertex fixed. All seven rooted matrices have nonzero exact fraction-free determinant, respectively \(2^{31},2^{22},2^{17},2^{13},2^8,2^8,2^3\). Independent two-adic pivot reductions modulo \(256\) yield exactly the invariant factors displayed in RESULT.md. The determinants show there are no missing odd-primary invariants.

**Scope of this evidence:** the code verifies the finite graph constructions, group presentations and Smith calculations. The geometric identification of sixteen curves and the relationship with Néron component schemes use the arguments and references given in RESULT.md; an external mathematical audit has not been performed. The results are conditional for arbitrary smoothings: the family must be proper, regular and semistable with unit node thicknesses.
