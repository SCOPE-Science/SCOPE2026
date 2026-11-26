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

The commutant is End_R(R²) with R=F_q[t]/(t^n). Divide a nonzero matrix by its minimum valuation k, obtaining a primitive rep over R_(n-k). If 2k<n, reduction to length m=n−2k must be square-zero. A primitive square-zero rep has basis (Uv,v) for a suitably chosen v by independence mod t; its orbit has (q²−1)q^(2m−2) elements. In each congruence fiber a unit cofactor makes the determinant uniform in t^m R_(m+k); the unit first pivot gives Smith exponents k and n−k+j for determinant valuation m+j, and k and n when the determinant is zero in that ring. This gives ranks n−j and n−k with exactly the stated weights. If 2k≥n there is no square constraint; a primitive rep over length e=n−k has residue rank two or one. Rank two contributes 2e; rank one has uniform determinant on tR_e and contributes 2e−s or e. Counting residue matrices and lifts gives the deep terms; only the zero matrix adds the constant. The deep layers cover 0 through 2 floor(n/2), and k=0 gives n. Summing gives the claimed total, also when n=1. No division by 2 or rank over R is used. The supplied script and verification were inspected as evidence, not executed. A separate bounded reproduction iterated the four polynomial entries, tested the truncated square and reduced the 2n coefficient vectors of A applied to the monomial basis over the prime field. It gave 1+9z+18z² at (n,q)=(2,2), 1+9z+30z²+72z³ at (3,2), and 1+32z+120z² at (2,3). These are finite checks, not the general proof.

## originality

FAIL

The exact labeled rank multiplicities, not just their support or total, are explicitly covered by a distinct indexed chain-ring spectrum. That catalogue entry is dated later than this frozen record, so this is a coverage ruling at review, not a finding that the earlier record lacked chronological priority.

## value

FAIL

The precise image-rank distribution is a natural invariant and genuinely finer than mere existence or the count at z=1. But the frozen claim supplies no distinct unknown invariant or consequence beyond a direct equal-characteristic specialization of the complete indexed spectrum. Thus it does not add a separate scientific result under the review standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
