---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
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

The open mean-share interval makes the quadratic payoff vertex traverse (0,1) monotonically. Since k is strictly increasing with k(0)=-1/6, the interior pin exists exactly when b²/3>a/2; the opening summary should be read with this explicit hypothesis. At the intersection, zero integral of the linearized coefficient gives multiplier one. In the quadratic variation integral, the term proportional to the time-dependent payoff slope integrates to an endpoint difference and vanishes, leaving the positive curvature contribution; variation in r likewise gives a strictly positive return-map derivative. This gives a nondegenerate local fold, with lower stable and upper unstable branches below it. Away from the pin, the zero-mean derivative operator is invertible on the oscillatory part, the first variations of the mean and r vanish, and the oscillation is Pr0k(s)W. Averaging its square gives the negative coefficient in (3), while the mixed term vanishes by averaging WW'. Cosine phase translation makes the fold even in amplitude. Independent substitutions reproduce both calibrations, including 50176/82355625 for the cosine coefficient after stripping its negative sign and omega^{-2}. Replay analytically via RESULT.md (2) and (6)–(8), then the averaged equation in step 3; verify.py and VERIFICATION.md were inspected, not executed. The source's reference to requirements.txt does not supply a dependency lock in the frozen package. The sign is perturbative at fixed period; exact arbitrary-waveform pinning is local and conditional, not a global threshold.

## originality

PASS

The distinct supported contribution is the unique source-model all-waveform pin with a nondegenerate return fold, together with the signed fixed-period waveform-primitive shift off the pin. Static mixed-game coexistence and generic frequency/amplitude shift mechanisms are known. The closest distinct periodic mixed-order result has a different payoff equation and threshold parameter. The bounded comparisons support the narrower claim, not absolute priority.

## value

PASS

A prescribed composition schedule can alter the onset of coexistence even at the same mean. Identifying exactly when the onset is invariant to all amplitudes and schedules, not merely when its small-amplitude coefficient is zero, gives a structural exception with an explicit model criterion. The opposite regime has a computable waveform-dependent signed response. This is useful without extrapolating the local deterministic result to finite-population fixation or a global cooperation threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
