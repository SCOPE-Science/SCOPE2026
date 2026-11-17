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

The directed Gaussian KL identity with m=tr Γ/n gives 2D=m∑1/y_i-n+∑log y_i-n log m. A one-coordinate derivative has cubic numerator P=Ty^3+(BT-n(n-1))y^2+(n-1)By-B^2; Cauchy–Schwarz BT≥(n-1)^2 makes P strictly increasing on y>0, so the one-coordinate objective first decreases then increases; every maximum is at box endpoints. Exactly j eigenvalues κ and n-j eigenvalues 1 give n/2 times Fκ(j/n) as claimed, and the Fκ derivative crosses zero exactly once. Independent symbolic differentiation proved the cubic identity; 2,400 random spectral vectors and all endpoint multiplicities for n=2,3,4,5,7 corroborated the sharp discrete maximum. The formula is mathematically correct but does not establish novelty.

## originality

FAIL

Decisive complete prior coverage. The October 18 published SCOPE theorem gives the identical KL orientation, exact trace-matched inverse covariance, all finite dimensions, sharp two-point optimizer spectra, adjacent-integer optimizer and fixed-k large-K coefficient, PLUS an explicit nonzero-residual Lanczos realization. The Nov 2 and same-day Nov 8 companion results confirm the identical formula. Let precision B=Γ^{-1} and set t=1-q. The earlier Φκ(t)=A t(1-t)-log(1-(1-1/κ)t)-t log κ equals the present Fκ(q)=A q(1-q)+q logκ-log(1+(κ-1)q) identically. This is mathematically the same theorem, not merely a similar title. The n=2 formula and simpler nonsharp Kantorovich envelope are routine corollaries.

## value

FAIL

The exact KL extremum is a meaningful mathematical result but already established in stronger earlier form. Rephrasing precision B as covariance Γ, reorienting endpoint multiplicity and adding the elementary n=2 or coarse strict envelope yields no independent unknown invariant or motivated new classification. Correctness and exact rational tests do not rescue covered science.

The dated certificate retains the supplied scientific assessment, sources and limitations.
