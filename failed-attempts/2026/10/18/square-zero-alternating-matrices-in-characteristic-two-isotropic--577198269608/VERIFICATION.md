---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

The claimed all-n rank classification and enumeration are mathematically correct. For any symmetric zero-diagonal X satisfying X²=0, symmetry gives ker X=(im X)^⊥; image U is totally isotropic, and F(v,w)=v^T Xw descends to a nonsingular alternating form on U*. Conversely this data uniquely reconstructs X. Nondegenerate alternating forms exist exactly when r is even, and GL_r/Sp_r gives E_q(r). The isotropic-vector hyperplane has dimension n−1, symplectic when n odd, radical R=<ones> when n even; the two disjoint even-n strata of U yield I_q(m,r−1)+q^r I_q(m,r). The r=0 term is one, odd ranks vanish, and the sharp support is the even ranks 0..2⌊n/4⌋. These are proofs for all q=2^f and n≥1, not extrapolation from finite tests.

## originality

FAIL

The all-n, all-even-q, fixed-rank count is a direct orbit-quotient corollary of the already-published complete rank enumeration of rectangular isotropic frames. Buckhiester (1974), Theorem 4.1, covers precisely the numerator N(I_n,0,n,r,r); dividing by the standard symplectic basis stabilizer yields all claimed rank fibers. His proof also explicitly handles the canonical all-ones radical vector in even n. This decisive statement-level implication invalidates the source self-review argument that different matrix dimensions or a nonmatching title establish novelty. The canonical image-form description is mathematically correct but an elementary reformulation of this quotient.

## value

FAIL

The object and invariant are natural and the formula is correct, but as an independent new mathematical finding the entire exact count is mechanically implied by the already-published rank enumeration for isotropic frames using the textbook Sp_r orbit quotient. The image/form parametrization is an elementary linear-algebra reconstruction, and the even-dimensional radical split is a standard feature already used in the prior enumeration. No separate non-implied structural boundary, unknown exact invariant, or genuinely new classification remains to motivate a standalone contribution. Reproducibility and an elegant packaging do not alone satisfy the mathematical-value bar for a new claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
