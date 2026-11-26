---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The 2-by-2 leading Gram block is positive definite; its Schur complement has the sign of the determinant, which proves exactly the stated phase cutoff and covers the singular endpoint. With x=λ−1 the characteristic polynomial is x³−3t²x−2t³c. A repeated root must be x=±t and hence c=∓1, so the implicit-root formula is valid in the open interval. The divided-difference integral has the sign of (p−1)(p−2) for positive eigenvalues, and the largest-root derivative is positive. Continuity handles repeated roots and a zero eigenvalue at the endpoints, gives every intermediate value, and, with strict interior monotonicity, gives the exact phase labels. The spectra at both boundaries follow by factoring the cubic; the trace and Hilbert–Schmidt cases, the fourth moment from Newton's identities, and overlaps t=0,1 check out. The finite script is supplementary and was inspected, not run.

## originality

FAIL

The central sharp attainable Schatten interval—including the reversal in the sharp envelope and both extremal spectral branches—is already a specialization of Sakai–Iwata's sharp ℓ^β bounds at fixed ℓ^α norm. This is direct prior coverage, not merely resemblance. The explicit monotonic phase parametrization is not asserted to be in that paper; it follows here from a cubic and a classical divided-difference identity and does not make the claimed sharp envelope new.

## value

FAIL

The constrained operator question is natural, but the promised exact answer (branches, exponent reversal, and rank transition) is precisely the prior fixed-purity norm theorem in dimension three. What is left is a direct determinant phase translation and a short classical divided-difference calculation for the interior of the same one-parameter cubic. No independently needed unknown invariant beyond this specialization is established in the frozen finding; the argument may be useful as an exposition but not as the claimed scientific gap. No substantive repair is justified.

The dated certificate retains the supplied scientific assessment, sources and limitations.
