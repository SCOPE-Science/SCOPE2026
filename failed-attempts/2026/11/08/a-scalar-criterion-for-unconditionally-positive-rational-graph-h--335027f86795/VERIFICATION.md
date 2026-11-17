---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

The complete multipartite Laplacian has orthogonal projectors onto constants (eigenvalue 0), part-constant zero-sum modes (n), and within-part zero-sum modes (n-a_i). Hence between-part entries equal (1-F(nh))/n, within-part distinct entries equal (n-a_i)h/a_i[g((n-a_i)h)-g(nh)], and diagonals are nonnegative convex combinations when 0<=F<=1. K2 enforces F<=1; large complete stars/complete graphs and boundedness enforce F>=0; dense rational part-size ratios enforce nonincreasing g=(1-F)/x. The [2/2] Gauss filter F=(x^2-6x+12)/(x^2+6x+12) has strictly positive numerator and strictly decreasing g=12/(x^2+6x+12), so all positive steps on this graph class have positive stochastic entries. Independent exact rational matrix algebra verifies the P4 h=20 negative entry -643260/32303047 outside the class.

## originality

FAIL

The October 13, 2026 published Resultary theorem An exact positivity criterion on complete multipartite diffusion graphs already states the identical universal if-and-only-if over ALL continuous f with f(0)=1 (a stronger domain than bounded F), and the identical fourth-order Gauss-Legendre strict-positive end-step. Its spectral projector entry formulas and converse are the same proof. The submitted path P4 negative illustration cannot restore originality of the covered main theorem.

## value

FAIL

The scalar criterion is a well motivated mathematical result, but this package reproduces the full earlier theorem and specific Gauss application with a redundant global boundedness assumption. The P4 example is a routine illustration of the same limitation rather than an independently valuable unclassified invariant. Correctness of the derivation does not turn known coverage into new value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
