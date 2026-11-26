---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Affine invariance of det(Cov)/Vol² reduces the claim to K_t with the distinguished vertex at zero. Independently, write X=S U with S=ΣX_i∈[t,1] and U uniform on the unit-sum triangle, independent of S by section scaling. The density of S is proportional to S². U is Dirichlet(1,1,1); its covariance is 1/12 on the zero-sum plane and zero on the axis, and its mean is (1,1,1)/3. Total covariance gives eigenvalues E(S²)/12 twice and Var(S)/3 once. The slice integral gives volume (1−t³)/6, E(S)=(1−t⁴)/(4∫_t^1 s² ds), and E(S²)=(1−t⁵)/(5∫_t^1 s² ds). Substitution, exact differentiation, and expansions at t=0,1 in `python3 /workspace/checks/independent_01_05.py` (check 3) recover the full rational expression, the factor t²(t−1)(t+1)³P(t) with positive prefactor, and the cubic and quadratic leading changes. The derivative is strict for 0<t<1; continuity gives the t=0 endpoint. Project onto the zero-sum plane and replace the sum coordinate S by (S−t)/(1−t); the cross-sections in the projected plane are S times the same centered triangle and converge uniformly to it. This gives the prism limit without treating K_1 as full-dimensional. The limiting ratio is 500/729. The frozen 151-test triangulation result is recorded corroboration, not the proof or an independent rerun.

## originality

PASS

The supported distinction is the exact all-depth strict classification, including the endpoint orders, for an asymmetric one-vertex tetrahedral cut. Neither a new tetrahedron moment formula nor a new general frustum integration method is claimed.

## value

PASS

A single parallel corner cut is a natural perturbation linking the simplex to a prism. The all-depth order resolves more than local behavior or the two known endpoint constants and distinguishes the cubic response to a small cut from the quadratic approach to a thin prism. This is a useful sharp family comparison, not evidence of monotonicity under arbitrary truncations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
