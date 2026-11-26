---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Reassessed /workspace/repairs/5/RESULT.md. Radius variable t=|z|²/(1−|z|²) gives the stated positive diagonal beta-prime eigenvalues, and splitting 2m ternary digits gives the translates of μ_m. The CDF bound follows by induction on each branch (on the right, 1+u^δ≤(2+u)^δ by monotonicity of the difference; the middle gap has CDF 1/2); rescaling gives F_m(t)≤t^δ even beyond the support. For k≥1, Stieltjes integration by parts discards the nonpositive term on the rising side of g_k and bounds the rest by ∫_(k/2)^∞ t^δ(−g_k')dt. Ordinary integration by parts yields A_k plus the truncated beta integral; J_k is decreasing by its gamma recurrence, and A_x decreases for x≥2 from log(1+2/x)≥2/(x+1) and δ<2/3. For k=1 the missing piece of the full beta integral is kept as a subtraction and bounded using (1+t)^3≤(3/2)^3 up to 1/2. The four-cylinder Jensen lower bound uses exact means 1/6 and 5/6. Independent bounded replay: python3 /workspace/branches/independent_exact_replay.py; exact rational interval arithmetic verifies the dimension, sine, exponential, beta-integral and Jensen inequalities (vacuum lower ≈0.62900005 and first-mode upper ≈0.62095097 in the independent enclosure). Higher modes are uniformly below 0.600. Thus the normalized spectral gap is strictly greater than 1/200 and the claimed squared-distance estimate follows by expansion in the diagonal basis. Local weak convergence follows from the fixed digit decomposition, and the tail is O(R^(δ−2)) uniformly by the CDF bound and integration by parts, establishing the vacuum series, its positivity and finiteness. The approximate decimal is not a certificate. The frozen CHECK.py was inspected, not executed. No claim for odd stages, general weights or arbitrary dilations is needed for the repaired gap.

## originality

PASS

Pass only for the repaired, explicit strictly positive gap in balanced normalization uniformly over all m≥2 and all excited modes, with its norming-vector stability. The frozen claim's general even-limit existence was covered; vacuum identification and finite-stage uniqueness also follow by combining the earlier even-limit characterization with a subsequently dated all-scale Gaussian dominance result. The repaired finding attributes those overlaps and does not claim priority for them.

## value

PASS

The explicit gap is at the same scale as the decaying norm and is simultaneous in stage and mode. It ensures uniform stability of the extremizing subspace for almost-maximal Rayleigh quotients, a distinction not obtained from uniqueness at individual stages or from convergence of the maximal spectral value alone. The repair foregrounds this gap already certified by the original uniform estimates instead of claiming the known norm-limit existence as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
