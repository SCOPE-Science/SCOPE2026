---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

For odd n=2k+1>=3 with v_i=e_i+e_(i+1) in Euclidean R^n, A=I+S has inverse B=(1/2)sum_{h=0}^{n-1}(-S)^h. Barycentric gradients projected onto the affine tangent H0=1-perp have squared norm (n^2-1)/(4n) and dot product [(-1)^d n(n-2d)-1]/(4n). Their negative normalized dot product is the claimed interior facet-dihedral cosine. Each distance d=1..k supplies n unordered ridge pairs, with alternating acute/obtuse parity, and the parity submeshes of cos theta each have gap 4/n, proving the uniform-cosine and (1/2)sin theta limiting law with O(n^-1) CDF discrepancy. Determinant 2, projection and squared-distance averaging yield the ancillary inradius 2/sqrt(n(n^2-1)), circumradius sqrt(2-4/n), volume sqrt(n)/(n-1)!. Independently checked all projected Gram entries in exact fractions for odd n=3..25; the complete all-n proof is the inverse matrix and mesh argument, not those samples.

## originality

PASS

PASS best-of-knowledge for the exact inherited-Euclidean unsigned odd-cycle edge-simplex angle multiplicities and sine limiting law. Earlier graph-edge-polytope algebra, lattice volume one, and directed or symmetric edge polytope results do not establish this Euclidean metric angle distribution. No dominating or equivalent mathematical statement emerged from Resultary/primary searches; exact-alias priority remains a residual risk.

## value

PASS

PASS: the canonical graph edge polytope is a natural embedding and its complete Euclidean facet angular spectrum is an intrinsic geometric invariant; the explicit parity alternation and nonconcentrating sine-law asymptotics would be directly useful for graph-polytope geometry and metric random ridges, beyond generic matrix-inverse formulas.

The dated certificate retains the supplied scientific assessment, sources and limitations.
