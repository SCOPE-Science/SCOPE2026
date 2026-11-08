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

# Verification and proof boundaries

The standalone script `verify_arbor_circumball.py` was run as packaged source using CPython's standard library. It enumerated all vertices for \(54\) parameter pairs with \(3\le n\le11\), checked \(12{,}102\) squared-distance evaluations and their contact identities, and verified each dual barycentric center certificate exactly. It also evaluated both vertex-orbit distance formulas for \(12\le n\le150\), \(1\le k<n\).

Recorded output: `PASS cases 54 enumerated_vertices 12102 exact_assertions 2307483`.

The proof in `RESULT.md` independently provides the vertex exhaustiveness argument, strict inequalities for all omitted contact orbits, and the weighted variance identity proving global optimality and uniqueness. Enumerations are finite checks; they do not certify the infinite parameter range. The uniqueness result depends on the standard Euclidean norm, not affine invariance. Historical priority and independent scientific audit remain unperformed.
