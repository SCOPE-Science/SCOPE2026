---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

For G=GL_2(F_q), the rank-dependent ambient additive Fourier coefficient is N at rank0, -q(q-1) at rank1, q at rank2, N=(q²-1)(q²-q). Thus Gram B=q^4I-q²C_W/(q-1)+qJ, where C_W is the permutation-character kernel of GL2 acting on nonzero vectors. The decomposition 1⊕dimension-q V⊕(q-2) irreducible dimension-(q+1) sectors gives Gram eigen q² mult1+q², q³ mult(q-2)(q+1)², q^4 remaining. Independent direct q2,3 construction matched exact spectrum. Endpoint q2 has missing middle band. Claim’s full algebra and general Schur orthogonality argument reviewed.

## originality

FAIL

FAIL: GL2 is complement of the split determinant zero cone in four-dimensional matrix vector space; bilinear polar pairing of determinant is connected to coordinate dot by an invertible adjugate-transpose linear permutation preserving the invertible locus. The published all-even-dimensional cone spectrum at split m=2, transferred through ambient unitary-complement identity, yields exactly submitted three levels and multiplicities, a stronger theorem than the present group-specific setting.

## value

FAIL

FAIL: complete final singular multiset and sharp condition q follow mechanically from the stronger published cone theorem by m=2 split substitution and unitary-complement transfer. Permutation-character derivation is an alternative proof of already determined invariant rather than a distinctly motivated new claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
