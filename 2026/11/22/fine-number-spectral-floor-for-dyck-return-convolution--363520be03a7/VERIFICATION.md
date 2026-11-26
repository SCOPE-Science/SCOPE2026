---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

A primitive excursion of semilength r contributes C_(r−1) choices. Multiplying these weights and inserting the sign at each proper partial sum gives exactly the unnormalized Walsh transform of the multiplicity kernel. Selecting paths that return at j and deleting the sign at j gives the product Z_j Z_(n−j), since concatenation across that specified return is a bijection. At all-negative signs the signed excursion sum is H=W/(1+W)=zF(z), and z=W(1−W) gives H=z+zH^2/(1−2H). Coefficient induction gives m_1=1, m_2=0, and m_n≥2^(n−3) for n≥3 from z·2^(n−3)H^(n−1). With these base values, the factored sign differences and induction on n show coordinate monotonicity and hence the asserted full-support minimizer, without claiming uniqueness. The trivial character attains the Catalan maximum by the triangle inequality. The n=1 operator has one eigenvalue 1; at n=2 the spectrum is (2,0), and all other cases are positive definite. Standard square-root transfer from H=1/3−(2/9)sqrt(1−4z)+O(1−4z) at its sole dominant singularity gives m_n/C_n→1/9, proving the stated conditioning limits and the effect of probability normalization. A separate step-by-step census and full character sum through n=10 gave the minima 1,0,1,2,6,18,57,186,622,2120, with full support always a minimizer and multiple minima for several n.

## originality

PASS

The Catalan and Fine generating functions and the signed coefficient at full support are not the original contribution. The supported distinct statement is position-resolved simultaneous nonnegativity and extremality of that full-support character, yielding the exact spectral floor and condition number. The inspected comparisons do not establish this extremum.

## value

PASS

Optimizing over all return-position characters, not just evaluating the signed return-count statistic, resolves singularity and supplies a sharp stability guarantee for inversion of the natural counting and probability convolution operators. The uniform positive spectral gap for normalized kernels as n grows is meaningful beyond the finite numerical checks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
