---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

For a nontrivial rooted tree, let b=sqrt(S), c=||v||/b. Positive definiteness follows from the shift plus the sum of edge squares. The absence of triangles gives (A-alpha1)q1-b*q0=v/b, with a unique two-edge contribution at every distance-two vertex. When v is nonzero the Galerkin solution has basis coefficients (alpha1*alpha2-c^2, -b*alpha2, b*c)/Delta by cofactors of the positive-definite compression. In original coordinates the two nonroot terms are w_i*alpha2/Delta plus v_i/Delta for neighbors and v_j/Delta for distance two. This proves all the asserted signs, including equality at a zero, and the root cofactor is positive. For two steps the coefficients are (alpha1,-b)/det(T2); for one step only a_r^{-1} at the root is nonzero. A one-vertex tree, if included, terminates at step one. With v=0 the two-dimensional Krylov space is invariant and the result is exact. For inverse positivity independently, a minimum of the solution cannot be negative because at a negative minimum both the Laplacian term and the shift give a strictly negative right-hand side there; a zero minimum propagates to the root by connectedness and contradicts the unit source. On the broom the distance-two residual is nonzero for each t>0. Independent exact Galerkin elimination yields the three stated neighbor polynomials over Q, v^T v=2D/(t^2+26) and Q=Delta D. Exact Sturm variations are 3 to 2 for P and 2 to 2 for each other numerator. The latter start strictly positive; P(28)=-609696 and P(29)=3005694 certify the unique transition and the t=30 vertex-2 value is -77253/484548896. This is an exact-arithmetic, unpreconditioned result only. The indexing of v in the piecewise display is clarified immediately below it; there is no substantive ambiguity in the formula.

## originality

PASS

Broad transient CG negativity and Lanczos/Galerkin theory are prior. The narrower point-source neighbor criterion and complete weighted-broom sign transition are supported as distinct to the best of the checked evidence, not as a claim of methodological novelty or certified priority.

## value

PASS

Point forcing is the natural test of whether an iterative approximation to a positive graph Green function preserves the maximum principle. The general certificate isolates the only shell where signs can fail and the reproducible continuous conductance transition shows exactly when the discrepancy appears in a concrete tree. This is stronger than a single arbitrary numerical example. No minimum tree size, preconditioning, or rounding robustness is claimed; 'local' permits the diagonal entries in the Rayleigh quotient of a vector supported within distance two.

The dated certificate retains the supplied scientific assessment, sources and limitations.
