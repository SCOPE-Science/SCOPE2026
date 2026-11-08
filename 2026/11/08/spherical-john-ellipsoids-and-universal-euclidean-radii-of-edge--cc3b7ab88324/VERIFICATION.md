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

# Mathematical verification

The claim was checked by reconstructing its geometric objects, boundary cases and formulas. The normalized graph has bipartition classes of size \(n\), degree \(d\), and \(D=nd-2n+1\) tangent dimensions. The norm is Euclidean on the degree-equality affine hull, and the orthogonal projection diagonal is \(D/(nd)\). The John contact vectors have zero weighted first moment and identity weighted second moment. The unique circumcenter follows from an exact perfect-matching factorization and the mean squared-distance identity.

The included `verify.py` requires only Python 3 and its standard library. Execute `python3 verify.py` to reproduce independent exact-rational checks on 15 graph instances, including crown, complete bipartite, even-cycle and Boolean-cube examples. The checks include rational orthogonal projectors and perfect-matching decompositions. Printed PASS means those finite checks succeeded; it is not an independent proof or external certification. The paper proof, not the test enumeration, covers every graph satisfying the hypotheses.

No external independent audit has been performed. Geometric claims outside the stated scope (arbitrary irregular graphs, unsupported edges, ambient nonintrinsic metrics or exact Löwner ellipsoids) are not established.
