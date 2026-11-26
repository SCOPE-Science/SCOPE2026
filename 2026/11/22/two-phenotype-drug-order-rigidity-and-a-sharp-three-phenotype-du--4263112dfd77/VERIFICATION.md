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

For each 2×2 matrix the real-eigenvalue discriminant is (M_11−M_22)^2+4rs>0. The exponential interpolant αI+βM has β>0 at every positive time. The ordered product difference therefore equals β_A(u)β_B(v)(BA−AB); in the AB convention of the finding, BA−AB=(B−A)A−A(B−A), giving the stated positive upper-right and negative lower-left factors relative to the difference of loss contrasts. The total readout leaves r x₂−s x₁, which vanishes on the stationary ray of Q, not necessarily of the full untreated dynamics Q+G. All durations and zero factors have the stated behavior; scalar propagators commute. For the fixed three-state matrices, the norm bounds and exponential Taylor remainder in the source are valid. Independently shifted both matrices by 3I, whose common exponential factor cancels in the sign comparison, and evaluated their nonnegative Taylor polynomials with rational geometric majorants of their tails. The independent enclosures confirm both strict reported decimal thresholds, about −0.016199346015221782 and +0.0092842024968862, with the sign taken in the original order convention. Linearity and continuity preserve the strict witness at sufficiently small positive perturbations of the initial vector. The 2×2 obstruction and fixed 3×3 witness establish minimality, not a statement about arbitrary switched generators or biological treatment. Replay: python3 /workspace/branches/reproduce_3_4_5.py. The supplied checker and verification notes were inspected, not run.

## originality

PASS

Two-by-two exponential interpolation and the commutator identity are standard. The supported distinct claim is the exact terminal-readout sign classification in the stated common-switching model together with a strict three-dimensional reversal for fixed matrices and equal durations, establishing the dimensional threshold. Neither the inspected mathematical analogues nor accessible primary comparisons gives the same combination. This is a bounded priority assessment.

## value

PASS

The constraints define a natural finite-time ordering question: fix switching, the two loss profiles, and the starting state, then ask whether the advantage of a reversed product can depend only on how long the two stages last. The complete two-state sign rule is a useful diagnostic, and the strict witness at the next dimension shows its limits without changing the readout, switching generator, or relative pulse durations. The certified threshold is more informative than a generic observation of noncommutativity. Its value is as an abstract model benchmark, not as a biological or clinical prescription.

The dated certificate retains the supplied scientific assessment, sources and limitations.
