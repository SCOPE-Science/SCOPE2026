---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Normal equations remove the component of b−Ax_* perpendicular to col(A). For batch missing i, exact block minimization leaves in col(A) the rank-one projector onto the normalized ith dual column. Scaling and sign choices do not change the block spaces. Let W be the matrix of these unit normals after flipping the middle sign. Its Gram M is the sign-conjugated normalized inverse Gram and has all entries positive. With S=diag(1,−1,1) and D=diag(a,1,c)/sqrt(Δ), M^{-1}=SDGDS. The row sums r=M^{-1}1 are (a(a−u),1−ua−vc,c(c−v))/Δ, all positive since a>u, c>v and ua+vc≤sqrt((u²+v²)(2−u²−v²))<1. With τ=1ᵀr=Z/Δ, the unit vector W r/sqrt(τ) gives the same Rayleigh value 1/τ for every probability law. At p=r/τ the matrix diag(sqrt(p)) M diag(sqrt(p)) has sqrt(p) as a positive eigenvector at 1/τ; positivity implies this is its top eigenvalue, hence the top eigenvalue of the mean residual operator. Equality in the common Rayleigh bound forces the mean operator to have the witness as eigenvector; column independence gives p=r/τ uniquely, including against boundary laws. In the rational example symmetry splits the uniform normal Gram into an odd eigenvalue 7/16 and an even block of trace 41/16 and discriminant 9·137/16²; division by 3 gives the stated top uniform factor. Repeated conditional expectation proves the k-step upper bound, not an exact asymptotic exponent. The supplied finite checker was read, not executed; its simplex loops are 101×101, not the 10,552 grid trials named in the print text, which does not affect the theorem.

## originality

FAIL

A distinct extant Resultary record, --e118fcf8fe26, proves an all-but-one-coordinate minimax theorem with precisely the same one-step objective and a sign-balanced normalized inverse Gram hypothesis. That hypothesis holds throughout the frozen Gram-path domain, and direct substitution gives both the unique law and the exact retention stated here. The indexed proof explicitly notes related path calculations; it does not identify a source by record ID. Its later catalogue date does not establish priority in either direction. The finding is correct but no longer distinct from the stronger published coverage as examined in this audit; this is not a conclusion that the earlier primary literature contained the formula.

## value

FAIL

An unknown exact minimax batch design in this smallest correlated path is a meaningful benchmark, and the formula makes the effect of correlation rather than column scaling explicit. But the actual frozen probabilities, sharp factor and uniqueness all follow by direct row sums from a verified existing general omission theorem. The remaining rational illustration and repeated-step inequality do not supply an independently valuable unknown result. The result remains useful as a worked example, not a distinct scientific contribution under this review.

The dated certificate retains the supplied scientific assessment, sources and limitations.
