---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

Ding's partition multiplier (alpha)_partition/(genus+gamma)_partition gives the positive factors a_m b_n with alpha=gamma+1, genus four and a/2=1. The U(2) highest weight (m,n) has dimension m-n+1, so the product type has squared multiplicity; the nonholomorphic complement is killed. With x=tau^(-1/3), h_n=(A_gamma b_n)^(1/3), the strict upper cutoff in m is the ceiling of the real cubic cutoff minus one, hence x h_n+O_gamma(1). The squared-multiplicity row sum differs from (x h_n-n)_+^3/3 by O_gamma((x h_n)^2+1) on the union of active rows, including possible mismatches close to the boundary. There are O_gamma(sqrt(x)) such rows and sum h_n^2 converges, giving O_gamma(x^2) total error. With Q=(A_gamma B_gamma)^(1/6) sqrt(x)+O_gamma(1), the cubic leading term can be extended to all n for O_gamma(x^2) error and sum b_n=(gamma+2)/2 by a telescoping difference of reciprocal quadratic products. Of the remaining cubic terms, only -x^2 sum_{n<=Q} n h_n^2 exceeds O_gamma(x^2): it is -(A_gamma B_gamma)^(2/3) x^2 log(x)/2+O_gamma(x^2). This gives the stated negative coefficient after log(x)=log(1/tau)/3. Ordinary monotone inversion gives s_j~C_gamma/j, and convergence of the ordinary logarithmic mean yields the stated Dixmier trace and Schatten assertions.

## originality

PASS

The exact spectral characteristic and Schatten threshold are prior results. The additional result is a quantitative two-term ordered count, including an interaction of both partition coordinates, and its explicit weak trace; the inspected prior statements do not give those counting constants or remainder.

## value

PASS

The trace boundary is canonical for this positive determinant kernel. An explicit weak-trace mass and a genuinely rank-two negative logarithmic correction distinguish a spectral ordering phenomenon invisible to the known membership criterion. The result explains the interaction through a borderline sum over the second partition coordinate rather than reporting a numerical cutoff or a new notation for the same criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
