---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Over the splitting field the quadric has ruling classes swapped by Frobenius, so an F2 curve has type (d,d), degree 2d and smooth genus (d-1)^2. A smooth conic has only three rational points. A smooth quartic filling the quadric would be genus one with five F2-points; its trace -2 gives five F4-points. An F2-point identifies its degree-two Picard torsor with the elliptic curve, so all degree-two classes rational over F4 are already rational over F2. The two projection bundles are exchanged by Frobenius and thus must coincide. Each projection uses the complete two-section series, so coincident bundles would put the embedded curve in the graph of a projectivity, contrary to type (2,2). The given quadric is smooth and nonsplit and has the five listed points. The cubic is not a multiple of the quadric (compare its wz^2 term) and vanishes at all five. An independent exact four-chart Jacobian check gave the unit ideal on each chart. Over the closure the (3,3) divisor is connected: disjoint effective components would have pairwise intersection zero, forcing all into the same ruling and contradicting the total class. Smoothness and connectedness give geometric integrality. All smooth nonsplit quadrics over F2 have the same projective form, so the witness transfers.

## originality

FAIL

Existing results give both decisive bounds, and the displayed sextic is projectively equivalent to the published Faber–Grantham example. The earlier indexed exact exclusion of a smooth filling anticanonical section, the standard even-degree and conic facts, and the published explicit smooth sextic mechanically give the frozen threshold. No separate new theorem is established by packaging these ingredients. This is demonstrated coverage, not an absence-of-search-evidence judgment.

## value

FAIL

The binary nonsplit filling problem is natural and the minimum is useful, but the frozen claim adds no unknown finite threshold or distinct witness: the minimum is a direct consequence of known bounds and even the displayed cubic model is equivalent to the published one. The proof is expository in this submission; it does not yield a further filling criterion, classification or new invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
