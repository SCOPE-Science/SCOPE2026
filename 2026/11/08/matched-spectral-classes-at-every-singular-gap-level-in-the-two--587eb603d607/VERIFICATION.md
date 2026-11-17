---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-11.md",
      "INDEPENDENT_AUDIT_2026-11-11.json"
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

Full RESULT.md, exact Jacobian product rule L=diag(2,1), R=[[0,-2],[1,0]], and one-to-one Saiki–Takahasi–Yorke symbolic periodic coding checked. Cumulative right-visit parities are a bijection of F_2^n; the monomial Jacobian has singular magnitudes 2^A,2^(n-A), where A is the parity-zero occupancy. Conditional absolute binomial histograms match for even/odd right parity; odd parity creates imaginary conjugate eigenvalues, even parity produces real diagonal eigenvalues. Removing the sole all-L fixed-face word subtracts one real maximal-gap point. The independent all-word calculation exactly multiplies the Jacobians for n=1..10; finite verification corroborates, but the bijection and binomial proof establish all n.

## originality

PASS

The precise all-length class-conditioned singular-gap census plus coupled eigen/singular-gap weak limit at iterate-fixed points is distinct from already known spectral-parity margins and from Lebesgue-sampled singular-value central limits. This is best-of-knowledge with historical priority risk.

## value

PASS

The first exact all-n spectral-class and singular-anisotropy joint distribution is a natural invariant of periodic-point derivative dynamics; it sharply distinguishes eigenvalue-based expansion from singular-value nonnormal expansion at the same return points, and its one-word extreme defect prevents a naive independence assertion on actual fixed points.

The dated certificate retains the supplied scientific assessment, sources and limitations.
