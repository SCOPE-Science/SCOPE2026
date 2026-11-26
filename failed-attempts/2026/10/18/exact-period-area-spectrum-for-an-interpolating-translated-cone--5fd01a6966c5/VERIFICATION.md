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

With s=Cy, translating the left endpoint to zero leaves cuts at 1−s and 1; a circle rotation through λ first returns in one step on the outer branches and two on the central branch. For λ=p/q each coset has p+q equally spaced points, exactly floor(q(s+r)) of which are deleted for residue 0≤r<1/q. First return visits all surviving points before returning, so these periods are primitive. Size-weighting the residue lengths and integrating the piecewise-linear slice laws yields the two half-weight endpoints, the stated absolute areas, and the centered second trapezoidal sum for the mean. The normalized weights give the claimed density by Riemann sums. For irrational λ, dense circle orbits induce dense interval orbits, and lifting the invariant measures through the bounded return-time tower gives unique ergodicity. These are fiberwise results with the stated null boundary exceptions. Source verifier inspected but not executed; independent exact direct-cone enumeration checked 1,032 slices for reduced denominators 2–12 and two unequal cotangent pairs, and recovered area and mean. Replay: python3 /workspace/branches/independent_replay.py 2; output /workspace/branches/independent_replay.out.

## originality

FAIL

A distinct indexed result supplies the same three-cone map on the same trapezoid, the same all-height induction and irrational dynamics, and the same entire rational staircase and absolute/normalized area spectrum. Its path is dated later; this establishes mathematical coverage in the reviewed catalogue, not earlier chronological priority or dependence. The frozen mean and high-denominator density add no nonmechanical remainder to those exact masses.

## value

FAIL

The underlying angle-independent classification is well motivated and useful, but it is already supplied in full by the matching record. Beyond it the stated mean and weak limit are routine summation and Riemann-sum consequences of the exact mass function. No separately valuable surviving claim is established for repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
