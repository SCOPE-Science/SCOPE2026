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

Primitive four-words are exactly the arcs left after deleting abab, and the balanced positive degrees are q-1 at aba and q elsewhere. On the zero-sum space A^3 vanishes, so the unrestricted rooted cofactor is q^(q^3-4). The non-loop deletions are disjoint pairs of opposite arcs: with the oriented difference matrix F their correction is FF^T. The I, A and A^2 terms of the inverse act in the reduced determinant via F^TF=2I, F^TAF=-2I and F^TA^2F=B^TB, where B is the alphabet complete-graph incidence matrix. Its Gram eigenvalues q and 0 give the two stated factors, both positive for q>=2. A positive cofactor and balance give strong connectivity. Fixing one specified arc first gives a unique representative in each rotation class, so BEST has no additional start or length factor. The resulting formula covers q=2 without singular cases.

## originality

FAIL

A distinct indexed record gives the same complete all-q count and low-rank proof as part of a stronger order classification. Verified mathematical coverage is the reason for rejection, not a judgment about who proved it first. The matching catalogue path is dated 2026-11-02, later than the frozen source path; the dates do not establish historical priority or dependence.

## value

FAIL

Counting rotations of primitive-factor cycles at the first composite order is a natural exact question, and the deletion correction is meaningful. The assigned claim, however, gives neither an additional invariant nor a different mathematical method beyond the verified indexed statement and proof, so it does not stand as a separate contribution. No surviving distinct claim was supported for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
