---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

The λ-analytic basis is a homogeneous degree-n polynomial, with nonnegative real-axis coefficients. The source provides |φ_n(z)|≤ε_n^(−1)|z|^n, and explicitly φ_n(1)=ε_n^(−1). Homogeneity immediately gives equality at z=r>0, while the exact eigen identity D_z(zφ_n)=(n+λ+1)φ_n reduces its Bloch norm to (n+λ+1)ε_n^(−1) max_(0≤r<1)(1−r²)r^n. Derivative r^(n−1)[n−(n+2)r²] gives unique maximizer r²=n/(n+2) for n≥1; n=0 attains at r=0. Gamma quotient (2λ+1)_n/n! gives the stated 2/(e√Γ(2λ+1)) n^λ asymptotic. Independent symbolic Pochhammer convolution checked n=0..8, but the infinite n statement follows from generating functions and the source identities, not finite testing.

## originality

FAIL

The precise exact basis norm and its maximizing radius are an immediate implication of formulas the originating 2026 primary paper already publishes: Bloch norm Definition 1.1 (equation 2), canonical basis homogeneity (equation 1), sharp pointwise bound (equation 5), eigen identity (equation 6), and explicit boundary saturation φ_n(1)=ε_n^(-1) on printed page 10. Plugging these into the norm and maximizing the elementary scalar (1−r²)r^n completes the claim with no new nonstandard lemma or uncomputed invariant. Absence of the final closed form verbatim is not originality; corollaries of a stronger published package count as covered.

## value

FAIL

Norms of canonical basis elements in a newly introduced function space are natural objects, and in another setting could be independently useful. In this package, however, the exact value requires only substitution of the already sharp published pointwise bound and eigenvalue, followed by the standard one-dimensional maximum of (1−r²)r^n and routine gamma asymptotics. It supplies neither a new structural theorem, a genuinely uncomputed invariant requiring mathematical work, nor a motivated obstacle overcome beyond the originating article. Its numerical exactness and reproducibility alone cannot rescue the essentially textbook corollary. This scientific rejection preserves the correct claim and complete source package, without cosmetic repair or publication.

The dated certificate retains the supplied scientific assessment, sources and limitations.
