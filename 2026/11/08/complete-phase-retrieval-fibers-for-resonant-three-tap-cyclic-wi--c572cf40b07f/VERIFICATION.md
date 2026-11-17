---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For N≥6 full-frequency intensity extracts zero, first and second correlation lags without aliasing. W invertible recovers every |f_t|² also for competitors with zeros; the nonzero second lag forces parity-constant phases. The two alternating first-lag identities imply κ r_t conjugate(r_{t+1})=δ^{±1}, hence r_{t+2}=κ²r_t. Cyclicity yields κ^N=1, ρ^m=1 and the exact interlaced quadratic-chirp formulas; δ is uniquely determined, and substitution verifies the sole alternative. Independently checked full intensities for several even N and the explicit g=(1,3,ω) pair, not used as infinite proof.

## originality

PASS

The nontrivial phase-twisted κ≠1 chirp fibers and all-even-N at-most-two-class classification extend the earlier equal-tap boxcar geometric-progression case; generic recovery, odd endpoint-lag recovery and even two-point amplitude swaps do not imply this formula.

## value

PASS

An exact failure-of-uniqueness classification for a natural fully sampled short-time Fourier measurement design locates the entire full-support ambiguity locus and proves it has at most two phase classes, including resonant nontrivial chirps and a concrete family in every even dimension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
