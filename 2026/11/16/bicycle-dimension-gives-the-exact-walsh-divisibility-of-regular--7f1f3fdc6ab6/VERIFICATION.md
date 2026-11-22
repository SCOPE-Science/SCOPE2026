---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

For a full-row-rank totally unimodular A, signed Walsh basis sum equals det(A diag((-1)^t) A^T) by Cauchy–Binet because nonzero maximal minors have squared determinant 1. A binary congruence separates the rank-k radical of AA^T from an odd-invertible block; its even Schur complement proves 2^k divides every signing determinant. Independent bottom rows of PA provide k columns with invertible reduced bottom matrix. The multilinear Boolean top coefficient of det(D+sum x_i z_i z_i^T) is det[z_1,...,z_k]^2=1, so some signing attains valuation exactly k. For Q_d, the mod-2 Laplacian is multiplication by y_1+...+y_d in the Boolean truncated group algebra, with kernel 2^(d-1); deleting one vertex reduces its nullity by one. This is a genuine infinite proof; the finite checks cannot establish arbitrary-rank sharpness.

## originality

PASS

Sharp exact content across every signing is stronger than the classical unweighted determinant, but no prior universal signed-regular-matroid gcd implication was identified. Full primary inspection was strongest for Pendavingh; inaccessible Berman 1986 and potentially older arithmetic matroid interpretations remain explicit priority risks.

## value

PASS

The exact dyadic content is a natural representation-independent harmonic invariant of any regular matroid; its universal divisibility and attainment theorem goes beyond textbook unsigned enumeration. The hypercube law gives a nontrivial exponential-dimension evaluation and the b=0 case characterizes guaranteed Fourier nonvanishing. Exact 2-adic content, not exact smallest nonzero absolute magnitude or all zeros, is the useful boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
