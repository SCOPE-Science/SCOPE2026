---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-14.md",
      "INDEPENDENT_AUDIT_2026-11-14.json"
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

The m-1 interior Fourier eigenspaces are two-dimensional; two-site shell evaluation has determinant proportional to sin(pi k h/m) and loses exactly one direction at k=j m/g for 1<=j<g. The spatial-visible space thus has dimension 2m-g+1. A Vandermonde with pairwise distinct spectral multipliers demixes all m+1 shell values after m+1 time steps. At m steps its one-dimensional kernel has no zero entry, so the endpoint and degenerate shell ratios force beta=alpha and alpha=(-1)^(h/g)alpha, producing an additional transient 1D defect iff h/g even. Counting coprime offsets gives stated parity census; below m dimension bound forbids full recovery. Independently built exact SymPy matrices for all 2<=m<=7, 1<=h<2m and checked both rank formulas. For C6,h=2 ranks 5 at t=3, 6 at t=4; this is a precise test case, not the proof.

## originality

PASS

PASS best-of-knowledge: a related Nov 8 published even-cycle information-volume theorem determines when the minimal square m-snapshot observation determinant is nonzero, but not the exact rank deficiency when zero or whether one additional time step repairs it. The primary 2011 Parlangeli–Notarstefano cycle observability theorem (4.10) expresses a full-n gcd criterion, seemingly conflicting with the explicit C6,h=2 spectral calculation; we do not silently treat it as dominating coverage. The candidate exact two-horizon formula follows from direct Fourier analysis, and residual convention/older-theorem reconciliation remains a live priority risk. A 2026 graph dynamical-sampling preprint could be inspected only at bibliographic/abstract level.

## value

PASS

PASS: identifying how many Fourier modes are permanently invisible versus how many require precisely one more snapshot is a natural complete finite-time observability invariant. A zero determinant alone is insufficient for experimental sensor-time planning; this theorem yields exact rank deficits, minimum horizon, and counts of full-recovery separations across all even cycles. It is a motivated structural sharpening, not a tiny arbitrary matrix instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
