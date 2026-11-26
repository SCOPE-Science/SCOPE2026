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

The reflected density derivative is dz/du=dz/dv=-1. At a coexistence root F=0, u=(d/z-b)/H and v=1-z-u, the displayed Jacobian follows; its determinant simplifies to -uv z^2 H F'. The independent exact-rational replay proves the bracket, both density enclosures, strict reaction stability, and modal determinant signs +,-,-,+ at 0.069, 0.070, 0.156, 0.157. Orthogonal Laplacian decomposition gives trace tr J-21 x<0 and one strict unstable interval (alpha,beta) in x=epsilon*lambda for each positive eigenvalue. The weighted incidence Gram matrix is D^(1/2)(I+11^T)D^(1/2), bounded in Loewner order between D and (m+1)D. Thus consecutively ordered eigenvalues are separated by a factor of at least 10, larger than beta/alpha<3. The m rescaled intervals are pairwise disjoint, including the m=1 case, and separated by open intervals of exponential stability; the zero mode remains Hurwitz. The at-most-m bound follows by counting one quadratic negative interval per nonzero mode for stable uncoupled kinetics. At crossings a zero eigenvalue is present; nonlinear behavior there and pattern selection are not decided.

## originality

PASS

Credit the stated normalized weighted-star extremal realization and exact certificate, not the ecological parameters, finite mode band or underlying common-scale dispersion relation, which are prior. The sharp attainment for every size is the distinct contribution.

## value

PASS

Shows that the number of strict instability windows under just one common mobility scalar can scale with all available spatial modes, even with fixed viable kinetics and a unit conductance budget. The construction supplies an exact benchmark against monotonic or single-window intuition, independently of nonlinear pattern claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
