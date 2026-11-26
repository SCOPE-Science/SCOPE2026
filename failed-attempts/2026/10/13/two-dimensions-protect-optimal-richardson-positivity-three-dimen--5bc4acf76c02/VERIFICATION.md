---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

At n=1 the step solves the equation. At n=2 the optimal residual matrix T=I−αA has trace zero and eigenvalues ±q with 0≤q<1, so its square is q²I by Cayley–Hamilton. I+T has positive diagonal entries and nonnegative off-diagonal entries; summing consecutive even and odd powers proves all even Richardson iterates nonnegative, and the odd ones add αq^(2m)b. For the 3×3 block witness, the block eigenvalues are 9 and 11 and the singleton eigenvalue is 1. With α=1/6, the active residual block has diagonal −2/3 and off-diagonal 1/6. Exact successive active coordinates are (0,1/6), (1/36,1/18), (−1/108,29/216); the third coordinate stays zero. The residual spectral radius is 5/6, and solving the block system gives (1/99,10/99,0). Thus the frozen threshold and witness are correct.

## originality

FAIL

Verified existing coverage, not an access-based failure. The prior Newton–Schulz record writes precisely the same inverse approximant as Richardson at step 2^j and its proof establishes two-dimensional positivity for every even number of terms. Optimal damping makes every odd step in dimension two the preceding even step plus a nonnegative scalar multiple of b. More decisively, the prior degree-three Chebyshev record's explicit polynomial has the same ratio of the A and A² coefficients as optimal Richardson at step three. The two approximants differ only by positive scaling and an identity shift, and both have strictly positive diagonals. The earlier Chebyshev sharpness theorem therefore transfers its three-dimensional obstruction at k=3, even using the frozen matrix and right-hand side as a direct parameter choice from its family. The combination covers the minimal dimension and the third-step failure. The particular fractions in the new presentation are a recurrence evaluation, not a distinct scientific claim.

## value

FAIL

The separation between spectral convergence and sign preservation is a worthwhile question, but after the verified prior implications the frozen addition is a particular rational evaluation of an already sufficient witness family and a direct pairing of powers of the same inverse polynomial. It does not establish a distinct useful boundary, new case or invariant that would justify the incremental presentation as a research finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
