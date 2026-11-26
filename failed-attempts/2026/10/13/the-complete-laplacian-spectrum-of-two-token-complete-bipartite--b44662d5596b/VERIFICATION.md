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

The incidence-block proof is valid for the unnormalized Laplacian. The constant quotient gives 0, m+n, and 2(m+n-1). The mixed tensor of two zero-sum spaces has eigenvalue m+n-2. A one-shore zero-sum sector couples with squared off-diagonal entry n(m-2) or m(n-2), respectively; when the relevant shore has size two the same-shore zero-sum image vanishes, not merely its coupling. The pair-incidence kernels fill exactly the remaining dimensions. Coincident values are counted additively. Kirchhoff's theorem gives the tree product with prefactor 4. An independent symmetric-difference construction and exact characteristic polynomials matched the table at (2,2),(2,3),(3,2),(3,3),(3,4),(4,2); exact cofactors at (2,2),(2,3) gave 32 and 10800. Reproduction: /workspace/branches/b648819a-11b0-4491-aecf-5e68bab73869/independent_check.py. No frozen script was executed. The finite checks corroborate the uniform proof, not replace it.

## originality

FAIL

The earlier Dalfó et al. lifting and graph/complement theorem, together with their explicit Cartesian-Johnson description for this very family, yield the exact spectrum in the two-token case by multiset subtraction in a single remaining Johnson eigenspace. The tree count is then Kirchhoff's formula. This demonstrated prior implication covers even the size-two boundaries; neither the date of a separate catalogue match nor an inaccessible paper supplies the failure reason.

## value

FAIL

The graphs and the requested multiset are natural, and the explicit product can be useful. But the table is a mechanical specialization of published spectral pairing already applied to this family, and the tree count is its standard Matrix–Tree corollary. The size-two convention is likewise automatic from J(2,2); it is not a separate gap. The alternative block calculation does not supply a distinct structural result beyond this exact known implication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
