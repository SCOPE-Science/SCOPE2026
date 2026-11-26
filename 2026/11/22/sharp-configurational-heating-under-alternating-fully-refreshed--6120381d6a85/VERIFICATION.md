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

In the stated unit oscillator and full-refresh limit, the last kick gives p_n=ξ_n−h_n q_n/2. Substitution in the next first kick and two half drifts gives q_n=A_n q_{n−1}+h_n(ξ_{n−1}+ξ_n)/2 with A_n=1−h_n(h_n+h_{n−1})/4. The two-step affine Gaussian recursion contracts (|A_s A_t|<1), giving unique centered stationary phase laws; retaining Cov(q_{n−1},ξ_{n−1})=h_{n−1}/2 yields the stated coupled moment equations. After subtracting unit variance the forcing at phase s is s²(s+t)(s−t)/16 and at phase t is −t²(s+t)(s−t)/16. Inverting with determinant (1−A_s A_t)(1+A_s A_t)=(s+t)²(4−st)D/256 reproduces both variances, with D>0. Their difference and sum give the phase sign test and heating formula. With u=s+t, v=st, the excess decreases strictly in v at fixed u. Its lower-v boundary is v=0 for u≤2, with excess u²/(8−u²)≤1, and v=2(u−2) for u≥2, with denominator minus numerator 2(u−2)(u²−4u+8). These boundary comparisons also hold by continuity on the closed step square (D≥352/27 there); equality in the upper bound occurs only at the two limiting corners. The equal split maximizes v. Uniform phase selection gives a centered Gaussian mixture with fourth cumulant 3(V_s−V_t)²/4, strictly positive off-diagonal. An independent exact diagnostic at (1,4/5) gives phase variances 345/338 and 168/169 and mean 681/676. The supplied verifier was inspected, not executed; recorded symbolic and finite checks are supplementary, not the proof. The result does not concern time-weighted observation, random steps, or finite damping.

## originality

PASS

Existing coverage gives constant-step harmonic configurational exactness and related deterministic stability results, not the alternating stochastic phase laws. On the evidence inspected, the off-diagonal invariant, its sharp ceiling and phase-law distinction are supported distinct content. This is a bounded comparison, not a priority certificate.

## value

PASS

Constant-step BAOAB exactness makes unequal-step invariant sampling a naturally motivated test. The theorem distinguishes systematic configurational heating from phase-specific cooling and gives a sharp twofold ceiling under the stated stability caps. It also shows why phase mixing is not described by a single Gaussian with the averaged variance. These are usable properties for diagnosing alternating sampling, not fixed-step recomputations or a claim about general Langevin dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
