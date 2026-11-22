---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

For b_i=(n−a_i)(n−a_i+1), introduce tau=m−2n. Then T_i−m=b_i−tau; the exact threshold solves sum a_i(b_i−tau)_+=2n². Vertex center t_i=(b_i−tau)_+/(2n)−1 has weighted zero sum, w_v=(b_i−tau)_+/(2n²). Direct full-column Laplacian computation gives squared distance n+min(b_i,tau)+S/(4n²), radius n+tau+S/(4n²), and nonnegative variance certificate proves uniqueness. Independent exact-Fraction direct full-Laplacian checks for (3,3,6),(4,17,17),(2,8,28),(12,13,13) verified all vertex distances and contacts (12,4,10,38). The actual full fixed-source proof is correct within r≥3 unweighted canonical embedding.

## originality

FAIL

DECISIVE COVERAGE: complete already-published Water-filling contact strata of complete multipartite Laplacian simplices (Resultary 2026/11/17/...e213ee1cfdd8) states exactly the same theorem. Its tau is m−2n; equations for unique center, radius, clearance, weight, sorted active prefix and zero-weight touching classes are algebraically identical. Full RESULT.md inspected, including K_3,3,6 and K_4,17,17 exact examples. Thus the claim is a reparameterization of a covered statement despite different title, and cannot be accepted as original.

## value

FAIL

As an independent research contribution this package adds no new structural invariant beyond the covered published full multipartite theorem; sorted-prefix formula and all examples are already given there. The mathematical object and invariant are worthwhile, but this record is a restatement of the prior resolved result, so incremental new scientific value fails.

The dated certificate retains the supplied scientific assessment, sources and limitations.
