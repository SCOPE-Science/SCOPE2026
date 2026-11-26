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

For the frozen RESULT.md lines 5–38, the centered linear coordinate x has squared norm S_n, path gradients 1 and closing gradient n−1. Its Rayleigh quotient is [B−(t−(n−1)^2)c]/S_n. The parabolic path weights solve Lx=Λx, and on monomials of degree k the scaled path operator is triangular with leading coefficient k(k+1)/2, so the path gap is simple and separated. Equality in Rayleigh at c=0 determines all weights by the vertex recurrences. The positive directional derivative at t<(n−1)^2 follows from the simple eigenvalue, decreasing each path weight uniformly while adding the chord. At equality Rayleigh attainment forces w_i=Λu_i−(n−1)c; positivity of L−ΛI on centered vectors is then equivalent to positivity of A_n−(c/Λ)((n−1)I−11^T) in difference coordinates. Indeed the squared norm of a centered cumulative sum has Gram entry C_ij=i(n−j)/n for i<=j; summing each row gives u_i. The constant gradient is a null vector; the smallest eigenvalue on its orthogonal complement gives precisely the claimed cutoff. The e_1 test yields ρ_n≤(n−1)/(2n)<1/2, so path weights remain strictly positive; a nonconstant null gradient appears at the endpoint. Independent exact characteristic polynomials confirm all four example radicals (python3 /tmp/opencode/frozen_math_reproduction.py). The supplied script was inspected but not executed; neither finite checks nor the recorded numerical optimization prove the unrestricted optimizer statement.

## originality

FAIL

The distinct indexed result b8eae264de71 demonstrably covers the one-exceptional-price theorem including the complete critical interval. This is a coverage verdict, not a historical priority claim: the broader record has a later catalogue date path, which is not a verification of discovery or priority order. The older-path C4/C5 records separately cover their sizes. The Brownian-bridge spectral expression is an exact change of coordinates in the broader variational endpoint, not an independent remaining optimization result.

## value

PASS

Viewed as a mathematical theorem apart from the overlap, an exact threshold distinguishing mandatory and forbidden use of an optional link, and a full critical optimal segment including its multiplicity endpoint, is meaningful for diffusion network design. It does not solve the whole subcritical optimization; the failing axis is demonstrable originality coverage.

The dated certificate retains the supplied scientific assessment, sources and limitations.
