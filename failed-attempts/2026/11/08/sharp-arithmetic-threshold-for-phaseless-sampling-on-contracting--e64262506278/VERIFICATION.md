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

The lifted nodes t_ab=ρ^(a+b) exp(i(a−b)θ) are nonzero. Node equality forces a+b=c+e and (a−c)θ∈πZ. Thus there can be no unequal pairs for d<q, and (q,0),(0,q) collide when q≤d. The matrix of the first N=(d+1)² squared magnitudes equals an ordinary Vandermonde with columns multiplied by the nonzero nodes. Recovering H=cc* gives the coefficient vector up to phase via a nonzero diagonal entry, or gives the zero polynomial if H=0. Hermitian matrices have real dimension N and are spanned over R by cc*. The mixed monomials are independent (as complex polynomials in real coordinates after the invertible substitution z=x+iy, conjugate(z)=x−iy), so this proves the lower bound for linear ambient reconstruction only. For finite q, each (λ^n)^q is real, and 1±iz^q give the same magnitudes at all nodes but are not phase multiples. For irrational angle and equal holomorphic samples, |f|²−|g|² is real analytic near zero. If it has a first nonzero homogeneous term, dividing its zero sample values by the corresponding power of ρ^n makes that term tend to zero along the rotating unit directions; each tail is dense, so it vanishes on the circle, contradicting homogeneity. Equal moduli therefore hold on a neighborhood. If a function is identically zero both are; otherwise on a smaller open disk avoiding zeros the holomorphic quotient of unit modulus is constant, and the identity theorem extends the phase relation across the connected domain. This also treats vanishing at 0 and d=0.

## originality

FAIL

A distinct indexed November 2 theorem already states the same polynomial iff threshold, the same first-prefix Vandermonde reconstruction, the same linear ambient optimality, and the same rational-angle ambiguity. It also gives the holomorphic iff statement under the weaker requirement that the connected domain contain zero and just a sufficiently late tail. Its conclusion immediately covers a domain containing the whole orbit. There is no material residual claim. This is a statement-level comparison, not an authorship or historical-priority finding from a catalog date.

## value

FAIL

An exact angular threshold and an explicit lifting algorithm on a prescribed orbit would be useful as a distinct result. Here both, including the sample-count qualification, are already covered along with a stronger holomorphic-data theorem. Restating them on domains that contain more data supplies no new identifiability or stability result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
