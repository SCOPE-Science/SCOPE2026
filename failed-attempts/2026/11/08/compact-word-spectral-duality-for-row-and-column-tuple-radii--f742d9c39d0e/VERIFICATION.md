---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

For all finite Kraus tuples with compact generators, finite-rank approximants yield norm-compact positive maps on B(H). On a common finite corner the paired superoperators are Hilbert–Schmidt adjoints; isolated nonzero Riesz eigenvalues and algebraic multiplicities persist in the compact norm limit. Their spectral radii agree, and Gelfand formula with positivity gives row/column equality; grouping all length-m compact words gives the assertion for the powers. The compact-positive Perron eigenvector is compact because the nonzero eigenvalue puts it in the compact range. Norm-convergent compressions of compact entries give the finite-section limit. Independent finite-matrix HS adjoint and two-word expansion checks passed; these do not prove infinite-dimensional compact perturbation. Boundary m=1, radius 0 and Fock isometries are handled consistently.

## originality

FAIL

The 26 October 2026 power-compact Kraus theorem covers all finite tuples and even square-summable countable families with compact length-m words: it proves compactness equivalence, nonzero multisets of both powers with Riesz multiplicities across B(H), K(H), Schatten ideals, and equal row/column radii. Identical multisets imply the submitted weaker conjugate equality since each completely positive superoperator is adjoint-preserving and has conjugate spectral pairs. The submitted compact Perron eigenvectors and finite-section convergence follow from standard compact positive operator and spectral approximation results.

## value

FAIL

The underlying compact-word radius and nonzero spectral-multiset duality are entirely covered by a broader earlier theorem. Positive compact eigenoperators at positive radius and compact finite-section convergence are routine consequences of standard compact positivity and norm-perturbation, not a separately motivated new invariant; a narrower repackaging adds no substantive mathematical value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
