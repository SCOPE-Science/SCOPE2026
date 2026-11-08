---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and reproducibility

Run `python3 check_moment_curve.py` with Python 3.9 or later. The program uses exact modular integer arithmetic only and requires no external packages or network access. It recomputes the two-sum histogram for exponents \(1\le k\le10\), verifies pointwise positive fibers at all these moduli, exhaustively verifies zero fibers through \(k=5\), samples other zero fibers for larger moduli, and checks stabilization against higher power sums through degree nine for \(k\le8\). The algebraic proof in RESULT.md establishes the assertions for every \(k\ge2\); finite testing is not a substitute for it.

Observed successful marker: `DYADIC_THREE_MOMENT_STABILIZATION_AND_FULL_FIBERS_PASS`.

Observed exact examples (exponent, sumset cardinality, energy): \((4,88,1024)\), \((6,1248,24576)\), \((8,19328,524288)\), \((10,306688,10485760)\).

No independent mathematical audit or external verification was performed. Historical-priority comparison is necessarily bounded; no claim of exhaustive priority clearance is made.
