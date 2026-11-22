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

# Verification notes

The proof is self-contained. Two determinant-root arguments are required: (a) a homogeneous cubic in a nonzero real vector used to annihilate at most three independent linear measurement constraints and obtain a nonzero rank-one matrix, and (b) a real odd cubic in the coefficients of an arbitrary two-plane of three-by-three matrices, forcing a nonzero singular member. Their continuity, sign change, and nonzero-witness conditions were checked directly.

For the sharp upper test, the real symmetric traceless matrices form a five-dimensional subspace of all nine-dimensional real matrices, with codimension four. Spectral decomposition yields absolute eigenvalues \((M,a,b)\) with \(M=a+b\). Convexity of \(x\mapsto x^q\) for \(q\ge1\), and subadditivity of \(x\mapsto x^p\) for \(0<p\le1\), give the two required norm bounds. Both boundaries are attained on \(\operatorname{diag}(1,-1,0)\); the full-rank final bound is attained on \(I_3\).

No experimental enumeration is claimed as proof or as independent validation. Scientific literature inspection and nearest published comparisons are documented separately in the review. The theorem has not undergone an independent mathematical audit.
