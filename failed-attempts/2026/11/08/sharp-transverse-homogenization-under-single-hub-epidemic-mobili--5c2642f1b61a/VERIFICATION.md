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

For the stipulated symmetric linear model, the subspace of zero-sum ordinary entries with zero hub entry is invariant under Phi, and the middle diagonal operator is the identity there. Hence the restriction is beta_0 B² minus gamma I, and by symmetry the orthogonal projection to that subspace commutes with the generator, giving autonomy for arbitrary initial perturbations. The nonnegative constant-row-sum block has all eigenvalues in [-(1-q),1-q], and symmetry gives the exact Euclidean semigroup norm from the largest squared transverse eigenvalue. The stated interpolation is admissible and spans the full interval. The positive reduced Perron eigenvector lifts to a positive full eigenvector, including at q=1/m; the common-value/hub quotient therefore gives the full reproduction number. The exact frozen example has quotient eigenvalues 0 and 4/3 and contrast exponents 1 and 5/8.

## originality

FAIL

The distinct indexed finding 3575e4cfa8c0, proof parts 1 and 5, supplies the exact rank-one decomposition of the same matrix and explicitly specializes to every symmetric constant-row-sum ordinary block with uniform hub flux. It states the invariant quotient, background independence of the dominant block and the upper bound on contrast eigenvalues. On the contrast subspace the rank-one term is zero and the mobility restricts to B, giving the complete contrast operator and Euclidean exponent by direct restriction and spectral mapping. The sharpened attainability statement adds the scalar interpolation of the ordinary identity and averaging blocks; it does not require any new spectral bound or structural result. The originality rejection is based on demonstrated implication, not on a title match, date, or source access failure.

## value

FAIL

The distinction between a dominant mode and contrast dynamics is useful, but the prior same-class invariant block and contrast bound already establish that distinction. What remains is an immediate scalar interpolation of two standard matrices under that known block decomposition. The frozen record does not establish an independently nonroutine result beyond this specialization; no repair is justified merely by rephrasing the same interval.

The dated certificate retains the supplied scientific assessment, sources and limitations.
