---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The objective equals N(tr((L+11^T/N)^(-1))-1) on connected support. The trace inverse is strictly convex (its second derivative in a nonzero symmetric direction is strictly positive), and the simple-graph Laplacian is injective in edge weights. The compact budget domain and blow-up at disconnection ensure existence; rescaling exhausts the budget. Uniqueness forces orbit invariance, not vice versa. The nonzero eigenvalues are x with multiplicity m-1, x+ry with multiplicity m(r-1), and Nx once. With t=(x+ry)/x>=1 the normalized objective is alpha*A+beta*D+beta*A*t+alpha*D/t, whose unique minimum is on the boundary if alpha<=0 or beta*A>=alpha*D, and otherwise at sqrt(alpha*D/(beta*A)). The identity A+D=mr² gives the stated threshold including equality. A second check at the uniform star gives derivative -2N/x² for any leaf-to-leaf edge and -(N-1)/x² for any spoke. The gradient per unit price thus gives the same threshold regardless of peripheral candidate edges whenever at least one such edge is available. The light-price optimum tends to m²Ara/B, giving the stated ratio and divergence for fixed m and increasing r.

## originality

FAIL

The identical independently adjustable two-price windmill design, unique optimum, price cutoff including equality, and explicit resistance formula are already present in a distinct Resultary record. Earlier heterogeneous-petal statements also specialize to the same theorem. The ratio and unboundedness are immediate limits of the already stated formulas; there is no independent finding to preserve by narrowing to that calculation.

## value

FAIL

Optimal design of clique windmills is a natural question, but the submitted explicit design and threshold re-evaluate a covered design. The remaining spoke-only penalty follows by direct substitution in the known two-regime expressions and does not establish a new bound or design phenomenon beyond them.

The dated certificate retains the supplied scientific assessment, sources and limitations.
