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

With the e^(-inx) coefficient convention, the two periodic equations have multipliers (1+inℓ)^(-1) and (1-inℓ)^(-1). The reverse shift contributes e^(-inδ) and the baselines only affect mode zero. Thus R_n=ρ e^(-inδ)(1+inℓ)/(1-inℓ). Unit-normalizing and dividing the second mode by the square of the first cancels δ. The resulting phase Θ=2 arctan(2ℓ)−4 arctan(ℓ) has derivative −12ℓ²/[(1+ℓ²)(1+4ℓ²)] and decreases from 0 to −π with neither endpoint attained. This gives the open lower semicircle exactly, with no unwrapping ambiguity. The tangent difference yields the positive inverse equation 2ℓ³/(1+3ℓ²)=−tan(Θ/2); the first ratio then recovers the gain modulus and shift modulo one lap. An arbitrary smooth field consisting of those two harmonics plus a sufficiently large constant realizes every feasible ratio pair. One mode allows any positive ℓ by adjusting the shift, even if the measured forward coefficient is held fixed by changing the unknown concentration coefficient. The small-length phase expansion is −4ℓ³+12ℓ⁵+O(ℓ⁷) and the large-length one is −π+3/ℓ+O(ℓ⁻³), giving the stated inverse sensitivity. At ℓ=1/2 the half-angle tangent has magnitude 1/7, giving z=(24−7i)/25. No numerical test is needed for the result. Positivity is an explicit physical hypothesis; the remark about a sign-flip ambiguity should not be read as a necessity theorem for signed relative gains (a negative gain would instead put the two-mode invariant in the other open half-circle).

## originality

PASS

The exact identifiable region and two-mode inverse jointly treating lag, relative position and unknown positive gain survive the strongest inspected comparisons. First-order correction, Fourier shift cancellation, and broad blind calibration are not themselves claimed as new.

## value

PASS

A field traverse confounds response lag with relative registration even when one harmonic is measured without error. The exact two-mode feasibility test breaks that confounding without knowing the input and provides concrete rejection tests and sharp endpoint conditioning. It is a useful benchmark for noiseless paired-scan calibration and for judging when noisy extensions should be unstable, not a claim of calibrated deployment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
