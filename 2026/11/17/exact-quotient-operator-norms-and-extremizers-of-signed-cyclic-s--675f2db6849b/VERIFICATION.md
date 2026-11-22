---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

PASS. For n>=3 and holonomy mu in {+1,-1}, the signed cyclic adjacency A=U+U* has eigenvalues 2cos((2pi j+theta)/n), theta=0 or pi. Trace-pairing with every feasible Hermitian completion fixes tr(AB)=2n, giving ||B||_op >=2n/tr|A|. Twisted cyclic-shift symmetry makes each prescribed edge of sign(A) equal its edge sign times tr|A|/(2n); hence the scaled spectral sign attains the lower bound. Pairing equality rigidly fixes the entire nonzero spectral subspace. A has a two-dimensional kernel only when n is even and mu=(-1)^(n/2); its even/odd site kernel generators have disjoint cyclic-edge supports and force mixed kernel terms to vanish. Diagonal kernel coefficients independently range over [-tau,tau]. Thus all minimizers form exactly the advertised rectangle, and other cases are unique. The Fourier sums give the stated odd/even tangent/sine formulas; checked all 44 signed instances n=3..24 with an independent eigensolver and direct edge/norm tests. Numerical checks corroborate, not prove, the all-n theorem.

## originality

PASS

PASS, bounded with significant known overlap. The primary Bottazzi–Varela 2026 preprint gives the universal trace/Frobenius lower bound and generic minimality criteria but not the flux-resolved signed-cycle evaluations or complete minimizers. The full public Resultary theorem on edge-transitive graphs proves the unsigned cycle optimum and one sign involution; it covers the mu=+1 value and is duly excluded as independent novelty. Its hypotheses fix all edge entries to +1 and it does not classify all minimizers; it does not imply the negative-flux completion and exceptional full two-parameter equality family without additional sign-covariance and kernel analysis. Cohen–Pereira 2021 addresses cycle partial-matrix completions but its accessible original material treats rank/inertia, not norm; unverified portions remain a named priority risk. Claim treated as one signed/optimizer theorem, not a novelty claim for the unsigned special case.

## value

PASS

PASS. Optimizing spectral norm under a cyclic sparse Hermitian entry pattern is a natural graph/operator completion invariant. The exact all-size signed-flux classification and exhaustive extremizers resolve the singular-kernel nonuniqueness boundary, a substantive structural issue not supplied by an elementary lower bound or known unsigned single-solution certificate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
