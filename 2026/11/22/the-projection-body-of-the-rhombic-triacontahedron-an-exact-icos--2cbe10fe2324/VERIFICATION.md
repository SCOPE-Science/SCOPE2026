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

# Verification and limits

Execute `python rt_projection_checker.py` with SymPy installed. This checks exact identities in \(\mathbb Q(\sqrt5)\), namely the 20 source-vector triple minors, 455 projection-generator triple minors, five multiplicity classes, 31 unoriented facet normal lines, regularity of each facet type, volume formulas and the normalized quotient. The verifier prints `ALL_CHECKS_PASSED` on success and raises an exception on failure. An independent numerical convex hull algorithm reproduced the 32 and 120 vertex counts and the two volumes; that cross-check does not replace the symbolic exhaustion. The proof uses the exact classical zonotope determinant formula, rather than interpreting finite sampling as an infinite result.

Prior work establishes the general sharp zonoid bound and provides standard generators; only the explicit fixed-icosahedral map and complete determinant spectrum are submitted for novelty comparison. A historical lookup is bounded, not proof of first publication. No independent external audit has occurred.
