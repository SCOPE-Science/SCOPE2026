---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

The actual truncated Bargmann–Fock source (n basis vectors, degrees 0 to n-1, m>=n positive weighted samples on a single circle) is analytically correct. Its Gram diagonal is e^{-x} x^k/k!, and largest/minimum eigenvalue estimates give the universal diagonal ratio. The log-concavity of x^k/k! fixes the unique radius x=((n-1)!)^(1/(n-1)). Equality forces e_0 to be a smallest eigenvector, which annihilates all nonconstant angular moments through n-1; square Vandermonde unitarity yields a regular weighted n-gon. Stirling gives the asserted exponential condition-number asymptotic. These are infinite proofs, not consequences of the finite check_ring_sampling.py trials.

## originality

FAIL

FAIL: the fully inspected prior published circle-only coherent-frame theorem states precisely the same all-positive-weight, all-angle, arbitrary-sample-count universal optimum and iff equality classification, with exactly one dimension/index shift. Set d=n-1 in the prior degree-d space (d+1 monomials), normalize weights to unit total, put x=R^2, and take the square root of its optimal frame-bound ratio B/A; every submitted formula including the exponential asymptotic follows. Both records date to 2026-11-08, so intra-day release ordering is unproven; the mathematical implication/coverage is decisive regardless.

## value

FAIL

FAIL: no independently useful mathematical remainder is identified after the earlier theorem already covers the global radius optimization, arbitrary positive-weight angular designs, minimizer rigidity, oversampling obstruction, and sharp asymptotic. The correct proof is a reparameterization of the exact prior result, not a new natural invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
